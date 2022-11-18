#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list(trains):
    if trains:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "No",
                "Пункт назначиния",
                "Номер поезда",
                "время отправления"
            )
        )
        print(line)
        for idx, train in enumerate(trains, 1):
            time = train.get('time', '')
            print(
                '| {:>4} | {:<30} | {:<20} | {}{} |'.format(
                    idx,
                    train.get('punkt_nazn', ''),
                    train.get('nomer', ''),
                    time,
                    ' ' * 5
                )
            )
        print(line)