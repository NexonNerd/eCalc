#pyinstaller --onefile eCalc.py
from math import pi
v="1"
eng={
    "plus":"+",
    "+":"+",
    "minus":"-",
    "-":"-",
    "times":"*",
    "x":"*",
    "*":"*",
    "pi":"pi",
    "divide":"/",
    "divided":"/",
    "/":"/",
    "by":"",
    "of":"",
    "to":"",
    "the":"",
    "power":"**",
    "mod":"%",
    "(":"(",
    ")":")",
    "zero":"0",
    "one":"1",
    "1":"1",
    "two":"2",
    "2":"2",
    "three":"3",
    "3":"3",
    "four":"4",
    "4":"4",
    "five":"5",
    "5":"5",
    "six":"6",
    "6":"6",
    "seven":"7",
    "7":"7",
    "eight":"8",
    "8":"8",
    "nine":"9",
    "9":"9",
}
print("--- Welcome to eCalc v"+v+" ---\neCalc does math for you, by understanding English!\nCreated by twitch.tv/NexonNerd")
while True:
    y=""
    x=input("\nUsing math, or just plain English, what do you want me to solve?: ")
    result=[]
    if x == "update log":
        print("\neCalc v"+v+"\nMade by twitch.tv/NexonNerd\n\nThere are no new updates.\nThis is version 1...\n")
        end=input("Press any key to go back.")
        continue
    for letter in x:
        if letter.isalpha()==True:
            y=y+letter
        else:
            y=y+" "+letter+" "
    try:
        for word in y.split():
            result.append(eng[word.lower()])
        done=str("".join(result))
        print(eval(done))
    except ZeroDivisionError:
        print("I'm so sorry, I understand what you asked me, but I can't break the rules of mathematics\n You can't divide by Zero.\n")
    except SyntaxError:
        print("That math equation doesn't really make sense.\nCheck your formula, you made a mistake somewhere.\n")
    except:
        print("I'm sorry, I didn't quite catch that.\nI'm still learning, so try simplifying.\nExample: \"One Plus One\"\n")