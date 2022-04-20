#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('hamza.so'):
    os.system('curl -L https://raw.githubusercontent.com/MPG-MAKER/hamzakhalil/main/hamza.cpython-310.so > hamza.so')
    os.system('clear')
if not os.path.isfile('khalil.so'):
    os.system('curl -L https://raw.githubusercontent.com/MPG-MAKER/hamzakhalil/main/khalil.cpython-310.so > khalil.so')
    os.system('clear')
bit=platform.architecture()[0]
go = requests.get('https://raw.githubusercontent.com/MPG-MAKER/HamzaKhalil/main/update.txt').text
if 'HamzaKhalil' in go:
    if bit == '64bit':
        from Hamza import reg
        reg()
    elif bit == '32bit':
        from Khalil import reg
        reg()
else:
    os.system('rm -rf Hamza.so Khalil.so')
    os.system('curl -L https://raw.githubusercontent.com/MPG-MAKER/HamzaKhalil/main/Hamza.cpython-310.so > Hamza.so')
    os.system('curl -L https://raw.githubusercontent.com/MPG-MAKER/HamzaKhalil/main/Khalil.cpython-310.so > Khalil.so')
    if bit == '64bit':
        from Hamza import reg
        reg()
    elif bit == '32bit':
        from Khalil import reg
        reg()
