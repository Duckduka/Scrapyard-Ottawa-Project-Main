from random import randint 
warning = 0
yap = 0
print("Welcome to the very useful chatbox! Here you can talk with the bot and find very useful information.(If you want, type hint for some options)")
while True:
  funVal = randint(1,100)
  if funVal >= 0 and funVal <= 10:
    imput = str(input("Please type something in the chat! ")).lower()
  else:
    imput = str(input("Enter some text or ask a question! ")).lower()
  text = randint(1,35)
  if len(imput) < 150:
    if "hack club" in imput or "scrapyard" in imput:
      if funVal >= 11 and funVal <= 15:
        print("Very cool! Nice!!!")
      else:
        print("Nice.")
    if "fuck" in imput or "bitch" in imput or "stupid" in imput or "idiot" in imput or "nigg" in imput or "shit" in imput or "crap" in imput or "ass" in imput:
      print("STOP SWEARING!!!!!!!!!!")
      if funVal == 16:
        for i in range(500):
          print("Error")
        break
      else:
        warning += 1
        if warning == 1:
          swear = str(input("You have been given a warning. Do you wish to continue?(Yes to continue.)")).lower()
          if swear == "yes" or swear == "y":
            continue
          else: 
            print("Alright then.")
            break
  
        else:
          print("You lost your chance.")
          break
    if imput == "hint":
      print("----------------------------------------------------------------------------------------------------------------------------------")
      print('Things you could type: "yap", "nothing", "chess", "egg", etc... *There may be a variety of easter eggs in this project! So make sure to explore each command thoroughly! (For example, some commands may need repeated typing, while others have luck playing as their biggest factor. Try to find all of the eggs! Good luck!)')
      print("-----------------------------------------------------------------------------------------------------------------------------------")
    elif imput == "fun value":
      print("Sorry, I can't do that.")
    elif imput == "yap":
      if yap < 10:
        yap = yap + 1
        if yap <= 2:
          print("Okay.")
        elif yap >= 3 and yap <= 5:
          print("Okay, please stop yapping so much!")
        elif yap >= 6 and yap <= 8:
          print("Just stop yapping.")
        else:
          print()
          if funVal >= 40 and funVal <= 42:
            print("S T O P  Y A P P I N G")
          elif funVal >= 43 and funVal <= 53:
            print("PLEASE STOP YAPPERING")
          else:
            print("You yap too much, take a break.")
          break
    elif imput == "battle cats" or imput == "the battle cats":
      if funVal == 22:
        print("Cat")
      else:
        print("Battle Cats is cool.")
    elif imput == "stop" or imput == "stop it" or imput == "stop it.":
      print("Nah, I'd win.")
    elif imput == "booster" or imput == "fighter" or imput == "triangle":
      if funVal >= 23 and funVal <= 28:
        print("I've got places to be.")
      else:
        print("Cool.")
    elif imput == "lasvoss" or imput == "lazvoz":
      print("The Boss Executioner.")
    elif imput == "nothing":
      if funVal == 32:
        print()
        print("missing.")
        break
      else:
        print("aw man")
    elif imput == "" or imput == "...":
      if funVal >= 29 and funVal <= 31:
        print("Nothing.")
      else:
        print("Nothing?")
    elif imput == "i've had enough" or imput == "ive had enough" or imput == "ive had enough." or imput == "i've had enough.":
      spame = randint(2000,5000)
      for y in range(spame):
        print("SPAM", end="")
      print()
    elif imput == "hi":
      print("Bye.")
    elif imput == "baha blast":
      if funVal >= 33 and funVal <= 35:
        print("Ponos destroyed their own game.")
      else:
       bahamut = randint(1,3)
       if bahamut == 1:
         print("235 NP for the most OP talent?")
       elif bahamut == 2:
         print("BAHAMUT OP YAY")
       else:
          print("Bahamut king")
    elif imput == "chess":
      if funVal >= 36:
        print("Bishop snipe")
      else:
        print("Bishop check!")
    elif imput == "what?":
      print("Huh?")
    elif imput == "some text or ask a question!":
      if funVal >= 17 and funVal <= 22:
        print("If you are going to just copy me, go ahead.")
      else:
        print("Hey! I didn't want you to say it LITERALLY!")
    elif imput == "seven":
      print("Seven of what?")
    elif imput == "easter egg" or imput == "easter eggs" or imput == "egg" or imput == "eggs":
      egg = randint(1,1000)
      if egg <= 1 and egg >= 20:
        print("You are damn lucky.")
      elif egg >= 21 and egg <= 200:
        print("You have ok luck")
      elif egg >= 201 and egg <= 250:
        print("You have decent luck.")
      elif egg == 337:
        print("XXX Broken XXX")
      else:
        print("You have bad luck!")
    else:
      if text == 1:
        print("Have a good day!")
      elif text == 2:
        print("Could you please repeat that?")
      elif text == 3:
        print("What?")
      elif text == 4:
        print("Sorry, I'm too lazy to respond.")
      elif text == 5:
        rand = randint(30,60)
        for x in range(rand):
          rand2 = randint(1,9)
          print(rand2, end="")
        print()
      elif text == 6:
        print("No comment.")
      elif text == 7:
        print("Life's a beach....")
      elif text == 8:
        print("Hey! Say that again please!")
      elif text == 9:
        print("I know!")
      elif text == 10:
        print("Thanks!")
      elif text == 11:
        print("You're welcome!")
      elif text == 12:
        print("Nah.")
      elif text == 13:
        print("Coding is the best!")
      elif text == 14:
        print("Yes.")
      elif text == 15:
        print("No.")
      elif text == 16:
        print("I know right?")
      elif text == 17:
        print("Good job!")
      elif text == 18:
        print("Thanks for the compliment.")
      elif text == 19:
        if funVal >= 93 and funVal <= 96:
          print("one two three four five six seven Seven sSevVen 7sEv=en sVen 0sE7n SevvevvVvvvvVVVV")
        else:
          print("One plus one equals three.")
      elif text == 20:
        if funVal >= 97:
          print("gar gar")
        else:
          print("grr grr")
      elif text == 21:
        print("What do you mean?")
      elif text == 22:
        if funVal >= 85 and funVal <= 88:
          print("r3537 7ry 4641n r3537 7ry 4641n r3537 7ry 4641n r3537 7ry 4641n r3537 7ry 4641n r3537 7ry 4641n")
        else:
          print("Sorry, try again.")
      elif text == 23:
        print("I'm too busy.")
      elif text == 24:
        print("I don't understand.")
      elif text == 25:
        if funVal >= 89 and funVal <= 92:
          print("FILE 01 - [REDACTED]")
        elif funVal == 66:
          aster = randint(66,66)
          if aster == 66:
            print("☼︎☜︎👎︎✌︎👍︎❄︎☜︎👎︎")
        else:
          print("Chatbox isn't working. Please try again.")
      elif text == 26:
        print("Go away.")
      elif text == 27:
        print("That's interesting.")
      elif text == 28:
        print("Sorry, What?")
      elif text == 29:
        print("Maybe ask someone else?")
      elif text == 30:
        print("Shoo! Get out!")
      elif text == 31:
        stand = randint(1,100)
        if stand == 1:
          if "help" in imput and "please" in imput:
            print("Unable to process command.")
          else:
            print("Your answer was not found.")
        elif stand >=2 and stand <= 10:
          if "help" in imput and "please" in imput:
            print("Sorry, can't help you now, try again.")
          else:
            print("An error occurred. Try again.")
        else:
          if "help" in imput and "please" in imput:
            print("Sorry, I can't help you with that.")
          else:
            print("Wait, I can't do that right now.")
      elif text == 32:
        if warning == 0:
          print("Do you want an apple?")
        else:
          if funVal >=75 and funVal <= 79:
            print("I KNOW WHAT YOU DID.")
          else:
            print("Have you learned your lesson?")
          
  
  else:
    if funVal >= 80 and funVal <= 88:
      print("Your chat has closed.")
    else:
      print("You talk too much.")
    break
