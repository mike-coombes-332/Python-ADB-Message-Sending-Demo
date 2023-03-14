# Python-ADB-Message-Sending-Demo

Anyone controlling a device via ADB, can use python to send the messages and collect the result. In this example I show how to request 2 items from the device.

uptime

>>adb -s R9WTB0RFR6L shell uptime
<< 15:13:39 up 4 days, 17:16, 0 users, load average: 30.65, 30.31, 30.20

Uptime is a command that returns information about how long your system has been running together with the current time, number of users with running sessions, and the system load averages for the past 1, 5, and 15 minutes.


build.version.release (Android Version)

>>adb -s R9WTB0RFR6L shell getprop ro.build.version.release
<<13
