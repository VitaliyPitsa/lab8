#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select(trains, nomer):
    result = [train for train in trains if train.get('nomer', '') == nomer]
    return result