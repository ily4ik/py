import random
counter = 0
while(True):
    userinput = input()
    if (userinput == userinput.upper()):
        if(userinput == "ПОКА!"):
            counter += 1
            print(f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!")
        else:
            print(f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!")
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
    if(counter == 3):
        print("ДО СВИДАНИЯ, МИЛЫЙ!")
        break
