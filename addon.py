# -*- coding: utf-8 -*-

import control

info = ''
state = control.get_setting('state')
if state == 'true':
    control.turn_off()
    control.set_setting('state', 'false')
    info = 'OFF'
else:
    control.turn_on()
    control.set_setting('state', 'true')
    info = 'ON'

control.send_notification(info)
