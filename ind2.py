#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from packet.add import add
from packet.help import help
from packet.list import list
from packet.select import select


def main():
    trains = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            train = add()
            trains.append(train)
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('nomer')[::-1])
        elif command == 'list':
            list(trains)
        elif command.startswith('select'):
            print("Введите номер поезда: ")
            nom = input()
            selected = select(trains, nom)
            list(selected)
        elif command == 'help':
            help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
