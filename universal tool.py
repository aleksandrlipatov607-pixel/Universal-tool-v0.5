import time,webbrowser,math,random,string
print ("=starting systems")
time.sleep (2)
print ("=system started")
time.sleep (3)
while 1:	
    print("[UNIVERSAL TOOL V0.5]")
    print ("1:PI")
    print ("2:browser")
    print ("3:password generator")
    chose=input("please select a number:")
    if chose==("1"):
      print (math.pi)
    if chose==("2"):
      web=input("select you url:")
      time.sleep (2)
      webbrowser.open(web)
    if chose == "3":
        p = [random.choice(string.ascii_lowercase),   random.choice(string.ascii_uppercase), random.choice(string.digits), random.choice("!@#$%^&*()")]
        l = int(input("Длина пароля: "))
        p += [random.choice(string.ascii_letters + string. digits + "!@#$%^&*()") for _ in range(l - 4)]
        random.shuffle(p)
        print(f"Пароль: {''.join(p)}")
        time.sleep(3)
