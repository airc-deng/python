#!/usr/bin/env python

import os

def addContact(name, number):
    #ctlist = [name, ': ', number]
    str = name + ': ' + number + '\n'
    f = open("contacts.txt", "a+")
    f.write(str)
    f.close()

def main():
    nam = input("name:")
    tel = input("phone:")
    addContact(nam, tel)
    return

main()
