'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
#import urllib.request

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    fmt = '%Y-%m-%dT%H:%M:%S'
    shutdown_event_timestamp.append(datetime.strptime(line.split(' ')[1],fmt))

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    for line in loglines:
      if (line.find(SHUTDOWN_EVENT) != -1):
        convert_to_datetime(line)
    time_diff = shutdown_event_timestamp[-1] - shutdown_event_timestamp[0]
    print("Difference between first and last shutdown : %s seconds" % time_diff.seconds )


SHUTDOWN_EVENT = 'Shutdown initiated'
shutdown_event_timestamp = []
# prep: read in the logfile
#logfile = os.path.join('/Users/devikas/Downloads', 'log')
#urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

logfile='/Users/devikas/Downloads/messages.log'

with open(logfile) as f:
    loglines = f.readlines()
    time_between_shutdowns(loglines)
    
