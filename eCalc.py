#pyinstaller --onefile eCalc.py
from math import pi
import time
v="2.1"
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
    "power":"**",
    "squared":"**2",
    "cubed":"**3",
    "mod":"%",
    "remainder":"%",
    "%":"%",
    "(":"(",
    ")":")",
    "zero":"0",
    "0":"0",
    "one":"1",
    "1":"1",
    "a":"1",
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
    "ten":"10",
    "eleven":"11",
    "twelve":"12",
    "thirteen":"13",
    "fourteen":"14",
    "fifteen":"15",
    "sixteen":"16",
    "seventeen":"17",
    "eighteen":"18",
    "nineteen":"19",
    "twenty":"20",
    "thirty":"30",
    "forty":"40",
    "fifty":"50",
    "sixty":"60",
    "seventy":"70",
    "eighty":"80",
    "ninety":"90",
    "hundred":"00",
    "thousand":"000",
    "million":"0000",
    "billion":"00000",
    "and":".",
    "point":".",
    "dot":".",
    "decimal":".",
    "negative":"-",
    "null":"",
    "update":""
}
print("--- Welcome to eCalc v"+v+" ---\neCalc does math for you, by understanding English!\nCreated by twitch.tv/NexonNerd")
while True:
    y=""
    x=input("\nUsing math, or just plain English, what do you want me to solve?: ")
    start=time.time()
    code_to_test=""
    result=[]
    if x.lower() == "update log":
        print("\neCalc v"+v+"\nMade by twitch.tv/NexonNerd\n")
        print("v2: Update log command now works in full caps.\n Better spaced out results.\n Added time to see how long it took.\nCalculator now able to handle words it doesn't know.\nNow knows words: squared, cubed, \"0\", \"%\", and remainder.\nCalculator now knows how to do math for numbers over 9, nagative numbers, and decimals.\n")
        print("v2.1: Fixed hundred giving weird number. Example: three hundred = 3100.")
        end=input("Press any key to go back.")
        continue
    for letter in x:
        if letter.isalpha()==True:
            y=y+letter
        else:
            y=y+" "+letter+" "
    try:
        for word in y.split():
            if word not in eng:
                word="null"
            result.append(eng[word.lower()])
        done=str("".join(result))
        print("\nThe answer is: "+str(eval(done)))
        clock=time.time()-start
        print("\nThat took me "+str(clock)+" seconds to figure out!")
    except ZeroDivisionError:
        print("I'm so sorry, I understand what you asked me, but I can't break the rules of mathematics\n You can't divide by Zero.\n")
    except SyntaxError:
        print("I'm sorry, I didn't quite catch that.\nI'm still learning, so try simplifying.\nExample: \"One Plus One\"\n")
    except:
        print("You managed to do something, that I wasn't expecting. Amazing!")