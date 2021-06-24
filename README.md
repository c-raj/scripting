# Question
Given access log find all the client IPs that made request to "robot.txt" and print the response status code for the request.

# Answer
## Using grep & awk
This can be done with awk and grep using the following command:
```
$ cat access.log | grep "robots.txt" | awk '{print $1,$9}'
```

The output will look like the following snippet:
```
1.202.218.8 404
1.202.218.8 404
46.165.197.142 404
199.58.86.211 404
1.202.218.8 404
64.246.165.190 404
64.246.165.200 404
207.46.199.54 404
1.202.218.8 404
```

## Using Python
The same logic is implemented in Python in [log_parser.py!](https://github.com/c-raj/scripting/blob/main/log_parser.py) file.

### Pre-Requisites
Install Python 3.7 or higher version

### Assumptions

For the sake of simplicity we assume the following:
* Log file is not too big.
* There are no processes currently updating the log file
* Each line in the log format has the correct format. This is to avoid doing input validation.
 