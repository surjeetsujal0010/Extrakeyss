import os
os.system("clear")

name = '''\033[1;33;45m

#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#
0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0
#0                                                 0#
0#      .d8888b.       .d8888b.       .d8888b.     #0
#0     d88P  Y88b     d88P  Y88b     d88P  Y88b    0#
0#     888    888     Y88b.          888    888    #0
#0     888             "Y888b.       888           0#
0#     888                "Y88b.     888  88888    #0
#0     888    888           "888     888    888    0#
0#     Y88b  d88P d8b Y88b  d88P d8b Y88b  d88P    #0
#0      "Y8888P"  Y8P  "Y8888P"  Y8P  "Y8888P88    0#
0#                                                 #0
#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#
0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0

'''

print (name)

menu = '''\033[1;31;40m
                 *****Menu*****
\033[1;34;40m
{1}--> Extrakeys options
{2}--> Addextrakeys
{3}--> saved extrakey
{0}--> Exit
'''
print (menu)

ch = input("Select choice  from 1 to 00 -->\033[1;32;40m ")
choice = str(ch) and int(ch)
if choice==1:
 os.chdir("/data/data/com.termux/files/usr/C.S.G/Extrakeyss/.core")
 os.system("bash extrak.sh")
  
elif choice==2:
 os.chdir("/data/data/com.termux/files/usr/C.S.G/Extrakeyss/.core")
 os.system("python adex.py")

elif choice==3:
 os.chdir("/data/data/com.termux/files/usr/C.S.G/Extrakeyss/.core")
 os.system("cp termux.properties /data/data/com.termux/files/home/.termux/")
 os.system("clear")
 print ("***** yours saved extrakeys are ready *****")
 os.system("termux-reload-settings")
 print ("\033[1;37;40m")

elif choice==0:
 os.system("exit")

else:
 os.system("python install.py")

