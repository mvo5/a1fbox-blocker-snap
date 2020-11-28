#!/usr/bin/python3

# This is taken from:
#  https://github.com/bufemc/a1fbox/blob/master/example2.py
#  from 3c1ab7c 

# This more complex example shows how to connect the modules aka building blocks.
# It listens to the call monitor of the Fritz!Box, and will examine the calls.
# If the score is too bad it will block the call (for the next time) by adding it
# to the blacklisted (has to be configured to do so!) phonebook (here id 2).

# REQUIRED: To enable call monitor dial #96*5* and to disable dial #96*4.
# REQUIRED: A phonebook id where bad calls should be added. Configure it in Fritzbox to decline calls!

# To see some action e.g. call from intern phone 1 to phone 2,
# or use your mobile phone to call the landline. This will print and log the calls.

import os

from a1fbox.fritzconn import FritzConn
from a1fbox.callmonitor import CallMonitor, CallMonitorLog
from a1fbox.callblocker import CallBlocker, CallBlockerLog

if __name__ == "__main__":

    from config import (FRITZ_IP_ADDRESS, FRITZ_USERNAME)
    print("using {} {}".format(FRITZ_IP_ADDRESS, FRITZ_USERNAME))
    
    
    
    # Initialize by using parameters from config file
    fritzconn = FritzConn()

    # There are two loggers. cm_log logs the raw line from call monitor of Fritzbox,
    # cb_log logs the actions of the call blocker. The CallMonitor uses the
    # CallBlocker and it's parse_and_examine_line method to examine the raw line.

    # Idea: could also define which rating method should be used?
    log_dir = os.getenv("SNAP_DATA")
    print("using log dir: {}".format(log_dir))
    cb_log = CallBlockerLog(log_folder=log_dir, daily=True, anonymize=False)
    cb = CallBlocker(fc=fritzconn, whitelist_pbids=[0], blacklist_pbids=[1, 2], blocklist_pbid=2,
                     blockname_prefix='[Spam] ', min_score=6, min_comments=2, logger=cb_log.log_line)

    cm_log = CallMonitorLog(log_folder=log_dir,daily=True, anonymize=False)
    cm = CallMonitor(host=fritzconn.address, logger=cm_log.log_line, parser=cb.parse_and_examine_line)
