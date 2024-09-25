#!/usr/bin/python
import socket
import requests
import psutil
import time
import datetime
import settings as settings

from time import strftime
from time import gmtime

def seconds_elapsed():
    '''get seconds since boot time'''
    return time.time() - psutil.boot_time()

def sec2time(sec, n_msec=3):
    ''' Convert seconds to 'D days, HH:MM:SS.FFF' '''
    if hasattr(sec,'__len__'):
        return [sec2time(s) for s in sec]
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if n_msec > 0:
        pattern = '%%02d hours, %%02d min, %%0%d.%df sec' % (n_msec+3, n_msec)
    else:
        pattern = r'%02d hours, %02d min, %02d sec'
    if d == 0:
        return pattern % (h, m, s)
    return ('%d days, ' + pattern) % (d, h, m, s)

def get_ip():
    '''get current IP Address'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# post connectivity and uptime datahub
r = requests.post("https://" + settings.deviceLoggerAPI + "/api/log/", data={'device': socket.gethostname(), 'value1': get_ip(), 'value2': sec2time(seconds_elapsed())})
print(r.status_code, r.reason)
print(r.text)

