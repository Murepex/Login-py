import os
from time import sleep
import random

def clear():
    os.system("cls||clear")
    print("  _                 _        __      ____ _  _   ")
    print(" | |               (_)       \ \    / /_ | || |  ")
    print(" | |     ___   __ _ _ _ __    \ \  / / | | || |_ ")
    print(" | |    / _ \ / _` | | '_ \    \ \/ /  | |__   _|")
    print(" | |___| (_) | (_| | | | | |    \  /   | |_ | |  ")
    print(" |______\___/ \__, |_|_| |_|     \/    |_(_)|_|  ")
    print("               __/ |                             ")
    print("              |___/                              ")
    print("_________________________________________________")

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Lottery Leaderboard------------------------------------------------------------------------------------------------------

leaderboardpath = "Data/System/Leaderboard.lot"

def leaderboard(path, username):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    broketimes = lines[1]
    broketimes = broketimes.split("\n")
    broketimes = broketimes [0]
    highscore = lines[2]
    highscore = highscore.split("\n")
    highscore = highscore [0]
    c = 0
    rankfound = False
    top5 = []
    try:
        file = open(leaderboardpath, "r")
        for line in file:
            rsplit = line.split(",")
            rscore = rsplit[0]
            rname = rsplit[1]
            rname = rname.split("\n")
            rname = rname[0]
            if rname.upper().lower() == username.upper().lower():
                rankfound = True
                rank = c + 1
            if c <= 5:
                top5.append(rscore + "," + rname)
            else:
                if rankfound == True:
                    break
            c =+ 1
        file.close()
        if top5 != []:
            print(color.BOLD + "TOP 5 Player" + color.END)
            print("-------------------------------------------------------")
            print("{:<3}".format("Rank") + "  " + "{:<16}".format("Name") + "  " + "{:<9}".format("Highscore"))
            c = 1
            for p in top5:
                psplit = p.split(",")
                pscore = psplit[0]
                pname = psplit[1]
                print("{:<3}".format(str(c)) + "  " + "{:<16}".format(" " + pname) + "  " + "{:<9}".format(" " + str(pscore)))
                c = c + 1
            print("-------------------------------------------------------")
            print(color.BOLD + "Your Stats" + color.END)
            print("{:<3}".format("Rank") + "  " + "{:<16}".format("Name") + "  " + "{:<9}".format("Highscore") + "  " + "{:<9}".format("Went Broke (Times)"))
            print("{:<3}".format(str(rank)) + "  " + "{:<16}".format(" " + username) + "  " + "{:<9}".format(str(" " + highscore)) + "  " + "{:<9}".format(str(" " + broketimes)))
        else:
            print("-------------------------------------------------------")
            print("No one yet...")
            print("-------------------------------------------------------")
        input("Press enter to continue")
        clear()
    except FileNotFoundError:
        print("-------------------------------------------------------")
        print("No one yet...")
        print("-------------------------------------------------------")
        input("Press enter to continue")
        clear()

def updateleaderboard(insert):
    repeat = True
    while repeat == True:
        try:
            file = open(leaderboardpath, "r")
            lines = file.readlines()
            file.close()
            c = 0
            file = open(leaderboardpath, "r")
            for line in file:
                split = line.split("\n")
                replace = split[0]
                lines.remove(line)
                lines.insert(c,replace)
                c =+ 1
            file.close()

            isplit = insert.split(",")
            iscore = isplit[0]
            iname = isplit[1]

            newplayer = True
            for line in lines:
                rsplit = line.split(",")
                rscore = rsplit[0]
                rname = rsplit[1]
                if rname.upper().lower() == iname.upper().lower():
                    lines.remove(line)
                    lines.append(iscore + "," + iname)
                    newplayer = False
            if newplayer == True:
                lines.append(iscore + "," + iname)

            toplist = ["0,END"]
            c = 0
            while c < len(lines):
                data = lines[c]
                split = data.split(",")
                score = split[0]
                name = split[1]
                rankc = 0
                for rank in toplist:
                    rsplit = rank.split(",")
                    rscore = rsplit[0]
                    rname = rsplit[1]
                    if int(score) > int(rscore):
                        toplist.insert(rankc,data)
                        break
                    rankc += 1
                c += 1
            toplist.remove("0,END")
            print(toplist)

            strc = 0
            topliststr = ""
            for rank in toplist:
                ranknewline = rank + "\n"
                topliststr = topliststr + ranknewline
                strc += 1

            file = open(leaderboardpath, 'r')
            content = file.read()
            content = content.replace(content, topliststr)
            file.close()

            file = open(leaderboardpath, 'w')
            file.write(content)
            file.close()
            repeat = False
        except FileNotFoundError:
            file = open(leaderboardpath, "w")
            file.write(insert + "\n")
            file.close()

#Lottery------------------------------------------------------------------------------------------------------


random.seed()

def lottery(path, username):
    money = 1
    lottery = 1
    print("!Welcome to Lottery!")
    sleep(1)
    print("The money you play with can be multiplied, divided, subtracted, added up (You can go broke)")
    sleep(5)
    print("Have fun losing :)")
    sleep(3)
    while lottery == 1:
        file = open(path, 'r')
        lines = file.readlines()
        file.close()
        try:
            score = lines[1]
            try:
                score = lines[2]
            except:
                file = open(path, 'w')
                file.write("0\n")
                file.close()
        except:
            file = open(path, 'w')
            file.write("0\n")
            file.close()
        if money < 1:
            print("You went broke!")
            file = open(path, 'r')
            lines = file.readlines()
            timeswentbroke = lines[1]
            timeswentbroke = timeswentbroke.split("\n")
            timeswentbroke = int(timeswentbroke[0])
            timeswentbrokeset = str(timeswentbroke + 1)
            file.close()
            replaceline = ""
            line_number = 0
            file = open(path, 'r')
            for line in file:
                line = line.strip()
                if line_number == 1:
                    newline = line.replace(str(timeswentbroke), timeswentbrokeset)
                else:
                    newline = line
                replaceline = replaceline + newline + "\n"
                line_number = line_number + 1
            file.close()
            wfile = open(path, 'w')
            wfile.write(replaceline)
            wfile.close()
            input("Press enter to continue")
            break
        else:
            print("Bank balance: " + str(money))
            try:
                money_to_play = int(input("Enter how much money you want to play with: "))
            except ValueError:
                print("pls just use integers not anything else")
            except TypeError:
                print("pls just use integers not anything else")
            if money != "":
                if int(money_to_play) > money:
                    print("You don't have enough money.")
                else:
                    if int(money_to_play) < 1:
                        print("Why so less?")
                    else:
                        money -= int(money_to_play)
                        print("Spinning the Wheel for +,-,*,:")
                        s = 0
                        while s <= 2:
                            justshow = random.randint(1, 4)
                            if justshow == 1:
                                print("addition +")
                            elif justshow == 2:
                                print("subtraction -")
                            elif justshow == 3:
                                print("multiplication *")
                            elif justshow == 1:
                                print("division :")
                            if s <= 1:
                                s = s + 0.1
                            elif s < 2:
                                s = s + 0.2
                            elif s == 2:
                                s = 3
                            sleep(s)
                        mathidontlike = random.randint(1, 4)
                        print("And the result is:")
                        sleep(2)
                        if mathidontlike == 1:
                            print("addition +")
                        if mathidontlike == 2:
                            print("subtraction -")
                        if mathidontlike == 3:
                            print("multiplication *")
                        if mathidontlike == 4:
                            print("division :")
                        sleep(2)
                        print("Processing...")
                        sleep(3)
                        print("Spinning the FINAL-Wheel...")
                        s = 0
                        while s <= 2:
                            justshow = random.randint(1, 100)
                            print(justshow)
                            if s <= 1:
                                s = s + 0.1
                            elif s < 2:
                                s = s + 0.2
                            elif s == 2:
                                s = 3
                            sleep(s)
                        WINNUMBER = random.randint(1, 100)
                        print("And the FINAL-NUMBER")
                        sleep(2)
                        print("IS")
                        sleep(2)
                        print("!!!!!" + str(WINNUMBER) + "!!!!!")
                        sleep(2)
                        if mathidontlike == 1:
                            print("+")
                        if mathidontlike == 2:
                            print("-")
                        if mathidontlike == 3:
                            print("*")
                        if mathidontlike == 4:
                            print(":")
                        sleep(2)
                        print(int(money_to_play))
                        sleep(1)
                        print("=")
                        sleep(2)
                        if mathidontlike == 1:
                            winamount = int(money_to_play)+int(WINNUMBER)
                        if mathidontlike == 2:
                            winamount = int(money_to_play)-int(WINNUMBER)
                        if mathidontlike == 3:
                            winamount = int(money_to_play)*int(WINNUMBER)
                        if mathidontlike == 4:
                            winamount = int(money_to_play)/int(WINNUMBER)
                        if winamount < 1:
                            if winamount < 0:
                                print("You Lost! Final Result: -" + str(winamount))
                                money += int(winamount)
                            else:
                                print("You Lost! Final Result: " + str(winamount))
                                money += int(winamount)
                        else:
                            money += int(winamount)
                            file = open(path, 'r')
                            lines = file.readlines()
                            highscore = lines[2]
                            highscoreint = highscore.split("\n")
                            highscoreint = int(highscoreint[0])
                            file.close()
                            if money > highscoreint:
                                replaceline = ""
                                line_number = 0
                                file = open(path, 'r')
                                for line in file:
                                    line = line.strip()
                                    if line_number == 2:
                                        newline = line.replace(str(highscoreint), str(money))
                                    else:
                                        newline = line
                                    replaceline = replaceline + newline + "\n"
                                    line_number = line_number + 1
                                file.close()
                                wfile = open(path, 'w')
                                wfile.write(replaceline)
                                wfile.close()
                                updateleaderboard(str(money) + "," + str(username))
                                print("!New Highscore!")
                            if winamount < 10:
                                print("Something! Final Result: +" + str(winamount))
                            elif winamount < 30:
                                print("Well thats better! Final Result: +" + str(winamount))
                            elif winamount < 60:
                                print("Pretty Good, no complains! Final Result: +" + str(winamount))
                            elif winamount < 80:
                                print("NICE SHOT! Final Result: +" + str(winamount))
                            elif winamount < 100:
                                print("NEARLY THERE! Final Result: +" + str(winamount))
                            elif winamount < 500:
                                print("SHEEEEEEEEEESH! Final Result: +" + str(winamount))
                            elif winamount > 500:
                                print("SUIIIIIIIIIIIIII! Final Result: +" + str(winamount))

#Login------------------------------------------------------------------------------------------------------

def changepass(path):
    clear()
    print("Change Password!")
    print("")
    oldpw = ""
    while oldpw == "":
        oldpw = input("Old Password: ")
        file = open(path, 'r')
        lines = file.readlines()
        file.close()
        passwd = lines[0]
        x = 0
        while x < len(oldpw):
            try:
                converted = converted + (str(ord(oldpw[x])))
                x = x + 1
            except NameError:
                converted = (str(ord(oldpw[x])))
                x = x + 1
        oldconverted = converted + "\n"
        if oldconverted == passwd:
            repeat = True
            while repeat:
                newpw = ""
                while newpw == "":
                    newpw = input("New Password: ")
                newpw2 = ""
                while newpw2 == "":
                    newpw2 = input("Repeat Password: ")
                if newpw == newpw2:
                    repeat = False
                    encrypted = ""
                    x = 0
                    while x < len(newpw):
                        encrypted = encrypted + (str(ord(newpw[x])))
                        x = x + 1
                    file = open(path, 'r')
                    replaceline = ""
                    for line in file:
                        line = line.strip()
                        newline = line.replace(converted, encrypted)
                        replaceline = replaceline + newline + "\n"
                    file.close()
                    wfile = open(path, 'w')
                    wfile.write(replaceline)
                    wfile.close()
                    return True


                else:
                    print(color.RED + "E: Passwords are not the same!" + color.END)
        else:
            return "Old Password not correct!"
            
def delaccount(path):
    clear()
    if path == "Data/Accounts/Admin.acc":
        print(color.RED + "E: Command not found!" + color.END)
        return "Account deletion canceled!"
    else:
        print("Delete Account!")
        print("")
        pw = ""
        while pw == "":
            pw = input("Password: ")
            file = open(path, 'r')
            lines = file.readlines()
            file.close()
            passwd = lines[0]
            x = 0
            while x < len(pw):
                try:
                    converted = converted + (str(ord(pw[x])))
                    x = x + 1
                except NameError:
                    converted = (str(ord(pw[x])))
                    x = x + 1
            converted = converted + "\n"
            if converted == passwd:
                q = input("Are you sure you want to delete that account? [Y/N]")
                if q == "Y":
                    os.remove(path)
                    return True
                elif q == "y":
                    os.remove(path)
                    return True
                else:
                    return "Account deletion canceled!"

LegalCharacters = ["0","1","2","3","4","5","6","7","8","9","-","_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

clear()
while True:
    converted = ""
    try:
        os.mkdir("Data")
        os.mkdir("Data/Accounts")
        os.mkdir("Data/System")
    except PermissionError:
        print(color.RED + "It seems like the program doesnt has permission to write/read" + color.END)
        input("Press enter to close")
        exit()
    except FileExistsError:
        try:
            file = open("Data/Accounts/Admin.acc", 'r')
            file.close()
            del converted
            illegalcheck = True
            while illegalcheck == True:
                u = input("Username: ")
                if len(u) >= 3 and len(u) <= 16:
                    illegalcheck = False
                    for x in u:
                        if x not in LegalCharacters:
                            illegalcheck = True
                            print(color.RED + "E: You can only use the Characters A-Z, a-z , 0-9, - and _"+ color.END)
                            break
                else:
                    print(color.RED + "E: The Username has to be between 3-16 Characters" + color.END)
            if illegalcheck == False:
                try:
                    path = "Data/Accounts/" + u + ".acc"
                    file = open(path, 'r')
                    lines = file.readlines()
                    file.close()
                    line = lines[0]
                    i = ""
                    while i == "":
                        i = input("Password: ")
                    x = 0
                    while x < len(i):
                        try:
                            converted = converted + (str(ord(i[x])))
                            x = x + 1
                        except NameError:
                            converted = (str(ord(i[x])))
                            x = x + 1
                    converted = converted + "\n"
                    if converted == line:
                        loginactive = True
                        clear()
                        print(f"Welcome, {u}!")
                        print("What do you want to do?")
                        while loginactive:
                            print("")
                            print("1 - Change Password")
                            print("2 - Play Lottery")
                            print("3 - Lottery Leaderboard/Stats")
                            print("4 - Logout")
                            if path.upper().lower() != "Data/Accounts/Admin.acc".upper().lower():
                                print("5 - Delete Account")
                            i = ""
                            i = input("Select a number: ")
                            if i == "1":
                                result = changepass(path)
                                if result == True:
                                    clear()
                                    print("Password succsessfully changed!")
                                else:
                                    clear()
                                    print(color.RED + "E: {result}" + color.END)
                            elif i == "2":
                                clear()
                                print("Loading Lottery...")
                                lottery(path, u)
                            elif i == "3":
                                clear()
                                print("Loading Lottery-Leaderboard...")
                                leaderboard(path, u)
                            elif i == "4":
                                loginactive = False
                                print("")
                                input("Press enter to logout")
                                clear()
                            elif i == "5":
                                if path.upper().lower() == "Data/Accounts/Admin.acc".upper().lower():
                                    clear()
                                    print(color.RED + "E: Command not found!" + color.END)
                                else:
                                    result = delaccount(path)
                                    if result == True:
                                        loginactive = False
                                        print("Files deleted!")
                                        print("")
                                        input("Press enter to logout")
                                        clear()
                                    else:
                                        clear()
                                        print(color.RED + "E: {result}" + color.END)
                            else:
                                clear()
                                print(color.RED + "E: Command not found!" + color.END)
                    else:
                        clear()
                        print(color.RED + "E: Password not correct!" + color.END)
                except FileNotFoundError:
                    print("Username not found!")
                    q = input("Do you want to create that account? [Y/N]:")
                    if q == "Y":
                        clear()
                        print("Username: " + u)
                        i = ""
                        while i == "":
                            i = input("New Password: ")
                        i2 = ""
                        while i2 == "":
                            i2 = input("Repeat password: ")
                        if i == i2:
                            path = "Data/Accounts/" + u + ".acc"
                            file = open(path, 'w+')
                            x = 0
                            while x < len(i):
                                file.write(str(ord(i[x])))
                                x = x + 1
                            file.write("\n")
                            file.write("0\n")
                            file.write("0\n")
                            file.close()
                            converted = ""
                            print("Password set!")
                            input("Press enter to login")
                            clear()
                    elif q == "y":
                        clear()
                        print("Username: " + u)
                        i = ""
                        while i == "":
                            i = input("New Password: ")
                        i2 = ""
                        while i2 == "":
                            i2 = input("Repeat password: ")
                        if i == i2:
                            path = "Data/Accounts/" + u + ".acc"
                            file = open(path, 'w+')
                            x = 0
                            while x < len(i):
                                file.write(str(ord(i[x])))
                                x = x + 1
                            file.write("\n")
                            file.write("0\n")
                            file.write("0\n")
                            file.close()
                            converted = ""
                            print("Password set!")
                            input("Press enter to login")
                            clear()
                    else:
                        q = ""
                        clear()
        except FileNotFoundError:
            print("Create an admin-account!")
            print("Username: Admin")
            i = ""
            while i == "":
                i = input("New Password: ")
            i2 = ""
            while i2 == "":
                i2 = input("Repeat password: ")
            if i == i2:
                file = open("Data/Accounts/Admin.acc", 'w+')
                x = 0
                while x < len(i):
                    file.write(str(ord(i[x])))
                    x = x + 1
                file.write("\n")
                file.write("0\n")
                file.write("0\n")
                file.close()
                converted = ""
                print("Password set!")
                input("Press enter to login")
                clear()
            else:
                print("The passwords are not the same!")

