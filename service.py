# -*- coding: utf-8 -*-

import control

state = control.get_setting('state')
control_type = control.get_setting('control_type')
startup_notif = control.get_setting('startup_notif')
info = ''
if control_type == '0':
    if state == 'true':
        control.turn_on()
        info = 'ON'
    else:
        control.turn_off()
        info = 'OFF'
    if startup_notif == 'true':
        control.send_notification(info)
else:
    print()
