#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime


def add():
    punkt_nazn = input("Пункт назначения ")
    nomer = input("Номер поезда? ")
    time_str = input("время отправления? (hh/mm)\n ")
    time = datetime.datetime.strptime(time_str, '%H/%M').time()
    return {
        'punkt_nazn': punkt_nazn,
        'nomer': nomer,
        'time': time,
    }
