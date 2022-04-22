# Utilities

import getpass
import time


def validate_secret_input(msg, opts):
    resp = getpass.getpass(prompt=msg)
    if not resp.lower().strip() in opts:
        resp = validate_secret_input(msg, opts)
    return resp


def validate_int_input(msg, opts):
    resp = input(msg).lower().strip()
    try:
        answer = int(resp)
        if answer not in opts:
            resp = validate_int_input(msg, opts)
        else:
            return answer
    except ValueError:
        resp = validate_int_input(msg, opts)
    return resp


def print_wait(msg):
    print(msg)
    time.sleep(2)
