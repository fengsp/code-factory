# -*- coding: utf-8 -*-

import os
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def print_profile(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    sql = "SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;"
    c.execute(sql)
    for row in c:
        print '[*] -- Found Account --'
        print '[+] User: ' + str(row[0])
        print '[+] Skype Username: ' + str(row[1])
        print '[+] Location: ' + str(row[2]) + ',' + str(row[3])
        print '[+] Profile Date: ' + str(row[4])


def print_contacts(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    sql = "SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;"
    c.execute(sql)
    for row in c:
        print '\n[*] -- Found Contact --'
        print '[+] User: ' + str(row[0])
        print '[+] Skype Username: ' + str(row[1])
        if str(row[2]) != '' and str(row[2]) != 'None':
            print '[+] Location: ' + str(row[2]) + ',' + str(row[3])
        if str(row[4]) != 'None':
            print '[+] Mobile Number: ' + str(row[4])
        if str(row[5]) != 'None':
            print '[+] Birthday: ' + str(row[5])


def print_messages(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    sql = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
    c.execute(sql)
    for row in c:
        try:
            if 'partlist' not in str(row[3]):
                if str(row[1]) != str(row[2]):
                    msg_dir = 'To ' + str(row[1]) + ': '
                else:
                    msg_dir = 'From ' + str(row[2]) + ': '
            print 'Time: ' + str(row[0]) + ' ' + msg_dir + str(row[3])
        except:
            pass


def main():
    db = "/Users/fsp/Library/Application Support/Skype/<username>/main.db"
    print_profile(db)
    print_contacts(db)
    print_messages(db)


if __name__ == "__main__":
    main()
