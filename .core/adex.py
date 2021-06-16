import os
import sys

name = '''\033[1;31;40m

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
                *****EXTRAKEYS*****
\033[1;33;40m
{1}--> cd ..       {11}--> ↑
{2}--> ls -a       {12}--> ↓
{3}--> NANO        {13}--> ←
{4}--> HOME        {14}--> →
{5}--> PAGEUP      {15}--> /
{6}--> END         {16}--> ×
{7}--> TAB         {17}--> -
{8}--> CTRL        {18}--> "
{9}--> ALT         {19}--> '
{10}--> PAGEDOWN   {20}--> &

'''
print (menu)

def info():


  A = "cd .."
  B = "ls -a"
  C = "nano"
  D = "HOME"
  E = "PGUP"
  F = "END"
  G = "TAB"
  H = "CTRL"
  I = "ALT"
  J = "PGDN"
  K = "UP"
  L = "DOWN"
  M = "LEFT"
  N = "RIGHT"
  O = "/"
  P = "*"
  Q = "-"
  R = '"'
  S = "'"
  T = "&"


  profile = {}
  print ("\033[1;31;40m")
  print ("-->FIRST LINE ")
  print ("")
  a = input("\033[1;34;40mfirst code:-->\033[1;32;40m")
  profile["a"] = str(a) and int(a)
  if profile["a"] == 1:
     profile["a"] = A
  elif profile["a"] == 2:
     profile["a"] = B
  elif profile["a"] == 3:
     profile["a"] = C
  elif profile["a"] == 4:
     profile["a"] = D
  elif profile["a"] == 5:
     profile["a"] = E
  elif profile["a"] == 6:
     profile["a"] = F
  elif profile["a"] == 7:
     profile["a"] = G
  elif profile["a"] == 8:
     profile["a"] = H
  elif profile["a"] == 9:
     profile["a"] = I
  elif profile["a"] == 10:
     profile["a"] = J
  elif profile["a"] == 11:
     profile["a"] = K
  elif profile["a"] == 12:
     profile["a"] = L
  elif profile["a"] == 13:
     profile["a"] = M
  elif profile["a"] == 14:
     profile["a"] = N
  elif profile["a"] == 15:
     profile["a"] = O
  elif profile["a"] == 16:
     profile["a"] = P
  elif profile["a"] == 17:
     profile["a"] = Q
  elif profile["a"] == 18:
     profile["a"] = R
  elif profile["a"] == 19:
     profile["a"] = S
  elif profile["a"] == 20:
     profile["a"] = T

  b = input("\033[1;34;40msecond code:-->\033[1;32;40m")
  profile["b"] = str(b) and int(b)
  if profile["b"] == 1:
     profile["b"] = A
  elif profile["b"] == 2:
     profile["b"] = B
  elif profile["b"] == 3:
     profile["b"] = C
  elif profile["b"] == 4:
     profile["b"] = D
  elif profile["b"] == 5:
     profile["b"] = E
  elif profile["b"] == 6:
     profile["b"] = F
  elif profile["b"] == 7:
     profile["b"] = G
  elif profile["b"] == 8:
     profile["b"] = H
  elif profile["b"] == 9:
     profile["b"] = I
  elif profile["b"] == 10:
     profile["b"] = J
  elif profile["b"] == 11:
     profile["b"] = K
  elif profile["b"] == 12:
     profile["b"] = L
  elif profile["b"] == 13:
     profile["b"] = M
  elif profile["b"] == 14:
     profile["b"] = N
  elif profile["b"] == 15:
     profile["b"] = O
  elif profile["b"] == 16:
     profile["b"] = P
  elif profile["b"] == 17:
     profile["b"] = Q
  elif profile["b"] == 18:
     profile["b"] = R
  elif profile["b"] == 19:
     profile["b"] = S
  elif profile["b"] == 20:
     profile["b"] = T


  c = input("\033[1;34;40mthird code:-->\033[1;32;40m")
  profile["c"] = str(c) and int(c)
  if profile["c"] == 1:
     profile["c"] = A
  elif profile["c"] == 2:
     profile["c"] = B
  elif profile["c"] == 3:
     profile["c"] = C
  elif profile["c"] == 4:
     profile["c"] = D
  elif profile["c"] == 5:
     profile["c"] = E
  elif profile["c"] == 6:
     profile["c"] = F
  elif profile["c"] == 7:
     profile["c"] = G
  elif profile["c"] == 8:
     profile["c"] = H
  elif profile["c"] == 9:
     profile["c"] = I
  elif profile["c"] == 10:
     profile["c"] = J
  elif profile["c"] == 11:
     profile["c"] = K
  elif profile["c"] == 12:
     profile["c"] = L
  elif profile["c"] == 13:
     profile["c"] = M
  elif profile["c"] == 14:
     profile["c"] = N
  elif profile["c"] == 15:
     profile["c"] = O
  elif profile["c"] == 16:
     profile["c"] = P
  elif profile["c"] == 17:
     profile["c"] = Q
  elif profile["c"] == 18:
     profile["c"] = R
  elif profile["c"] == 19:
     profile["c"] = S
  elif profile["c"] == 20:
     profile["c"] = T


  d = input("\033[1;34;40mfourth code:-->\033[1;32;40m")
  profile["d"] = str(d) and int(d)
  if profile["d"] == 1:
     profile["d"] = A
  elif profile["d"] == 2:
     profile["d"] = B
  elif profile["d"] == 3:
     profile["d"] = C
  elif profile["d"] == 4:
     profile["d"] = D
  elif profile["d"] == 5:
     profile["d"] = E
  elif profile["d"] == 6:
     profile["d"] = F
  elif profile["d"] == 7:
     profile["d"] = G
  elif profile["d"] == 8:
     profile["d"] = H
  elif profile["d"] == 9:
     profile["d"] = I
  elif profile["d"] == 10:
     profile["d"] = J
  elif profile["d"] == 11:
     profile["d"] = K
  elif profile["d"] == 12:
     profile["d"] = L
  elif profile["d"] == 13:
     profile["d"] = M
  elif profile["d"] == 14:
     profile["d"] = N
  elif profile["d"] == 15:
     profile["d"] = O
  elif profile["d"] == 16:
     profile["d"] = P
  elif profile["d"] == 17:
     profile["d"] = Q
  elif profile["d"] == 18:
     profile["d"] = R
  elif profile["d"] == 19:
     profile["d"] = S
  elif profile["d"] == 20:
     profile["d"] = T


  e = input("\033[1;34;40mfifth code:-->\033[1;32;40m")
  profile["e"] = str(e) and int(e)
  if profile["e"] == 1:
     profile["e"] = A
  elif profile["e"] == 2:
     profile["e"] = B
  elif profile["e"] == 3:
     profile["e"] = C
  elif profile["e"] == 4:
     profile["e"] = D
  elif profile["e"] == 5:
     profile["e"] = E
  elif profile["e"] == 6:
     profile["e"] = F
  elif profile["e"] == 7:
     profile["e"] = G
  elif profile["e"] == 8:
     profile["e"] = H
  elif profile["e"] == 9:
     profile["e"] = I
  elif profile["e"] == 10:
     profile["e"] = J
  elif profile["e"] == 11:
     profile["e"] = K
  elif profile["e"] == 12:
     profile["e"] = L
  elif profile["e"] == 13:
     profile["e"] = M
  elif profile["e"] == 14:
     profile["e"] = N
  elif profile["e"] == 15:
     profile["e"] = O
  elif profile["e"] == 16:
     profile["e"] = P
  elif profile["e"] == 17:
     profile["e"] = Q
  elif profile["e"] == 18:
     profile["e"] = R
  elif profile["e"] == 19:
     profile["e"] = S
  elif profile["e"] == 20:
     profile["e"] = T


  f = input("\033[1;34;40msixth code:-->\033[1;32;40m")
  profile["f"] = str(f) and int(f)
  if profile["f"] == 1:
     profile["f"] = A
  elif profile["f"] == 2:
     profile["f"] = B
  elif profile["f"] == 3:
     profile["f"] = C
  elif profile["f"] == 4:
     profile["f"] = D
  elif profile["f"] == 5:
     profile["f"] = E
  elif profile["f"] == 6:
     profile["f"] = F
  elif profile["f"] == 7:
     profile["f"] = G
  elif profile["f"] == 8:
     profile["f"] = H
  elif profile["f"] == 9:
     profile["f"] = I
  elif profile["f"] == 10:
     profile["f"] = J
  elif profile["f"] == 11:
     profile["f"] = K
  elif profile["f"] == 12:
     profile["f"] = L
  elif profile["f"] == 13:
     profile["f"] = M
  elif profile["f"] == 14:
     profile["f"] = N
  elif profile["f"] == 15:
     profile["f"] = O
  elif profile["f"] == 16:
     profile["f"] = P
  elif profile["f"] == 17:
     profile["f"] = Q
  elif profile["f"] == 18:
     profile["f"] = R
  elif profile["f"] == 19:
     profile["f"] = S
  elif profile["f"] == 20:
     profile["f"] = T


  while True:
    try:
      print ("")
      choose = input("\033[1;32;40mDo you want second line:(y/n):-->")
      if choose == "y":
         print ("")
         print ("\033[1;31;40m-->SECOND LINE")
         print ("")
         g = input("\033[1;36;40mfirst code:-->\033[1;32;40m")
         profile["g"] = str(g) and int(g)
         if profile["g"] == 1:
            profile["g"] = A
         elif profile["g"] == 2:
            profile["g"] = B
         elif profile["g"] == 3:
       	    profile["g"] = C
         elif profile["g"] == 4:
            profile["g"] = D
         elif profile["g"] == 5:
            profile["g"] = E
         elif profile["g"] == 6:
            profile["g"] = F
         elif profile["g"] == 7:
            profile["g"] = G
         elif profile["g"] == 8:
            profile["g"] = H
         elif profile["g"] == 9:
            profile["g"] = I
         elif profile["g"] == 10:
            profile["g"] = J
         elif profile["g"] == 11:
            profile["g"] = K
         elif profile["g"] == 12:
            profile["g"] = L
         elif profile["g"] == 13:
            profile["g"] = M
         elif profile["g"] == 14:
            profile["g"] = N
         elif profile["g"] == 15:
            profile["g"] = O
         elif profile["g"] == 16:
            profile["g"] = P
         elif profile["g"] == 17:
            profile["g"] = Q
         elif profile["g"] == 18:
            profile["g"] = R
         elif profile["g"] == 19:
            profile["g"] = S
         elif profile["g"] == 20:
            profile["g"] = T


         h = input("\033[1;36;40msecond code:-->\033[1;32;40m")
         profile["h"] = str(h) and int(h)
         if profile["h"] == 1:
            profile["h"] = A
         elif profile["h"] == 2:
            profile["h"] = B
         elif profile["h"] == 3:
            profile["h"] = C
         elif profile["h"] == 4:
            profile["h"] = D
         elif profile["h"] == 5:
            profile["h"] = E
         elif profile["h"] == 6:
            profile["h"] = F
         elif profile["h"] == 7:
            profile["h"] = G
         elif profile["h"] == 8:
            profile["h"] = H
         elif profile["h"] == 9:
            profile["h"] = I
         elif profile["h"] == 10:
            profile["h"] = J
         elif profile["h"] == 11:
            profile["h"] = K
         elif profile["h"] == 12:
            profile["h"] = L
         elif profile["h"] == 13:
            profile["h"] = M
         elif profile["h"] == 14:
            profile["h"] = N
         elif profile["h"] == 15:
            profile["h"] = O
         elif profile["h"] == 16:
            profile["h"] = P
         elif profile["h"] == 17:
            profile["h"] = Q
         elif profile["h"] == 18:
            profile["h"] = R
         elif profile["h"] == 19:
            profile["h"] = S
         elif profile["h"] == 20:
            profile["h"] = T


         i = input("\033[1;36;40mthird code:-->\033[1;32;40m")
         profile["i"] = str(i) and int(i)
         if profile["i"] == 1:
            profile["i"] = A
         elif profile["i"] == 2:
            profile["i"] = B
         elif profile["i"] == 3:
            profile["i"] = C
         elif profile["i"] == 4:
            profile["i"] = D
         elif profile["i"] == 5:
            profile["i"] = E
         elif profile["i"] == 6:
            profile["i"] = F
         elif profile["i"] == 7:
            profile["i"] = G
         elif profile["i"] == 8:
            profile["i"] = H
         elif profile["i"] == 9:
            profile["i"] = I
         elif profile["i"] == 10:
            profile["i"] = J
         elif profile["i"] == 11:
            profile["i"] = K
         elif profile["i"] == 12:
            profile["i"] = L
         elif profile["i"] == 13:
            profile["i"] = M
         elif profile["i"] == 14:
            profile["i"] = N
         elif profile["i"] == 15:
            profile["i"] = O
         elif profile["i"] == 16:
            profile["i"] = P
         elif profile["i"] == 17:
            profile["i"] = Q
         elif profile["i"] == 18:
            profile["i"] = R
         elif profile["i"] == 19:
            profile["i"] = S
         elif profile["i"] == 20:
            profile["i"] = T



       	 j = input("\033[1;36;40mfourth code:-->\033[1;32;40m")
       	 profile["j"] = str(j) and int(j)
         if profile["j"] == 1:
            profile["j"] = A
         elif profile["j"] == 2:
            profile["j"] = B
         elif profile["j"] == 3:
            profile["j"] = C
         elif profile["j"] == 4:
            profile["j"] = D
         elif profile["j"] == 5:
            profile["j"] = E
         elif profile["j"] == 6:
            profile["j"] = F
         elif profile["j"] == 7:
            profile["j"] = G
         elif profile["j"] == 8:
            profile["j"] = H
         elif profile["j"] == 9:
            profile["j"] = I
         elif profile["j"] == 10:
            profile["j"] = J
         elif profile["j"] == 11:
            profile["j"] = K
         elif profile["j"] == 12:
            profile["j"] = L
         elif profile["j"] == 13:
            profile["j"] = M
         elif profile["j"] == 14:
            profile["j"] = N
         elif profile["j"] == 15:
            profile["j"] = O
         elif profile["j"] == 16:
            profile["j"] = P
         elif profile["j"] == 17:
            profile["j"] = Q
         elif profile["j"] == 18:
            profile["j"] = R
         elif profile["j"] == 19:
            profile["j"] = S
         elif profile["j"] == 20:
            profile["j"] = T
 
         k = input("\033[1;36;40mfifth code:-->\033[1;32;40m")
         profile["k"] = str(k) and int(k)
         if profile["k"] == 1:
            profile["k"] = A
         elif profile["k"] == 2:
            profile["k"] = B
         elif profile["k"] == 3:
            profile["k"] = C
         elif profile["k"] == 4:
            profile["k"] = D
         elif profile["k"] == 5:
            profile["k"] = E
         elif profile["k"] == 6:
            profile["k"] = F
         elif profile["k"] == 7:
            profile["k"] = G
         elif profile["k"] == 8:
            profile["k"] = H
         elif profile["k"] == 9:
            profile["k"] = I
         elif profile["k"] == 10:
            profile["k"] = J
         elif profile["k"] == 11:
            profile["k"] = K
         elif profile["k"] == 12:
            profile["k"] = L
         elif profile["k"] == 13:
            profile["k"] = M
         elif profile["k"] == 14:
            profile["k"] = N
         elif profile["k"] == 15:
            profile["k"] = O
         elif profile["k"] == 16:
            profile["k"] = P
         elif profile["k"] == 17:
            profile["k"] = Q
         elif profile["k"] == 18:
            profile["k"] = R
         elif profile["k"] == 19:
            profile["k"] = S
         elif profile["k"] == 20:
            profile["k"] = T


         l = input("\033[1;36;40msixth code:-->\033[1;32;40m")
         profile["l"] = str(l) and int(l)
         if profile["l"] == 1:
            profile["l"] = A
         elif profile["l"] == 2:
            profile["l"] = B
         elif profile["l"] == 3:
            profile["l"] = C
         elif profile["l"] == 4:
            profile["l"] = D
         elif profile["l"] == 5:
            profile["l"] = E
         elif profile["l"] == 6:
            profile["l"] = F
         elif profile["l"] == 7:
            profile["l"] = G
         elif profile["l"] == 8:
            profile["l"] = H
         elif profile["l"] == 9:
            profile["l"] = I
         elif profile["l"] == 10:
            profile["l"] = J
         elif profile["l"] == 11:
            profile["l"] = K
         elif profile["l"] == 12:
            profile["l"] = L
         elif profile["l"] == 13:
            profile["l"] = M
         elif profile["l"] == 14:
            profile["l"] = N
         elif profile["l"] == 15:
            profile["l"] = O
         elif profile["l"] == 16:
            profile["l"] = P
         elif profile["l"] == 17:
            profile["l"] = Q
         elif profile["l"] == 18:
            profile["l"] = R
         elif profile["l"] == 19:
            profile["l"] = S
         elif profile["l"] == 20:
            profile["l"] = T
         break
      elif choose == "n":
         print ("ok")
         break
      print ("\033[1;31;40mwrong choice")
    except Exception as e:
      print (e)
  storevalue = []
  if choose == "n":
     storevalue = (
     [
      profile["a"],
      profile["b"],
      profile["c"],
      profile["d"],
      profile["e"],
      profile["f"],
     ]
     )
     result = []
     for i in storevalue:
      if i not in result:
         result.append(i)
         for i in result:
          if (i == ''):
              result.remove('')
     k = [result]
  else:
      a = (
      [
       profile["a"],
       profile["b"],
       profile["c"],
       profile["d"],
       profile["e"],
       profile["f"],
      ]
      )
      result1 = []
      for i in a:
       if i not in result1:
          result1.append(i)
          for i in result1:
           if (i == ''):
               result1.remove('')

      b = (
      [
       profile["g"],
       profile["h"],
       profile["i"],
       profile["j"],
       profile["k"],
       profile["l"],
      ]
      )
      result2 = []
      for i in b:
       if i not in result2:
          result2.append(i)
          for i in result2:
           if (i == ''):
               result2.remove('')
      k = [result1, result2]
  x = ("extra-keys = " + str(k))
  
  os.chdir("/data/data/com.termux/files/home/") 
  cd = os.getcwd()
  cd1 = os.path.join(cd, ".termux")
  filename = os.path.join(cd1, "termux.properties")
  os.system("clear")
  print ("\033[1;36;40m*****your extrakeys are ready*****")


  f = open (filename, "w")
  x
  f.write(str(x))
  f.close()

  os.system("termux-reload-settings")

  copy(x)

def copy(x):
  while True:
    try:
      ch = input("\033[1;32;40mDo you want to add this key in saved key (y/n)--> ")
      choice = str(ch)
      if choice == "y":
         os.chdir("/data/data/com.termux/files/usr/C.S.G/Extrakeyss/.core")
         print ("The extrakeys is saved in savedkey")
         break
      elif choice == "n":
         break
      print ("\033[1;31;40mwrong choice")
    except Exception as e:
      print (e)
  f = open ("termux.properties", "w")
  x
  f.write(str(x))
  f.close()

def main():
    info()

if __name__ == "__main__":
    main()


