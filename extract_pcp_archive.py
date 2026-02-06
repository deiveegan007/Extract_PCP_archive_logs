#!/usr/bin/env python3
import subprocess
import concurrent.futures
import os
from datetime import datetime


def list_current_directory():
    """List files in the current working directory."""
    try:
        result = subprocess.run(
            ["ls", "-lh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("\nAvailable files in current directory:\n")
        print(result.stdout.decode())
    except Exception as e:
        print("Failed to list current directory:", e)


def get_hostname_from_pmdumplog(logname):
    """
    Run pmdumplog -L and extract hostname.
    Example line:
    Performance metrics from host kvm-box
    """
    try:
        result = subprocess.run(
            ["pmdumplog", "-L", logname],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True   # Python 3.6 compatible
        )

        for line in result.stdout.splitlines():
            if "Performance metrics from host" in line:
                return line.strip().split()[-1]

        return "unknown-host"

    except Exception as e:
        print("Failed to run pmdumplog -L:", e)
        return "unknown-host"


def format_time(date_str, year=2026):
    """
    Convert input date/time into month-name format.
    Example: "Jan 16 00:15"
    """
    try:
        date_str_with_year = "{} {}".format(date_str, year)
        date_obj = datetime.strptime(date_str_with_year, "%b %d %H:%M %Y")
        return date_obj.strftime("%b %d %H:%M:%S")
    except ValueError as e:
        print("Error formatting time:", e)
        return None


def run_command(command, output_file):
    """Run shell command and save output to file."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output = result.stdout.decode() + result.stderr.decode()

        with open(output_file, "w") as f:
            f.write(output)

        print("Saved:", output_file)

    except Exception as e:
        print("Command failed:", command, e)


def main():
    # ---- List current directory ----
    list_current_directory()

    logname = input("Enter the PCP archive file name: ").strip()

    if not os.path.exists(logname):
        print("File not found:", logname)
        return

    # ---- Get hostname ----
    hostname = get_hostname_from_pmdumplog(logname)
    print("\nDetected hostname:", hostname)

    # ---- Show archive info ----
    subprocess.call("pmdumplog -z -L {}".format(logname), shell=True)

    # ---- Time inputs ----
    stime_input = input("Enter the Start time (e.g., Jan 16 00:15): ")
    etime_input = input("Enter the End time   (e.g., Jan 16 01:15): ")

    stime = format_time(stime_input)
    etime = format_time(etime_input)

    if not stime or not etime:
        print("Invalid time format. Exiting.")
        return

    # ---- Directory creation ----
    now = datetime.now()
    day = now.strftime("%d")
    time_now = now.strftime("%H%M")

    start_dir = stime_input.split()[-1].replace(":", "")
    end_dir = etime_input.split()[-1].replace(":", "")

    time_dir = "{}_{}-{}_{}".format(start_dir, end_dir, day, time_now)
    base_dir = os.path.join(hostname, time_dir)

    os.makedirs(base_dir, exist_ok=True)

    print("\nOutput directory:\n{}/\n".format(base_dir))

    # ---- Commands ----
    commands = [
        ('/usr/bin/pmrep -z -a {} -p kernel.all.load -S "@{}" -T "@{}"'.format(logname, stime, etime), "load.txt"),
        ('/usr/bin/pcp -z -a {} --start "@{}" --finish "@{}" atop'.format(logname, stime, etime), "atop.txt"),
        ('/usr/bin/pcp -z -a {} --start "@{}" --finish "@{}" mpstat'.format(logname, stime, etime), "mpstat.txt"),
        ('/usr/bin/pmrep -z -a {} :meminfo-1 -p -S "@{}" -T "@{}"'.format(logname, stime, etime), "meminfo.txt"),
        ('/usr/bin/pcp -z -a {} --start "@{}" --finish "@{}" iostat -x t'.format(logname, stime, etime), "iostat.txt"),
        ('/usr/bin/pmrep -z -a {} :vmstat -p -S "@{}" -T "@{}"'.format(logname, stime, etime), "vmstat.txt"),
        ('/usr/bin/pcp -z -a {} --start "@{}" --finish "@{}" ps -u'.format(logname, stime, etime), "ps.txt"),
        ('/usr/bin/pmrep -z -a {} -p proc.runq.runnable proc.runq.blocked -S "@{}" -T "@{}"'.format(logname, stime, etime), "runq.txt"),
        ('/usr/bin/pmrep -z -a {} :slabinfo -p -S "@{}" -T "@{}"'.format(logname, stime, etime), "slabinfo.txt"),
        ('/usr/bin/pmrep -z -a {} :numastat-1 -u -p -S "@{}" -T "@{}"'.format(logname, stime, etime), "numastat.txt"),
    ]

    # ---- Parallel execution ----
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for cmd, fname in commands:
            outfile = os.path.join(base_dir, fname)
            futures.append(executor.submit(run_command, cmd, outfile))

        for _ in concurrent.futures.as_completed(futures):
            pass

    print("\nAll commands executed and outputs saved successfully.")


if __name__ == "__main__":
    main()
