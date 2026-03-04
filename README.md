**Extract the Performance Co-Pilot(PCP) logs - minimal OSWatcher logs**

1. Go to the directory where you have the PCP collections


2. Execute the python script with the full location:

 # /root/pcp-pwd.py

    Available files in current directory:
    
    total 143M
    
    -rw-r--r-- 1 root root 1.8M Jan 23 02:11 20260120.0.xz
    -rw-r--r-- 1 root root 1.7M Jan 23 02:11 20260120.1.xz
    -rw-r--r-- 1 root root 1.8M Jan 23 02:11 20260120.2.xz
    -rw-r--r-- 1 root root 1.9M Jan 23 02:11 20260120.3.xz
    -rw-r--r-- 1 root root 1.7M Jan 23 02:11 20260120.4.xz
    -rw-r--r-- 1 root root 1.7M Jan 23 02:11 20260120.5.xz
    -rw-r--r-- 1 root root 411K Jan 23 02:11 20260120.6.xz
    -rw-r--r-- 1 root root  57K Jan 23 02:11 20260120.index
    -rw-r--r-- 1 root root 131K Jan 23 02:11 20260120.meta.xz
    -rw-r--r-- 1 root root 1.7M Jan 23 02:11 20260121.0.xz
    -rw-r--r-- 1 root root 1.6M Jan 23 02:11 20260121.1.xz
    -rw-r--r-- 1 root root 1.7M Jan 23 02:11 20260121.2.xz
    -rw-r--r-- 1 root root 1.7M Jan 23 02:11 20260121.3.xz
    -rw-r--r-- 1 root root 1.8M Jan 23 02:11 20260121.4.xz
    -rw-r--r-- 1 root root 1.7M Jan 23 02:11 20260121.5.xz
    -rw-r--r-- 1 root root 338K Jan 23 02:11 20260121.6.xz
    -rw-r--r-- 1 root root  57K Jan 23 02:11 20260121.index
    -rw-r--r-- 1 root root 118K Jan 23 02:11 20260121.meta.xz
    -rw-r--r-- 1 root root  315 Jan 23 02:11 Latest
    -rw-r--r-- 1 root root  37K Jan 23 02:11 pmlogger.log
    -rw-r--r-- 1 root root  91K Jan 23 02:11 pmlogger.log.prev
    -rw-r--r-- 1 root root  67K Jan 23 02:11 pmlogger.log.prior
    
    Enter the PCP archive file name: 20260121.5.xz
    
    Detected hostname: <HOSTNAME>
    Note: timezone set to local timezone of host "<HOSTNAME>" from archive
    
    Log Label (Log Format Version 2)
    Performance metrics from host <HOSTNAME>
        commencing Wed Jan 21 00:11:20.153287 2026
        ending     Thu Jan 22 00:11:08.270407 2026
    Archive timezone: IST-5:30
    PID for pmlogger: 2233
    Enter the Start time (e.g., Jan 16 00:15): Jan 21 00:11
    Enter the End time   (e.g., Jan 16 01:15): Jan 21 00:15
    
    Output directory:
    **<HOSTNAME>/0011_0015-04_0345/**
    
    Saved: <HOSTNAME>/0011_0015-04_0345/numastat.txt
    Saved: <HOSTNAME>/0011_0015-04_0345/runq.txt
    Saved: <HOSTNAME>/0011_0015-04_0345/meminfo.txt
    Saved: <HOSTNAME>/0011_0015-04_0345/iostat.txt
    Saved: <HOSTNAME>/0011_0015-04_0345/load.txt
    Saved: <HOSTNAME>/0011_0015-04_0345/vmstat.txt
    Saved: <HOSTNAME>/0011_0015-04_0345/mpstat.txt
    Saved: <HOSTNAME>/0011_0015-04_0345/slabinfo.txt
    Saved: <HOSTNAME>/0011_0015-04_0345/atop.txt
    Saved: <HOSTNAME>/0011_0015-04_0345/ps.txt
    
    All commands executed and outputs saved successfully.

# ls -l <HOSTNAME>/0011_0015-04_0345/
total 14620
-rw-r--r-- 1 root root   106584 Mar  4 03:45 atop.txt
-rw-r--r-- 1 root root    31373 Mar  4 03:45 iostat.txt
-rw-r--r-- 1 root root     8697 Mar  4 03:45 load.txt
-rw-r--r-- 1 root root    37520 Mar  4 03:45 meminfo.txt
-rw-r--r-- 1 root root    18990 Mar  4 03:45 mpstat.txt
-rw-r--r-- 1 root root      408 Mar  4 03:45 numastat.txt
-rw-r--r-- 1 root root  4394116 Mar  4 03:46 ps.txt
-rw-r--r-- 1 root root     7992 Mar  4 03:45 runq.txt
-rw-r--r-- 1 root root 10317346 Mar  4 03:45 slabinfo.txt
-rw-r--r-- 1 root root    25079 Mar  4 03:45 vmstat.txt


