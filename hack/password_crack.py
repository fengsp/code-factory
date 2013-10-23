# -*- coding: utf-8 -*-
import crypt


def test_pass(crypt_pass):
    salt = crypt_pass[0:2]
    dict_file = open('dictionary.txt', 'r')
    for word in dict_file.readlines():
        word = word.strip('\n')
        crypted = crypt.crypt(word, salt)
        if (crypted == crypt_pass):
            print "[+] Found Password: " + word
            return
    print "[-] Password Not Found."
    return


def main():
    pass_file = open('password.txt')
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            crypt_pass = line.split(':')[1].strip()
            print "[*] Cracking Password For: " + user
            test_pass(crypt_pass)
            print


if __name__ == "__main__":
    main()
