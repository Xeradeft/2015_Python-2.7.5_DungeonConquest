'''
Mitchell Van Braeckel
19/05/2015
Created for the end-of-the-year python programming challenge assignment
A text-based RPG game where you have an entertaining prologue/backstory leading to victory of the game by the conquest of a dungeon.
It also incorporates a Battle Simulator as the fight sequence.
'''

# finish all pathways
    # make 'easter egg' speech parts for DBZ related choices
# create fighting sequence
    # create enemy monsters
    # ????????? -- create shop system -- ??????????
# create potion system
            # ????????? -- create bag system -- ????????? - only HP / MP potions - ????????
# create the dungeon and/or infinite (almost) loop battle encounters
# randomize all systems
# ADD GRAPHICS / PICTURES / IMAGES / TEXT ART

# IMPORTS
import time
from random import randint

# start play timer
starttime = time.time()
time.clock

# Declare variables
#counters for eof loop for names, races, and classes
nameCount = 0
raceCount = 0
fclassCount = 0
#counters for y/n answers and EXP LV system
ynCount = 0
pLVupEXPCount = 0
turnCounta = 0
turnCount = 0
turnCounta += turnCount
mobfleeAttempts = 0
fleeAttempts = 0
escapechance = 0
mobEscape = False
pEscape = False
encounternum = 0
defeatboss = False
dungeonend = False

# standard base stats and level / exp / gold
# exp level up = 50
# exp until next lv = last time + (last time / 2) rounded to nearest whole #
pLV = 1
pEXP = 0
pLVupEXP = 50
pLVupEXPCount += pLVupEXP
pGold = 0
mobkills = 0
goldLost = 0

pHPmax = 100
pHP = pHPmax
pHPregenRate = 0.25
pHPregen = int(round(pHPmax * pHPregenRate))
pMPmax = 50
pMP = pMPmax
pMPregenRate = 0.25
pMPregen = int(round(pMPmax * pMPregenRate))
pSTR = 15
pWPN = 0
pWPNd = "Fists"
pWPNl = 0
pATK = pSTR + pWPN
pDEF = 9
pDEX = 11
pINT = 8
pLUK = 9
pCRITb = 0
pCRIT = round(pLUK + pWPNl + pCRITb) / 2
pAVO = round(pLUK + pDEX) / 2

mobWPN = 0
mobWPNd = "Nothing"
mobWPNl = 0
mobDropwc = 0
mobDropw = "Nothing"

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

# DEFINE FUNCTIONS

# prints things when player loses
def gameoverl():
    # calc time spent playing
    elapsedtime = 0
    cmin = 0
    minutes = 0
    seconds = 0
    elapsedtime = time.time() - starttime
    if round(elapsedtime) >= 60:
        cmin = round(elapsedtime) % 60
        minutes = round(elapsedtime) - cmin
        minutes = int(round(elapsedtime) / 60)
        seconds = cmin
    else:
        seconds = int(round(elapsedtime))
    # display end game stats
    cont = raw_input("\n(Press enter to continue)\n")
    print "GAME OVER - YOU LOSE"
    stopwatch2(1)
    print "\nFinal Statistics:"
    playerstats()
    cont = raw_input("\n(Press enter to continue)\n")
    print "Number of Enemies Slain: " + str(mobkills)
    print "Number of Turns Survived: " + str(turnCounta)
    print "Number of Encounters: " + str(encounternum)
    stopwatch2(1)
    print "Death by: "
    enemystatsall()
    print "\nTime spent playing: " + str(minutes) + " minutes, " + str(seconds) + " seconds"
    print "\nTHANKS FOR PLAYING"
    
# prints things when player wins
def gameoverw():
    # calc time spent playing
    elapsedtime = 0
    cmin = 0
    minutes = 0
    seconds = 0
    elapsedtime = time.time() - starttime
    if round(elapsedtime) >= 60:
        cmin = round(elapsedtime) % 60
        minutes = round(elapsedtime) - cmin
        minutes = int(round(elapsedtime) / 60)
        seconds = cmin
    else:
        seconds = round(elapsedtime)
        cont = raw_input("\n(Press enter to continue)\n")
    print "\nFinal Statistics:"
    playerstats()
    cont = raw_input("\n(Press enter to continue)\n")
    print "Number of Enemies Slain: " + str(mobkills)
    print "Number of Turns Survived: " + str(turnCounta)
    print "Number of Encounters: " + str(encounternum)
    print "Last Monster Defeated: "
    enemystatsall()
    print "\nTime spent playing: " + str(minutes) + " minutes, " + str(seconds) + " seconds"
    print "\nTHANKS FOR PLAYING"

# creates a settable timer
def stopwatch(secs):
    starttimer = time.time()
    time.clock()    
    timeElapsed = 0
    while timeElapsed < secs:
        timeElapsed = time.time() - starttimer
        print "."
        time.sleep(1)

# creates a settable timer #2
def stopwatch2(secs):
    starttimer = time.time()
    time.clock()    
    timeElapsed = 0
    while timeElapsed < secs:
        timeElapsed = time.time() - starttimer
        time.sleep(1)

# displays the users current name/class/race & stats & level & exp
def playerstats():
    print "Character: " + name + " the " + fclass + " " + race
    print "Level " + str(pLV)
    print "Total EXP = " + str(pEXP)
    print "EXP until next level = " + str(pLVupEXPCount - pEXP)
    print "Gold: " + str(pGold) + " coins"
    print "HP = " + str(pHP) + "/" + str(pHPmax)
    print "MP = " + str(pMP) + "/" + str(pMPmax)
    print "(Immediatley regenerate " + str(pHPregenRate * 100) + "% of max HP & " + str(pMPregenRate * 100) + "% of max MP after each battle)"
    print "ATK = " + str(pATK)
    print "     STR = " + str(pSTR)
    print "     Weapon = " + pWPNd + " | Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT"
    print "DEF = " + str(pDEF)
    print "DEX = " + str(pDEX)
    print "INT = " + str(pINT)
    print "LUK = " + str(pLUK)
    print "     CRIT chance = " + str(pCRIT - pCRITb) + "% (+" + str(pCRITb) + "%)"
    print "     AVO chance = " + str(pAVO) + "%"

# display the enemy lv, name, class, race, wpn stats
def enemystats():
    print "[HP = " + str(mobHP) + "/" + str(mobHPmax) + "]"
    print "[MP = " + str(mobMP) + "/" + str(mobMPmax) + "]"
    print "[The enemy wields a +" + str(mobWPN) + " ATK / +" + str(mobWPNl) + " CRIT " + mobWPNd + "]"
    print "     CRIT chance = " + str(mobCRIT - mobCRITb) + "% (+" + str(mobCRITb) + "%)"
    print "     AVO chance = " + str(mobAVO) + "%"

def enemystatsall():
    print "Enemy: " + mob
    print "Level " + str(mobLV)
    print "Gold: " + str(mobGold) + " coins"
    print "HP = " + str(mobHP) + "/" + str(mobHPmax)
    print "MP = " + str(mobMP) + "/" + str(mobMPmax)
    print "ATK = " + str(mobATK)
    print "     STR = " + str(mobSTR)
    print "     Weapon = " + mobWPNd + " | Bonus: +" + str(mobWPN) + " ATK, +" + str(mobWPNl) + " CRIT | Weapon Drop Chance: " + str(mobDropwc)
    print "DEF = " + str(mobDEF)
    print "DEX = " + str(mobDEX)
    print "INT = " + str(mobINT)
    print "LUK = " + str(mobLUK)
    print "     CRIT chance = " + str(mobCRIT - mobCRITb) + "% (+" + str(mobCRITb) + "%)"
    print "     AVO chance = " + str(mobAVO) + "%"
    
# calc flee chance from battle
def fleechance(A, B, C):
    return (((A * 128) / B) + 30 * C) % 256

# how to round to nearest 5
def roundint5(val):
    if (int(val) - 7) % 10 == 0 or (int(val) - 7) == 0:
        val = (int(val) + 1)
    return int(round(val*2, -1)) / 2

# how to display commands for the user in what to do
def HELP():
    print "'/playerstats'"

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

# CREATOR NOTES TO PLAYER
print "     CREATOR'S NOTES"
print "     ===============\n"
stopwatch2(1)
#print "In this game there, exists a high-risk critical hit factor where the resulting damage is NOT twice the normal amount because it doubles your attacking power instead of the calculated damage."
print "\n[NOTE TO PLAYER:   MP and INT stats as well as GOLD amounts are irrevelant and only for display purposes]\n"
print "There are timers in the game that allow you to fully immerse yourself in its rich storyline as they slow down the constant feed of information."
print "     Like this: (time delay)"
stopwatch2(1)
print "     And this ('.' delay):"
stopwatch(2)
print "     And this ('ENTER' prompt):"
cont = raw_input("\n(Press enter to continue)\n")
print "     Therefore, do not fret if no prompts are appearing as it is only a delay that allows you to read the text before making a hasty decision."
print "Also, when you come to a decision, type carefully, as some situations will auto-decline."
print "The choice you must type into the prompt is not caps-sensitive, it only appears as [type 'YOUR ANSWER'] to make it easier to spot.\n"
print "Please enjoy the game!"
cont = raw_input("\n(Press enter to continue)\n")
# WELCOME
print "\nWelcome to Dungeon Conquest, an RPG Battle Simulator.\n"
# BACKSTORY (tavern)
print "You begin your adventure in a local tavern in the small village of Konoha.\n"
print "Your Goal:   To clear a dungeon and survive\n"
cont = raw_input("(Press enter to continue)")
print "\nAfter coming home from a lonq journey where you slew dragons, creatures, and beasts alike, \nthis warm and familiar atmosphere relieves you of all your stress as you laugh and drink with your comrades."
print "As you are gleefully downing your well-deserved ale, you spot an intriguing poster on the request board."
stopwatch2(1)
decision = raw_input("\nIf you want to get up and investigate further, type 'BOARD'.  Otherwise, you will continue to merrily celebrate your victory with your comrades.  ")
if decision.lower() == "board":
    # walk over and investigate the request board
    print "\nUpon closer inspection of the request, you read:\n"
    print "     HELP WANTED"
    print "     ==========="
    print "     An unconquerable dungeon has emmerged from the depths of the earth southeast of the Konoha main gate."
    print "     We require a courageous hero to clear the dungeon, vanquish the monsters, reap the rewards, and claim the treasure.\n"
    print "      -- Hiruzen Sarutobi, Konaha Village Chief\n"
    print "[You finish reading the poster.]\n"
    stopwatch2(1)
    # accept or decline request
    accdec = raw_input("Do you 'ACCEPT' the quest?  Or would you rather continue merrily drinking with your comrades?   ")
    if accdec.lower() == "accept":
        # ACCEPT
        print "\nYou decide to begin a new quest!\n"
        cont = raw_input("(Press enter to continue)\n")
        print "Old Man:     'Ah, I see you've noticed the request I placed there.'"
        print "\n[In shock you realize that this Old Man, is actually Hiruzen Sarutobi, the Chief of Konoha Village]\n"
        cont = raw_input("(Press enter to continue)")
        print "Hiruzen:     'I would take this challenge on, but alas, I have greatly exceeded my prime.  I am much too old for this life now and must find an heir."
        print "Hiruzen:     'Therefore, I put this here to encourage newcomers like yourself to show their potential."
        print "Hiruzen:     'Young lad, what is your name?  I would like to remember it because you have spiked my curiosity and interest, which is very rare for me to find."
        print "\n[Introduce yourself]\n"
        stopwatch2(1)
        while nameCount == 0:
            name = raw_input("Enter your name:      ")
            ynName = raw_input("Are you sure with the name " + name + "?    ('Y'es or 'N'o)     ")
            if ynName.lower() == "y":
                nameCount = 1
        # RACE
        while raceCount == 0:
            race = raw_input("\nEnter your race:\nHUMAN\nORC\nELF\nUNDEAD\nMYSTERY\nSAIYAN [for testing purposes]   ")
            if race.lower() == "human":
                race = "Human"
                # balanced race
                pHPmax = 15
                pHP = pHPmax
                pHPregenRate = 0.25
                pHPregen = int(round(pHPmax * pHPregenRate))
                pMPmax = 15
                pMP = pMPmax
                pMPregenRate = 0.25
                pMPregen = int(round(pMPmax * pMPregenRate))
                pSTR = 10
                pATK = pSTR + pWPN
                pDEF = 10
                pDEX = 10
                pINT = 10                   
                pLUK = 15
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                raceCount = 1
            elif race.lower() == "orc":
                race = "Orc"
                # tank race
                pHPmax = 30
                pHP = pHPmax
                pHPregenRate = 0.3
                pHPregen = int(round(pHPmax * pHPregenRate))
                pMPmax = 20
                pMP = pMPmax
                pMPregenRate = 0.25
                pMPregen = int(round(pMPmax * pMPregenRate))
                pSTR = 13
                pATK = pSTR + pWPN
                pDEF = 15
                pDEX = 5
                pINT = 5
                pLUK = 8
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                raceCount = 1
            elif race.lower() == "elf":
                race = "Elf"
                # standard elf perks
                pHPmax = 15
                pHP = pHPmax
                pHPregenRate = 0.25
                pHPregen = int(round(pHPmax * pHPregenRate))
                pMPmax = 25
                pMP = pMPmax
                pMPregenRate = 0.3
                pMPregen = int(round(pMPmax * pMPregenRate))
                pSTR = 10
                pATK = pSTR + pWPN
                pDEF = 9
                pDEX = 13
                pINT = 13
                pLUK = 15
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                raceCount = 1
            elif race.lower() == "undead":
                race = "Undead"
                # str & mp & luk race
                pHPmax = 20
                pHP = pHPmax
                pHPregenRate = 0.35
                pHPregen = int(round(pHPmax * pHPregenRate))
                pMPmax = 30
                pMP = pMPmax
                pMPregenRate = 0.2
                pMPregen = int(round(pMPmax * pMPregenRate))
                pSTR = 17
                pATK = pSTR + pWPN
                pDEF = 12
                pDEX = 5
                pINT = 7
                pLUK = 30
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                raceCount = 1
            elif race.lower() == "mystery":
                race = "Mystery"
                # random generated stats from 5 -> 30
                pHPmax = randint(10, 30)
                pHP = pHPmax
                pHPregenRate = (roundint5(randint(15, 35))) * 0.01
                pHPregen = int(round(pHPmax * pHPregenRate))
                pMPmax = randint(10, 30)
                pMP = pMPmax
                pMPregenRate = (roundint5(randint(15, 35))) * 0.01
                pMPregen = int(round(pMPmax * pMPregenRate))
                pSTR = randint(5, 20)
                pATK = pSTR + pWPN
                pDEF = randint(5, 20)
                pDEX = randint(5, 20)
                pINT = randint(5, 20)
                pLUK = randint(5, 30)
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                raceCount = 1
            elif race.lower() == "saiyan":
                race = "Saiyan"
                # testing OP race
                pLV = 1
                pEXP = 0
                pLVupEXP = 50
                pHPmax = 9001
                pHP = pHPmax
                pHPregenRate = 0.001
                pHPregen = int(round(pHPmax * pHPregenRate))
                pMPmax = 9001
                pMP = pMPmax
                pMPregenRate = 0.001
                pMPregen = int(round(pMPmax * pMPregenRate))
                pSTR = 9001
                pWPN = 0
                pWPNd = "Saiyan Fists"
                pWPNl = 0
                pATK = pSTR + pWPN
                pDEF = 20
                pDEX = 10
                pINT = 9001
                pLUK = 50
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                raceCount = 1
            else:
                print ("\n[INVALID, please try again]")
            
        # CLASS
        while fclassCount == 0:
            fclass = raw_input("\nChoose a class:\nWARRIOR (bal)\nROGUE (dps)\nPALADIN (tank)\nUNKNOWN\nSSGSS [for testing purposes]     ")
            if fclass.lower() == "warrior":
                fclass = "Warrior"
                # balanced class
                #BALANCED
                pWPN = 3
                pWPNd = "Bronze Sword"
                pWPNl = 5
                pATK = pSTR + pWPN
                pLUK += 15
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                fclassCount = 1
            elif fclass.lower() == "rogue":
                fclass = "Rogue"
                # dps class
                #HP
                #MP
                pSTR += 10
                pWPN = 2
                pWPNd = "Bronze Dagger"
                pWPNl = 15
                pATK = pSTR + pWPN
                #DEF
                pDEX += 10
                pINT += 3
                pLUK += 20
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                fclassCount = 1
            elif fclass.lower() == "paladin":
                fclass = "Paladin"
                # tank class
                pHPmax += 5
                pHP = pHPmax
                #MP
                pSTR += 5
                pWPN = 4
                pWPNd = "Bronze Lance"
                pWPNl = 5
                pATK = pSTR + pWPN
                pDEF += 10
                pDEX -= 3
                pINT -= 2
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                #LUK
                fclassCount = 1
            elif fclass.lower() == "unknown":
                fclass = "Unknown"
                # random stat bonus / minus class
                pmCount = randint(1, 2)
                if pmCount == 1:
                    pHPmax += randint(1, 5)
                else:
                    pHPmax -= randint(1, 5)
                pHP = pHPmax
                pmCount = randint(1, 2)
                if pmCount == 1:
                    pMPmax += randint(1, 5)
                else:
                    pMPmax -= randint(1, 5)
                pMP = pMPmax
                pmCount = randint(1, 2)
                if pmCount == 1:
                    pSTR += randint(1, 5)
                else:
                    pSTR -= randint(1, 5)
                pmCount = randint(1, 5)
                if pmCount == 1:
                    pWPN = 2
                    pWPNd = "Bronze Dagger"
                    pWPNl = 15
                elif pmCount == 2:
                    pWPN = 3
                    pWPNd = "Bronze Sword"
                    pWPNl = 5
                elif pmCount == 3:
                    pWPN = 4
                    pWPNd = "Bronze Lance"
                    pWPNl = 5
                elif pmCount == 4:
                    pWPN = 5
                    pWPNd = "Bronze Hammer"
                    pWPNl = 5
                else:
                    pWPN = 5
                    pWPNd = "Bronze Axe"
                    pWPNl = 10
                pATK = pSTR + pWPN
                pmCount = randint(1, 2)
                if pmCount == 1:
                    pDEF += randint(1, 5)
                else:
                    pDEF -= randint(1, 5)
                pmCount = randint(1, 2)
                if pmCount == 1:
                    pDEX += randint(1, 5)
                else:
                    pDEX -= randint(1, 5)
                pmCount = randint(1, 2)
                if pmCount == 1:
                    pINT += randint(1, 5)
                else:
                    pINT -= randint(1, 5)
                pmCount = randint(1, 2)
                if pmCount == 1:
                    pLUK += randint(1, 5)
                else:
                    pLUK -= randint(1, 5)
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                fclassCount = 1
            elif fclass.lower() == "ss g ss" or fclass.lower() == "ssgss":
                fclass = "Super Saiyan God Super"
                # str & mp & luk race
                pLV = 1
                pEXP = 0
                pLVupEXP = 50
                pHPmax = 9999
                pHP = pHPmax
                pHPregenRate = 0.001
                pHPregen = int(round(pHPmax * pHPregenRate))
                pMPmax = 9999
                pMP = pMPmax
                pMPregenRate = 0.001
                pMPregen = int(round(pMPmax * pMPregenRate))
                pSTR = 9999
                pWPN = 0
                pWPNd = "Super Saiyan God Super " + name + " Fists"
                pWPNl = 25
                pATK = pSTR + pWPN
                pDEF = 20
                pDEX = 10
                pINT = 9999
                pLUK = 50
                pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                pAVO = round(pLUK + pDEX) / 2
                fclassCount = 1
            else:
                print ("\n[INVALID, please try again]")
                
        cont = raw_input("\n(Press enter to continue)\n")
        print "Hiruzen:     'Ah, so I see.  " + name + " the " + fclass + " " + race + ", I will memorize you for I sense I potential from you.'"
        print "Hiruzen:     'Here, allow me to teach you a few basic skills.'"
        # 3 levels from showing the skills
        stopwatch2(1)
        print "\n[Hiruzen unsheathes his Royal Sword of the Hokage and demonstrates a blinding flurry of attacks]\n"
        stopwatch2(1)
        print "[From his demonstration and the basic skills that you have just learned, you gained three levels!]\n"
        cont = raw_input("\n(Press enter to continue)\n")
        # +3 lvs
        pEXP += (pLVupEXPCount - pEXP) #+1 lv
        pLVupEXP += 75
        pLVupEXPCount += pLVupEXP
        pEXP += (pLVupEXPCount - pEXP) #+1 lv
        pLVupEXP += 75
        pLVupEXPCount += pLVupEXP
        pEXP += (pLVupEXPCount - pEXP) #+1 lv
        pLVupEXP += 75
        pLVupEXPCount += pLVupEXP
        newpHPmax = pHPmax
        newpMPmax = pMPmax
        newpSTR = pSTR
        newpDEF = pDEF
        newpDEX = pDEX
        newpINT = pINT
        newpLUK = pLUK
        # give enough exp for 2 lvups and no more
        for i in range(3):
            #LV UP
            pLV += 1
            statCount = int(round(randint(0, 100) / 20))
            newpHPmax += statCount
            pHP += statCount
            statCount = int(round(randint(0, 100) / 20))
            newpMPmax += statCount
            pMP += statCount
            statCount = int(round(randint(0, 100) / 20))
            newpSTR += statCount
            newpATK = newpSTR + pWPN
            statCount = int(round(randint(0, 100) / 20))
            newpDEF += statCount
            statCount = int(round(randint(0, 100) / 20))
            newpDEX += statCount
            statCount = int(round(randint(0, 100) / 20))
            newpINT += statCount
            statCount = int(round(randint(0, 100) / 20))
            newpLUK += statCount
            newpCRIT = round(newpLUK + pWPNl + pCRITb) / 2
            newpAVO = round(newpLUK + newpDEX) / 2
        # print stat changes    
        print "[You gained 3 Levels]"
        print "\n[LEVEL UP: " + name + ", you are now a Level " + str(pLV) + " " + fclass + " " + race + "]"
        print "\nHP MAX: " + str(pHPmax) + " -> " + str(newpHPmax) + "      (+" + str(newpHPmax - pHPmax) + ")"
        pHPmax = newpHPmax
        print "MP MAX: " + str(pMPmax) + " -> " + str(newpMPmax) + "        (+" + str(newpMPmax - pMPmax) + ")"
        pMPmax = newpMPmax
        print "ATK: " + str(pATK) + " -> " + str(newpATK) + "           (+" + str(newpATK - pATK) + ")"
        print "     STR: " + str(pSTR) + " -> " + str(newpSTR) + "      (+" + str(newpSTR - pSTR) + ")"
        print "     Weapon = " + pWPNd + " | Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT"
        pATK = newpATK
        pSTR = newpSTR
        print "DEF: " + str(pDEF) + " -> " + str(newpDEF) + "           (+" + str(newpDEF - pDEF) + ")"
        pDEF = newpDEF
        print "DEX: " + str(pDEX) + " -> " + str(newpDEX) + "           (+" + str(newpDEX - pDEX) + ")"
        pDEX = newpDEX
        print "INT: " + str(pINT) + " -> " + str(newpINT) + "           (+" + str(newpINT - pINT) + ")"
        pINT = newpINT
        print "LUK: " + str(pLUK) + " -> " + str(newpLUK) + "           (+" + str(newpLUK - pLUK) + ")"
        pLUK = newpLUK
        print "     CRIT chance: " + str(pCRIT - pCRITb) + "% (+" + str(pCRITb) + "%) -> " + str(newpCRIT) + "% (+" + str(pCRITb) + "%)     (+" + str(newpCRIT - pCRIT) + ")"
        print "     AVO chance: " + str(pAVO) + "% -> " + str(newpAVO) + "%                  (+" + str(newpAVO - pAVO) + ")\n"
        pCRIT = newpCRIT
        pAVO = newpAVO
        cont = raw_input("\n(Press enter to continue)")
        # display exp until next lv
        print "\nEXP until next level = " + str(pLVupEXPCount - pEXP)
        pHPregen = int(round(pHPmax * pHPregenRate))
        pMPregen = int(round(pMPmax * pMPregenRate))
        stopwatch2(1)
        print "\nHiruzen:     'Farewell, " + name + ", I wish you luck on your quest.'"
        print "\nYou set out on your journey to the mysterious new dungeon southeast of Konoha."
        print "However, your comrades decide not to join you in the new mission so you decide to solo it.\n"
        # travels to dungeon
        print "[You travel to the dungeon on foot alone]"
    else:
        # DECLINE
        print "\nYou decide that risking your life in an unknown dungeon is not worth it and countinue to merrily drink with your comrades.\n"
        cont = raw_input("(Press enter to continue)")
        # panicked MESSENGER
        print "\n[Panicked Messenger burst into the tavern screaming nonsense]"
        print "\nOld Man:   'Spit it out, boy!  What's the matter?'"
        cont = raw_input("\n(Press enter to continue)\n")
        print "Panicked Messenger:  'HELP!  HELP!  There are monsters approaching!'"
        print "Young Hunter:    'Hark!  We need a hero to fend off these monsters, but I have left my weapons in my other garments.'"
        cont = raw_input("\n(Press enter to continue)\n")
        print "Heavy Brute:     'Who possesses the bravery to fend off the advancing horde of creatures?'\n"
        stopwatch2(1)
        # CHALLENGE the horde of approaching monsters
        challenge = raw_input("If you want to challenge the horde of creatures and save the tavern, type 'CHALLENGE'.  Otherwise, someone else will most likely kill them and take the glory.   ")
        if challenge.lower() == "challenge":
            # ACCEPT
            print "\n[You volunteer to fight]\n"
            print "Bartender:   'Who are you?  You're fresh meat, eh?'"
            print "Old man:     'Hey there newbie!  I'm Isaac the Wise, one of the first adventurers and the very first Hunter in existence.'"
            print "Isaac the Wise:  And you are?"
            print "\n[Introduce yourself]\n"
            stopwatch2(1)
            # NAME
            while nameCount == 0:
                name = raw_input("Enter your name:      ")
                ynName = raw_input("Are you sure with the name " + name + "?    ('Y'es or 'N'o)     ")
                if ynName.lower() == "y":
                    nameCount = 1
            print "\nIsaac the Wise:  So, " + name + ", what's your race and class?\n"
            stopwatch2(1)
            # RACE
            while raceCount == 0:
                race = raw_input("Enter your race:\nHUMAN\nORC\nELF\nUNDEAD\nMYSTERY\nSAIYAN [for testing purposes]   ")
                if race.lower() == "human":
                    race = "Human"
                    # balanced race
                    pHPmax = 15
                    pHP = pHPmax
                    pHPregenRate = 0.25
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 15
                    pMP = pMPmax
                    pMPregenRate = 0.25
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 10
                    pATK = pSTR + pWPN
                    pDEF = 10
                    pDEX = 10
                    pINT = 10                   
                    pLUK = 15
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "orc":
                    race = "Orc"
                    # tank race
                    pHPmax = 30
                    pHP = pHPmax
                    pHPregenRate = 0.3
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 20
                    pMP = pMPmax
                    pMPregenRate = 0.25
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 13
                    pATK = pSTR + pWPN
                    pDEF = 15
                    pDEX = 5
                    pINT = 5
                    pLUK = 8
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "elf":
                    race = "Elf"
                    # standard elf perks
                    pHPmax = 15
                    pHP = pHPmax
                    pHPregenRate = 0.25
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 25
                    pMP = pMPmax
                    pMPregenRate = 0.3
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 10
                    pATK = pSTR + pWPN
                    pDEF = 9
                    pDEX = 13
                    pINT = 13
                    pLUK = 15
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "undead":
                    race = "Undead"
                    # str & mp & luk race
                    pHPmax = 20
                    pHP = pHPmax
                    pHPregenRate = 0.35
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 30
                    pMP = pMPmax
                    pMPregenRate = 0.2
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 17
                    pATK = pSTR + pWPN
                    pDEF = 12
                    pDEX = 5
                    pINT = 7
                    pLUK = 30
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "mystery":
                    race = "Mystery"
                    # random generated stats from 5 -> 30
                    pHPmax = randint(10, 30)
                    pHP = pHPmax
                    pHPregenRate = (roundint5(randint(15, 35))) * 0.01
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = randint(10, 30)
                    pMP = pMPmax
                    pMPregenRate = (roundint5(randint(15, 35))) * 0.01
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = randint(5, 20)
                    pATK = pSTR + pWPN
                    pDEF = randint(5, 20)
                    pDEX = randint(5, 20)
                    pINT = randint(5, 20)
                    pLUK = randint(5, 30)
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "saiyan":
                    race = "Saiyan"
                    # testing OP race
                    pLV = 1
                    pEXP = 0
                    pLVupEXP = 50
                    pHPmax = 9001
                    pHP = pHPmax
                    pHPregenRate = 0.001
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 9001
                    pMP = pMPmax
                    pMPregenRate = 0.001
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 9001
                    pWPN = 0
                    pWPNd = "Saiyan Fists"
                    pWPNl = 0
                    pATK = pSTR + pWPN
                    pDEF = 20
                    pDEX = 10
                    pINT = 9001
                    pLUK = 50
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                else:
                    print ("\n[INVALID, please try again]")
                
            # CLASS
            while fclassCount == 0:
                fclass = raw_input("\nChoose a class:\nWARRIOR (bal)\nROGUE (dps)\nPALADIN (tank)\nUNKNOWN\nSSGSS [for testing purposes]     ")
                if fclass.lower() == "warrior":
                    fclass = "Warrior"
                    # balanced class
                    #BALANCED
                    pWPN = 3
                    pWPNd = "Bronze Sword"
                    pWPNl = 5
                    pATK = pSTR + pWPN
                    pLUK += 15
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    fclassCount = 1
                elif fclass.lower() == "rogue":
                    fclass = "Rogue"
                    # dps class
                    #HP
                    #MP
                    pSTR += 10
                    pWPN = 2
                    pWPNd = "Bronze Dagger"
                    pWPNl = 15
                    pATK = pSTR + pWPN
                    #DEF
                    pDEX += 10
                    pINT += 3
                    pLUK += 20
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    fclassCount = 1
                elif fclass.lower() == "paladin":
                    fclass = "Paladin"
                    # tank class
                    pHPmax += 5
                    pHP = pHPmax
                    #MP
                    pSTR += 5
                    pWPN = 4
                    pWPNd = "Bronze Lance"
                    pWPNl = 5
                    pATK = pSTR + pWPN
                    pDEF += 10
                    pDEX -= 3
                    pINT -= 2
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    #LUK
                    fclassCount = 1
                elif fclass.lower() == "unknown":
                    fclass = "Unknown"
                    # random stat bonus / minus class
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pHPmax += randint(1, 5)
                    else:
                        pHPmax -= randint(1, 5)
                    pHP = pHPmax
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pMPmax += randint(1, 5)
                    else:
                        pMPmax -= randint(1, 5)
                    pMP = pMPmax
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pSTR += randint(1, 5)
                    else:
                        pSTR -= randint(1, 5)
                    pmCount = randint(1, 5)
                    if pmCount == 1:
                        pWPN = 2
                        pWPNd = "Bronze Dagger"
                        pWPNl = 15
                    elif pmCount == 2:
                        pWPN = 3
                        pWPNd = "Bronze Sword"
                        pWPNl = 5
                    elif pmCount == 3:
                        pWPN = 4
                        pWPNd = "Bronze Lance"
                        pWPNl = 5
                    elif pmCount == 4:
                        pWPN = 5
                        pWPNd = "Bronze Hammer"
                        pWPNl = 5
                    else:
                        pWPN = 5
                        pWPNd = "Bronze Axe"
                        pWPNl = 10
                    pATK = pSTR + pWPN
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pDEF += randint(1, 5)
                    else:
                        pDEF -= randint(1, 5)
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pDEX += randint(1, 5)
                    else:
                        pDEX -= randint(1, 5)
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pINT += randint(1, 5)
                    else:
                        pINT -= randint(1, 5)
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pLUK += randint(1, 5)
                    else:
                        pLUK -= randint(1, 5)
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    fclassCount = 1
                elif fclass.lower() == "ss g ss" or fclass.lower() == "ssgss":
                    fclass = "Super Saiyan God Super"
                    # str & mp & luk race
                    pLV = 1
                    pEXP = 0
                    pLVupEXP = 50
                    pHPmax = 9999
                    pHP = pHPmax
                    pHPregenRate = 0.001
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 9999
                    pMP = pMPmax
                    pMPregenRate = 0.001
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 9999
                    pWPN = 0
                    pWPNd = "Super Saiyan God Super " + name + " Fists"
                    pWPNl = 25
                    pATK = pSTR + pWPN
                    pDEF = 20
                    pDEX = 10
                    pINT = 9999
                    pLUK = 50
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    fclassCount = 1
                else:
                    print ("\n[INVALID, please try again]")

            # print stats to user
            print "\n[NOTE TO PLAYER]\n[Your current stats:]\n"
            stopwatch2(1)
            playerstats()
            print "\n[NOTE TO PLAYER:]"
            stopwatch2(1)
            print "[You can now type /help to see commands you can use in any enter text instance.]"
            cont = raw_input("\n(Press enter to continue)\n")
            
            print "Isaac the Wise:  Nice to meet you, " + name + " the " + fclass + " " + race + ".  Are you ready to slay some beasts!?"
            while True:
                yn = raw_input("'Y'es or 'N'o:  ")
                if yn.lower() == "y":
                    print "\nIsaac the Wise:  Then let's go hunting!"
                    break
                elif yn.lower() == "/help":
                    HELP()
                elif yn.lower() == "/playerstats":
                    playerstats()
                else:
                    print "\nIsaac the Wise:  Well too bad for you, out here it's kill or be killed when your facing off with a monster."
                    break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
            # random choose monster for 3 fights
            for i in range(3):
                rndegMob = randint(1, 4)
                if rndegMob == 1:
                    mob = "Green Slime"
                    mobLV = 3
                    mobGold = 15
                    mobEXP = 175
                    mobHPmax = 22
                    mobHP = mobHPmax
                    mobMPmax = 0
                    mobMP = mobMPmax
                    mobSTR = 10
                    mobWPN = 3
                    mobWPNd = "Green Slime Goo"
                    mobWPNl = 10
                    mobATK = mobSTR + mobWPN
                    mobDEF = 7
                    mobDEX = 8
                    mobINT = 5
                    mobLUK = 10
                    mobCRITb = 0
                    mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
                    mobAVO = round(mobLUK + mobDEX) / 2
                    mobDropwc = 0
                    encounternum += 1
                elif rndegMob == 2:
                    mob = "Dark Wolf"
                    mobLV = 3
                    mobGold = 10
                    mobEXP = 150
                    mobHPmax = 19
                    mobHP = mobHPmax
                    mobMPmax = 0
                    mobMP = mobMPmax
                    mobSTR = 7
                    mobWPN = 5
                    mobWPNd = "Wolf Claw"
                    mobWPNl = 17
                    mobATK = mobSTR + mobWPN
                    mobDEF = 5
                    mobDEX = 15
                    mobINT = 11
                    mobLUK = 16
                    mobCRITb = 0
                    mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
                    mobAVO = round(mobLUK + mobDEX) / 2
                    mobDropwc = 0
                    encounternum += 1
                elif rndegMob == 3:
                    mob = "Goblin"
                    mobLV = 3
                    mobGold = 30
                    mobEXP = 200
                    mobHPmax = 27
                    mobHP = mobHPmax
                    mobMPmax = 13
                    mobMP = mobMPmax
                    mobSTR = 11
                    mobWPN = 4
                    mobWPNd = "Goblin Thieve's Knife"
                    mobWPNl = 25
                    mobATK = mobSTR + mobWPN
                    mobDEF = 9
                    mobDEX = 20
                    mobINT = 16
                    mobLUK = 30
                    mobCRITb = 0
                    mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
                    mobAVO = round(mobLUK + mobDEX) / 2
                    mobDropwc = 30
                    encounternum += 1
                else:
                    mob = "Giant Rat"
                    mobLV = 3
                    mobGold = 10
                    mobEXP = 150
                    mobHPmax = 13
                    mobHP = mobHPmax
                    mobMPmax = 0
                    mobMP = mobMPmax
                    mobSTR = 4
                    mobWPN = 2
                    mobWPNd = "Giant Rat Tooth"
                    mobWPNl = 17
                    mobATK = mobSTR + mobWPN
                    mobDEF = 5
                    mobDEX = 18
                    mobINT = 11
                    mobLUK = 25
                    mobCRITb = 0
                    mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
                    mobAVO = round(mobLUK + mobDEX) / 2
                    mobDropwc = 0
                    encounternum += 1

                # display the encounter info
                stopwatch2(1)
                if i == 0:
                    print "\nThe first monster approaches!"
                elif i == 1:
                    print "\nThe second monster approaches!"
                else:
                    print "\nThe last monster approaches!"
                print "\n[You encounter a Level " + str(mobLV) + " " + mob + "!]"
                enemystats()
                cont = raw_input("\n(Press enter to continue)")
                
                # start fight2 sequence
                while pHP > 0 and mobHP > 0 and not mobEscape and not pEscape:
                    # turn fight sequence
                    # calc enemy action
                    mobTURNc = randint(1, 100)
                    if mobTURNc <= 10:
                        # attempts to flee
                        mobTURN = "Flee"
                    elif mobTURNc >= 50:
                        # attacks
                        mobTURN = "Attack"
                    elif mobTURNc > 10 and mobTURNc < 30:
                        # guards
                        mobTURN = "Guard"
                    else:
                        # CRIT +10
                        mobTURN = "Focus"
                    # player decides action
                    while True:
                        pTURN = raw_input("\n[OPTIONS: 'ATTACK', 'FOCUS' (+10% CRIT), 'GUARD' (1/2 DMG), 'FLEE' (" + str(int((fleechance(pDEX, mobDEX, fleeAttempts) / float(256) * 100))) + "%)]    ")
                        if pTURN.lower() == "attack":
                            # attacks
                            pTURN = "Attack"
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            if mobTURN == "Attack":
                                tiebreaker = randint(1, 2)
                                # calc who attacks first
                                if pDEX > mobDEX or pDEX == mobDEX and tiebreaker == 1:
                                    turnCount += 1
                                    #player first
                                    print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                                    #crit chance
                                    if pCRIT >= randint(1, 100):
                                        pDMG = (pATK - mobDEF) * 2
                                        if pDMG < 0:
                                            #make it=0
                                            pDMG = 0
                                        if mobAVO >= randint(1, 100):
                                            # mob dodge
                                            stopwatch2(1)
                                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                        else:
                                            #crit atk
                                            print "[CRITICAL HIT!    x2 DAMAGE]"
                                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                            newmobHP = mobHP
                                            newmobHP -= pDMG
                                            if newmobHP < 0:
                                                #make it not<0                                
                                                newmobHP = 0
                                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                            mobHP = newmobHP
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                            if mobHP == 0:
                                                stopwatch2(1)
                                                # mob defeated, player wins
                                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                # gain gold
                                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                                pGold += mobGold
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                mobkills += 1
                                                break
                                            #else cont fight (still alive)
                                    else:
                                        #no crit chance
                                        pDMG = pATK - mobDEF
                                        if pDMG < 0:
                                            #make it=0
                                            pDMG = 0
                                        if mobAVO >= randint(1, 100):
                                            # mob dodge
                                            stopwatch2(1)
                                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                        else:
                                            #no crit atk
                                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                            newmobHP = mobHP
                                            newmobHP -= pDMG
                                            if newmobHP < 0:
                                                #make it not<0
                                                newmobHP = 0
                                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                            mobHP = newmobHP
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                            if mobHP == 0:
                                                stopwatch2(1)
                                                # mob defeated, player wins
                                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                # gain gold
                                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                                pGold += mobGold
                                                pGold += mobGold
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                mobkills += 1
                                                break
                                            #else cont fight (still alive)
                                    stopwatch2(1)
                                    turnCount += 1
                                    #mob attacks (not KO)
                                    print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                                    #mob crit chance
                                    if mobCRIT >= randint(1, 100):
                                        mobDMG = (mobATK - pDEF) * 2
                                        if mobDMG < 0:
                                            #make it=0
                                            mobDMG = 0
                                        if pAVO >= randint(1, 100):
                                            # player dodge
                                            stopwatch2(1)
                                            print "You dodge the attack!"
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                            break
                                        else:
                                            #mob crit atk
                                            print "[CRITICAL HIT!    x2 DAMAGE]"
                                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                            newpHP = pHP
                                            newpHP -= mobDMG
                                            if newpHP < 0:
                                                #make it not<0
                                                newpHP = 0
                                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                            pHP = newpHP
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                            if pHP == 0:
                                                # player defeated, player loses
                                                stopwatch2(1)
                                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                gameoverl()
                                                exit = raw_input("(Press enter to exit the game)    ")
                                                # exits the game by death
                                                raise SystemExit
                                            #else cont fight (still alive)
                                            break
                                    else:
                                        #no mob crit atk
                                        mobDMG = mobATK - pDEF
                                        if mobDMG < 0:
                                            #make it=0
                                            mobDMG = 0
                                        if pAVO >= randint(1, 100):
                                            # player dodge
                                            stopwatch2(1)
                                            print "You dodge the attack!"
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                        else:
                                            #mob no crit atk
                                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                            newpHP = pHP
                                            newpHP -= mobDMG
                                            if newpHP < 0:
                                                #make it not<0
                                                newpHP = 0
                                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                            pHP = newpHP
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                            if pHP == 0:
                                                # player defeated, player loses
                                                stopwatch2(1)
                                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                gameoverl()
                                                exit = raw_input("(Press enter to exit the game)    ")
                                                # exits the game by death
                                                raise SystemExit
                                            #else cont fight (still alive)
                                        break
            #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                                elif mobDEX > pDEX or mobDEX == pDEX and tiebreaker == 2:
                                    turnCount += 1
                                    # enemy first
                                    print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                                    #mob crit chance
                                    if mobCRIT >= randint(1, 100):
                                        mobDMG = (mobATK - pDEF) * 2
                                        if mobDMG < 0:
                                            #make it=0
                                            mobDMG = 0
                                        if pAVO >= randint(1, 100):
                                            # player dodge
                                            stopwatch2(1)
                                            print "You dodge the attack!"
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                        else:
                                            #mob crit atk
                                            print "[CRITICAL HIT!    x2 DAMAGE]"
                                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                            newpHP = pHP
                                            newpHP -= mobDMG
                                            if newpHP < 0:
                                                #make it not<0
                                                newpHP = 0
                                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                            pHP = newpHP
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                            if pHP == 0:
                                                # player defeated, player loses
                                                stopwatch2(1)
                                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                gameoverl()
                                                exit = raw_input("(Press enter to exit the game)    ")
                                                # exits the game by death
                                                raise SystemExit
                                            #else cont fight (still alive)
                                    else:
                                        #no mob crit atk
                                        mobDMG = mobATK - pDEF
                                        if mobDMG < 0:
                                            #make it=0
                                            mobDMG = 0
                                        if pAVO >= randint(1, 100):
                                            # player dodge
                                            stopwatch2(1)
                                            print "You dodge the attack!"
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                        else:
                                            #mob no crit atk
                                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                            newpHP = pHP
                                            newpHP -= mobDMG
                                            if newpHP < 0:
                                                #make it not<0
                                                newpHP = 0
                                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                            pHP = newpHP
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                            if pHP == 0:
                                                # player defeated, player loses
                                                stopwatch2(1)
                                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                gameoverl()
                                                exit = raw_input("(Press enter to exit the game)    ")
                                                # exits the game by death
                                                raise SystemExit
                                            #else cont fight (still alive)
                                    stopwatch2(1)
                                    turnCount += 1
                                    print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                                    #crit chance
                                    if pCRIT >= randint(1, 100):
                                        pDMG = (pATK - mobDEF) * 2
                                        if pDMG < 0:
                                            #make it=0
                                            pDMG = 0
                                        if mobAVO >= randint(1, 100):
                                            # mob dodge
                                            stopwatch2(1)
                                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                        else:
                                            #crit atk
                                            print "[CRITICAL HIT!    x2 DAMAGE]"
                                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                            newmobHP = mobHP
                                            newmobHP -= pDMG
                                            if newmobHP < 0:
                                                #make it not<0                                
                                                newmobHP = 0
                                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                            mobHP = newmobHP
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                            if mobHP == 0:
                                                # mob defeated, player wins
                                                stopwatch2(1)
                                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                # gain gold
                                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                                pGold += mobGold
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                mobkills += 1
                                                break
                                    else:
                                        #no crit chance
                                        pDMG = pATK - mobDEF
                                        if pDMG < 0:
                                            #make it=0
                                            pDMG = 0
                                        if mobAVO >= randint(1, 100):
                                            # mob dodge
                                            stopwatch2(1)
                                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                        else:
                                            #no crit atk
                                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                            newmobHP = mobHP
                                            newmobHP -= pDMG
                                            if newmobHP < 0:
                                                #make it not<0
                                                newmobHP = 0
                                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                            mobHP = newmobHP
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                            if mobHP == 0:
                                                stopwatch2(1)
                                                # mob deafeated, player wins
                                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                # gain gold
                                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                                pGold += mobGold
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                mobkills += 1
                                                break
                                            #else cont fight (still alive)
            #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            elif mobTURN == "Focus":
                                turnCount += 1
                                # enemy focuses
                                mobCRITb += 10
                                print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+ 10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                                stopwatch2(1)
                                turnCount += 1
                                # player attacks
                                print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                                #crit chance
                                if pCRIT >= randint(1, 100):
                                    pDMG = (pATK - mobDEF) * 2
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #crit atk
                                        print "[CRITICAL HIT!    x2 DAMAGE]"
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0                                
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                        if mobHP == 0:
                                            # mob defeated, player wins
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                        #else cont fight (still alive)
                                else:
                                    #no crit chance
                                    pDMG = pATK - mobDEF
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #no crit atk
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                           print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                        pCRITb = 0
                                        if mobHP == 0:
                                            # mob deafeated, player wins
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                        #else cont fight (still alive)
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            elif mobTURN == "Flee":
                                turnCount += 1
                                # enemy attempts to flee - if fail, player attacks
                                print "\nThe Level " + str(mobLV) + " " + mob + " tries to flee!"
                                mobfleeAttempts += 1
                                escapechance = randint(0, 255)
                                escape = fleechance(mobDEX, pDEX, mobfleeAttempts)
                                print "Chance of escape = " + str(int((escape / float(256) * 100))) + "%"
                                if escape > 255:
                                    # Auto-escape
                                    stopwatch(2)
                                    print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                    if pCRITb > 0:
                                        print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                        pCRITb = 0
                                    # set mob escape to true
                                    print "\nYou gain 100 EXP"
                                    pEXP += 100
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobEscape = True
                                    break
                                elif escape > escapechance:
                                    # Successful escape
                                    stopwatch(2)
                                    print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                    if pCRITb > 0:
                                        print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                        pCRITb = 0
                                    # chance for drop gold and wpn
                                    if randint(1, 100) <= round(pLUK / 3):
                                        # drops all gold
                                        print "However, it dropped all of its gold in the process!"
                                        print "You gained " + str(mobGold) + " coins (Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins)"
                                        pGold += mobGold
                                    elif randint(1, 100) <= round(pLUK / 2):
                                        print "However, it dropped half of its gold in the process!"
                                        print "You gained " + str(int(round(mobGold * 0.5))) + " coins (Gold: " + str(pGold) + " -> " + str(int(round(pGold + mobGold * 0.5))) + " coins)"
                                        pGold += int(round((mobGold * 0.5)))
                                    # set mob escape to true
                                    print "\nYou gain 100 EXP"
                                    pEXP += 100
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobEscape = True
                                    break
                                else:
                                    # Failed flee attempt
                                    stopwatch(2)
                                    print "And is unsuccessful!\n[The Level " + str(mobLV) + " " + mob + " failed to escape]"
                                    turnCount += 1
                                    #player attacks
                                    stopwatch2(1)
                                    print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                                    #crit chance
                                    if pCRIT >= randint(1, 100):
                                        pDMG = (pATK - mobDEF) * 2
                                        if pDMG < 0:
                                            #make it=0
                                            pDMG = 0
                                        if mobAVO >= randint(1, 100):
                                            # mob dodge
                                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                        else:
                                            #crit atk
                                            print "[CRITICAL HIT!    x2 DAMAGE]"
                                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                            newmobHP = mobHP
                                            newmobHP -= pDMG
                                            if newmobHP < 0:
                                                #make it not<0                                
                                                newmobHP = 0
                                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                            mobHP = newmobHP
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                            if mobHP == 0:
                                                # mob defeated, player wins
                                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                # gain gold
                                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                                pGold += mobGold
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                mobkills += 1
                                                break
                                            #else cont fight (still alive)
                                    else:
                                        #no crit chance
                                        pDMG = pATK - mobDEF
                                        if pDMG < 0:
                                            #make it=0
                                            pDMG = 0
                                        if mobAVO >= randint(1, 100):
                                            # mob dodge
                                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                        else:
                                            #no crit atk
                                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                            newmobHP = mobHP
                                            newmobHP -= pDMG
                                            if newmobHP < 0:
                                                #make it not<0
                                                newmobHP = 0
                                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                            mobHP = newmobHP
                                            if pCRITb > 0:
                                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                                pCRITb = 0
                                            if mobHP == 0:
                                                # mob deafeated, player wins
                                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                # gain gold
                                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                                pGold += mobGold
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                mobkills += 1
                                                break
                                            #else cont fight (still alive)
            #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            else:   # enemy guard
                                turnCount += 1
                                turnCount += 1
                                #player attacks
                                print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                                # enemy guards
                                print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!\n"
                                stopwatch2(1)
                                #crit chance
                                if pCRIT >= randint(1, 100):
                                    pDMG = int(round(((pATK * 2) - mobDEF) / 2))
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #crit atk
                                        print "[CRITICAL HIT!    x2 DAMAGE]"
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0                                
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                        if mobHP == 0:
                                            # mob defeated, player wins
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                        #else cont fight (still alive)
                                else:
                                    #no crit chance
                                    pDMG = int(round((pATK - mobDEF) / 2))
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #no crit atk
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                        if mobHP == 0:
                                            # mob deafeated, player wins
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                        #else cont fight (still alive)
                            break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif pTURN.lower() == "guard":
                            turnCount += 1
                            # player guards
                            pTURN = "Guard"
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            if mobTURN == "Flee":
                                turnCount += 1
                                # enemy attempts to flee - if fail, player guards
                                print "\nThe Level " + str(mobLV) + " " + mob + " tries to flee!"
                                mobfleeAttempts += 1
                                escapechance = randint(0, 255)
                                escape = fleechance(mobDEX, pDEX, mobfleeAttempts)
                                print "Chance of escape = " + str(int((escape / float(256) * 100))) + "%"
                                if escape > 255:
                                    # Auto-escape
                                    stopwatch(2)
                                    print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                    if pCRITb > 0:
                                        print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                        pCRITb = 0
                                    # set mob escape to true
                                    print "\nYou gain 100 EXP"
                                    pEXP += 100
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobEscape = True
                                    break
                                elif escape > escapechance:
                                    # Successful escape
                                    stopwatch(2)
                                    print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                    if pCRITb > 0:
                                        print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                        pCRITb = 0
                                    # chance for drop gold and wpn
                                    if randint(1, 100) <= round(pLUK / 3):
                                        # drops all gold
                                        print "However, it dropped all of its gold in the process!"
                                        print "You gained " + str(mobGold) + " coins (Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins)"
                                        pGold += mobGold
                                    elif randint(1, 100) <= round(pLUK / 2):
                                        print "However, it dropped half of its gold in the process!"
                                        print "You gained " + str(int(round(mobGold * 0.5))) + " coins (Gold: " + str(pGold) + " -> " + str(int(round(pGold + mobGold * 0.5))) + " coins)"
                                        pGold += int(round((mobGold * 0.5)))
                                    # set mob escape to true
                                    print "\nYou gain 100 EXP"
                                    pEXP += 100
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobEscape = True
                                    break
                                else:
                                    # Failed flee attempt
                                    stopwatch(2)
                                    print "And is unsuccessful!\n[The Level " + str(mobLV) + " " + mob + " failed to escape]"
                                    #player guards, and fails
                                    stopwatch2(1)
                                    print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                                    print "     but it fails."
                                    break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            elif mobTURN == "Guard":
                                turnCount += 1
                                turnCount += 1
                                #player guards, and fails
                                print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                                print "     but it fails."
                                stopwatch2(1)
                                # enemy guards, and fails
                                print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!"
                                print "     but it fails."
                                break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            elif mobTURN == "Focus":
                                turnCount += 1
                                turnCount += 1
                                #player guards, and fails
                                print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                                print "     but it fails."
                                stopwatch2(1)
                                # enemy focuses
                                mobCRITb += 10
                                print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+ 10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                                break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            elif mobTURN == "Attack":
                                turnCount += 1
                                #player guards
                                print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                                turnCount += 1
                                stopwatch2(1)
                                # enemy attacks
                                print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                                #mob crit chance
                                if mobCRIT >= randint(1, 100):
                                    mobDMG = int(round(((mobATK * 2) - pDEF) / 2))
                                    if mobDMG < 0:
                                        #make it=0
                                        mobDMG = 0
                                    if pAVO >= randint(1, 100):
                                        # player dodge
                                        print "You dodge the attack!"
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                    else:
                                        #mob crit atk
                                        print "[CRITICAL HIT!    x2 DAMAGE]"
                                        print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                        newpHP = pHP
                                        newpHP -= mobDMG
                                        if newpHP < 0:
                                            #make it not<0
                                            newpHP = 0
                                        print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                        pHP = newpHP
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        if pHP == 0:
                                            # player defeated, player loses
                                            print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            gameoverl()
                                            exit = raw_input("(Press enter to exit the game)    ")
                                            # exits the game by death
                                            raise SystemExit
                                        #else cont fight (still alive)
                                else:
                                    #no mob crit atk
                                    mobDMG = int(round((mobATK - pDEF) / 2))
                                    if mobDMG < 0:
                                        #make it=0
                                        mobDMG = 0
                                    if pAVO >= randint(1, 100):
                                        # player dodge
                                        print "You dodge the attack!"
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                    else:
                                        #mob no crit atk
                                        print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                        newpHP = pHP
                                        newpHP -= mobDMG
                                        if newpHP < 0:
                                            #make it not<0
                                            newpHP = 0
                                        print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                        pHP = newpHP
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        if pHP == 0:
                                            # player deafeated, player loses
                                            print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            gameoverl()
                                            exit = raw_input("(Press enter to exit the game)    ")
                                            # exits the game by death
                                            raise SystemExit
                                        #else cont fight (still alive)
                                break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif pTURN.lower() == "focus":
                            pTURN = "Focus"
                            turnCount += 1
                            # player focuses, CRIT +10
                            pCRITb += 10
                            print "\nYou focus your energy (+10 CRIT -|- Total: + " + str(pCRITb) + " CRIT)"
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            if mobTURN == "Flee":
                                turnCount += 1
                                stopwatch2(1)
                                # enemy attempts to flee - if fail, player focuses
                                print "\nThe Level " + str(mobLV) + " " + mob + " tries to flee!"
                                mobfleeAttempts += 1
                                escapechance = randint(0, 255)
                                escape = fleechance(mobDEX, pDEX, mobfleeAttempts)
                                print "Chance of escape = " + str(int((escape / float(256) * 100))) + "%"
                                if escape > 255:
                                    # Auto-escape
                                    stopwatch(2)
                                    print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                    if pCRITb > 0:
                                        print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                        pCRITb = 0
                                    # set mob escape to true
                                    print "\nYou gain 100 EXP"
                                    pEXP += 100
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobEscape = True
                                    break
                                elif escape > escapechance:
                                    # Successful escape
                                    stopwatch(2)
                                    print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                    if pCRITb > 0:
                                        print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                        pCRITb = 0
                                    # chance for drop gold and wpn
                                    if randint(1, 100) <= round(pLUK / 3):
                                        # drops all gold
                                        print "However, it dropped all of its gold in the process!"
                                        print "You gained " + str(mobGold) + " coins (Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins)"
                                        pGold += mobGold
                                    elif randint(1, 100) <= round(pLUK / 2):
                                        print "However, it dropped half of its gold in the process!"
                                        print "You gained " + str(int(round(mobGold * 0.5))) + " coins (Gold: " + str(pGold) + " -> " + str(int(round(pGold + mobGold * 0.5))) + " coins)"
                                        pGold += int(round((mobGold * 0.5)))
                                    # set mob escape to true
                                    print "\nYou gain 100 EXP"
                                    pEXP += 100
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobEscape = True
                                    break
                                else:
                                    # Failed flee attempt
                                    stopwatch(2)
                                    print "And is unsuccessful!\n[The Level " + str(mobLV) + " " + mob + " failed to escape]"
                                    #player focuses, and gets bonus +5 CRIT
                                    pCRITb += 5
                                    print "During the time the Level " + str(mobLV) + " " + mob + " tried to flee, you were able to focus a little longer!\n\nYou focus your energy a little extra (+ 5 CRIT -|- Total: + " + str(pCRITb) + " CRIT)"
                                    break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            elif mobTURN == "Guard":
                                turnCount += 1
                                stopwatch2(1)
                                # enemy guards, and fails
                                print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!"
                                print "     but it fails."
                                break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            elif mobTURN == "Focus":
                                turnCount += 1
                                stopwatch2(1)
                                # enemy focuses
                                mobCRITb += 10
                                print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                                #player and enemy focus, and get bonus +5 CRIT each
                                pCRITb += 5
                                print "\nDuring the time the Level " + str(mobLV) + " " + mob + " was also focusing, you were able to focus a little longer!\n\nYou focus your energy a little extra (+ 5 CRIT -|- Total: + " + str(pCRITb) + " CRIT)"
                                mobCRITb += 5
                                print "\n     but so did the Level " + str(mobLV) + " " + mob + " (+ 5 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                                break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            elif mobTURN == "Attack":
                                turnCount += 1
                                stopwatch2(1)
                                #mob attacks (not KO)
                                print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                                #mob crit chance
                                if mobCRIT >= randint(1, 100):
                                    mobDMG = (mobATK - pDEF) * 2
                                    if mobDMG < 0:
                                        #make it=0
                                        mobDMG = 0
                                    if pAVO >= randint(1, 100):
                                        # player dodge
                                        print "You dodge the attack!"
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        break
                                    else:
                                        #mob crit atk
                                        print "[CRITICAL HIT!    x2 DAMAGE]"
                                        print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                        newpHP = pHP
                                        newpHP -= mobDMG
                                        if newpHP < 0:
                                            #make it not<0
                                            newpHP = 0
                                        print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                        pHP = newpHP
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        if pHP == 0:
                                            # player defeated, player loses
                                            print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            gameoverl()
                                            exit = raw_input("(Press enter to exit the game)    ")
                                            # exits the game by death
                                            raise SystemExit
                                        #else cont fight (still alive)
                                        break
                                else:
                                    #no mob crit atk
                                    mobDMG = mobATK - pDEF
                                    if mobDMG < 0:
                                        #make it=0
                                        mobDMG = 0
                                    if pAVO >= randint(1, 100):
                                        # player dodge
                                        print "You dodge the attack!"
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                    else:
                                        #mob no crit atk
                                        print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                        newpHP = pHP
                                        newpHP -= mobDMG
                                        if newpHP < 0:
                                            #make it not<0
                                            newpHP = 0
                                        print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                        pHP = newpHP
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        if pHP == 0:
                                            # player defeated, player loses
                                            print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            gameoverl()
                                            exit = raw_input("(Press enter to exit the game)    ")
                                            # exits the game by death
                                            raise SystemExit
                                        #else cont fight (still alive)
                                    break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif pTURN.lower() == "flee":
                            pTURN = "Flee"
                            turnCount += 1
                            # attempts to flee
                            print "\nYou try to escape from the Level " + str(mobLV) + " " + mob + "!"
                            if mobTURN == "Flee":
                                # mob flees too
                                turnCount += 1
                                print "\nThis particular Level " + str(mobLV) + " " + mob + " has also tried to flee at the same time so the battle ends in a draw!"
                                print "\nWhat a coincidence!  You learn from this unique experience and gain 200 EXP!"
                                pEXP += 200
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobkills += 1
                                # set mob escape to true
                                mobEscape = True
                                # set player escape to true
                                pEscape = True
                                break
                            else:
                                fleeAttempts += 1
                                escapechance = randint(0, 255)
                                escape = fleechance(pDEX, mobDEX, fleeAttempts)
                                if escape > 255:
                                    # Auto-escape
                                    stopwatch(2)
                                    print "And are successful!\n[You manage to successfully get away from the Level " + str(mobLV) + " " + mob + "]"
                                    if pCRITb > 0:
                                        print "You lose all your focus after you escape (-" + str(pCRITb) + " CRIT)"
                                        pCRITb = 0
                                    # set player escape to true
                                    print "\nYou gain 50 EXP"
                                    pEXP += 50
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    pEscape = True
                                    break
                                elif escape > escapechance:
                                    # Successful escape
                                    stopwatch(2)
                                    print "And are successful!\n[You manage to successfully get away from the Level " + str(mobLV) + " " + mob + "]"
                                    if pCRITb > 0:
                                        print "You lose all your focus after you escape (-" + str(pCRITb) + " CRIT)"
                                        pCRITb = 0
                                    # chance for you to lose gold
                                    if randint(1, 100) <= round(mobLUK / 5):
                                        # lose 25% of gold
                                        goldLost = int(round(pGold * 0.25))
                                        print "However, the Level " + str(mobLV) + " " + mob + " managed to steal a quarter of your gold."
                                        print "You lost " + str(goldLost) + " coins (Gold: " + str(pGold) + " -> " + str(pGold - goldLost) + " coins)"
                                        pGold -= goldLost
                                        goldLost = 0
                                    elif randint(1, 100) <= round(mobLUK / 4):
                                        # lose 10% of gold
                                        goldLost = int(round(pGold * 0.1))
                                        print "However, the Level " + str(mobLV) + " " + mob + " managed to steal a fraction of your gold."
                                        print "You lost " + str(goldLost) + " coins (Gold: " + str(pGold) + " -> " + str(pGold - goldLost) + " coins)"
                                        pGold -= goldLost
                                        goldLost = 0
                                    # set player escape to true
                                    print "\nYou gain 50 EXP"
                                    pEXP += 50
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    pEscape = True
                                    break
                                else:
                                    # Failed flee attempt
                                    stopwatch(2)
                                    print "And are unsuccessful!\n[You failed to get away from the Level " + str(mobLV) + " " + mob + " successfully]"
                                    stopwatch2(1)
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                                    if mobTURN == "Guard":
                                        turnCount += 1
                                        # enemy guards, and fails
                                        print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!"
                                        print "     but it fails."
                                        break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                                    elif mobTURN == "Focus":
                                        turnCount += 1
                                        # enemy focuses
                                        mobCRITb += 10
                                        print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+ 10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                                        break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                                    elif mobTURN == "Attack":
                                        turnCount += 1
                                        # enemy attacks
                                        print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                                        #mob crit chance
                                        if mobCRIT >= randint(1, 100):
                                            mobDMG = (mobATK - pDEF) * 2
                                            if mobDMG < 0:
                                                #make it=0
                                                mobDMG = 0
                                            if pAVO >= randint(1, 100):
                                                # player dodge
                                                print "You dodge the attack!"
                                                if mobCRITb > 0:
                                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                    mobCRITb = 0
                                            else:
                                                #mob crit atk
                                                print "[CRITICAL HIT!    x2 DAMAGE]"
                                                print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                                newpHP = pHP
                                                newpHP -= mobDMG
                                                if newpHP < 0:
                                                    #make it not<0
                                                    newpHP = 0
                                                print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                                pHP = newpHP
                                                if mobCRITb > 0:
                                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                    mobCRITb = 0
                                                if pHP == 0:
                                                    # player defeated, player loses
                                                    print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                    turnCounta += turnCount
                                                    turnCount = 0
                                                    mobfleeAttempts = 0
                                                    mobEscape = False
                                                    fleeAttempts = 0
                                                    pEscape = False
                                                    gameoverl()
                                                    exit = raw_input("(Press enter to exit the game)    ")
                                                    # exits the game by death
                                                    raise SystemExit
                                                #else cont fight (still alive)
                                        else:
                                            #no mob crit atk
                                            mobDMG = mobATK - pDEF
                                            if mobDMG < 0:
                                                #make it=0
                                                mobDMG = 0
                                            if pAVO >= randint(1, 100):
                                                # player dodge
                                                print "You dodge the attack!"
                                                if mobCRITb > 0:
                                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                    mobCRITb = 0
                                            else:
                                                #mob no crit atk
                                                print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                                newpHP = pHP
                                                newpHP -= mobDMG
                                                if newpHP < 0:
                                                    #make it not<0
                                                    newpHP = 0
                                                print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                                pHP = newpHP
                                                if mobCRITb > 0:
                                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                    mobCRITb = 0
                                                if pHP == 0:
                                                    # player deafeated, player loses
                                                    print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                    turnCounta += turnCount
                                                    turnCount = 0
                                                    mobfleeAttempts = 0
                                                    mobEscape = False
                                                    fleeAttempts = 0
                                                    pEscape = False
                                                    gameoverl()
                                                    exit = raw_input("(Press enter to exit the game)    ")
                                                    # exits the game by death
                                                    raise SystemExit
                                                #else cont fight (still alive)
                                        break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif pTURN.lower() == "/help":
                            print "'/enemystats'"
                            HELP()
                        elif pTURN.lower() == "/playerstats":
                            playerstats()
                        elif pTURN.lower() == "/enemystats":
                            enemystats()
                        else:
                            print ("\n[INVALID, please try again]")

        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            
                else: # check these after battle is won
                    if mobHP <= 0:
                        # gain exp for win
                        print "\nYou obtain " + str(mobEXP) + " EXP for defeating the Level " + str(mobLV) + " " + mob + "."
                        pEXP += mobEXP
                        
                    if mobHP <= 0 or mobTURN == "Flee":
                        # calc chance to drop mob wpn
                        if randint(1, 100) <= mobDropwc:
                            print "\nThe Level " + str(mobLV) + " " + mob + " dropped its " + mobWPNd + "!"
                            #ask if want to use instead of current wpn
                            while True:
                                yn = raw_input("[Do you want to equip the " + mobWPNd + " (Bonus: +" + str(mobWPN) + " ATK, +" + str(mobWPNl) + " CRIT)]     ('Y'es or 'N'o)     ")
                                if yn.lower() == "y" or yn.lower() == "n":
                                    ayn = raw_input("Last Chance, do you want it or not?  ('Y'es or 'N'o)     ")
                                    if ayn.lower() == "y":
                                        print "\n[You swap your " + pWPNd + " (Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT) for the " + mobWPNd + " (Bonus: +" + str(mobWPN) + " ATK, +" + str(mobWPNl) + " CRIT)]"
                                        pWPN = mobWPN
                                        pWPNd = mobWPNd
                                        pWPNl = mobWPNl
                                        break
                                    elif ayn.lower() == "n":
                                        print "\n[You decide your weapon is still better and destroy the Level " + str(mobLV) + " " + mob + "'s " + mobWPNd + "]\n[ + 500 EXP]"
                                        pEXP += 500
                                        break
                                    elif ayn.lower() == "/help":
                                        HELP()
                                    elif ayn.lower() == "/playerstats":
                                        playerstats()
                                    elif ayn.lower() == "/enemystats":
                                        enemystats()
                                    else:
                                        print ("\n[INVALID, please try again]")
                                elif yn.lower() == "/help":
                                    HELP()
                                elif yn.lower() == "/playerstats":
                                    playerstats()
                                elif yn.lower() == "/enemystats":
                                    enemystats()
                                else:
                                    print ("\n[INVALID, please try again]")
                                
                    while pEXP >= pLVupEXPCount:
                        #LV UP
                        pLV += 1
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        print "\n[LEVEL UP: " + name + ", you are now a Level " + str(pLV) + " " + fclass + " " + race + "]"
                        statCount = int(round(randint(0, 100) / 20))
                        newpHPmax = pHPmax + statCount
                        print "\nHP MAX: " + str(pHPmax) + " -> " + str(newpHPmax) + "    (+" + str(newpHPmax - pHPmax) + ")"
                        pHPmax = newpHPmax
                        pHP += statCount
                        statCount = int(round(randint(0, 100) / 20))
                        newpMPmax = pMPmax + statCount
                        print "MP MAX: " + str(pMPmax) + " -> " + str(newpMPmax) + "    (+" + str(newpMPmax - pMPmax) + ")"
                        pMPmax = newpMPmax
                        pMP += statCount
                        statCount = int(round(randint(0, 100) / 20))
                        newpSTR = pSTR + statCount
                        newpATK = newpSTR + pWPN
                        print "ATK: " + str(pATK) + " -> " + str(newpATK) + "       (+" + str(newpATK - pATK) + ")"
                        print "     STR: " + str(pSTR) + " -> " + str(newpSTR) + "  (+" + str(newpSTR - pSTR) + ")"
                        print "     Weapon = " + pWPNd + " | Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT"
                        pATK = newpATK
                        pSTR = newpSTR
                        statCount = int(round(randint(0, 100) / 20))
                        newpDEF = pDEF + statCount
                        print "DEF: " + str(pDEF) + " -> " + str(newpDEF) + "       (+" + str(newpDEF - pDEF) + ")"
                        pDEF = newpDEF
                        statCount = int(round(randint(0, 100) / 20))
                        newpDEX = pDEX + statCount
                        print "DEX: " + str(pDEX) + " -> " + str(newpDEX) + "       (+" + str(newpDEX - pDEX) + ")"
                        pDEX = newpDEX
                        statCount = int(round(randint(0, 100) / 20))
                        newpINT = pINT + statCount
                        print "INT: " + str(pINT) + " -> " + str(newpINT) + "       (+" + str(newpINT - pINT) + ")"
                        pINT = newpINT
                        statCount = int(round(randint(0, 100) / 20))
                        newpLUK = pLUK + statCount
                        print "LUK: " + str(pLUK) + " -> " + str(newpLUK) + "       (+" + str(newpLUK - pLUK) + ")"
                        pLUK = newpLUK
                        newpCRIT = round(pLUK + pWPNl + pCRITb) / 2
                        newpAVO = round(pLUK + pDEX) / 2
                        print "     CRIT chance: " + str(pCRIT - pCRITb) + "% (+" + str(pCRITb) + "%) -> " + str(newpCRIT) + "% (+" + str(pCRITb) + "%)" + "    (+" + str(newpCRIT - pCRIT) + ")"
                        print "     AVO chance: " + str(pAVO) + "% -> " + str(newpAVO) + "%                 (+" + str(newpAVO - pAVO) + ")\n"
                        pCRIT = newpCRIT
                        pAVO = newpAVO
                        cont = raw_input("\n(Press enter to continue)")

                    # display exp until next lv
                    print "\nEXP until next level = " + str(pLVupEXPCount - pEXP)
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPregen = int(round(pMPmax * pMPregenRate))
                        
                    # HP regen
                    newpHP = pHP
                    newpHP += pHPregen
                    if newpHP > pHPmax:
                        # make it=max
                        newpHP = pHPmax
                    print "\nYou regenerate " + str(pHPregen) + " HP after the battle\nHP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                    pHP = newpHP
                    # MP regen
                    newpMP = pMP
                    newpMP += pMPregen
                    if newpMP > pMPmax:
                        # make it=max
                        newpMP = pMPmax
                    print "You regenerate " + str(pMPregen) + " MP after the battle\nMP = " + str(pMP) + "/" + str(pMPmax) + " -> " + str(newpMP) + "/" + str(pMPmax) + "\n"
                    pMP = newpMP

                    turnCounta += turnCount
                    turnCount = 0
                    mobfleeAttempts = 0
                    mobEscape = False
                    fleeAttempts = 0
                    pEscape = False
                    mobkills += 1
                    '''if mobTURN == "Flee" and mobHP != 0:
                        print "DAMN!  It got away!"'''
                    # end fight sequence
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

            stopwatch2(1)
            print "[All of the monsters have been defeated!]"
            cont = raw_input("\n(Press enter to continue)\n")
            print "Young Hunter:    'Wow, kid.  You've got some untapped potential.'"
            print "Isaac the Wise:  'Yes indeed.  I predict that you will accomplish great things if you can survive this tragedy.'"
            print "Heavy Brute:     'Anyways, where did all these pests come from?  They just started rampaging out of nowhere!'"
            cont = raw_input("\n(Press enter to continue)\n")
            print "\n[By now, the Panicked Messenger has calmed down and relaxed himself]\n"
            print "Messenger:       'They flooded out of the unconquerable dungeon that rose out of out of the earth southeast of here.'"
            print "Noble Knight:    'Friends, he speaks the truth.  I also saw the horde running rampant on my way to the village before I encountered some of the pesky fiends myself.'"
            print "Heavy Brute:     'I heard from my brother that they have been spilling out of the dungeon in attempt to overpower adventurers with sheer numbers.'"
            cont = raw_input("\n(Press enter to continue)\n")
            print "Isaac the Wise:  'This is very bad my friends.  As it seems, the monsters will continue to devestate Konaha and its inhabitants.'"
            print "Isaac the Wise:  'Therefore, we must clear the dungeon in order to protect our village.'"
            print "Young Hunter:    'But no one here is strong enough to defeat an entire dungeon of creatures and the final boss!'"
            cont = raw_input("\n(Press enter to continue)\n")
            print "Isaac the Wise:  'However, we must try anyways.  If they're left alone, they will build up enough strength to overrun the village.'"
            print "Noble Knight:    'Rest assurred fellow adventurers.  I have devised a plan to conquer the dungeon.'"
            print "Heavy Brute:     'What are you thinking?  How can someone achieve a feat that great?'"
            cont = raw_input("\n(Press enter to continue)\n")
            print "Noble Knight:    'Our new friend here has display potential unlike any I have ever seen.  I believe that, with the proper mentoring, he will become a valiant warrior capable of accomplishing in the task we ask of him.'"
            print "Isaac the Wise:  'What!?  Are you sure?  He is but a child who has inhaled his first breath of intense combat.'"
            print "Noble Knight:    'And yet he has done very well considering his severe lack of experience.  Look over there.'"
            cont = raw_input("\n(Press enter to continue)\n")
            print "[The Noble Knight points to a human corpse at the edge of the tree line]\n"
            print "Isaac the Wise:  'Great Zeus!  That is the skilled assassin who was just boasting of his last job just a moment ago!'"
            print "Noble Knight:    'Exactly my point.  No matter how skilled one is he must have acceptional knowledge and tutoring to survive.'"
            print "Noble Knight:    'Even the strongest warrior can be killed by even a weak Slime by the cause of one simple, but costly mistake.'"
            cont = raw_input("\n(Press enter to continue)\n")
            print "Isaac the Wise:  'I'm sorry lad, but it appears that a large portion of your youth is going to be stolen from you for the greater good of Konoha.'"
            stopwatch2(1)
            while True:
                mentor = raw_input("\n(If you wish to accept the Noble Knight as your teacher for three long years, type 'TEACHER'.  Otherwise, type 'SOLO', to try and conquer the dungeon now.)    ")
                if mentor.lower() == "teacher":
                    # train for 3 years, +3-5 lvs
                    print "\n[You become the new apprentice of the Noble Knight as you accept him as a mentor]"
                    cont = raw_input("\n(Press enter to continue)\n")
                    print "Noble Knight:    'Very well then, I, Sir Theodore the Galant, shall train you as my disciple.  It may be a tedious and long three years, but the fruits that we produce shall be well worth the effort.'"
                    print "Isaac the Wise:  'Farewell, young lad, I hope our paths will cross again.  I wish you the best of luck on your training.'"
                    print "Sir Theodore:    'Follow me, " + name + ", we have a lot of traiing ahead of us.'"
                    print "\n[You leave Konoha Village to train with Sir Theodore the Galant]\n"
                    cont = raw_input("\n(Press enter to continue)\n")
                    print "[With your new mentor, you train vigorously for the three long years]"
                    # +3-5 lvs
                    rndnum = randint(3, 5)
                    if rndnum == 3:
                        # +3 lvs
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        newpHPmax = pHPmax
                        newpMPmax = pMPmax
                        newpSTR = pSTR
                        newpDEF = pDEF
                        newpDEX = pDEX
                        newpINT = pINT
                        newpLUK = pLUK
                        # give enough exp for 3 lvups and no more
                        for i in range(3):
                            #LV UP
                            pLV += 1
                            statCount = int(round(randint(0, 100) / 20))
                            newpHPmax += statCount
                            pHP += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpMPmax += statCount
                            pMP += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpSTR += statCount
                            newpATK = newpSTR + pWPN
                            statCount = int(round(randint(0, 100) / 20))
                            newpDEF += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpDEX += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpINT += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpLUK += statCount
                            newpCRIT = round(newpLUK + pWPNl + pCRITb) / 2
                            newpAVO = round(newpLUK + newpDEX) / 2
                    elif rndnum == 4:
                        # +4 lvs
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        newpHPmax = pHPmax
                        newpMPmax = pMPmax
                        newpSTR = pSTR
                        newpDEF = pDEF
                        newpDEX = pDEX
                        newpINT = pINT
                        newpLUK = pLUK
                        # give enough exp for 4 lvups and no more
                        for i in range(4):
                            #LV UP
                            pLV += 1
                            statCount = int(round(randint(0, 100) / 20))
                            newpHPmax += statCount
                            pHP += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpMPmax += statCount
                            pMP += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpSTR += statCount
                            newpATK = newpSTR + pWPN
                            statCount = int(round(randint(0, 100) / 20))
                            newpDEF += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpDEX += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpINT += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpLUK += statCount
                            newpCRIT = round(newpLUK + pWPNl + pCRITb) / 2
                            newpAVO = round(newpLUK + newpDEX) / 2
                    else:
                        # +5 lvs
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        pEXP += (pLVupEXPCount - pEXP) #+1 lv
                        pLVupEXP += 75
                        pLVupEXPCount += pLVupEXP
                        newpHPmax = pHPmax
                        newpMPmax = pMPmax
                        newpSTR = pSTR
                        newpDEF = pDEF
                        newpDEX = pDEX
                        newpINT = pINT
                        newpLUK = pLUK
                        # give enough exp for 5 lvups and no more
                        for i in range(5):
                            #LV UP
                            pLV += 1
                            statCount = int(round(randint(0, 100) / 20))
                            newpHPmax += statCount
                            pHP += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpMPmax += statCount
                            pMP += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpSTR += statCount
                            newpATK = newpSTR + pWPN
                            statCount = int(round(randint(0, 100) / 20))
                            newpDEF += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpDEX += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpINT += statCount
                            statCount = int(round(randint(0, 100) / 20))
                            newpLUK += statCount
                            newpCRIT = round(newpLUK + pWPNl + pCRITb) / 2
                            newpAVO = round(newpLUK + newpDEX) / 2
                        
                    # print stat changes    
                    print "[You gained " + str(rndnum) + " Levels]"
                    print "\n[LEVEL UP: " + name + ", you are now a Level " + str(pLV) + " " + fclass + " " + race + "]"
                    print "\nHP MAX: " + str(pHPmax) + " -> " + str(newpHPmax) + "    (+" + str(newpHPmax - pHPmax) + ")"
                    pHPmax = newpHPmax
                    print "MP MAX: " + str(pMPmax) + " -> " + str(newpMPmax) + "    (+" + str(newpMPmax - pMPmax) + ")"
                    pMPmax = newpMPmax
                    print "ATK: " + str(pATK) + " -> " + str(newpATK) + "           (+" + str(newpATK - pATK) + ")"
                    print "     STR: " + str(pSTR) + " -> " + str(newpSTR) + "      (+" + str(newpSTR - pSTR) + ")"
                    print "     Weapon = " + pWPNd + " | Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT"
                    pATK = newpATK
                    pSTR = newpSTR
                    print "DEF: " + str(pDEF) + " -> " + str(newpDEF) + "           (+" + str(newpDEF - pDEF) + ")"
                    pDEF = newpDEF
                    print "DEX: " + str(pDEX) + " -> " + str(newpDEX) + "       (+" + str(newpDEX - pDEX) + ")"
                    pDEX = newpDEX
                    print "INT: " + str(pINT) + " -> " + str(newpINT) + "       (+" + str(newpINT - pINT) + ")"
                    pINT = newpINT
                    print "LUK: " + str(pLUK) + " -> " + str(newpLUK) + "       (+" + str(newpLUK - pLUK) + ")"
                    pLUK = newpLUK
                    print "     CRIT chance: " + str(pCRIT - pCRITb) + "% (+" + str(pCRITb) + "%) -> " + str(newpCRIT) + "% (+" + str(pCRITb) + "%)     (+" + str(newpCRIT - pCRIT) + ")"
                    print "     AVO chance: " + str(pAVO) + "% -> " + str(newpAVO) + "%                     (+" + str(newpAVO - pAVO) + ")\n"
                    pCRIT = newpCRIT
                    pAVO = newpAVO
                    cont = raw_input("\n(Press enter to continue)")
                    # display exp until next lv
                    print "\nEXP until next level = " + str(pLVupEXPCount - pEXP)
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPregen = int(round(pMPmax * pMPregenRate))
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                    
                    print "\n[During the time you are training, the unconquerable dungeon southeast of Konoha has become even more dangerous]"
                    cont = raw_input("\n(Press enter to continue)\n")
                    print "Sir Theodore:    '" + name + ", I beleive that you are finally ready to take on the infamous dungeon.'"
                    print "Sir Theodore:    'I have taught you all of my knowledge and you have surpassed me in skill quite some time ago.  The only difference in our power is the amount of true battle experience.'"
                    print "Sir Theodore:    'And that, my student, is something one cannot teach, but must be obtained through the act it self.'"
                    cont = raw_input("\n(Press enter to continue)\n")
                    print "Sir Theodore:    'Now, set out for the dungeon.  Let us not waste anymore time than we already have.  I shall pray to Zeus for your well-being and I wish you good luck on your journey.'"
                    print "\n[You leave your master and travel back to Konoha village to conquer the dungeon that has been wrecking havoc there]"
                    break
                
                elif mentor.lower() == "solo":
                    # go to dungeon right now
                    print "\n[You decide that you are already strong enough to clear the dungeon]"
                    cont = raw_input("\n(Press enter to continue)\n")
                    print "Heavy Brute:     'Amazing a youthful spirit like yourself is very rare in these dark times.'"
                    print "Noble Knight:    'As you wish, " + name + ", if you believe that you can overcome such a feat, I will trust in you capabilities and raw, natural talent and skill.'"
                    print "Isaac the Wise:  'I guess you will be able to retain your youthful fire.  I wish you the best of luck, " + name + " the " + fclass + " " + warior + ".'"
                    print "\n[You leave the tavern and head southeast to conquer the dungeon that mysteriously emmerged from the earth]"
                    break
                elif mentor.lower() == "/help":
                    print "/playerstats"
                elif mentor.lower() == "/playerstats":
                    playerstats()
                else:
                    print "\n[INVALID, please try again]"
                
            # FINISH THIS

    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
        else:
            # NO challenger
            print "[You stay seated and quiet.  You continue to drink your ale like the true coward you are; however, the bartender calls you out]\n"
            print "Bartender:   'What about you?  You're fresh meat, eh?'"
            print "Old man:     'Hey there newbie!  I'm Isaac the Wise, one of the first adventurers and the very first Hunter in existence.'"
            print "Isaac the Wise:  And you are?"
            # enter name, class, race
            print "\n[Introduce yourself]\n"
            stopwatch2(1)
            # NAME
            while nameCount == 0:
                name = raw_input("Enter your name:      ")
                ynName = raw_input("Are you sure with the name " + name + "?    ('Y'es or 'N'o)     ")
                if ynName.lower() == "y":
                    nameCount = 1
            # RACE
            while raceCount == 0:
                race = raw_input("\nEnter your race:\nHUMAN\nORC\nELF\nUNDEAD\nMYSTERY\nSAIYAN [for testing purposes]   ")
                if race.lower() == "human":
                    race = "Human"
                    # balanced race
                    pHPmax = 15
                    pHP = pHPmax
                    pHPregenRate = 0.25
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 15
                    pMP = pMPmax
                    pMPregenRate = 0.25
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 10
                    pATK = pSTR + pWPN
                    pDEF = 10
                    pDEX = 10
                    pINT = 10                   
                    pLUK = 15
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "orc":
                    race = "Orc"
                    # tank race
                    pHPmax = 30
                    pHP = pHPmax
                    pHPregenRate = 0.3
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 20
                    pMP = pMPmax
                    pMPregenRate = 0.25
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 13
                    pATK = pSTR + pWPN
                    pDEF = 15
                    pDEX = 5
                    pINT = 5
                    pLUK = 8
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "elf":
                    race = "Elf"
                    # standard elf perks
                    pHPmax = 15
                    pHP = pHPmax
                    pHPregenRate = 0.25
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 25
                    pMP = pMPmax
                    pMPregenRate = 0.3
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 10
                    pATK = pSTR + pWPN
                    pDEF = 9
                    pDEX = 13
                    pINT = 13
                    pLUK = 15
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "undead":
                    race = "Undead"
                    # str & mp & luk race
                    pHPmax = 20
                    pHP = pHPmax
                    pHPregenRate = 0.35
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 30
                    pMP = pMPmax
                    pMPregenRate = 0.2
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 17
                    pATK = pSTR + pWPN
                    pDEF = 12
                    pDEX = 5
                    pINT = 7
                    pLUK = 30
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "mystery":
                    race = "Mystery"
                    # random generated stats from 5 -> 30
                    pHPmax = randint(10, 30)
                    pHP = pHPmax
                    pHPregenRate = (roundint5(randint(15, 35))) * 0.01
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = randint(10, 30)
                    pMP = pMPmax
                    pMPregenRate = (roundint5(randint(15, 35))) * 0.01
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = randint(5, 20)
                    pATK = pSTR + pWPN
                    pDEF = randint(5, 20)
                    pDEX = randint(5, 20)
                    pINT = randint(5, 20)
                    pLUK = randint(5, 30)
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                elif race.lower() == "saiyan":
                    race = "Saiyan"
                    # testing OP race
                    pLV = 1
                    pEXP = 0
                    pLVupEXP = 50
                    pHPmax = 9001
                    pHP = pHPmax
                    pHPregenRate = 0.001
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 9001
                    pMP = pMPmax
                    pMPregenRate = 0.001
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 9001
                    pWPN = 0
                    pWPNd = "Saiyan Fists"
                    pWPNl = 0
                    pATK = pSTR + pWPN
                    pDEF = 20
                    pDEX = 10
                    pINT = 9001
                    pLUK = 50
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    raceCount = 1
                else:
                    print ("\n[INVALID, please try again]")
                
            # CLASS
            while fclassCount == 0:
                fclass = raw_input("\nChoose a class:\nWARRIOR (bal)\nROGUE (dps)\nPALADIN (tank)\nUNKNOWN\nSSGSS [for testing purposes]     ")
                if fclass.lower() == "warrior":
                    fclass = "Warrior"
                    # balanced class
                    #BALANCED
                    pWPN = 3
                    pWPNd = "Bronze Sword"
                    pWPNl = 5
                    pATK = pSTR + pWPN
                    pLUK += 15
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    fclassCount = 1
                elif fclass.lower() == "rogue":
                    fclass = "Rogue"
                    # dps class
                    #HP
                    #MP
                    pSTR += 10
                    pWPN = 2
                    pWPNd = "Bronze Dagger"
                    pWPNl = 15
                    pATK = pSTR + pWPN
                    #DEF
                    pDEX += 10
                    pINT += 3
                    pLUK += 20
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    fclassCount = 1
                elif fclass.lower() == "paladin":
                    fclass = "Paladin"
                    # tank class
                    pHPmax += 5
                    pHP = pHPmax
                    #MP
                    pSTR += 5
                    pWPN = 4
                    pWPNd = "Bronze Lance"
                    pWPNl = 5
                    pATK = pSTR + pWPN
                    pDEF += 10
                    pDEX -= 3
                    pINT -= 2
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    #LUK
                    fclassCount = 1
                elif fclass.lower() == "unknown":
                    fclass = "Unknown"
                    # random stat bonus / minus class
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pHPmax += randint(1, 5)
                    else:
                        pHPmax -= randint(1, 5)
                    pHP = pHPmax
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pMPmax += randint(1, 5)
                    else:
                        pMPmax -= randint(1, 5)
                    pMP = pMPmax
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pSTR += randint(1, 5)
                    else:
                        pSTR -= randint(1, 5)
                    pmCount = randint(1, 5)
                    if pmCount == 1:
                        pWPN = 2
                        pWPNd = "Bronze Dagger"
                        pWPNl = 15
                    elif pmCount == 2:
                        pWPN = 3
                        pWPNd = "Bronze Sword"
                        pWPNl = 5
                    elif pmCount == 3:
                        pWPN = 4
                        pWPNd = "Bronze Lance"
                        pWPNl = 5
                    elif pmCount == 4:
                        pWPN = 5
                        pWPNd = "Bronze Hammer"
                        pWPNl = 5
                    else:
                        pWPN = 5
                        pWPNd = "Bronze Axe"
                        pWPNl = 10
                    pATK = pSTR + pWPN
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pDEF += randint(1, 5)
                    else:
                        pDEF -= randint(1, 5)
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pDEX += randint(1, 5)
                    else:
                        pDEX -= randint(1, 5)
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pINT += randint(1, 5)
                    else:
                        pINT -= randint(1, 5)
                    pmCount = randint(1, 2)
                    if pmCount == 1:
                        pLUK += randint(1, 5)
                    else:
                        pLUK -= randint(1, 5)
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    fclassCount = 1
                elif fclass.lower() == "ss g ss" or fclass.lower() == "ssgss":
                    fclass = "Super Saiyan God Super"
                    # str & mp & luk race
                    pLV = 1
                    pEXP = 0
                    pLVupEXP = 50
                    pHPmax = 9999
                    pHP = pHPmax
                    pHPregenRate = 0.001
                    pHPregen = int(round(pHPmax * pHPregenRate))
                    pMPmax = 9999
                    pMP = pMPmax
                    pMPregenRate = 0.001
                    pMPregen = int(round(pMPmax * pMPregenRate))
                    pSTR = 9999
                    pWPN = 0
                    pWPNd = "Super Saiyan God Super " + name + " Fists"
                    pWPNl = 25
                    pATK = pSTR + pWPN
                    pDEF = 20
                    pDEX = 10
                    pINT = 9999
                    pLUK = 50
                    pCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    pAVO = round(pLUK + pDEX) / 2
                    fclassCount = 1
                else:
                    print ("\n[INVALID, please try again]")

            # print stats to user
            print "\n[NOTE TO PLAYER]\n[Your current stats:]\n"
            stopwatch2(1)
            playerstats()
            print "\n[NOTE TO PLAYER:]"
            stopwatch2(1)
            print "[You can now type /help to see commands you can use in any enter text instance.]"
            cont = raw_input("\n(Press enter to continue)\n")
            
            print "Isaac the Wise:  Nice to meet you, " + name + " the " + fclass + " " + race + ".  I'm not much of a fighter myself, as you can clearly see.  I retired from that life a long time ago.'"
            # white paladin volunteers instead of you
            print "\n[A White Paladin across the bar volunteers]\n"
            cont = raw_input("\n(Press enter to continue)\n")
            print "White Paladin:   'I will do whatever I can to help my friends, 'tis my nature to protect others.'"
            print "\n[The other adventurers take-on the horde of creatures stampeding towards the tavern]\n"
            print "[Simply watching the skilled warriors partake in combat has taught you a few tricks (+50 exp)]\n"
            pEXP += 50
            while pEXP >= pLVupEXPCount:
                #LV UP
                pLV += 1
                pLVupEXP += 75
                pLVupEXPCount += pLVupEXP
                print "\n[LEVEL UP: " + name + ", you are now a Level " + str(pLV) + " " + fclass + " " + race + "]"
                statCount = int(round(randint(0, 100) / 20))
                newpHPmax = pHPmax + statCount
                print "\nHP MAX: " + str(pHPmax) + " -> " + str(newpHPmax) + "    (+" + str(newpHPmax - pHPmax) + ")"
                pHPmax = newpHPmax
                pHP += statCount
                statCount = int(round(randint(0, 100) / 20))
                newpMPmax = pMPmax + statCount
                print "MP MAX: " + str(pMPmax) + " -> " + str(newpMPmax) + "    (+" + str(newpMPmax - pMPmax) + ")"
                pMPmax = newpMPmax
                pMP += statCount
                statCount = int(round(randint(0, 100) / 20))
                newpSTR = pSTR + statCount
                newpATK = newpSTR + pWPN
                print "ATK: " + str(pATK) + " -> " + str(newpATK) + "       (+" + str(newpATK - pATK) + ")"
                print "     STR: " + str(pSTR) + " -> " + str(newpSTR) + "  (+" + str(newpSTR - pSTR) + ")"
                print "     Weapon = " + pWPNd + " | Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT"
                pATK = newpATK
                pSTR = newpSTR
                statCount = int(round(randint(0, 100) / 20))
                newpDEF = pDEF + statCount
                print "DEF: " + str(pDEF) + " -> " + str(newpDEF) + "       (+" + str(newpDEF - pDEF) + ")"
                pDEF = newpDEF
                statCount = int(round(randint(0, 100) / 20))
                newpDEX = pDEX + statCount
                print "DEX: " + str(pDEX) + " -> " + str(newpDEX) + "       (+" + str(newpDEX - pDEX) + ")"
                pDEX = newpDEX
                statCount = int(round(randint(0, 100) / 20))
                newpINT = pINT + statCount
                print "INT: " + str(pINT) + " -> " + str(newpINT) + "       (+" + str(newpINT - pINT) + ")"
                pINT = newpINT
                statCount = int(round(randint(0, 100) / 20))
                newpLUK = pLUK + statCount
                print "LUK: " + str(pLUK) + " -> " + str(newpLUK) + "       (+" + str(newpLUK - pLUK) + ")"
                pLUK = newpLUK
                newpCRIT = round(pLUK + pWPNl + pCRITb) / 2
                newpAVO = round(pLUK + pDEX) / 2
                print "     CRIT chance: " + str(pCRIT - pCRITb) + "% (+" + str(pCRITb) + "%) -> " + str(newpCRIT) + "% (+" + str(pCRITb) + "%)" + "    (+" + str(newpCRIT - pCRIT) + ")"
                print "     AVO chance: " + str(pAVO) + "% -> " + str(newpAVO) + "%                 (+" + str(newpAVO - pAVO) + ")\n"
                pCRIT = newpCRIT
                pAVO = newpAVO
                cont = raw_input("\n(Press enter to continue)")
            # display exp until next lv
            print "\nEXP until next level = " + str(pLVupEXPCount - pEXP)
            pHPregen = int(round(pHPmax * pHPregenRate))
            pMPregen = int(round(pMPmax * pMPregenRate))

            # after all mobs KO, story of where come from, need to beat dungeon, but who?
            print "\n\n[All of the monsters have been defeated!]\n"
            print "Heavy Brute:     'Where did all these pests come from?  They just started rampaging out of nowhere!'"
            cont = raw_input("\n(Press enter to continue)\n")
            print "\n[By now, the Panicked Messenger has calmed down and relaxed himself]\n"
            print "Messenger:       'They flooded out of the unconquerable dungeon that rose out of the earth southeast of here.'"
            print "White Paladin:   'Friends, he speaks the truth.  I also saw the horde running rampant on my way to the village before I encountered some of the pesky fiends myself.'"
            print "Heavy Brute:     'I heard from my brother that they have been spilling out of the dungeon in attempt to overpower adventurers with sheer numbers.'"
            cont = raw_input("\n(Press enter to continue)\n")
            print "Isaac the Wise:  'This is very bad my friends.  As it seems, the monsters will continue to devestate Konaha and its inhabitants.'"
            print "Isaac the Wise:  'Therefore, we must clear the dungeon in order to protect our village.'"
            print "Young Hunter:    'But no one here is strong enough to defeat an entire dungeon of creatures and the final boss!'"
            cont = raw_input("\n(Press enter to continue)\n")
            print "Isaac the Wise:  'However, we must try anyways.  If they're left alone, they will build up enough strength to overrun the village.'"
            print "\n[You have been eavesdropping on this conversation the whole time]\n"
            stopwatch2(1)
            while True:
                sneakignore = raw_input("(If you want to sneak away and challenge the dungeon by yourself, type 'SNEAK'.  If you believe that you are a weakling and can't accomplish anything of notable achievement, type 'IGNORE'.)      ")
                if sneakignore.lower() == "sneak":
                    # travel to the dungeon immediately after sneaking away from the group
                    print "\n[You decide to sneak away in the midst of the discussion and travel to the dungeon alone]\n"
                    break
                elif sneakignore.lower() == "ignore":
                    # ignore conv & win alt ending of peace
                    print "\n[You decide to ignore the adventurers pursuaded that you are a weakling after seeing them in battle.]\n"
                    print "[You travel back to Konoha Village to lead a normal life, where you get married to the love of your life and build a large, happy family."
                    print "     Also, you pursue your new dream -- To run a successful food restaurant called '" + name + "'s Ramen Shop' and achieve it]"
                    # calc time spent playing
                    elapsedtime = 0
                    cmin = 0
                    minutes = 0
                    seconds = 0
                    elapsedtime = time.time() - starttime
                    if round(elapsedtime) >= 60:
                        cmin = round(elapsedtime) % 60
                        minutes = round(elapsedtime) - cmin
                        minutes = int(round(elapsedtime) / 60)
                        seconds = cmin
                    else:
                        seconds = int(round(elapsedtime))
                    # display end game stats
                    cont = raw_input("\n(Press enter to continue)\n")
                    print "GAME OVER - YOU WIN (the alternate peaceful ending)"
                    stopwatch2(1)
                    print "\nFinal Statistics:"
                    playerstats()
                    cont = raw_input("\n(Press enter to continue)\n")
                    print "Win by:"
                    print "         - Having a normal life in a dark time"
                    print "         - Finding your true love"
                    print "         - Creating a successful ramen business that becomes famous"
                    print "\nTime spent playing: " + str(minutes) + " minutes, " + str(seconds) + " seconds"
                    print "\nTHANKS FOR PLAYING"
                    exit = raw_input("(Press enter to exit the game)    ")
                    # exits the game by win alt end of peace
                    raise SystemExit
                    break
                elif sneakignore.lower() == "/help":
                    print "/playerstats"
                elif sneakignore.lower() == "/playerstats":
                    playerstats()
                else:
                    print "INVALID"
                    
else:
    # cont drinking w/ friends & win alt ending of peace
    print "\n[After you finish your last mug of ale, you travel back to your home in Konoha Village]\n"
    print "[You travel back to Konoha Village to lead a normal life, where you get married to the love of your life and build a large, happy family."
    print "     Also, you pursue your new dream -- To run a successful food restaurant called 'Ichiraku's Ramen Shop' and achieve it]"
    # calc time spent playing
    elapsedtime = 0
    cmin = 0
    minutes = 0
    seconds = 0
    elapsedtime = time.time() - starttime
    if round(elapsedtime) >= 60:
        cmin = round(elapsedtime) % 60
        minutes = round(elapsedtime) - cmin
        minutes = int(round(elapsedtime) / 60)
        seconds = cmin
    else:
        seconds = int(round(elapsedtime))
    # display end game stats
    cont = raw_input("\n(Press enter to continue)\n")
    print "GAME OVER - YOU WIN (the alternate peaceful ending)"
    stopwatch2(1)
    print "Win by:"
    print "         - Having a normal life in a dark time"
    print "         - Finding your true love"
    print "         - Creating a successful ramen business that becomes famous"
    print "\nTime spent playing: " + str(minutes) + " minutes, " + str(seconds) + " seconds"
    print "\nTHANKS FOR PLAYING"
    exit = raw_input("(Press enter to exit the game)    ")
    # exits the game by win alt end of peace
    raise SystemExit
    # FINISH THIS

# DATA START QUEST
cont = raw_input("\n(Press enter to continue)\n")
#chance for bandit encounter (make sure it's not standard stats still)
if pHP != 100:
    if 100 <= 80: # now always encounter used to be 80% chance
        #bandit encounter
        #chance for immediate damage
        print "\n[You are ambushed by a group of bandits during your travels!]\n"
        if randint(1, 100) <= 30:
            print "[One of them manages to land an attack before you can prepare for the ambush! (-10 HP)]\n"
            newpHP = pHP
            newpHP -= 10
            if newpHP < 0:
                #make it not<0
                newpHP = 0
            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
            pHP = newpHP
        # calc how many bandits (3 -> 5)
        rndnum2 = randint(3, 5)
        for i in range(rndnum2):
            # 3 lv-matched bandits attack
            if pLV >= 8:
                mob = "Ruthless Bandit"
                mobLV = 10
                mobGold = 75
                mobEXP = 300
                mobHPmax = randint(35, 40)
                mobHP = mobHPmax
                mobMPmax = randint(19, 25)
                mobMP = mobMPmax
                mobSTR = randint(20, 24)
                mobWPN = randint(5, 7)
                mobWPNd = "Sneaky Bastard Sword"
                mobWPNl = randint(28, 35)
                mobATK = mobSTR + mobWPN
                mobDEF = randint(19, 22)
                mobDEX = randint(17, 21)
                mobINT = randint(15, 21)
                mobLUK = randint(30, 50)
                mobCRITb = 0
                mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
                mobAVO = round(mobLUK + mobDEX) / 2
                mobDropwc = 25
                encounternum += 1
            elif pLV >= 6:
                mob = "Ruthless Bandit"
                mobLV = 8
                mobGold = 70
                mobEXP = 275
                mobHPmax = randint(30, 37)
                mobHP = mobHPmax
                mobMPmax = randint(17, 22)
                mobMP = mobMPmax
                mobSTR = randint(17, 19)
                mobWPN = randint(5, 7)
                mobWPNd = "Sneaky Bastard Sword"
                mobWPNl = randint(28, 35)
                mobATK = mobSTR + mobWPN
                mobDEF = randint(17, 20)
                mobDEX = randint(15, 20)
                mobINT = randint(12, 18)
                mobLUK = randint(25, 45)
                mobCRITb = 0
                mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
                mobAVO = round(mobLUK + mobDEX) / 2
                mobDropwc = 30
                encounternum += 1
            elif pLV >= 4:
                mob = "Ruthless Bandit"
                mobLV = 6
                mobGold = 70
                mobEXP = 250
                mobHPmax = randint(25, 30)
                mobHP = mobHPmax
                mobMPmax = randint(15, 20)
                mobMP = mobMPmax
                mobSTR = randint(13, 17)
                mobWPN = randint(5, 7)
                mobWPNd = "Sneaky Bastard Sword"
                mobWPNl = randint(28, 35)
                mobATK = mobSTR + mobWPN
                mobDEF = randint(11, 15)
                mobDEX = randint(13, 18)
                mobINT = randint(8, 12)
                mobLUK = randint(20, 35)
                mobCRITb = 0
                mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
                mobAVO = round(mobLUK + mobDEX) / 2
                mobDropwc = 35
                encounternum += 1
            else: # pLV < 4:
                mob = "Ruthless Bandit"
                mobLV = 4
                mobGold = 70
                mobEXP = 225
                mobHPmax = randint(20, 25)
                mobHP = mobHPmax
                mobMPmax = randint(12, 16)
                mobMP = mobMPmax
                mobSTR = randint(11, 15)
                mobWPN = randint(5, 7)
                mobWPNd = "Sneaky Bastard Sword"
                mobWPNl = randint(28, 35)
                mobATK = mobSTR + mobWPN
                mobDEF = randint(10, 14)
                mobDEX = randint(11, 15)
                mobINT = randint(6, 10)
                mobLUK = randint(15, 30)
                mobCRITb = 0
                mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
                mobAVO = round(mobLUK + mobDEX) / 2
                mobDropwc = 40
                encounternum += 1
                
            # display the encounter info
            stopwatch2(1)
            if i == 0:
                print "\nThe first bandit approaches!"
            elif i == 1:
                print "\nThe second bandit approaches!"
            else:
                print "\nThe last bandit approaches!"
            print "\n[You encounter a Level " + str(mobLV) + " " + mob + "!]"
            enemystats()
            cont = raw_input("\n(Press enter to continue)")

            # start fight sequence
            while pHP > 0 and mobHP > 0 and not mobEscape and not pEscape:
                # turn fight sequence
                # calc enemy action
                mobTURNc = randint(1, 100)
                if mobTURNc <= 10:
                    # attempts to flee
                    mobTURN = "Flee"
                elif mobTURNc >= 50:
                    # attacks
                    mobTURN = "Attack"
                elif mobTURNc > 10 and mobTURNc < 30:
                    # guards
                    mobTURN = "Guard"
                else:
                    # CRIT +10
                    mobTURN = "Focus"
                # player decides action
                while True:
                    pTURN = raw_input("\n[OPTIONS: 'ATTACK', 'FOCUS' (+10% CRIT), 'GUARD' (1/2 DMG), 'FLEE' (" + str(int((fleechance(pDEX, mobDEX, fleeAttempts) / float(256) * 100))) + "%)]    ")
                    if pTURN.lower() == "attack":
                        # attacks
                        pTURN = "Attack"
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        if mobTURN == "Attack":
                            tiebreaker = randint(1, 2)
                            # calc who attacks first
                            if pDEX > mobDEX or pDEX == mobDEX and tiebreaker == 1:
                                turnCount += 1
                                #player first
                                print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                                #crit chance
                                if pCRIT >= randint(1, 100):
                                    pDMG = (pATK - mobDEF) * 2
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        stopwatch2(1)
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #crit atk
                                        print "[CRITICAL HIT!    x2 DAMAGE]"
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0                                
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                        if mobHP == 0:
                                            stopwatch2(1)
                                            # mob defeated, player wins
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                        #else cont fight (still alive)
                                else:
                                    #no crit chance
                                    pDMG = pATK - mobDEF
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        stopwatch2(1)
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #no crit atk
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                        if mobHP == 0:
                                            stopwatch2(1)
                                            # mob defeated, player wins
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                        #else cont fight (still alive)
                                stopwatch2(1)
                                turnCount += 1
                                #mob attacks (not KO)
                                print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                                #mob crit chance
                                if mobCRIT >= randint(1, 100):
                                    mobDMG = (mobATK - pDEF) * 2
                                    if mobDMG < 0:
                                        #make it=0
                                        mobDMG = 0
                                    if pAVO >= randint(1, 100):
                                        # player dodge
                                        stopwatch2(1)
                                        print "You dodge the attack!"
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        break
                                    else:
                                        #mob crit atk
                                        print "[CRITICAL HIT!    x2 DAMAGE]"
                                        print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                        newpHP = pHP
                                        newpHP -= mobDMG
                                        if newpHP < 0:
                                            #make it not<0
                                            newpHP = 0
                                        print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                        pHP = newpHP
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        if pHP == 0:
                                            # player defeated, player loses
                                            stopwatch2(1)
                                            print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            gameoverl()
                                            exit = raw_input("(Press enter to exit the game)    ")
                                            # exits the game by death
                                            raise SystemExit
                                        #else cont fight (still alive)
                                        break
                                else:
                                    #no mob crit atk
                                    mobDMG = mobATK - pDEF
                                    if mobDMG < 0:
                                        #make it=0
                                        mobDMG = 0
                                    if pAVO >= randint(1, 100):
                                        # player dodge
                                        stopwatch2(1)
                                        print "You dodge the attack!"
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                    else:
                                        #mob no crit atk
                                        print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                        newpHP = pHP
                                        newpHP -= mobDMG
                                        if newpHP < 0:
                                            #make it not<0
                                            newpHP = 0
                                        print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                        pHP = newpHP
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        if pHP == 0:
                                            # player defeated, player loses
                                            stopwatch2(1)
                                            print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            gameoverl()
                                            exit = raw_input("(Press enter to exit the game)    ")
                                            # exits the game by death
                                            raise SystemExit
                                        #else cont fight (still alive)
                                    break
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                            elif mobDEX > pDEX or mobDEX == pDEX and tiebreaker == 2:
                                turnCount += 1
                                # enemy first
                                print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                                #mob crit chance
                                if mobCRIT >= randint(1, 100):
                                    mobDMG = (mobATK - pDEF) * 2
                                    if mobDMG < 0:
                                        #make it=0
                                        mobDMG = 0
                                    if pAVO >= randint(1, 100):
                                        # player dodge
                                        stopwatch2(1)
                                        print "You dodge the attack!"
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                    else:
                                        #mob crit atk
                                        print "[CRITICAL HIT!    x2 DAMAGE]"
                                        print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                        newpHP = pHP
                                        newpHP -= mobDMG
                                        if newpHP < 0:
                                            #make it not<0
                                            newpHP = 0
                                        print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                        pHP = newpHP
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        if pHP == 0:
                                            # player defeated, player loses
                                            stopwatch2(1)
                                            print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            gameoverl()
                                            exit = raw_input("(Press enter to exit the game)    ")
                                            # exits the game by death
                                            raise SystemExit
                                        #else cont fight (still alive)
                                else:
                                    #no mob crit atk
                                    mobDMG = mobATK - pDEF
                                    if mobDMG < 0:
                                        #make it=0
                                        mobDMG = 0
                                    if pAVO >= randint(1, 100):
                                        # player dodge
                                        stopwatch2(1)
                                        print "You dodge the attack!"
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                    else:
                                        #mob no crit atk
                                        print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                        newpHP = pHP
                                        newpHP -= mobDMG
                                        if newpHP < 0:
                                            #make it not<0
                                            newpHP = 0
                                        print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                        pHP = newpHP
                                        if mobCRITb > 0:
                                            print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                            mobCRITb = 0
                                        if pHP == 0:
                                            # player defeated, player loses
                                            stopwatch2(1)
                                            print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            gameoverl()
                                            exit = raw_input("(Press enter to exit the game)    ")
                                            # exits the game by death
                                            raise SystemExit
                                        #else cont fight (still alive)
                                stopwatch2(1)
                                turnCount += 1
                                print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                                #crit chance
                                if pCRIT >= randint(1, 100):
                                    pDMG = (pATK - mobDEF) * 2
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        stopwatch2(1)
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #crit atk
                                        print "[CRITICAL HIT!    x2 DAMAGE]"
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0                                
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                        if mobHP == 0:
                                            # mob defeated, player wins
                                            stopwatch2(1)
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                else:
                                    #no crit chance
                                    pDMG = pATK - mobDEF
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        stopwatch2(1)
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #no crit atk
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                        if mobHP == 0:
                                            stopwatch2(1)
                                            # mob deafeated, player wins
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                        #else cont fight (still alive)
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Focus":
                            turnCount += 1
                            # enemy focuses
                            mobCRITb += 10
                            print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+ 10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                            stopwatch2(1)
                            turnCount += 1
                            # player attacks
                            print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                            #crit chance
                            if pCRIT >= randint(1, 100):
                                pDMG = (pATK - mobDEF) * 2
                                if pDMG < 0:
                                    #make it=0
                                    pDMG = 0
                                if mobAVO >= randint(1, 100):
                                    # mob dodge
                                    print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                    if pCRITb > 0:
                                        print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                        pCRITb = 0
                                else:
                                    #crit atk
                                    print "[CRITICAL HIT!    x2 DAMAGE]"
                                    print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                    newmobHP = mobHP
                                    newmobHP -= pDMG
                                    if newmobHP < 0:
                                        #make it not<0                                
                                        newmobHP = 0
                                    print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                    mobHP = newmobHP
                                    if pCRITb > 0:
                                        print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                        pCRITb = 0
                                    if mobHP == 0:
                                        # mob defeated, player wins
                                        print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        # gain gold
                                        print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                        pGold += mobGold
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        mobkills += 1
                                        break
                                    #else cont fight (still alive)
                            else:
                                #no crit chance
                                pDMG = pATK - mobDEF
                                if pDMG < 0:
                                    #make it=0
                                    pDMG = 0
                                if mobAVO >= randint(1, 100):
                                    # mob dodge
                                    print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                    if pCRITb > 0:
                                        print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                        pCRITb = 0
                                else:
                                    #no crit atk
                                    print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                    newmobHP = mobHP
                                    newmobHP -= pDMG
                                    if newmobHP < 0:
                                        #make it not<0
                                        newmobHP = 0
                                    print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                    mobHP = newmobHP
                                    if pCRITb > 0:
                                       print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                                    if mobHP == 0:
                                        # mob deafeated, player wins
                                        print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        # gain gold
                                        print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                        pGold += mobGold
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        mobkills += 1
                                        break
                                    #else cont fight (still alive)
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Flee":
                            turnCount += 1
                            # enemy attempts to flee - if fail, player attacks
                            print "\nThe Level " + str(mobLV) + " " + mob + " tries to flee!"
                            mobfleeAttempts += 1
                            escapechance = randint(0, 255)
                            escape = fleechance(mobDEX, pDEX, mobfleeAttempts)
                            print "Chance of escape = " + str(int((escape / float(256) * 100))) + "%"
                            if escape > 255:
                                # Auto-escape
                                stopwatch(2)
                                print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                if pCRITb > 0:
                                    print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                    pCRITb = 0
                                # set mob escape to true
                                print "\nYou gain 100 EXP"
                                pEXP += 100
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobEscape = True
                                break
                            elif escape > escapechance:
                                # Successful escape
                                stopwatch(2)
                                print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                if pCRITb > 0:
                                    print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                    pCRITb = 0
                                # chance for drop gold and wpn
                                if randint(1, 100) <= round(pLUK / 3):
                                    # drops all gold
                                    print "However, it dropped all of its gold in the process!"
                                    print "You gained " + str(mobGold) + " coins (Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins)"
                                    pGold += mobGold
                                elif randint(1, 100) <= round(pLUK / 2):
                                    print "However, it dropped half of its gold in the process!"
                                    print "You gained " + str(int(round(mobGold * 0.5))) + " coins (Gold: " + str(pGold) + " -> " + str(int(round(pGold + mobGold * 0.5))) + " coins)"
                                    pGold += int(round((mobGold * 0.5)))
                                # set mob escape to true
                                print "\nYou gain 100 EXP"
                                pEXP += 100
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobEscape = True
                                break
                            else:
                                # Failed flee attempt
                                stopwatch(2)
                                print "And is unsuccessful!\n[The Level " + str(mobLV) + " " + mob + " failed to escape]"
                                turnCount += 1
                                #player attacks
                                stopwatch2(1)
                                print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                                #crit chance
                                if pCRIT >= randint(1, 100):
                                    pDMG = (pATK - mobDEF) * 2
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #crit atk
                                        print "[CRITICAL HIT!    x2 DAMAGE]"
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0                                
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                        if mobHP == 0:
                                            # mob defeated, player wins
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                        #else cont fight (still alive)
                                else:
                                    #no crit chance
                                    pDMG = pATK - mobDEF
                                    if pDMG < 0:
                                        #make it=0
                                        pDMG = 0
                                    if mobAVO >= randint(1, 100):
                                        # mob dodge
                                        print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                    else:
                                        #no crit atk
                                        print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                        newmobHP = mobHP
                                        newmobHP -= pDMG
                                        if newmobHP < 0:
                                            #make it not<0
                                            newmobHP = 0
                                        print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                        mobHP = newmobHP
                                        if pCRITb > 0:
                                            print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                            pCRITb = 0
                                        if mobHP == 0:
                                            # mob deafeated, player wins
                                            print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                            # gain gold
                                            print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                            pGold += mobGold
                                            turnCounta += turnCount
                                            turnCount = 0
                                            mobfleeAttempts = 0
                                            mobEscape = False
                                            fleeAttempts = 0
                                            pEscape = False
                                            mobkills += 1
                                            break
                                        #else cont fight (still alive)
        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        else:   # enemy guard
                            turnCount += 1
                            turnCount += 1
                            #player attacks
                            print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                            # enemy guards
                            print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!\n"
                            stopwatch2(1)
                            #crit chance
                            if pCRIT >= randint(1, 100):
                                pDMG = int(round(((pATK * 2) - mobDEF) / 2))
                                if pDMG < 0:
                                    #make it=0
                                    pDMG = 0
                                if mobAVO >= randint(1, 100):
                                    # mob dodge
                                    print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                    if pCRITb > 0:
                                        print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                        pCRITb = 0
                                else:
                                    #crit atk
                                    print "[CRITICAL HIT!    x2 DAMAGE]"
                                    print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                    newmobHP = mobHP
                                    newmobHP -= pDMG
                                    if newmobHP < 0:
                                        #make it not<0                                
                                        newmobHP = 0
                                    print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                    mobHP = newmobHP
                                    if pCRITb > 0:
                                        print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                        pCRITb = 0
                                    if mobHP == 0:
                                        # mob defeated, player wins
                                        print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        # gain gold
                                        print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                        pGold += mobGold
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        mobkills += 1
                                        break
                                    #else cont fight (still alive)
                            else:
                                #no crit chance
                                pDMG = int(round((pATK - mobDEF) / 2))
                                if pDMG < 0:
                                    #make it=0
                                    pDMG = 0
                                if mobAVO >= randint(1, 100):
                                    # mob dodge
                                    print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                    if pCRITb > 0:
                                        print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                        pCRITb = 0
                                else:
                                    #no crit atk
                                    print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                    newmobHP = mobHP
                                    newmobHP -= pDMG
                                    if newmobHP < 0:
                                        #make it not<0
                                        newmobHP = 0
                                    print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                    mobHP = newmobHP
                                    if pCRITb > 0:
                                        print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                        pCRITb = 0
                                    if mobHP == 0:
                                        # mob deafeated, player wins
                                        print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        # gain gold
                                        print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                        pGold += mobGold
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        mobkills += 1
                                        break
                                    #else cont fight (still alive)
                        break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                    elif pTURN.lower() == "guard":
                        turnCount += 1
                        # player guards
                        pTURN = "Guard"
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        if mobTURN == "Flee":
                            turnCount += 1
                            # enemy attempts to flee - if fail, player guards
                            print "\nThe Level " + str(mobLV) + " " + mob + " tries to flee!"
                            mobfleeAttempts += 1
                            escapechance = randint(0, 255)
                            escape = fleechance(mobDEX, pDEX, mobfleeAttempts)
                            print "Chance of escape = " + str(int((escape / float(256) * 100))) + "%"
                            if escape > 255:
                                # Auto-escape
                                stopwatch(2)
                                print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                if pCRITb > 0:
                                    print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                    pCRITb = 0
                                # set mob escape to true
                                print "\nYou gain 100 EXP"
                                pEXP += 100
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobEscape = True
                                break
                            elif escape > escapechance:
                                # Successful escape
                                stopwatch(2)
                                print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                if pCRITb > 0:
                                    print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                    pCRITb = 0
                                # chance for drop gold and wpn
                                if randint(1, 100) <= round(pLUK / 3):
                                    # drops all gold
                                    print "However, it dropped all of its gold in the process!"
                                    print "You gained " + str(mobGold) + " coins (Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins)"
                                    pGold += mobGold
                                elif randint(1, 100) <= round(pLUK / 2):
                                    print "However, it dropped half of its gold in the process!"
                                    print "You gained " + str(int(round(mobGold * 0.5))) + " coins (Gold: " + str(pGold) + " -> " + str(int(round(pGold + mobGold * 0.5))) + " coins)"
                                    pGold += int(round((mobGold * 0.5)))
                                # set mob escape to true
                                print "\nYou gain 100 EXP"
                                pEXP += 100
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobEscape = True
                                break
                            else:
                                # Failed flee attempt
                                stopwatch(2)
                                print "And is unsuccessful!\n[The Level " + str(mobLV) + " " + mob + " failed to escape]"
                                #player guards, and fails
                                stopwatch2(1)
                                print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                                print "     but it fails."
                                break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Guard":
                            turnCount += 1
                            turnCount += 1
                            #player guards, and fails
                            print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                            print "     but it fails."
                            stopwatch2(1)
                            # enemy guards, and fails
                            print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!"
                            print "     but it fails."
                            break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Focus":
                            turnCount += 1
                            turnCount += 1
                            #player guards, and fails
                            print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                            print "     but it fails."
                            stopwatch2(1)
                            # enemy focuses
                            mobCRITb += 10
                            print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+ 10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                            break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Attack":
                            turnCount += 1
                            #player guards
                            print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                            turnCount += 1
                            stopwatch2(1)
                            # enemy attacks
                            print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                            #mob crit chance
                            if mobCRIT >= randint(1, 100):
                                mobDMG = int(round(((mobATK * 2) - pDEF) / 2))
                                if mobDMG < 0:
                                    #make it=0
                                    mobDMG = 0
                                if pAVO >= randint(1, 100):
                                    # player dodge
                                    print "You dodge the attack!"
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                else:
                                    #mob crit atk
                                    print "[CRITICAL HIT!    x2 DAMAGE]"
                                    print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                    newpHP = pHP
                                    newpHP -= mobDMG
                                    if newpHP < 0:
                                        #make it not<0
                                        newpHP = 0
                                    print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                    pHP = newpHP
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                    if pHP == 0:
                                        # player defeated, player loses
                                        print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        gameoverl()
                                        exit = raw_input("(Press enter to exit the game)    ")
                                        # exits the game by death
                                        raise SystemExit
                                    #else cont fight (still alive)
                            else:
                                #no mob crit atk
                                mobDMG = int(round((mobATK - pDEF) / 2))
                                if mobDMG < 0:
                                    #make it=0
                                    mobDMG = 0
                                if pAVO >= randint(1, 100):
                                    # player dodge
                                    print "You dodge the attack!"
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                else:
                                    #mob no crit atk
                                    print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                    newpHP = pHP
                                    newpHP -= mobDMG
                                    if newpHP < 0:
                                        #make it not<0
                                        newpHP = 0
                                    print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                    pHP = newpHP
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                    if pHP == 0:
                                        # player deafeated, player loses
                                        print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        gameoverl()
                                        exit = raw_input("(Press enter to exit the game)    ")
                                        # exits the game by death
                                        raise SystemExit
                                    #else cont fight (still alive)
                            break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                    elif pTURN.lower() == "focus":
                        pTURN = "Focus"
                        turnCount += 1
                        # player focuses, CRIT +10
                        pCRITb += 10
                        print "\nYou focus your energy (+10 CRIT -|- Total: + " + str(pCRITb) + " CRIT)"
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        if mobTURN == "Flee":
                            turnCount += 1
                            stopwatch2(1)
                            # enemy attempts to flee - if fail, player focuses
                            print "\nThe Level " + str(mobLV) + " " + mob + " tries to flee!"
                            mobfleeAttempts += 1
                            escapechance = randint(0, 255)
                            escape = fleechance(mobDEX, pDEX, mobfleeAttempts)
                            print "Chance of escape = " + str(int((escape / float(256) * 100))) + "%"
                            if escape > 255:
                                # Auto-escape
                                stopwatch(2)
                                print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                if pCRITb > 0:
                                    print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                    pCRITb = 0
                                # set mob escape to true
                                print "\nYou gain 100 EXP"
                                pEXP += 100
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobEscape = True
                                break
                            elif escape > escapechance:
                                # Successful escape
                                stopwatch(2)
                                print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                                if pCRITb > 0:
                                    print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                                    pCRITb = 0
                                # chance for drop gold and wpn
                                if randint(1, 100) <= round(pLUK / 3):
                                    # drops all gold
                                    print "However, it dropped all of its gold in the process!"
                                    print "You gained " + str(mobGold) + " coins (Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins)"
                                    pGold += mobGold
                                elif randint(1, 100) <= round(pLUK / 2):
                                    print "However, it dropped half of its gold in the process!"
                                    print "You gained " + str(int(round(mobGold * 0.5))) + " coins (Gold: " + str(pGold) + " -> " + str(int(round(pGold + mobGold * 0.5))) + " coins)"
                                    pGold += int(round((mobGold * 0.5)))
                                # set mob escape to true
                                print "\nYou gain 100 EXP"
                                pEXP += 100
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobEscape = True
                                break
                            else:
                                # Failed flee attempt
                                stopwatch(2)
                                print "And is unsuccessful!\n[The Level " + str(mobLV) + " " + mob + " failed to escape]"
                                #player focuses, and gets bonus +5 CRIT
                                pCRITb += 5
                                print "During the time the Level " + str(mobLV) + " " + mob + " tried to flee, you were able to focus a little longer!\n\nYou focus your energy a little extra (+ 5 CRIT -|- Total: + " + str(pCRITb) + " CRIT)"
                                break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Guard":
                            turnCount += 1
                            stopwatch2(1)
                            # enemy guards, and fails
                            print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!"
                            print "     but it fails."
                            break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Focus":
                            turnCount += 1
                            stopwatch2(1)
                            # enemy focuses
                            mobCRITb += 10
                            print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                            #player and enemy focus, and get bonus +5 CRIT each
                            pCRITb += 5
                            print "\nDuring the time the Level " + str(mobLV) + " " + mob + " was also focusing, you were able to focus a little longer!\n\nYou focus your energy a little extra (+ 5 CRIT -|- Total: + " + str(pCRITb) + " CRIT)"
                            mobCRITb += 5
                            print "\n     but so did the Level " + str(mobLV) + " " + mob + " (+ 5 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                            break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Attack":
                            turnCount += 1
                            stopwatch2(1)
                            #mob attacks (not KO)
                            print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                            #mob crit chance
                            if mobCRIT >= randint(1, 100):
                                mobDMG = (mobATK - pDEF) * 2
                                if mobDMG < 0:
                                    #make it=0
                                    mobDMG = 0
                                if pAVO >= randint(1, 100):
                                    # player dodge
                                    print "You dodge the attack!"
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                    break
                                else:
                                    #mob crit atk
                                    print "[CRITICAL HIT!    x2 DAMAGE]"
                                    print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                    newpHP = pHP
                                    newpHP -= mobDMG
                                    if newpHP < 0:
                                        #make it not<0
                                        newpHP = 0
                                    print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                    pHP = newpHP
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                    if pHP == 0:
                                        # player defeated, player loses
                                        print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        gameoverl()
                                        exit = raw_input("(Press enter to exit the game)    ")
                                        # exits the game by death
                                        raise SystemExit
                                    #else cont fight (still alive)
                                    break
                            else:
                                #no mob crit atk
                                mobDMG = mobATK - pDEF
                                if mobDMG < 0:
                                    #make it=0
                                    mobDMG = 0
                                if pAVO >= randint(1, 100):
                                    # player dodge
                                    print "You dodge the attack!"
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                else:
                                    #mob no crit atk
                                    print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                    newpHP = pHP
                                    newpHP -= mobDMG
                                    if newpHP < 0:
                                        #make it not<0
                                        newpHP = 0
                                    print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                    pHP = newpHP
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                    if pHP == 0:
                                        # player defeated, player loses
                                        print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        gameoverl()
                                        exit = raw_input("(Press enter to exit the game)    ")
                                        # exits the game by death
                                        raise SystemExit
                                    #else cont fight (still alive)
                                break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                    elif pTURN.lower() == "flee":
                        pTURN = "Flee"
                        turnCount += 1
                        # attempts to flee
                        print "\nYou try to escape from the Level " + str(mobLV) + " " + mob + "!"
                        if mobTURN == "Flee":
                            # mob flees too
                            turnCount += 1
                            print "\nThis particular Level " + str(mobLV) + " " + mob + " has also tried to flee at the same time so the battle ends in a draw!"
                            print "\nWhat a coincidence!  You learn from this unique experience and gain 200 EXP!"
                            pEXP += 200
                            turnCounta += turnCount
                            turnCount = 0
                            mobfleeAttempts = 0
                            mobEscape = False
                            fleeAttempts = 0
                            pEscape = False
                            mobkills += 1
                            # set mob escape to true
                            mobEscape = True
                            # set player escape to true
                            pEscape = True
                            break
                        else:
                            fleeAttempts += 1
                            escapechance = randint(0, 255)
                            escape = fleechance(pDEX, mobDEX, fleeAttempts)
                            if escape > 255:
                                # Auto-escape
                                stopwatch(2)
                                print "And are successful!\n[You manage to successfully get away from the Level " + str(mobLV) + " " + mob + "]"
                                if pCRITb > 0:
                                    print "You lose all your focus after you escape (-" + str(pCRITb) + " CRIT)"
                                    pCRITb = 0
                                # set player escape to true
                                print "\nYou gain 50 EXP"
                                pEXP += 50
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                pEscape = True
                                break
                            elif escape > escapechance:
                                # Successful escape
                                stopwatch(2)
                                print "And are successful!\n[You manage to successfully get away from the Level " + str(mobLV) + " " + mob + "]"
                                if pCRITb > 0:
                                    print "You lose all your focus after you escape (-" + str(pCRITb) + " CRIT)"
                                    pCRITb = 0
                                # chance for you to lose gold
                                if randint(1, 100) <= round(mobLUK / 5):
                                    # lose 25% of gold
                                    goldLost = int(round(pGold * 0.25))
                                    print "However, the Level " + str(mobLV) + " " + mob + " managed to steal a quarter of your gold."
                                    print "You lost " + str(goldLost) + " coins (Gold: " + str(pGold) + " -> " + str(pGold - goldLost) + " coins)"
                                    pGold -= goldLost
                                    goldLost = 0
                                elif randint(1, 100) <= round(mobLUK / 4):
                                    # lose 10% of gold
                                    goldLost = int(round(pGold * 0.1))
                                    print "However, the Level " + str(mobLV) + " " + mob + " managed to steal a fraction of your gold."
                                    print "You lost " + str(goldLost) + " coins (Gold: " + str(pGold) + " -> " + str(pGold - goldLost) + " coins)"
                                    pGold -= goldLost
                                    goldLost = 0
                                # set player escape to true
                                print "\nYou gain 50 EXP"
                                pEXP += 50
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                pEscape = True
                                break
                            else:
                                # Failed flee attempt
                                stopwatch(2)
                                print "And are unsuccessful!\n[You failed to get away from the Level " + str(mobLV) + " " + mob + " successfully]"
                                stopwatch2(1)
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                                if mobTURN == "Guard":
                                    turnCount += 1
                                    # enemy guards, and fails
                                    print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!"
                                    print "     but it fails."
                                    break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                                elif mobTURN == "Focus":
                                    turnCount += 1
                                    # enemy focuses
                                    mobCRITb += 10
                                    print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+ 10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                                    break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                                elif mobTURN == "Attack":
                                    turnCount += 1
                                    # enemy attacks
                                    print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                                    #mob crit chance
                                    if mobCRIT >= randint(1, 100):
                                        mobDMG = (mobATK - pDEF) * 2
                                        if mobDMG < 0:
                                            #make it=0
                                            mobDMG = 0
                                        if pAVO >= randint(1, 100):
                                            # player dodge
                                            print "You dodge the attack!"
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                        else:
                                            #mob crit atk
                                            print "[CRITICAL HIT!    x2 DAMAGE]"
                                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                            newpHP = pHP
                                            newpHP -= mobDMG
                                            if newpHP < 0:
                                                #make it not<0
                                                newpHP = 0
                                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                            pHP = newpHP
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                            if pHP == 0:
                                                # player defeated, player loses
                                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                gameoverl()
                                                exit = raw_input("(Press enter to exit the game)    ")
                                                # exits the game by death
                                                raise SystemExit
                                            #else cont fight (still alive)
                                    else:
                                        #no mob crit atk
                                        mobDMG = mobATK - pDEF
                                        if mobDMG < 0:
                                            #make it=0
                                            mobDMG = 0
                                        if pAVO >= randint(1, 100):
                                            # player dodge
                                            print "You dodge the attack!"
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                        else:
                                            #mob no crit atk
                                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                            newpHP = pHP
                                            newpHP -= mobDMG
                                            if newpHP < 0:
                                                #make it not<0
                                                newpHP = 0
                                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                            pHP = newpHP
                                            if mobCRITb > 0:
                                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                                mobCRITb = 0
                                            if pHP == 0:
                                                # player deafeated, player loses
                                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                                turnCounta += turnCount
                                                turnCount = 0
                                                mobfleeAttempts = 0
                                                mobEscape = False
                                                fleeAttempts = 0
                                                pEscape = False
                                                gameoverl()
                                                exit = raw_input("(Press enter to exit the game)    ")
                                                # exits the game by death
                                                raise SystemExit
                                            #else cont fight (still alive)
                                    break
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                    elif pTURN.lower() == "/help":
                        print "'/enemystats'"
                        HELP()
                    elif pTURN.lower() == "/playerstats":
                        playerstats()
                    elif pTURN.lower() == "/enemystats":
                        enemystats()
                    else:
                        print ("\n[INVALID, please try again]")

    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        
            else: # check these after battle is won
                if mobHP <= 0:
                    # gain exp for win
                    print "\nYou obtain " + str(mobEXP) + " EXP for defeating the Level " + str(mobLV) + " " + mob + "."
                    pEXP += mobEXP
                    
                if mobHP <= 0 or mobTURN == "Flee":
                    # calc chance to drop mob wpn
                    if randint(1, 100) <= mobDropwc:
                        print "\nThe Level " + str(mobLV) + " " + mob + " dropped its " + mobWPNd + "!"
                        #ask if want to use instead of current wpn
                        while True:
                            yn = raw_input("[Do you want to equip the " + mobWPNd + " (Bonus: +" + str(mobWPN) + " ATK, +" + str(mobWPNl) + " CRIT)]     ('Y'es or 'N'o)     ")
                            if yn.lower() == "y" or yn.lower() == "n":
                                ayn = raw_input("Last Chance, do you want it or not?  ('Y'es or 'N'o)     ")
                                if ayn.lower() == "y":
                                    print "\n[You swap your " + pWPNd + " (Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT) for the " + mobWPNd + " (Bonus: +" + str(mobWPN) + " ATK, +" + str(mobWPNl) + " CRIT)]"
                                    pWPN = mobWPN
                                    pWPNd = mobWPNd
                                    pWPNl = mobWPNl
                                    break
                                elif ayn.lower() == "n":
                                    print "\n[You decide your weapon is still better and destroy the Level " + str(mobLV) + " " + mob + "'s " + mobWPNd + "]\n[ + 500 EXP]"
                                    pEXP += 500
                                    break
                                elif ayn.lower() == "/help":
                                    HELP()
                                elif ayn.lower() == "/playerstats":
                                    playerstats()
                                elif ayn.lower() == "/enemystats":
                                    enemystats()
                                else:
                                    print ("\n[INVALID, please try again]")
                            elif yn.lower() == "/help":
                                HELP()
                            elif yn.lower() == "/playerstats":
                                playerstats()
                            elif yn.lower() == "/enemystats":
                                enemystats()
                            else:
                                print ("\n[INVALID, please try again]")
                            
                while pEXP >= pLVupEXPCount:
                    #LV UP
                    pLV += 1
                    pLVupEXP += 75
                    pLVupEXPCount += pLVupEXP
                    print "\n[LEVEL UP: " + name + ", you are now a Level " + str(pLV) + " " + fclass + " " + race + "]"
                    statCount = int(round(randint(0, 100) / 20))
                    newpHPmax = pHPmax + statCount
                    print "\nHP MAX: " + str(pHPmax) + " -> " + str(newpHPmax) + "    (+" + str(newpHPmax - pHPmax) + ")"
                    pHPmax = newpHPmax
                    pHP += statCount
                    statCount = int(round(randint(0, 100) / 20))
                    newpMPmax = pMPmax + statCount
                    print "MP MAX: " + str(pMPmax) + " -> " + str(newpMPmax) + "    (+" + str(newpMPmax - pMPmax) + ")"
                    pMPmax = newpMPmax
                    pMP += statCount
                    statCount = int(round(randint(0, 100) / 20))
                    newpSTR = pSTR + statCount
                    newpATK = newpSTR + pWPN
                    print "ATK: " + str(pATK) + " -> " + str(newpATK) + "       (+" + str(newpATK - pATK) + ")"
                    print "     STR: " + str(pSTR) + " -> " + str(newpSTR) + "  (+" + str(newpSTR - pSTR) + ")"
                    print "     Weapon = " + pWPNd + " | Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT"
                    pATK = newpATK
                    pSTR = newpSTR
                    statCount = int(round(randint(0, 100) / 20))
                    newpDEF = pDEF + statCount
                    print "DEF: " + str(pDEF) + " -> " + str(newpDEF) + "       (+" + str(newpDEF - pDEF) + ")"
                    pDEF = newpDEF
                    statCount = int(round(randint(0, 100) / 20))
                    newpDEX = pDEX + statCount
                    print "DEX: " + str(pDEX) + " -> " + str(newpDEX) + "       (+" + str(newpDEX - pDEX) + ")"
                    pDEX = newpDEX
                    statCount = int(round(randint(0, 100) / 20))
                    newpINT = pINT + statCount
                    print "INT: " + str(pINT) + " -> " + str(newpINT) + "       (+" + str(newpINT - pINT) + ")"
                    pINT = newpINT
                    statCount = int(round(randint(0, 100) / 20))
                    newpLUK = pLUK + statCount
                    print "LUK: " + str(pLUK) + " -> " + str(newpLUK) + "       (+" + str(newpLUK - pLUK) + ")"
                    pLUK = newpLUK
                    newpCRIT = round(pLUK + pWPNl + pCRITb) / 2
                    newpAVO = round(pLUK + pDEX) / 2
                    print "     CRIT chance: " + str(pCRIT - pCRITb) + "% (+" + str(pCRITb) + "%) -> " + str(newpCRIT) + "% (+" + str(pCRITb) + "%)" + "    (+" + str(newpCRIT - pCRIT) + ")"
                    print "     AVO chance: " + str(pAVO) + "% -> " + str(newpAVO) + "%                 (+" + str(newpAVO - pAVO) + ")\n"
                    pCRIT = newpCRIT
                    pAVO = newpAVO
                    cont = raw_input("\n(Press enter to continue)")

                # display exp until next lv
                print "\nEXP until next level = " + str(pLVupEXPCount - pEXP)
                pHPregen = int(round(pHPmax * pHPregenRate))
                pMPregen = int(round(pMPmax * pMPregenRate))
                    
                # HP regen
                newpHP = pHP
                newpHP += pHPregen
                if newpHP > pHPmax:
                    # make it=max
                    newpHP = pHPmax
                print "\nYou regenerate " + str(pHPregen) + " HP after the battle\nHP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                pHP = newpHP
                # MP regen
                newpMP = pMP
                newpMP += pMPregen
                if newpMP > pMPmax:
                    # make it=max
                    newpMP = pMPmax
                print "You regenerate " + str(pMPregen) + " MP after the battle\nMP = " + str(pMP) + "/" + str(pMPmax) + " -> " + str(newpMP) + "/" + str(pMPmax) + "\n"
                pMP = newpMP

                turnCounta += turnCount
                turnCount = 0
                mobfleeAttempts = 0
                mobEscape = False
                fleeAttempts = 0
                pEscape = False
                mobkills += 1
                '''if mobTURN == "Flee" and mobHP != 0:
                    print "DAMN!  It got away!"'''
                # end fight2 sequence
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                   
#else: nothing happens ///:-^-^-:\\\
# all possible paths that don't die or quit lead here
# arrive at the dungeon
print "[You arrive at the dungeon]"
cont = raw_input("\n(Press enter to continue)\n")
# GUARD
print "You meet an armed guard outside the dungeon."
print "Guard:   'HALT!  Who are you?'"
# checks if you have a name, race, and class yet
if nameCount == 0:
    while nameCount == 0:
        name = raw_input("Enter your name:      ")
        ynName = raw_input("Are you sure with the name " + name + "?    ('Y'es or 'N'o)     ")
        if ynName.lower() == "y":
            nameCount = 1
    # RACE
    while raceCount == 0:
        race = raw_input("\nEnter your race:\nHUMAN\nORC\nELF\nUNDEAD\nMYSTERY\nSAIYAN [for testing purposes]   ")
        if race.lower() == "human":
            race = "Human"
            # balanced race
            pHPmax = 15
            pHP = pHPmax
            pHPregenRate = 0.25
            pHPregen = int(round(pHPmax * pHPregenRate))
            pMPmax = 15
            pMP = pMPmax
            pMPregenRate = 0.25
            pMPregen = int(round(pMPmax * pMPregenRate))
            pSTR = 10
            pATK = pSTR + pWPN
            pDEF = 10
            pDEX = 10
            pINT = 10                   
            pLUK = 15
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            raceCount = 1
        elif race.lower() == "orc":
            race = "Orc"
            # tank race
            pHPmax = 30
            pHP = pHPmax
            pHPregenRate = 0.3
            pHPregen = int(round(pHPmax * pHPregenRate))
            pMPmax = 20
            pMP = pMPmax
            pMPregenRate = 0.25
            pMPregen = int(round(pMPmax * pMPregenRate))
            pSTR = 13
            pATK = pSTR + pWPN
            pDEF = 15
            pDEX = 5
            pINT = 5
            pLUK = 8
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            raceCount = 1
        elif race.lower() == "elf":
            race = "Elf"
            # standard elf perks
            pHPmax = 15
            pHP = pHPmax
            pHPregenRate = 0.25
            pHPregen = int(round(pHPmax * pHPregenRate))
            pMPmax = 25
            pMP = pMPmax
            pMPregenRate = 0.3
            pMPregen = int(round(pMPmax * pMPregenRate))
            pSTR = 10
            pATK = pSTR + pWPN
            pDEF = 9
            pDEX = 13
            pINT = 13
            pLUK = 15
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            raceCount = 1
        elif race.lower() == "undead":
            race = "Undead"
            # str & mp & luk race
            pHPmax = 20
            pHP = pHPmax
            pHPregenRate = 0.35
            pHPregen = int(round(pHPmax * pHPregenRate))
            pMPmax = 30
            pMP = pMPmax
            pMPregenRate = 0.2
            pMPregen = int(round(pMPmax * pMPregenRate))
            pSTR = 17
            pATK = pSTR + pWPN
            pDEF = 12
            pDEX = 5
            pINT = 7
            pLUK = 30
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            raceCount = 1
        elif race.lower() == "mystery":
            race = "Mystery"
            # random generated stats from 5 -> 30
            pHPmax = randint(10, 30)
            pHP = pHPmax
            pHPregenRate = (roundint5(randint(15, 35))) * 0.01
            pHPregen = int(round(pHPmax * pHPregenRate))
            pMPmax = randint(10, 30)
            pMP = pMPmax
            pMPregenRate = (roundint5(randint(15, 35))) * 0.01
            pMPregen = int(round(pMPmax * pMPregenRate))
            pSTR = randint(5, 20)
            pATK = pSTR + pWPN
            pDEF = randint(5, 20)
            pDEX = randint(5, 20)
            pINT = randint(5, 20)
            pLUK = randint(5, 30)
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            raceCount = 1
        elif race.lower() == "saiyan":
            race = "Saiyan"
            # testing OP race
            pLV = 1
            pEXP = 0
            pLVupEXP = 50
            pHPmax = 9001
            pHP = pHPmax
            pHPregenRate = 0.001
            pHPregen = int(round(pHPmax * pHPregenRate))
            pMPmax = 9001
            pMP = pMPmax
            pMPregenRate = 0.001
            pMPregen = int(round(pMPmax * pMPregenRate))
            pSTR = 9001
            pWPN = 0
            pWPNd = "Saiyan Fists"
            pWPNl = 0
            pATK = pSTR + pWPN
            pDEF = 20
            pDEX = 10
            pINT = 9001
            pLUK = 50
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            raceCount = 1
        else:
            print ("\n[INVALID, please try again]")
        
    # CLASS
    while fclassCount == 0:
        fclass = raw_input("\nChoose a class:\nWARRIOR (bal)\nROGUE (dps)\nPALADIN (tank)\nUNKNOWN\nSSGSS [for testing purposes]     ")
        if fclass.lower() == "warrior":
            fclass = "Warrior"
            # balanced class
            #BALANCED
            pWPN = 3
            pWPNd = "Bronze Sword"
            pWPNl = 5
            pATK = pSTR + pWPN
            pLUK += 15
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            fclassCount = 1
        elif fclass.lower() == "rogue":
            fclass = "Rogue"
            # dps class
            #HP
            #MP
            pSTR += 10
            pWPN = 2
            pWPNd = "Bronze Dagger"
            pWPNl = 15
            pATK = pSTR + pWPN
            #DEF
            pDEX += 10
            pINT += 3
            pLUK += 20
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            fclassCount = 1
        elif fclass.lower() == "paladin":
            fclass = "Paladin"
            # tank class
            pHPmax += 5
            pHP = pHPmax
            #MP
            pSTR += 5
            pWPN = 4
            pWPNd = "Bronze Lance"
            pWPNl = 5
            pATK = pSTR + pWPN
            pDEF += 10
            pDEX -= 3
            pINT -= 2
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            #LUK
            fclassCount = 1
        elif fclass.lower() == "unknown":
            fclass = "Unknown"
            # random stat bonus / minus class
            pmCount = randint(1, 2)
            if pmCount == 1:
                pHPmax += randint(1, 5)
            else:
                pHPmax -= randint(1, 5)
            pHP = pHPmax
            pmCount = randint(1, 2)
            if pmCount == 1:
                pMPmax += randint(1, 5)
            else:
                pMPmax -= randint(1, 5)
            pMP = pMPmax
            pmCount = randint(1, 2)
            if pmCount == 1:
                pSTR += randint(1, 5)
            else:
                pSTR -= randint(1, 5)
            pmCount = randint(1, 5)
            if pmCount == 1:
                pWPN = 2
                pWPNd = "Bronze Dagger"
                pWPNl = 15
            elif pmCount == 2:
                pWPN = 3
                pWPNd = "Bronze Sword"
                pWPNl = 5
            elif pmCount == 3:
                pWPN = 4
                pWPNd = "Bronze Lance"
                pWPNl = 5
            elif pmCount == 4:
                pWPN = 5
                pWPNd = "Bronze Hammer"
                pWPNl = 5
            else:
                pWPN = 5
                pWPNd = "Bronze Axe"
                pWPNl = 10
            pATK = pSTR + pWPN
            pmCount = randint(1, 2)
            if pmCount == 1:
                pDEF += randint(1, 5)
            else:
                pDEF -= randint(1, 5)
            pmCount = randint(1, 2)
            if pmCount == 1:
                pDEX += randint(1, 5)
            else:
                pDEX -= randint(1, 5)
            pmCount = randint(1, 2)
            if pmCount == 1:
                pINT += randint(1, 5)
            else:
                pINT -= randint(1, 5)
            pmCount = randint(1, 2)
            if pmCount == 1:
                pLUK += randint(1, 5)
            else:
                pLUK -= randint(1, 5)
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            fclassCount = 1
        elif fclass.lower() == "ss g ss" or fclass.lower() == "ssgss":
            fclass = "Super Saiyan God Super"
            # str & mp & luk race
            pLV = 1
            pEXP = 0
            pLVupEXP = 50
            pHPmax = 9999
            pHP = pHPmax
            pHPregenRate = 0.001
            pHPregen = int(round(pHPmax * pHPregenRate))
            pMPmax = 9999
            pMP = pMPmax
            pMPregenRate = 0.001
            pMPregen = int(round(pMPmax * pMPregenRate))
            pSTR = 9999
            pWPN = 0
            pWPNd = "Super Saiyan God Super " + name + " Fists"
            pWPNl = 25
            pATK = pSTR + pWPN
            pDEF = 20
            pDEX = 10
            pINT = 9999
            pLUK = 50
            pCRIT = round(pLUK + pWPNl + pCRITb) / 2
            pAVO = round(pLUK + pDEX) / 2
            fclassCount = 1
        else:
            print ("\n[INVALID, please try again]")
# print stats to user
print "\n[NOTE TO PLAYER]\n[Your current stats:]\n"
stopwatch2(1)
print "\n[You explain youself and your story to the Guard]\n"
playerstats()
cont = raw_input("\n(Press enter to continue)\n")
print "Guard:   'Ah, so I see.  " + name + " the " + fclass + " " + race + ", you have come to complete the quest."
print "Guard:   'Please accept this as a token of my gratitude as you are the very first I've seen with enough courage to attempt this.'"
# gives you iron upgrade of initial WPN
# calc what WPN you have
if pWPNd == "Bronze Dagger":
    mobWPN = 5
    mobWPNd = "Iron Dagger"
    mobWPNl = 30
elif pWPNd == "Bronze Sword":
    mobWPN = 6
    mobWPNd = "Iron Sword"
    mobWPNl = 15
elif pWPNd == "Bronze Lance":
    mobWPN = 8
    mobWPNd = "Iron Lance"
    mobWPNl = 15
elif pWPNd == "Bronze Hammer":
    mobWPN = 9
    mobWPNd = "Iron Hammer"
    mobWPNl = 20
else:
    mobWPN = 10
    mobWPNd = "Iron Axe"
    mobWPNl = 25
    
print "\n[The Guard hands you an " + mobWPNd + ".]\n"
# accept it or not
while True:
    yn = raw_input("[Do you want to equip the " + mobWPNd + " (Bonus: +" + str(mobWPN) + " ATK, +" + str(mobWPNl) + " CRIT)]     ('Y'es or 'N'o)     ")
    if yn.lower() == "y" or yn.lower() == "n":
        ayn = raw_input("Guard:     Last Chance, do you want it or not?  ('Y'es or 'N'o)     ")
        if ayn.lower() == "y":
            # take the iron upgrade
            print "\n[You swap your " + pWPNd + " (Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT) for the " + mobWPNd + " (Bonus: +" + str(mobWPN) + " ATK, +" + str(mobWPNl) + " CRIT)]"
            pWPN = mobWPN
            pWPNd = mobWPNd
            pWPNl = mobWPNl
            break
        elif ayn.lower() == "n":
            # say no and get 2 levels instead
            print "\n[You decide your weapon is still better and politely decline]\n"
            stopwatch2(1)
            print "Guard:   Well, I would feel bad if I didn't do anything for you, so I guess I can show a few of the elite Royal ANBU Guard techniques that I've learned."
            print "\n[The Guard unsheathes his sword and demonstrates a blinding flurry of attacks]\n"
            stopwatch2(1)
            print "[From his demonstration and the secret Royal ANBU Guard techniques that you have just learned, you gained two levels!]\n"
            # +2 lvs
            pEXP += (pLVupEXPCount - pEXP) #+1 lv
            pLVupEXP += 75
            pLVupEXPCount += pLVupEXP
            pEXP += (pLVupEXPCount - pEXP) #+1 lv
            pLVupEXP += 75
            pLVupEXPCount += pLVupEXP
            newpHPmax = pHPmax
            newpMPmax = pMPmax
            newpSTR = pSTR
            newpDEF = pDEF
            newpDEX = pDEX
            newpINT = pINT
            newpLUK = pLUK
            # give enough exp for 2 lvups and no more
            for i in range(2):
                #LV UP
                pLV += 1
                statCount = int(round(randint(0, 100) / 20))
                newpHPmax += statCount
                pHP += statCount
                statCount = int(round(randint(0, 100) / 20))
                newpMPmax += statCount
                pMP += statCount
                statCount = int(round(randint(0, 100) / 20))
                newpSTR += statCount
                newpATK = newpSTR + pWPN
                statCount = int(round(randint(0, 100) / 20))
                newpDEF += statCount
                statCount = int(round(randint(0, 100) / 20))
                newpDEX += statCount
                statCount = int(round(randint(0, 100) / 20))
                newpINT += statCount
                statCount = int(round(randint(0, 100) / 20))
                newpLUK += statCount
                newpCRIT = round(newpLUK + pWPNl + pCRITb) / 2
                newpAVO = round(newpLUK + newpDEX) / 2
            # print stat changes
            stopwatch2(1)
            print "[You gained 2 Levels]"
            print "\n[LEVEL UP: " + name + ", you are now a Level " + str(pLV) + " " + fclass + " " + race + "]"
            print "\nHP MAX: " + str(pHPmax) + " -> " + str(newpHPmax) + "      (+" + str(newpHPmax - pHPmax) + ")"
            pHPmax = newpHPmax
            print "MP MAX: " + str(pMPmax) + " -> " + str(newpMPmax) + "        (+" + str(newpMPmax - pMPmax) + ")"
            pMPmax = newpMPmax
            print "ATK: " + str(pATK) + " -> " + str(newpATK) + "           (+" + str(newpATK - pATK) + ")"
            print "     STR: " + str(pSTR) + " -> " + str(newpSTR) + "      (+" + str(newpSTR - pSTR) + ")"
            print "     Weapon = " + pWPNd + " | Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT"
            pATK = newpATK
            pSTR = newpSTR
            print "DEF: " + str(pDEF) + " -> " + str(newpDEF) + "           (+" + str(newpDEF - pDEF) + ")"
            pDEF = newpDEF
            print "DEX: " + str(pDEX) + " -> " + str(newpDEX) + "           (+" + str(newpDEX - pDEX) + ")"
            pDEX = newpDEX
            print "INT: " + str(pINT) + " -> " + str(newpINT) + "           (+" + str(newpINT - pINT) + ")"
            pINT = newpINT
            print "LUK: " + str(pLUK) + " -> " + str(newpLUK) + "           (+" + str(newpLUK - pLUK) + ")"
            pLUK = newpLUK
            print "     CRIT chance: " + str(pCRIT - pCRITb) + "% (+" + str(pCRITb) + "%) -> " + str(newpCRIT) + "% (+" + str(pCRITb) + "%)     (+" + str(newpCRIT - pCRIT) + ")"
            print "     AVO chance: " + str(pAVO) + "% -> " + str(newpAVO) + "%                  (+" + str(newpAVO - pAVO) + ")\n"
            pCRIT = newpCRIT
            pAVO = newpAVO
            cont = raw_input("\n(Press enter to continue)")
            # display exp until next lv
            print "\nEXP until next level = " + str(pLVupEXPCount - pEXP)
            pHPregen = int(round(pHPmax * pHPregenRate))
            pMPregen = int(round(pMPmax * pMPregenRate))
            stopwatch2(1)
            break
        elif ayn.lower() == "/help":
            HELP()
        elif ayn.lower() == "/playerstats":
            playerstats()
        elif ayn.lower() == "/enemystats":
            enemystats()
        else:
            print ("\n[INVALID, please try again]")
    elif yn.lower() == "/help":
        HELP()
    elif yn.lower() == "/playerstats":
        playerstats()
    elif yn.lower() == "/enemystats":
        enemystats()
    else:
        print ("\n[INVALID, please try again]")

# enter dungeon
print "\nGuard:     'Good luck, " + name + ", you'll need it in there.'"
print "\n[With those last words, the Guard unlocks the door with the seal of the Hokage]\n"
print "[You enter the dungeon and the door is closed and locked behind you, there is no turning back now]\n"

# dungeon start sequence

print "\nENTER THE DUNGEON\n"

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# random choose monster for 3 fights
# chance to encounter the boss (start at impossible to allow player to get stronger)
bosschance = -16
guardianchance = -11
vampchance = -6
while not defeatboss:
    # increase chance everytime
    bosschance += 1
    guardianchance += 1
    vampchance += 1
    if bosschance > 100:
        basschance = 100
    #random mob from dungeon
    rnddunMob = randint(1, 100)
    if rnddunMob > 0 and rnddunMob <= bosschance:
        # boss
        mob = "BOSS: Undead Demon Lord"
        mobLV = 50
        mobGold = 5000
        mobEXP = 10000
        mobHPmax = randint(150, 200)
        mobHP = mobHPmax
        mobMPmax = randint(100, 175)
        mobMP = mobMPmax
        mobSTR = randint(40, 55)
        mobWPN = randint(25, 30)
        mobWPNd = "Evil Overlord Dark Magic"
        mobWPNl = randint(75, 100)
        mobATK = mobSTR + mobWPN
        mobDEF = randint(60, 80)
        mobDEX = randint(20, 50)
        mobINT = randint(200, 300)
        mobLUK = randint(20, 40)
        mobCRITb = 0
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 0
        encounternum += 1
        
    elif rnddunMob > 0 and rnddunMob <= guardianchance:
        # guardian miniboss
        mob = "Minotaur Guardian"
        mobLV = randint(37, 43)
        mobGold = 500
        mobEXP = 1000
        mobHPmax = randint(100, 130)
        mobHP = mobHPmax
        mobMPmax = randint(50, 75)
        mobMP = mobMPmax
        mobSTR = randint(30, 45)
        mobWPN = randint(17, 25)
        mobWPNd = "Berserker Battleaxe"
        mobWPNl = randint(45, 55)
        mobATK = mobSTR + mobWPN
        mobDEF = randint(35, 50)
        mobDEX = randint(35, 50)
        mobINT = randint(40, 55)
        mobLUK = randint(35, 65)
        mobCRITb = 0
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 40
        encounternum += 1
        
    elif rnddunMob > 0 and rnddunMob <= vampchance:
        # lord miniboss
        mob = "Vampire"
        mobLV = randint(31, 36)
        mobGold = 250
        mobEXP = 650
        mobHPmax = randint(75, 90)
        mobHP = mobHPmax
        mobMPmax = randint(60, 80)
        mobMP = mobMPmax
        mobSTR = randint(30, 45)
        mobWPN = randint(15, 18)
        mobWPNd = "Vampire Lord Powers"
        mobWPNl = randint(35, 50)
        mobATK = mobSTR + mobWPN
        mobDEF = randint(25, 45)
        mobDEX = randint(40, 60)
        mobINT = randint(80, 100)
        mobLUK = randint(30, 50)
        mobCRITb = 0
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 0
        encounternum += 1
    #elif rnddunMob <= 100 and rnddunMob > 95:
        # 5% chance
        # SHOPKEEPER
        # develop shop sequence
        #nvm i didn't have time
        
    elif rnddunMob <= 100 and rnddunMob > 90:
        # 10% chance
        # CHEST
        mob = "Treasure Chest"
        mobLV = "Unknown    -   (It's a Treasure Chest! - Break to open)"
        mobGold = randint(200, 400)
        mobGold = int(round(mobGold, -1))
        mobEXP = randint(300, 500)
        mobEXP = int(round(mobEXP, -1))
        mobHPmax = 1
        mobHP = mobHPmax
        mobMPmax = 1
        mobMP = mobMPmax
        mobSTR = 1
        # rnd adamantium V.WPN
        rndWPN = randint(1, 5)
        if rndWPN == 1:
            mobWPN = 11
            mobWPNd = "Adamantium Dagger"
            mobWPNl = 45
        elif rndWPN == 2:
            mobWPN = 12
            mobWPNd = "Adamantium Sword"
            mobWPNl = 30
        elif rndWPN == 3:
            mobWPN = 14
            mobWPNd = "Adamantium Lance"
            mobWPNl = 30
        elif rndWPN == 4:
            mobWPN = 15
            mobWPNd = "Adamantium Hammer"
            mobWPNl = 35
        else:
            mobWPN = 16
            mobWPNd = "Adamantium Axe"
            mobWPNl = 40
        mobATK = mobSTR + mobWPN
        mobDEF = 1
        mobDEX = 1
        mobINT = 1
        mobLUK = 1
        mobCRITb = 1
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 100
        
    elif rnddunMob <= 100 and rnddunMob > 73:
        # 17% chance
        mob = "Dark Slime"
        mobLV = 12
        mobGold = 50
        mobEXP = 200
        mobHPmax = randint(43, 54)
        mobHP = mobHPmax
        mobMPmax = randint(12, 23)
        mobMP = mobMPmax
        mobSTR = randint(12, 20)
        mobWPN = randint(4, 7)
        mobWPNd = "Dark Slime Goo"
        mobWPNl = randint(15, 30)
        mobATK = mobSTR + mobWPN
        mobDEF = randint(12, 22)
        mobDEX = randint(15, 23)
        mobINT = randint(16, 21)
        mobLUK = randint(15, 30)
        mobCRITb = 0
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 0
        encounternum += 1
        
    elif rnddunMob <= 100 and rnddunMob > 56:
        # 17% chance
        mob = "Giant Spider"
        mobLV = 15
        mobGold = 65
        mobEXP = 250
        mobHPmax = randint(26, 37)
        mobHP = mobHPmax
        mobMPmax = randint(12, 28)
        mobMP = mobMPmax
        mobSTR = randint(16, 25)
        mobWPN = randint(5, 8)
        mobWPNd = "Giant Spider Fang"
        mobWPNl = randint(22, 36)
        mobATK = mobSTR + mobWPN
        mobDEF = randint(15, 23)
        mobDEX = randint(25, 37)
        mobINT = randint(18, 27)
        mobLUK = randint(21, 34)
        mobCRITb = 0
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 0
        encounternum += 1
        
    elif rnddunMob <= 100 and rnddunMob > 41:
        # 15% chance
        mob = "Angry Zombie"
        mobLV = 18
        mobGold = 75
        mobEXP = 300
        mobHPmax = randint(44, 57)
        mobHP = mobHPmax
        mobMPmax = randint(20, 27)
        mobMP = mobMPmax
        mobSTR = randint(20, 28)
        mobWPN = randint(6, 9)
        mobWPNd = "Zombie Tooth"
        mobWPNl = randint(15, 27)
        mobATK = mobSTR + mobWPN
        mobDEF = randint(18, 25)
        mobDEX = randint(5, 15)
        mobINT = randint(3, 12)
        mobLUK = randint(30, 37)
        mobCRITb = 0
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 0
        encounternum += 1
        
    elif rnddunMob <= 100 and rnddunMob > 26:
        # 15% chance
        mob = "Ghost"
        mobLV = 20
        mobGold = 80
        mobEXP = 350
        mobHPmax = randint(30, 60)
        mobHP = mobHPmax
        mobMPmax = 0
        mobMP = mobMPmax
        mobSTR = randint(20, 30)
        mobWPN = randint(7, 10)
        mobWPNd = "Ectoplasm"
        mobWPNl = randint(20, 35)
        mobATK = mobSTR + mobWPN
        mobDEF = randint(13, 25)
        mobDEX = randint(43, 57)
        mobINT = randint(23, 30)
        mobLUK = randint(26, 33)
        mobCRITb = 0
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 0
        encounternum += 1
        
    elif rnddunMob <= 100 and rnddunMob > 12:
        # 14% chance
        mob = "Skeleton Fighter"
        mobLV = randint(24, 26)
        mobGold = 125
        mobEXP = 450
        mobHPmax = randint(55, 70)
        mobHP = mobHPmax
        mobMPmax = randint(25, 35)
        mobMP = mobMPmax
        mobSTR = randint(29, 38)
        # rnd steel V.WPN
        rndWPN = randint(1, 5)
        if rndWPN == 1:
            mobWPN = 7
            mobWPNd = "Steel Dagger"
            mobWPNl = 35
        elif rndWPN == 2:
            mobWPN = 8
            mobWPNd = "Steel Sword"
            mobWPNl = 20
        elif rndWPN == 3:
            mobWPN = 10
            mobWPNd = "Steel Lance"
            mobWPNl = 20
        elif rndWPN == 4:
            mobWPN = 11
            mobWPNd = "Steel Hammer"
            mobWPNl = 25
        else:
            mobWPN = 12
            mobWPNd = "Steel Axe"
            mobWPNl = 30
        mobATK = mobSTR + mobWPN
        mobDEF = randint(30, 47)
        mobDEX = randint(35, 49)
        mobINT = randint(28, 37)
        mobLUK = randint(30, 45)
        mobCRITb = 0
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 75
        encounternum += 1
        
    else:
        # 11% chance
        mob = "Mummy"
        mobLV = randint(27, 29)
        mobGold = 200
        mobEXP = 500
        mobHPmax = randint(60, 80)
        mobHP = mobHPmax
        mobMPmax = randint(30, 45)
        mobMP = mobMPmax
        mobSTR = randint(35, 50)
        # rnd platinum V.WPN
        rndWPN = randint(1, 5)
        if rndWPN == 1:
            mobWPN = 9
            mobWPNd = "Platinum Dagger"
            mobWPNl = 40
        elif rndWPN == 2:
            mobWPN = 10
            mobWPNd = "Platinum Sword"
            mobWPNl = 25
        elif rndWPN == 3:
            mobWPN = 12
            mobWPNd = "Platinum Lance"
            mobWPNl = 25
        elif rndWPN == 4:
            mobWPN = 13
            mobWPNd = "Platinum Hammer"
            mobWPNl = 30
        else:
            mobWPN = 14
            mobWPNd = "Platinum Axe"
            mobWPNl = 35
        mobATK = mobSTR + mobWPN
        mobDEF = randint(35, 50)
        mobDEX = randint(30, 50)
        mobINT = randint(20, 40)
        mobLUK = randint(30, 50)
        mobCRITb = 0
        mobCRIT = round(mobLUK + mobWPNl + mobCRITb) / 2
        mobAVO = round(mobLUK + mobDEX) / 2
        mobDropwc = 60
        encounternum += 1

    # display the encounter info
    stopwatch2(1)
    if mob == "BOSS: Undead Demon Lord":
        print "\n[You encounter the DUNGEON BOSS: Level " + str(mobLV) + " Undead Demon Lord!]"
    elif mob == "Minotaur Guardian":
        print "\n[You encounter the DUNGEON GUARDIAN: Level " + str(mobLV) + " Minotaur!]"
    elif mob == "Vampire":
        print "\n[You encounter the DUNGEON MINIBOSS: Level " + str(mobLV) + " Vampire Minion Overlord!]"
    else:
        print "\n[You encounter a Level " + str(mobLV) + " " + mob + "!]"
    enemystats()
    cont = raw_input("\n(Press enter to continue)")

    # start fight2 sequence
    while pHP > 0 and mobHP > 0 and not mobEscape and not pEscape:
        # turn fight sequence
        # calc enemy action
        mobTURNc = randint(1, 100)
        if mobTURNc <= 10:
            # attempts to flee
            mobTURN = "Flee"
        elif mobTURNc >= 50:
            # attacks
            mobTURN = "Attack"
        elif mobTURNc > 10 and mobTURNc < 30:
            # guards
            mobTURN = "Guard"
        else:
            # CRIT +10
            mobTURN = "Focus"
        # player decides action
        while True:
            pTURN = raw_input("\n[OPTIONS: 'ATTACK', 'FOCUS' (+10% CRIT), 'GUARD' (1/2 DMG), 'FLEE' (" + str(int((fleechance(pDEX, mobDEX, fleeAttempts) / float(256) * 100))) + "%)]    ")
            if pTURN.lower() == "attack":
                # attacks
                pTURN = "Attack"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                if mobTURN == "Attack":
                    tiebreaker = randint(1, 2)
                    # calc who attacks first
                    if pDEX > mobDEX or pDEX == mobDEX and tiebreaker == 1:
                        turnCount += 1
                        #player first
                        print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                        #crit chance
                        if pCRIT >= randint(1, 100):
                            pDMG = (pATK - mobDEF) * 2
                            if pDMG < 0:
                                #make it=0
                                pDMG = 0
                            if mobAVO >= randint(1, 100):
                                # mob dodge
                                stopwatch2(1)
                                print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                            else:
                                #crit atk
                                print "[CRITICAL HIT!    x2 DAMAGE]"
                                print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                newmobHP = mobHP
                                newmobHP -= pDMG
                                if newmobHP < 0:
                                    #make it not<0                                
                                    newmobHP = 0
                                print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                mobHP = newmobHP
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                                if mobHP == 0:
                                    stopwatch2(1)
                                    # mob defeated, player wins
                                    print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    # gain gold
                                    print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                    pGold += mobGold
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobkills += 1
                                    if mob == "BOSS: Undead Demon Lord":
                                        # exit dungeon
                                        defeatboss = True
                                    break
                                #else cont fight (still alive)
                        else:
                            #no crit chance
                            pDMG = pATK - mobDEF
                            if pDMG < 0:
                                #make it=0
                                pDMG = 0
                            if mobAVO >= randint(1, 100):
                                # mob dodge
                                stopwatch2(1)
                                print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                            else:
                                #no crit atk
                                print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                newmobHP = mobHP
                                newmobHP -= pDMG
                                if newmobHP < 0:
                                    #make it not<0
                                    newmobHP = 0
                                print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                mobHP = newmobHP
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                                if mobHP == 0:
                                    stopwatch2(1)
                                    # mob defeated, player wins
                                    print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    # gain gold
                                    print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                    pGold += mobGold
                                    pGold += mobGold
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobkills += 1
                                    if mob == "BOSS: Undead Demon Lord":
                                        # exit dungeon
                                        defeatboss = True
                                    break
                                #else cont fight (still alive)
                        stopwatch2(1)
                        turnCount += 1
                        #mob attacks (not KO)
                        print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                        #mob crit chance
                        if mobCRIT >= randint(1, 100):
                            mobDMG = (mobATK - pDEF) * 2
                            if mobDMG < 0:
                                #make it=0
                                mobDMG = 0
                            if pAVO >= randint(1, 100):
                                # player dodge
                                stopwatch2(1)
                                print "You dodge the attack!"
                                if mobCRITb > 0:
                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                    mobCRITb = 0
                                break
                            else:
                                #mob crit atk
                                print "[CRITICAL HIT!    x2 DAMAGE]"
                                print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                newpHP = pHP
                                newpHP -= mobDMG
                                if newpHP < 0:
                                    #make it not<0
                                    newpHP = 0
                                print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                pHP = newpHP
                                if mobCRITb > 0:
                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                    mobCRITb = 0
                                if pHP == 0:
                                    # player defeated, player loses
                                    stopwatch2(1)
                                    print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    gameoverl()
                                    exit = raw_input("(Press enter to exit the game)    ")
                                    # exits the game by death
                                    raise SystemExit
                                #else cont fight (still alive)
                                break
                        else:
                            #no mob crit atk
                            mobDMG = mobATK - pDEF
                            if mobDMG < 0:
                                #make it=0
                                mobDMG = 0
                            if pAVO >= randint(1, 100):
                                # player dodge
                                stopwatch2(1)
                                print "You dodge the attack!"
                                if mobCRITb > 0:
                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                    mobCRITb = 0
                            else:
                                #mob no crit atk
                                print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                newpHP = pHP
                                newpHP -= mobDMG
                                if newpHP < 0:
                                    #make it not<0
                                    newpHP = 0
                                print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                pHP = newpHP
                                if mobCRITb > 0:
                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                    mobCRITb = 0
                                if pHP == 0:
                                    # player defeated, player loses
                                    stopwatch2(1)
                                    print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    gameoverl()
                                    exit = raw_input("(Press enter to exit the game)    ")
                                    # exits the game by death
                                    raise SystemExit
                                #else cont fight (still alive)
                            break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                    elif mobDEX > pDEX or mobDEX == pDEX and tiebreaker == 2:
                        turnCount += 1
                        # enemy first
                        print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                        #mob crit chance
                        if mobCRIT >= randint(1, 100):
                            mobDMG = (mobATK - pDEF) * 2
                            if mobDMG < 0:
                                #make it=0
                                mobDMG = 0
                            if pAVO >= randint(1, 100):
                                # player dodge
                                stopwatch2(1)
                                print "You dodge the attack!"
                                if mobCRITb > 0:
                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                    mobCRITb = 0
                            else:
                                #mob crit atk
                                print "[CRITICAL HIT!    x2 DAMAGE]"
                                print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                newpHP = pHP
                                newpHP -= mobDMG
                                if newpHP < 0:
                                    #make it not<0
                                    newpHP = 0
                                print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                pHP = newpHP
                                if mobCRITb > 0:
                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                    mobCRITb = 0
                                if pHP == 0:
                                    # player defeated, player loses
                                    stopwatch2(1)
                                    print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    gameoverl()
                                    exit = raw_input("(Press enter to exit the game)    ")
                                    # exits the game by death
                                    raise SystemExit
                                #else cont fight (still alive)
                        else:
                            #no mob crit atk
                            mobDMG = mobATK - pDEF
                            if mobDMG < 0:
                                #make it=0
                                mobDMG = 0
                            if pAVO >= randint(1, 100):
                                # player dodge
                                stopwatch2(1)
                                print "You dodge the attack!"
                                if mobCRITb > 0:
                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                    mobCRITb = 0
                            else:
                                #mob no crit atk
                                print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                newpHP = pHP
                                newpHP -= mobDMG
                                if newpHP < 0:
                                    #make it not<0
                                    newpHP = 0
                                print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                pHP = newpHP
                                if mobCRITb > 0:
                                    print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                    mobCRITb = 0
                                if pHP == 0:
                                    # player defeated, player loses
                                    stopwatch2(1)
                                    print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    gameoverl()
                                    exit = raw_input("(Press enter to exit the game)    ")
                                    # exits the game by death
                                    raise SystemExit
                                #else cont fight (still alive)
                        stopwatch2(1)
                        turnCount += 1
                        print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                        #crit chance
                        if pCRIT >= randint(1, 100):
                            pDMG = (pATK - mobDEF) * 2
                            if pDMG < 0:
                                #make it=0
                                pDMG = 0
                            if mobAVO >= randint(1, 100):
                                # mob dodge
                                stopwatch2(1)
                                print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                            else:
                                #crit atk
                                print "[CRITICAL HIT!    x2 DAMAGE]"
                                print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                newmobHP = mobHP
                                newmobHP -= pDMG
                                if newmobHP < 0:
                                    #make it not<0                                
                                    newmobHP = 0
                                print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                mobHP = newmobHP
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                                if mobHP == 0:
                                    # mob defeated, player wins
                                    stopwatch2(1)
                                    print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    # gain gold
                                    print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                    pGold += mobGold
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobkills += 1
                                    if mob == "BOSS: Undead Demon Lord":
                                        # exit dungeon
                                        defeatboss = True
                                    break
                        else:
                            #no crit chance
                            pDMG = pATK - mobDEF
                            if pDMG < 0:
                                #make it=0
                                pDMG = 0
                            if mobAVO >= randint(1, 100):
                                # mob dodge
                                stopwatch2(1)
                                print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                            else:
                                #no crit atk
                                print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                newmobHP = mobHP
                                newmobHP -= pDMG
                                if newmobHP < 0:
                                    #make it not<0
                                    newmobHP = 0
                                print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                mobHP = newmobHP
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                                if mobHP == 0:
                                    stopwatch2(1)
                                    # mob deafeated, player wins
                                    print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    # gain gold
                                    print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                    pGold += mobGold
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobkills += 1
                                    if mob == "BOSS: Undead Demon Lord":
                                        # exit dungeon
                                        defeatboss = True
                                    break
                                #else cont fight (still alive)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                elif mobTURN == "Focus":
                    turnCount += 1
                    # enemy focuses
                    mobCRITb += 10
                    print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+ 10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                    stopwatch2(1)
                    turnCount += 1
                    # player attacks
                    print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                    #crit chance
                    if pCRIT >= randint(1, 100):
                        pDMG = (pATK - mobDEF) * 2
                        if pDMG < 0:
                            #make it=0
                            pDMG = 0
                        if mobAVO >= randint(1, 100):
                            # mob dodge
                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                            if pCRITb > 0:
                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                pCRITb = 0
                        else:
                            #crit atk
                            print "[CRITICAL HIT!    x2 DAMAGE]"
                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                            newmobHP = mobHP
                            newmobHP -= pDMG
                            if newmobHP < 0:
                                #make it not<0                                
                                newmobHP = 0
                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                            mobHP = newmobHP
                            if pCRITb > 0:
                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                pCRITb = 0
                            if mobHP == 0:
                                # mob defeated, player wins
                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                # gain gold
                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                pGold += mobGold
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobkills += 1
                                if mob == "BOSS: Undead Demon Lord":
                                    # exit dungeon
                                    defeatboss = True
                                break
                            #else cont fight (still alive)
                    else:
                        #no crit chance
                        pDMG = pATK - mobDEF
                        if pDMG < 0:
                            #make it=0
                            pDMG = 0
                        if mobAVO >= randint(1, 100):
                            # mob dodge
                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                            if pCRITb > 0:
                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                pCRITb = 0
                        else:
                            #no crit atk
                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                            newmobHP = mobHP
                            newmobHP -= pDMG
                            if newmobHP < 0:
                                #make it not<0
                                newmobHP = 0
                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                            mobHP = newmobHP
                            if pCRITb > 0:
                               print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                            pCRITb = 0
                            if mobHP == 0:
                                # mob deafeated, player wins
                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                # gain gold
                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                pGold += mobGold
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobkills += 1
                                if mob == "BOSS: Undead Demon Lord":
                                    # exit dungeon
                                    defeatboss = True
                                break
                            #else cont fight (still alive)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                elif mobTURN == "Flee":
                    turnCount += 1
                    # enemy attempts to flee - if fail, player attacks
                    print "\nThe Level " + str(mobLV) + " " + mob + " tries to flee!"
                    mobfleeAttempts += 1
                    escapechance = randint(0, 255)
                    escape = fleechance(mobDEX, pDEX, mobfleeAttempts)
                    print "Chance of escape = " + str(int((escape / float(256) * 100))) + "%"
                    if escape > 255:
                        # Auto-escape
                        stopwatch(2)
                        print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                        if pCRITb > 0:
                            print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                            pCRITb = 0
                        # set mob escape to true
                        print "\nYou gain 100 EXP"
                        pEXP += 100
                        turnCounta += turnCount
                        turnCount = 0
                        mobfleeAttempts = 0
                        mobEscape = False
                        fleeAttempts = 0
                        pEscape = False
                        mobEscape = True
                        break
                    elif escape > escapechance:
                        # Successful escape
                        stopwatch(2)
                        print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                        if pCRITb > 0:
                            print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                            pCRITb = 0
                        # chance for drop gold and wpn
                        if randint(1, 100) <= round(pLUK / 3):
                            # drops all gold
                            print "However, it dropped all of its gold in the process!"
                            print "You gained " + str(mobGold) + " coins (Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins)"
                            pGold += mobGold
                        elif randint(1, 100) <= round(pLUK / 2):
                            print "However, it dropped half of its gold in the process!"
                            print "You gained " + str(int(round(mobGold * 0.5))) + " coins (Gold: " + str(pGold) + " -> " + str(int(round(pGold + mobGold * 0.5))) + " coins)"
                            pGold += int(round((mobGold * 0.5)))
                        # set mob escape to true
                        print "\nYou gain 100 EXP"
                        pEXP += 100
                        turnCounta += turnCount
                        turnCount = 0
                        mobfleeAttempts = 0
                        mobEscape = False
                        fleeAttempts = 0
                        pEscape = False
                        mobEscape = True
                        break
                    else:
                        # Failed flee attempt
                        stopwatch(2)
                        print "And is unsuccessful!\n[The Level " + str(mobLV) + " " + mob + " failed to escape]"
                        turnCount += 1
                        #player attacks
                        stopwatch2(1)
                        print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                        #crit chance
                        if pCRIT >= randint(1, 100):
                            pDMG = (pATK - mobDEF) * 2
                            if pDMG < 0:
                                #make it=0
                                pDMG = 0
                            if mobAVO >= randint(1, 100):
                                # mob dodge
                                print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                            else:
                                #crit atk
                                print "[CRITICAL HIT!    x2 DAMAGE]"
                                print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                newmobHP = mobHP
                                newmobHP -= pDMG
                                if newmobHP < 0:
                                    #make it not<0                                
                                    newmobHP = 0
                                print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                mobHP = newmobHP
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                                if mobHP == 0:
                                    # mob defeated, player wins
                                    print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    # gain gold
                                    print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                    pGold += mobGold
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobkills += 1
                                    if mob == "BOSS: Undead Demon Lord":
                                        # exit dungeon
                                        defeatboss = True
                                    break
                                #else cont fight (still alive)
                        else:
                            #no crit chance
                            pDMG = pATK - mobDEF
                            if pDMG < 0:
                                #make it=0
                                pDMG = 0
                            if mobAVO >= randint(1, 100):
                                # mob dodge
                                print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                            else:
                                #no crit atk
                                print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                                newmobHP = mobHP
                                newmobHP -= pDMG
                                if newmobHP < 0:
                                    #make it not<0
                                    newmobHP = 0
                                print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                                mobHP = newmobHP
                                if pCRITb > 0:
                                    print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                    pCRITb = 0
                                if mobHP == 0:
                                    # mob deafeated, player wins
                                    print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                    # gain gold
                                    print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                    pGold += mobGold
                                    turnCounta += turnCount
                                    turnCount = 0
                                    mobfleeAttempts = 0
                                    mobEscape = False
                                    fleeAttempts = 0
                                    pEscape = False
                                    mobkills += 1
                                    if mob == "BOSS: Undead Demon Lord":
                                        # exit dungeon
                                        defeatboss = True
                                    break
                                #else cont fight (still alive)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                else:   # enemy guard
                    turnCount += 1
                    turnCount += 1
                    #player attacks
                    print "\nYou attack the Level " + str(mobLV) + " " + mob + "!"
                    # enemy guards
                    print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!\n"
                    stopwatch2(1)
                    #crit chance
                    if pCRIT >= randint(1, 100):
                        pDMG = int(round(((pATK * 2) - mobDEF) / 2))
                        if pDMG < 0:
                            #make it=0
                            pDMG = 0
                        if mobAVO >= randint(1, 100):
                            # mob dodge
                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                            if pCRITb > 0:
                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                pCRITb = 0
                        else:
                            #crit atk
                            print "[CRITICAL HIT!    x2 DAMAGE]"
                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                            newmobHP = mobHP
                            newmobHP -= pDMG
                            if newmobHP < 0:
                                #make it not<0                                
                                newmobHP = 0
                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                            mobHP = newmobHP
                            if pCRITb > 0:
                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                pCRITb = 0
                            if mobHP == 0:
                                # mob defeated, player wins
                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                # gain gold
                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                pGold += mobGold
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobkills += 1
                                if mob == "BOSS: Undead Demon Lord":
                                    # exit dungeon
                                    defeatboss = True
                                break
                            #else cont fight (still alive)
                    else:
                        #no crit chance
                        pDMG = int(round((pATK - mobDEF) / 2))
                        if pDMG < 0:
                            #make it=0
                            pDMG = 0
                        if mobAVO >= randint(1, 100):
                            # mob dodge
                            print "The Level " + str(mobLV) + " " + mob + " dodged your attack..."
                            if pCRITb > 0:
                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                pCRITb = 0
                        else:
                            #no crit atk
                            print "You did " + str(pDMG) + " damage to the Level " + str(mobLV) + " " + mob
                            newmobHP = mobHP
                            newmobHP -= pDMG
                            if newmobHP < 0:
                                #make it not<0
                                newmobHP = 0
                            print "Level " + str(mobLV) + " " + mob + ": HP = " + str(mobHP) + "/" + str(mobHPmax) + " -> " + str(newmobHP) + "/" + str(mobHPmax)
                            mobHP = newmobHP
                            if pCRITb > 0:
                                print "You lose all your focus after attacking (-" + str(pCRITb) + ")"
                                pCRITb = 0
                            if mobHP == 0:
                                # mob deafeated, player wins
                                print "\nYou defeated the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                # gain gold
                                print "The Level " + str(mobLV) + " " + mob + " dropped " + str(mobGold) + " coins!\n[Your Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins]"
                                pGold += mobGold
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                mobkills += 1
                                if mob == "BOSS: Undead Demon Lord":
                                    # exit dungeon
                                    defeatboss = True
                                break
                            #else cont fight (still alive)
                break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
            elif pTURN.lower() == "guard":
                turnCount += 1
                # player guards
                pTURN = "Guard"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                if mobTURN == "Flee":
                    turnCount += 1
                    # enemy attempts to flee - if fail, player guards
                    print "\nThe Level " + str(mobLV) + " " + mob + " tries to flee!"
                    mobfleeAttempts += 1
                    escapechance = randint(0, 255)
                    escape = fleechance(mobDEX, pDEX, mobfleeAttempts)
                    print "Chance of escape = " + str(int((escape / float(256) * 100))) + "%"
                    if escape > 255:
                        # Auto-escape
                        stopwatch(2)
                        print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                        if pCRITb > 0:
                            print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                            pCRITb = 0
                        # set mob escape to true
                        print "\nYou gain 100 EXP"
                        pEXP += 100
                        turnCounta += turnCount
                        turnCount = 0
                        mobfleeAttempts = 0
                        mobEscape = False
                        fleeAttempts = 0
                        pEscape = False
                        mobEscape = True
                        break
                    elif escape > escapechance:
                        # Successful escape
                        stopwatch(2)
                        print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                        if pCRITb > 0:
                            print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                            pCRITb = 0
                        # chance for drop gold and wpn
                        if randint(1, 100) <= round(pLUK / 3):
                            # drops all gold
                            print "However, it dropped all of its gold in the process!"
                            print "You gained " + str(mobGold) + " coins (Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins)"
                            pGold += mobGold
                        elif randint(1, 100) <= round(pLUK / 2):
                            print "However, it dropped half of its gold in the process!"
                            print "You gained " + str(int(round(mobGold * 0.5))) + " coins (Gold: " + str(pGold) + " -> " + str(int(round(pGold + mobGold * 0.5))) + " coins)"
                            pGold += int(round((mobGold * 0.5)))
                        # set mob escape to true
                        print "\nYou gain 100 EXP"
                        pEXP += 100
                        turnCounta += turnCount
                        turnCount = 0
                        mobfleeAttempts = 0
                        mobEscape = False
                        fleeAttempts = 0
                        pEscape = False
                        mobEscape = True
                        break
                    else:
                        # Failed flee attempt
                        stopwatch(2)
                        print "And is unsuccessful!\n[The Level " + str(mobLV) + " " + mob + " failed to escape]"
                        #player guards, and fails
                        stopwatch2(1)
                        print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                        print "     but it fails."
                        break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                elif mobTURN == "Guard":
                    turnCount += 1
                    turnCount += 1
                    #player guards, and fails
                    print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                    print "     but it fails."
                    stopwatch2(1)
                    # enemy guards, and fails
                    print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!"
                    print "     but it fails."
                    break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                elif mobTURN == "Focus":
                    turnCount += 1
                    turnCount += 1
                    #player guards, and fails
                    print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                    print "     but it fails."
                    stopwatch2(1)
                    # enemy focuses
                    mobCRITb += 10
                    print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+ 10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                    break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                elif mobTURN == "Attack":
                    turnCount += 1
                    #player guards
                    print "\n[GUARD     1/2 DAMAGE]\nYou guard yourself for an attack!"
                    turnCount += 1
                    stopwatch2(1)
                    # enemy attacks
                    print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                    #mob crit chance
                    if mobCRIT >= randint(1, 100):
                        mobDMG = (mobATK - pDEF) * 2
                        if mobDMG < 0:
                            #make it=0
                            mobDMG = 0
                        if pAVO >= randint(1, 100):
                            # player dodge
                            print "You dodge the attack!"
                            if mobCRITb > 0:
                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                mobCRITb = 0
                        else:
                            #mob crit atk
                            print "[CRITICAL HIT!    x2 DAMAGE]"
                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                            newpHP = pHP
                            newpHP -= mobDMG
                            if newpHP < 0:
                                #make it not<0
                                newpHP = 0
                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                            pHP = newpHP
                            if mobCRITb > 0:
                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                mobCRITb = 0
                            if pHP == 0:
                                # player defeated, player loses
                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                gameoverl()
                                exit = raw_input("(Press enter to exit the game)    ")
                                # exits the game by death
                                raise SystemExit
                            #else cont fight (still alive)
                    else:
                        #no mob crit atk
                        mobDMG = int(round((mobATK - pDEF) / 2))
                        if mobDMG < 0:
                            #make it=0
                            mobDMG = 0
                        if pAVO >= randint(1, 100):
                            # player dodge
                            print "You dodge the attack!"
                            if mobCRITb > 0:
                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                mobCRITb = 0
                        else:
                            #mob no crit atk
                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                            newpHP = pHP
                            newpHP -= mobDMG
                            if newpHP < 0:
                                #make it not<0
                                newpHP = 0
                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                            pHP = newpHP
                            if mobCRITb > 0:
                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                mobCRITb = 0
                            if pHP == 0:
                                # player deafeated, player loses
                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                gameoverl()
                                exit = raw_input("(Press enter to exit the game)    ")
                                # exits the game by death
                                raise SystemExit
                            #else cont fight (still alive)
                    break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
            elif pTURN.lower() == "focus":
                pTURN = "Focus"
                turnCount += 1
                # player focuses, CRIT +10
                pCRITb += 10
                print "\nYou focus your energy (+10 CRIT -|- Total: + " + str(pCRITb) + " CRIT)"
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                if mobTURN == "Flee":
                    turnCount += 1
                    stopwatch2(1)
                    # enemy attempts to flee - if fail, player focuses
                    print "\nThe Level " + str(mobLV) + " " + mob + " tries to flee!"
                    mobfleeAttempts += 1
                    escapechance = randint(0, 255)
                    escape = fleechance(mobDEX, pDEX, mobfleeAttempts)
                    print "Chance of escape = " + str(int((escape / float(256) * 100))) + "%"
                    if escape > 255:
                        # Auto-escape
                        stopwatch(2)
                        print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                        if pCRITb > 0:
                            print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                            pCRITb = 0
                        # set mob escape to true
                        print "\nYou gain 100 EXP"
                        pEXP += 100
                        turnCounta += turnCount
                        turnCount = 0
                        mobfleeAttempts = 0
                        mobEscape = False
                        fleeAttempts = 0
                        pEscape = False
                        mobEscape = True
                        break
                    elif escape > escapechance:
                        # Successful escape
                        stopwatch(2)
                        print "And is successful!\n[The Level " + str(mobLV) + " " + mob + " successfully manages to get away]"
                        if pCRITb > 0:
                            print "You lose all your focus after it escapes (-" + str(pCRITb) + " CRIT)"
                            pCRITb = 0
                        # chance for drop gold and wpn
                        if randint(1, 100) <= round(pLUK / 3):
                            # drops all gold
                            print "However, it dropped all of its gold in the process!"
                            print "You gained " + str(mobGold) + " coins (Gold: " + str(pGold) + " -> " + str(pGold + mobGold) + " coins)"
                            pGold += mobGold
                        elif randint(1, 100) <= round(pLUK / 2):
                            print "However, it dropped half of its gold in the process!"
                            print "You gained " + str(int(round(mobGold * 0.5))) + " coins (Gold: " + str(pGold) + " -> " + str(int(round(pGold + mobGold * 0.5))) + " coins)"
                            pGold += int(round((mobGold * 0.5)))
                        # set mob escape to true
                        print "\nYou gain 100 EXP"
                        pEXP += 100
                        turnCounta += turnCount
                        turnCount = 0
                        mobfleeAttempts = 0
                        mobEscape = False
                        fleeAttempts = 0
                        pEscape = False
                        mobEscape = True
                        break
                    else:
                        # Failed flee attempt
                        stopwatch(2)
                        print "And is unsuccessful!\n[The Level " + str(mobLV) + " " + mob + " failed to escape]"
                        #player focuses, and gets bonus +5 CRIT
                        pCRITb += 5
                        print "During the time the Level " + str(mobLV) + " " + mob + " tried to flee, you were able to focus a little longer!\n\nYou focus your energy a little extra (+ 5 CRIT -|- Total: + " + str(pCRITb) + " CRIT)"
                        break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                elif mobTURN == "Guard":
                    turnCount += 1
                    stopwatch2(1)
                    # enemy guards, and fails
                    print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!"
                    print "     but it fails."
                    break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                elif mobTURN == "Focus":
                    turnCount += 1
                    stopwatch2(1)
                    # enemy focuses
                    mobCRITb += 10
                    print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                    #player and enemy focus, and get bonus +5 CRIT each
                    pCRITb += 5
                    print "\nDuring the time the Level " + str(mobLV) + " " + mob + " was also focusing, you were able to focus a little longer!\n\nYou focus your energy a little extra (+ 5 CRIT -|- Total: + " + str(pCRITb) + " CRIT)"
                    mobCRITb += 5
                    print "\n     but so did the Level " + str(mobLV) + " " + mob + " (+ 5 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                    break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                elif mobTURN == "Attack":
                    turnCount += 1
                    stopwatch2(1)
                    #mob attacks (not KO)
                    print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                    #mob crit chance
                    if mobCRIT >= randint(1, 100):
                        mobDMG = (mobATK - pDEF) * 2
                        if mobDMG < 0:
                            #make it=0
                            mobDMG = 0
                        if pAVO >= randint(1, 100):
                            # player dodge
                            print "You dodge the attack!"
                            if mobCRITb > 0:
                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                mobCRITb = 0
                            break
                        else:
                            #mob crit atk
                            print "[CRITICAL HIT!    x2 DAMAGE]"
                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                            newpHP = pHP
                            newpHP -= mobDMG
                            if newpHP < 0:
                                #make it not<0
                                newpHP = 0
                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                            pHP = newpHP
                            if mobCRITb > 0:
                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                mobCRITb = 0
                            if pHP == 0:
                                # player defeated, player loses
                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                gameoverl()
                                exit = raw_input("(Press enter to exit the game)    ")
                                # exits the game by death
                                raise SystemExit
                            #else cont fight (still alive)
                            break
                    else:
                        #no mob crit atk
                        mobDMG = mobATK - pDEF
                        if mobDMG < 0:
                            #make it=0
                            mobDMG = 0
                        if pAVO >= randint(1, 100):
                            # player dodge
                            print "You dodge the attack!"
                            if mobCRITb > 0:
                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                mobCRITb = 0
                        else:
                            #mob no crit atk
                            print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                            newpHP = pHP
                            newpHP -= mobDMG
                            if newpHP < 0:
                                #make it not<0
                                newpHP = 0
                            print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                            pHP = newpHP
                            if mobCRITb > 0:
                                print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                mobCRITb = 0
                            if pHP == 0:
                                # player defeated, player loses
                                print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                turnCounta += turnCount
                                turnCount = 0
                                mobfleeAttempts = 0
                                mobEscape = False
                                fleeAttempts = 0
                                pEscape = False
                                gameoverl()
                                exit = raw_input("(Press enter to exit the game)    ")
                                # exits the game by death
                                raise SystemExit
                            #else cont fight (still alive)
                        break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
            elif pTURN.lower() == "flee":
                pTURN = "Flee"
                turnCount += 1
                # attempts to flee
                print "\nYou try to escape from the Level " + str(mobLV) + " " + mob + "!"
                if mobTURN == "Flee":
                    # mob flees too
                    turnCount += 1
                    print "\nThis particular Level " + str(mobLV) + " " + mob + " has also tried to flee at the same time so the battle ends in a draw!"
                    print "\nWhat a coincidence!  You learn from this unique experience and gain 200 EXP!!"
                    pEXP += 200
                    turnCounta += turnCount
                    turnCount = 0
                    mobfleeAttempts = 0
                    mobEscape = False
                    fleeAttempts = 0
                    pEscape = False
                    # set mob escape to true
                    mobEscape = True
                    # set player escape to true
                    pEscape = True
                    break
                else:
                    fleeAttempts += 1
                    escapechance = randint(0, 255)
                    escape = fleechance(pDEX, mobDEX, fleeAttempts)
                    if escape > 255:
                        # Auto-escape
                        stopwatch(2)
                        print "And are successful!\n[You manage to successfully get away from the Level " + str(mobLV) + " " + mob + "]"
                        if pCRITb > 0:
                            print "You lose all your focus after you escape (-" + str(pCRITb) + " CRIT)"
                            pCRITb = 0
                        # set player escape to true
                        print "\nYou gain 50 EXP"
                        pEXP += 50
                        turnCounta += turnCount
                        turnCount = 0
                        mobfleeAttempts = 0
                        mobEscape = False
                        fleeAttempts = 0
                        pEscape = False
                        pEscape = True
                        break
                    elif escape > escapechance:
                        # Successful escape
                        stopwatch(2)
                        print "And are successful!\n[You manage to successfully get away from the Level " + str(mobLV) + " " + mob + "]"
                        if pCRITb > 0:
                            print "You lose all your focus after you escape (-" + str(pCRITb) + " CRIT)"
                            pCRITb = 0
                        # chance for you to lose gold
                        if randint(1, 100) <= round(mobLUK / 5):
                            # lose 25% of gold
                            goldLost = int(round(pGold * 0.25))
                            print "However, the Level " + str(mobLV) + " " + mob + " managed to steal a quarter of your gold."
                            print "You lost " + str(goldLost) + " coins (Gold: " + str(pGold) + " -> " + str(pGold - goldLost) + " coins)"
                            pGold -= goldLost
                            goldLost = 0
                        elif randint(1, 100) <= round(mobLUK / 4):
                            # lose 10% of gold
                            goldLost = int(round(pGold * 0.1))
                            print "However, the Level " + str(mobLV) + " " + mob + " managed to steal a fraction of your gold."
                            print "You lost " + str(goldLost) + " coins (Gold: " + str(pGold) + " -> " + str(pGold - goldLost) + " coins)"
                            pGold -= goldLost
                            goldLost = 0
                        # set player escape to true
                        print "\nYou gain 50 EXP"
                        pEXP += 50
                        turnCounta += turnCount
                        turnCount = 0
                        mobfleeAttempts = 0
                        mobEscape = False
                        fleeAttempts = 0
                        pEscape = False
                        pEscape = True
                        break
                    else:
                        # Failed flee attempt
                        stopwatch(2)
                        print "And are unsuccessful!\n[You failed to get away from the Level " + str(mobLV) + " " + mob + " successfully]"
                        stopwatch2(1)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        if mobTURN == "Guard":
                            turnCount += 1
                            # enemy guards, and fails
                            print "\n[GUARD!    1/2 DAMAGE]\nThe Level " + str(mobLV) + " " + mob + " guards itself!"
                            print "     but it fails."
                            break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Focus":
                            turnCount += 1
                            # enemy focuses
                            mobCRITb += 10
                            print "\nThe Level " + str(mobLV) + " " + mob + " focuses its energy (+ 10 CRIT -|- Total: + " + str(mobCRITb) + " CRIT)"
                            break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                        elif mobTURN == "Attack":
                            turnCount += 1
                            # enemy attacks
                            print "\nYou are attacked by the Level " + str(mobLV) + " " + mob + "!"
                            #mob crit chance
                            if mobCRIT >= randint(1, 100):
                                mobDMG = (mobATK - pDEF) * 2
                                if mobDMG < 0:
                                    #make it=0
                                    mobDMG = 0
                                if pAVO >= randint(1, 100):
                                    # player dodge
                                    print "You dodge the attack!"
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                else:
                                    #mob crit atk
                                    print "[CRITICAL HIT!    x2 DAMAGE]"
                                    print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                    newpHP = pHP
                                    newpHP -= mobDMG
                                    if newpHP < 0:
                                        #make it not<0
                                        newpHP = 0
                                    print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                    pHP = newpHP
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                    if pHP == 0:
                                        # player defeated, player loses
                                        print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        gameoverl()
                                        exit = raw_input("(Press enter to exit the game)    ")
                                        # exits the game by death
                                        raise SystemExit
                                    #else cont fight (still alive)
                            else:
                                #no mob crit atk
                                mobDMG = mobATK - pDEF
                                if mobDMG < 0:
                                    #make it=0
                                    mobDMG = 0
                                if pAVO >= randint(1, 100):
                                    # player dodge
                                    print "You dodge the attack!"
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                else:
                                    #mob no crit atk
                                    print "The Level " + str(mobLV) + " " + mob + " did " + str(mobDMG) + " damage"
                                    newpHP = pHP
                                    newpHP -= mobDMG
                                    if newpHP < 0:
                                        #make it not<0
                                        newpHP = 0
                                    print "Your HP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
                                    pHP = newpHP
                                    if mobCRITb > 0:
                                        print "The Level " + str(mobLV) + " " + mob + " loses its focus after attacking (-" + str(mobCRITb) + ")"
                                        mobCRITb = 0
                                    if pHP == 0:
                                        # player deafeated, player loses
                                        print "\nYou were defeated by the Level " + str(mobLV) + " " + mob + " in " + str(turnCount) + " turns!"
                                        turnCounta += turnCount
                                        turnCount = 0
                                        mobfleeAttempts = 0
                                        mobEscape = False
                                        fleeAttempts = 0
                                        pEscape = False
                                        gameoverl()
                                        exit = raw_input("(Press enter to exit the game)    ")
                                        # exits the game by death
                                        raise SystemExit
                                    #else cont fight (still alive)
                            break
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
            elif pTURN.lower() == "/help":
                print "'/enemystats'"
                HELP()
            elif pTURN.lower() == "/playerstats":
                playerstats()
            elif pTURN.lower() == "/enemystats":
                enemystats()
            else:
                print ("\n[INVALID, please try again]")

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
                
    else: # check these after battle is won
        if mobHP <= 0:
            # gain exp for win
            print "\nYou obtain " + str(mobEXP) + " EXP for defeating the Level " + str(mobLV) + " " + mob + "."
            pEXP += mobEXP
            
        if mobHP <= 0 or mobTURN == "Flee":
            # calc chance to drop mob wpn
            if randint(1, 100) <= mobDropwc:
                print "\nThe Level " + str(mobLV) + " " + mob + " dropped its " + mobWPNd + "!"
                #ask if want to use instead of current wpn
                while True:
                    yn = raw_input("[Do you want to equip the " + mobWPNd + " (Bonus: +" + str(mobWPN) + " ATK, +" + str(mobWPNl) + " CRIT)]     ('Y'es or 'N'o)     ")
                    if yn.lower() == "y" or yn.lower() == "n":
                        ayn = raw_input("Last Chance, do you want it or not?  ('Y'es or 'N'o)     ")
                        if ayn.lower() == "y":
                            print "\n[You swap your " + pWPNd + " (Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT) for the " + mobWPNd + " (Bonus: +" + str(mobWPN) + " ATK, +" + str(mobWPNl) + " CRIT)]"
                            pWPN = mobWPN
                            pWPNd = mobWPNd
                            pWPNl = mobWPNl
                            break
                        elif ayn.lower() == "n":
                            print "\n[You decide your weapon is still better and destroy the Level " + str(mobLV) + " " + mob + "'s " + mobWPNd + "]\n[ + 500 EXP]"
                            pEXP += 500
                            break
                        elif ayn.lower() == "/help":
                            HELP()
                        elif ayn.lower() == "/playerstats":
                            playerstats()
                        elif ayn.lower() == "/enemystats":
                            enemystats()
                        else:
                            print ("\n[INVALID, please try again]")
                    elif yn.lower() == "/help":
                        HELP()
                    elif yn.lower() == "/playerstats":
                        playerstats()
                    elif yn.lower() == "/enemystats":
                        enemystats()
                    else:
                        print ("\n[INVALID, please try again]")
                    
        while pEXP >= pLVupEXPCount:
            #LV UP
            pLV += 1
            pLVupEXP += 75
            pLVupEXPCount += pLVupEXP
            print "\n[LEVEL UP: " + name + ", you are now a Level " + str(pLV) + " " + fclass + " " + race + "]"
            statCount = int(round(randint(0, 100) / 20))
            newpHPmax = pHPmax + statCount
            print "\nHP MAX: " + str(pHPmax) + " -> " + str(newpHPmax) + "    (+" + str(newpHPmax - pHPmax) + ")"
            pHPmax = newpHPmax
            pHP += statCount
            statCount = int(round(randint(0, 100) / 20))
            newpMPmax = pMPmax + statCount
            print "MP MAX: " + str(pMPmax) + " -> " + str(newpMPmax) + "    (+" + str(newpMPmax - pMPmax) + ")"
            pMPmax = newpMPmax
            pMP += statCount
            statCount = int(round(randint(0, 100) / 20))
            newpSTR = pSTR + statCount
            newpATK = newpSTR + pWPN
            print "ATK: " + str(pATK) + " -> " + str(newpATK) + "       (+" + str(newpATK - pATK) + ")"
            print "     STR: " + str(pSTR) + " -> " + str(newpSTR) + "  (+" + str(newpSTR - pSTR) + ")"
            print "     Weapon = " + pWPNd + " | Bonus: +" + str(pWPN) + " ATK, +" + str(pWPNl) + " CRIT"
            pATK = newpATK
            pSTR = newpSTR
            statCount = int(round(randint(0, 100) / 20))
            newpDEF = pDEF + statCount
            print "DEF: " + str(pDEF) + " -> " + str(newpDEF) + "       (+" + str(newpDEF - pDEF) + ")"
            pDEF = newpDEF
            statCount = int(round(randint(0, 100) / 20))
            newpDEX = pDEX + statCount
            print "DEX: " + str(pDEX) + " -> " + str(newpDEX) + "       (+" + str(newpDEX - pDEX) + ")"
            pDEX = newpDEX
            statCount = int(round(randint(0, 100) / 20))
            newpINT = pINT + statCount
            print "INT: " + str(pINT) + " -> " + str(newpINT) + "       (+" + str(newpINT - pINT) + ")"
            pINT = newpINT
            statCount = int(round(randint(0, 100) / 20))
            newpLUK = pLUK + statCount
            print "LUK: " + str(pLUK) + " -> " + str(newpLUK) + "       (+" + str(newpLUK - pLUK) + ")"
            pLUK = newpLUK
            newpCRIT = round(pLUK + pWPNl + pCRITb) / 2
            newpAVO = round(pLUK + pDEX) / 2
            print "     CRIT chance: " + str(pCRIT - pCRITb) + "% (+" + str(pCRITb) + "%) -> " + str(newpCRIT) + "% (+" + str(pCRITb) + "%)" + "    (+" + str(newpCRIT - pCRIT) + ")"
            print "     AVO chance: " + str(pAVO) + "% -> " + str(newpAVO) + "%                 (+" + str(newpAVO - pAVO) + ")\n"
            pCRIT = newpCRIT
            pAVO = newpAVO
            cont = raw_input("\n(Press enter to continue)")

        # display exp until next lv
        print "\nEXP until next level = " + str(pLVupEXPCount - pEXP)
        pHPregen = int(round(pHPmax * pHPregenRate))
        pMPregen = int(round(pMPmax * pMPregenRate))
            
        # HP regen
        newpHP = pHP
        newpHP += pHPregen
        if newpHP > pHPmax:
            # make it=max
            newpHP = pHPmax
        print "\nYou regenerate " + str(pHPregen) + " HP after the battle\nHP = " + str(pHP) + "/" + str(pHPmax) + " -> " + str(newpHP) + "/" + str(pHPmax)
        pHP = newpHP
        # MP regen
        newpMP = pMP
        newpMP += pMPregen
        if newpMP > pMPmax:
            # make it=max
            newpMP = pMPmax
        print "You regenerate " + str(pMPregen) + " MP after the battle\nMP = " + str(pMP) + "/" + str(pMPmax) + " -> " + str(newpMP) + "/" + str(pMPmax) + "\n"
        pMP = newpMP

        turnCounta += turnCount
        turnCount = 0
        mobfleeAttempts = 0
        mobEscape = False
        fleeAttempts = 0
        pEscape = False
        '''if mobTURN == "Flee" and mobHP != 0:
            print "DAMN!  It got away!"'''
        # end fight sequence
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

# dungeon end sequence

print "\nAfter defeating the Dungeon Boss: Undead Demon Lord, a magical door appears out of air with the words EXIT scratched into the wood in large letters.\n"
print "Since you have been stuck down here for so long, you immediately burst through the door full of joy."
cont = raw_input("\n(Press enter to continue)\n")
print "[You are teleported to the front entrance]\n"
stopwatch2(1)
print "When you wake up from your unconcsciousness, you find the guard staring down on you.\n"
print "Guard:   'Hey there, " + name + ", I'm so glad to see your alright.'"
print "Guard:   'I was just minding my own business and doing the routine ol' guard post duty when all of a sudden a a great flash of light left me temporarily blinded.'"
print "Guard    'Once I could see again, I found you lying here unconcsious with a giant bag beside you.  Care to explain what happened down there?'"
stopwatch2(1)
print "\n[You explain what happened in the dungeon, every excruciating detail, and boast about how you spectacularly defeated the Undead Demon Lord]"
cont = raw_input("\n(Press enter to continue)\n")
print "Guard:   'WOW!!!  I'm really impressed!  I can't believe you actually cleared the dungeon.'"
print "Guard:   'I guess that's why the whole thing collapsed once you came out.'"
stopwatch2(1)
print "\n[You turn around and see what used to be the dungeon (that was named 'unconquerable' -- you sure proved them wrong), and see it in ruins, slowly seeping back into the earth]\n"
print "Guard:   'Well, I guess you deserce whatever's in that bag.  I'll go spread word of this in Konoha.'"
print "\n[The Guard hastily makes his way back to the village to tell everyone about your great feat]\n"
cont = raw_input("\n(Press enter to continue)\n")
print "[Meanwhile, you check to see what's in the bag...]"
stopwatch(2)
print "[You discover 1,000,000 GOLD!!!!  Now, you're set for life!]\n"
pGold += 1000000
cont = raw_input("\n(Press enter to continue)\n")
print "       CONGRATULATIONS"
print "       ==============="
print "\n   You successfully conquered the dungeon and beat the game!"
gameoverw()
exit = raw_input("(Press enter to exit the game)    ")
# exits the game by dungeon conquer
raise SystemExit
