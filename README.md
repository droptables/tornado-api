An API built with tornado, CB hostname lookups as an example

curl localhost/cblookup/HOSTNAME

respone:

{"status": "Offline", "has-agent": "True", "registrationtime": "2015-12-22 10:15:48.919446-08:00", "timestamp": "2016-01-06 16:24:31", "hostname": "HOSTNAME", "os": "Windows 7 Enterprise Service Pack 1, 64-bit"}

If a requested HOSTNAME has multiple matches, a list will be returned with the corespondign matches.

[{"status": "Offline", "has-agent": "True", "registrationtime": "2015-12-22 10:15:48.919446-08:00", "timestamp": "2016-01-06 16:24:31", "hostname": "HOSTNAME", "os": "Windows 7 Enterprise Service Pack 1, 64-bit"},{"status": "Offline", "has-agent": "True", "registrationtime": "2015-12-22 10:15:48.919446-08:00", "timestamp": "2016-01-06 16:24:31", "hostname": "HOSTNAME", "os": "Windows 7 Enterprise Service Pack 1, 64-bit"}]
