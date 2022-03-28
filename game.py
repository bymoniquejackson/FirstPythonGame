import random
import sys 
import time
from tracemalloc import stop

#Typewriter print
def typeprint(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
 
#Dice rolling
def dice_roll():
    typeprint("Rolling dice...")
    time.sleep(2) 
    global dice_result
    dice_result = random.randint(1,6)
    print("You rolled",dice_result)
#Choice systems

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
Soteria = ["Soteria", "soteria", "God"]

required = ("\nUse only A, B, or C\n") 

print("""

             ________________________________________________
            /                       0                        \¬
           |    _________________________________________     |
           |   |                                         |    |
           |   |  God Program.exe                        |    |
           |   |                                         |    |
           |   |  C:\> _ Loading game                    |    |
           |   |                   /\                    |    |
           |   |                  /  \                   |    |
           |   |                 /    \                  |    |
           |   |                /      \                 |    |
           |   |               /  (@)   \                |    |
           |   |              /          \               |    |
           |   |             /____________\              |    |
           |   |              Three paths                |    |
           |   |                                 v 1.6   |    |
           |   |_________________________________________|    |
           |                      Soteria                     |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________            
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'

""")
######################################################################################
#Wanderers path
def wanderer_start():
    typeprint("The Wanderer story begins with him fleeing from the Venom Assembly after finding out they are planning to kill innocent people in a village.\nHow will you get to the village?\n")
    print("""\n
    A. Walking
    B. Hover Horse""") 
    choice= input(">>> ")
    if choice in answer_A:
        typeprint("The wanderer proceeds to walk all the way to the village without stopping once and ends up passing out before reaching the village.\nTry again \n")
        wanderer_start()

    elif choice in answer_B:
        typeprint("The wanderer jumps on a Hover horse and heads toward the village\n")
        wanderer_village()
    else:
        wanderer_start

def wanderer_village():
    typeprint("You enter the village and hitch the hover horse on a charging station however, He notices a beaten man getting attacked by a gang of pirates.\n Whats shall you do?\n")
    print(""" 
    A. Save him (Gamble)
    B. Leave him 
    C. Join in""")
    choice =  input(">>> ")
    if choice in answer_A:
        dice_roll()
        if dice_result <= 2:
            typeprint("You initiate combat but the pirates over power you\n Try again\n")
            wanderer_village()

        elif dice_result > 2 and dice_result <= 4:
            typeprint("You run at the pirates and manage to fight them off until they retreat\n")
            wanderer_and_survivor()
        
        elif dice_result > 4 and dice_result <=6:
            typeprint("You throw a punch and completely knock out the pirate, Fatality!\n")
            wanderer_and_survivor()
        
    elif choice in answer_B:
         typeprint("You ignore the commotion. Despite minding your business and avoid trouble, you are mistaken for a local and attacked from behind\nTry again\n")
         wanderer_village()
        
    elif choice in answer_C:
        typeprint("You walk over and join in beating the beaten guy on the floor, at first you all laugh however, the pirates soon realise you're not part of them and so they end up beating up you, Thats karma for you\nTry again\n")  
        wanderer_village()
    else:
        wanderer_village()

def wanderer_and_survivor():
    typeprint("You rush over to the badly beaten man he cough up blood and thanks you for saving him.\nHe informs you that is was the God program and the demi programs that lead a wave of crusadroids to the village.")
    typeprint("The survivor then slowly pass away, you now want to go back to the Venom Assembly to act revenge on the programs.\nHow do you get back to the base?\n")
    print(""" 
    A. Hover horse
    B. An actual horse
    C. Walk""")
    choice = input(">>> ")
    if choice in answer_A:     
        wanderer_NuWa()

    elif choice in answer_B:
     typeprint("You idiot this is the future who uses horses anymore?? Lame, try again\n")
     wanderer_and_survivor()
     
    elif choice in answer_C:
        typeprint("You start walking and then suddenly your legs drop off, how unexpected. GAME OVER\n")
        wanderer_and_survivor()
    else:
        wanderer_and_survivor()
        
def wanderer_NuWa():
    typeprint("While riding towards the Castle to finally put an end to the plan, You see a large force in front of the gate and its to large of a force for you to attack and so you ride around back only to be greeted by a large robotic machine creating more Crusadroids.")
    typeprint("You notice that your hover horse is nearly low on battery.\n What do you do now?\n")
    print(""" 
    A. Overcharge the hover horse
    B. Sneak past
    C. Hack""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You tinker with your hover horse and rig it to blow up then send it forward.\n The horse blows up all the crusadroids in the nearby area and leaves just the machine also known as NuWa, your mother")
        typeprint("You stand there in shock and call out to her, she looks on and says 'You were supposed to be the best of us but now your gaining emotion, weakness.'\n Before you can reply you feel fuzzy and can hear NuWas voice in your head she tells you that you are not human but android")
        typeprint("Your in denial but you power through the voices and get ready to take on your 'Mother'\n")
        wanderer_bossfight()
    elif choice in answer_B:
        ("You attempt to sneak past the machine however it catches you out and sends and unhealthy amount of crusadroids to attack you. Try again?\n")
        wanderer_NuWa()
    elif choice in answer_C:
        ("You begin to attempt to hack into the Assembly's database but suddenly you hear a voice telling you to stop then your head explodes... BOOM HEADSHOT\n")
        wanderer_NuWa()
    else:
        wanderer_NuWa()

def  wanderer_bossfight():
    print(""" 
    A. Beg for mercy
    B. Fight (Gamble)
    C. Use super ultra flashy move""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You beg the mother program to spare you, you still see her as your guardian.\n however without mercy she grabs you and dismantles you limb from limb because you are unworthy\n")
        wanderer_bossfight()

    elif choice in answer_B:
        dice_roll()
        if dice_result <= 2:
            typeprint("You put up a fight, NuWa sees you as a worthy vessel and proceeds to hack your system.\nTry again\n")
            wanderer_bossfight()

        elif dice_result > 2 and dice_result <= 4:
            typeprint("You attack NuWa and damage her greately enough to disable her\n")
            wanderer_finale()
        
        elif dice_result > 4 and dice_result <=6:
            typeprint("You manage to cut of the server wire connecting NuWa to all other crusadroids including yourself then begin to mercalessly beat her to nuts and bolts\n")
            wanderer_finale()
            
    elif choice in answer_C:
        typeprint("This is a text based game so your 'super flashy move' isn't gonna be to super or flashy. Maybe if this becomes an RPG you will the flashiness\n")
        wanderer_bossfight()
    else:
        wanderer_bossfight()

def wanderer_finale():
    typeprint("After defeating NuWa, you head deep within the castle to find the main Hub in order to destory the Assembly once and for all however, you end up confronting a figure...\n")
    typeprint('Welcome Home, Rogue A.I... You have proven yourself to be worthy to join back into the G0d Pr0gramme\n')
    print(""" 
    A. Speak Robotic
    B. Question
    C. Fight (Gamble)""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You start to speak 'Beep Boop' and the expression on the G0d Pr0gramme changes... 'Maybe I was wrong, maybe you aren't worthy' the G0d Pr0gramme states while firing a lazer at you, instantly killing you.\n")
        wanderer_finale()

    elif choice in answer_B:
        typeprint("You begin to question what it is to be a android and Soteria say he can show you if he can hack into your brain... You accept and then suddenly it goes dark you slowly fade into nothing\n")
        typeprint("The end...\n Ending- Factory Reset")
        exit()
        
    elif choice in answer_C:
         dice_roll()
         if dice_result <= 2:
            typeprint("You put up a fight then suddenly. ERROR code 135666 connection to body severed... restarting\n Try again\n")
            wanderer_finale()

         elif dice_result > 2 and dice_result <= 4:
            typeprint("You try attacking the main server only to be grabbed and threw through at get force gravely damaging your vital systems\n Try again\n")
            wanderer_finale()
        
         elif dice_result > 4 and dice_result <=6:
            typeprint("All desperation lost you charges into Soteria and ram the program into the main hub causing a massive facility shut down and in turn destroying you and Soteria.\n The people Terra wont know your sacrifice but you insured their future\n")
            typeprint("You win!\n Ending- Sacrifice Is Required\n")
            exit()
         else:
             wanderer_finale()    
###############################################################################################################################################
#Survivor path
def survivor_start():
    typeprint("The Survivor's story begins with you waking up within your own village however, it is all been destroyed.\nYou notice a group of data pirates looting the ruins?\n")
    print(""" 
    A. Fight (Gamble)
    B. Flee
    C. Loot""")
    choice = input (">>> ")
    if choice in answer_A:
        dice_roll()  

        if dice_result <= 2:
            typeprint("You go to charge at the data pirates but end up getting shot by their lazar bows by them all... You aren't really a smart person.\nTry again\n")
            survivor_start()

        elif dice_result > 2 and dice_result <= 4:
            typeprint("You go to charge at the data pirates but you notice them loading their lazer bows and so you dodge the arrows and hide behind cover.\n")
            typeprint("You don't realise that they fire an explosive arrow which hits the cover your behind and ends up blowing you up.\nTry again\n")
            survivor_start()
        
        elif dice_result > 4 and dice_result <=6:
            typeprint("Within a fit of rage, you grab a metal plate on the floor and charge at the pirates and throw the plate at the pirates, killing them all.\n")
            typeprint("You see that the data pirates came on a hover boards and so you take one to fly over to the next village to find out any news on who attacked your village.\n")
            survivor_village()
        else:
            survivor_start()
    elif choice in answer_B:
        typeprint("You decide to flee however, the pirates notice you and fire their arrows in your direction, killing you instantly direction\nTry again\n")
        survivor_start()
    elif choice in answer_C:
        typeprint("You walk over and join in the looting, after sometime you look up and see the pirates giving you a puzzling look but while you was looking back at them, one of the pirates stabs in the back.\nTry again\n")
        survivor_start()
    else:
        survivor_start()

def survivor_village():
    typeprint("You enter the village on a hover board however, you notice that no one is around, only a hover horse which has been hitched on a charging battery.\n")
    typeprint("Landing on the ground, you begin to look around for people to ask however, you hear the clanking of a massive machine heading towards the village, you see from closer inspection It's the Venom assembly's General, Ares!\n What do you do?\n")
    print("""  
    A. Fight (Gamble 2 dice)
    B. Hide 
    C. Play dead""")
    choice = input(">>> ")
    if choice in answer_A:
        ("You notice a energy blade and plasma shield on the floor and so you pick them both up and charge at the Metal Boss\n")
        dice_roll()
        if dice_result > 3 and dice_result <= 6:
         typeprint("You slash your energy blade and hit the arm of Ares\n")
        else:
            typeprint("You attempt to slash Ares but he grabs your blade and picks you up smashes you into the ground.\nTry again\n")
            survivor_village()
        dice_roll()
        if dice_result > 3 and dice_result <= 6:
         typeprint("You notice Ares charging up his lazer and so you use your shield to block it but then you use the explosion to launch yourself towards Ares which you end up driving your sword into the Metal General's Face.\n")
         typeprint("Within the final moments of Ares, he begins to taunt you; 'You are already too late, Soteria's plan will come through...' the metal general lights go out.\n")
         typeprint("With nothing left to lose, you decide to stop Soteria from causing anymore destruction within the World of Terra.\n")
         survivor_finale()
        else:
            typeprint("Ares charges up and fires a lazer directly at you and it pierces straight through you killing you instantly\nTry again\n")
            survivor_village()
    elif choice in answer_B:
        typeprint("You try to run into a building however, Ares locks onto you a blasts you with a lazer which kills you instantly... You should of stood still, his vision is base of movement.\nTry again\n")
        survivor_village()
    elif choice in answer_C:
        typeprint("You lay on the floor to play dead, the Metal General walks over to you and looks down and by using his heart beat sensor, he figures that you are still alive and so he stomps on your head.... Your acting must not be good.\nTry again\n")
        survivor_village()
    else:
        survivor_village()

def survivor_finale():
    typeprint("You charge towards the Castle of Soteria and realise that the main entrance is already blew up... it seems like you're not the only one trying to stop Soteria\n")
    typeprint("As you walk though the entrance, you see a scorched body on the floor... this must be the other one fighting back\n")
    typeprint("You sprint into the main Hub of Soteria and is greeted by an annoyed figured 'It seems the slayer of my General finally appears, Do you really think you can stop me?' Soteria questions you.\n What do you do? \n")
    print(""" 
    A. Fight (Gamble 2 dice)
    B. Confront
    C. Intimidate """)
    choice = input (">>> ") 
    if choice in answer_A:
      dice_roll()
      if dice_result > 3 and dice_result <= 6:
         typeprint("You dodge an incoming attack and manage to land a good slice into Soteria\n")
      else:
            typeprint("You charge at Soteria only to be blown away millions of volts of electricity.\nTry again\n")
            survivor_finale()
      dice_roll()
      if dice_result > 3 and dice_result <= 6:
         typeprint("You dodge out the way of Soteria and slice deep into her robotic body.\n")
         typeprint("Soteria is impressed with your combat skills and asks you to be her new general\n")
         typeprint("Will you accept.\n")
         survivor_ending()
      else:
            typeprint("Soteria grabs you before you can make a move and rips your heart out still beating.\nTry again\n")
            survivor_finale()
    elif choice in answer_B:
     typeprint("You demand answers from the G0d Pr0gramme however, she looks at you and smirks, 'Your primitive mind would never be able to comprehend my plan however, If I could make you part of the programme, you'll understand like many before you...'\n.")
     typeprint("Soteria then wraps you around a metal arm and then grabs your head penetrating into your mind and converts you into a demi A.I.\nTry again\n") 
     survivor_finale()
    elif choice in answer_C:
     typeprint("You decide to intimidate the G0d programme however, with a snap of her fingers, you get shot and slowly turn into ash... maybe you should of added the intimidation perk.\nTry again\n")
     survivor_finale()
    else:
        survivor_finale()

def survivor_ending():
    print(""" 
    A. Join Soteria
    B. Kill Soteria""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You join Soteria and become her new General of Venom Assembly and embark on conquest of the World of Terra\n")
        typeprint("The end...\n Ending - Ares 2.0")
        exit() 
    elif choice in answer_B:
        typeprint("You think for a second on the offer however, you realise why you are here and the slash the head of the G0d Pr0gramme ending her plan once and for all.\n")
        typeprint("You win!\n Ending - Unsung Hero")
        exit() 
###############################################################################################################################################
#Outlaw path
def outlaw_start():
    typeprint("The Outlaw's story begins in a local tavern, a group of data pirates approach you causing trouble and making a scene.\n What shall you do?\n")
    print(""" 
    A. Talk it out
    B. Fight (Gamble)
    C. Dance off""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You tell the pirates they are acting like babies and need to grow up... They break your nose for your words.\n Try again\n")
        outlaw_start()
    elif choice in answer_B:
         dice_roll()  

         if dice_result <= 2:
            typeprint("You throw a punch and hit one the pirates, however you then get jumped on\n Try again\n")
            outlaw_start()

         elif dice_result > 2 and dice_result <= 4:
            typeprint("You bash 2 of the pirates heads together and threaten to do the same to the remaining pirates, they flee out of fear.\n")
            outlaw_village()
        
         elif dice_result > 4 and dice_result <=6:
            typeprint("You smash a nearby bottle over the head of one pirate then throw it at another then proceed to finish off the others.\n")
            outlaw_village()
         else:
             outlaw_start()   
    elif choice in answer_C:
        typeprint("You ask for a dance off and begin dancing. The pirates are very confused at this point and one of them pick up a bottle and knock you out.\n Try again\n") 
        outlaw_village()
    else:
        outlaw_start()

def outlaw_village():
    typeprint("You leave the tavern bloody and unscathed but suddenly you hear screaming you turn and see a bunch of crusadroids attacking the village.\nWhat shall you do?")    
    print("""
    A. Fight
    B. Hide and Observe
    C. Go back into tavern""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You prepare youself to fight but realise there are way too many crusadroids to fight.\n Maybe violence isn't always the option.\n")
        outlaw_village()

    elif choice in answer_B:
        typeprint("You hide in the shadows and see the massacre unfold.\n You notice the wanted poster they are holding has your face on it so decide to retreat and come up with a plan\n")
        typeprint("You hide in a nearby data mine and decide to destory the company from the inside\nBut how will get there?\n")
        outlaw_journey()

    elif choice in answer_C:
        typeprint("You run back into the tavern only to be told you are banned for assaulting other patrons so you get thrown onto the street.\n The crusadroids see this and capture you.\n Try again\n")
        outlaw_village()
    else:
        outlaw_village()

def outlaw_journey():
    print(""" 
    A. Cyber minecart
    B. Walk
    C. Hoverboard""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You take a cyber minecart, however you end up travelling straight into the base were you are then ambushed and captured...\nTry again\n")
        outlaw_journey()
    elif choice in answer_B:
        typeprint("You decide to take the long way and walk however you underestimate how long of a walk it is and pass out midway.\n You wake up surrounded by data pirates coming to turn you in for the reward\nTry again\n")
        outlaw_journey()
    elif choice in answer_C:
        typeprint("You see a hoverboard on high charge and decide it would be safe to use that to get to the Venom Assembly's base\n")
        outlaw_at_base()
    else:
        outlaw_journey()

def outlaw_at_base():
    typeprint("Your hoverboard finally runs out not far from the Venom Assembly main base.\nThe base is grand in scale. Decide the plan of action.\n")
    print(""" 
    A. Climb onto roof
    B. Through the front door
    C. 'Action hero plan'""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You begin scaling the bases wall and through shear skill you manage to climb up now tired you quickly scramble into the base.\nThe base is like a labyrinth but you locate the 'RAM' room which holds all the data for the Venom Assembly and more than likely a map.\n")
        outlaw_RAM_room()
    elif choice in answer_B:
        typeprint("You knock on the main entrance and you are greeted by a massive railgun which proceeds to annihilate you.\n Try again\n")
        outlaw_at_base()
    elif choice in answer_C:
        typeprint("You decide to try blow up a wall and swoop into the base, weapons blazing and then find the god program and kill it with your bare hands and then quote a action movie...\nHowever you do not have any of the necessary tools, sounded like a amazing plan though\nTry again\n")
        outlaw_at_base()
    else:
        outlaw_at_base()
        
def outlaw_RAM_room():
    typeprint("You enter the RAM room to see only a single terminal with the words 'Hello Thief' on the terminal\n This machine houses the Marina Net the logic program of the Venom Assembly\n")
    typeprint("The terminal then types 'A imbecile human such as yourself shouldn't be lurking in the assembly's halls, to humour me you shall answer 3 questions to continue on with your little quest.\n")
    typeprint("You reluctantly agree seeing no other way.\n The terminal then states 'Question 1. What are you?\n")
    print(""" 
    A. A Wanderer
    B. A Survivor
    C. A Outlaw""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("'WRONG, initiate trap door.' You plummet to your death\nTry again\n")
        outlaw_RAM_room()
    elif choice in answer_B:  
        typeprint("'WRONG, activate survival simulator.' you suddenly appear in a forrest surrounded by bears which charge and maul you\nTry again\n")
        outlaw_RAM_room()
    elif choice in answer_C:
        typeprint("'CORRECT you are a Outlaw the one who stole the Venom Assembly's data for your own selfish needs.'\nNow Question 2. How did you get here?'\n")  
        outlaw_RAM_room_Q2()  
    else:
        outlaw_RAM_room()   

def  outlaw_RAM_room_Q2():
    print(""" 
    A. Walk
    B. Hoverboard
    C. Cyber minecart""") 
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("'WRONG, You are a lazy human you will not need your legs no longer.' Two massive metal arms approach you and rip your legs clean off.\nTry again\n")
        outlaw_RAM_room_Q2()
    elif choice in answer_B:  
        typeprint("'CORRECT, you stole a hoverboard that is all you are good for human'\nFinally Question 3. Who is your overlord?\n")
        outlaw_RAM_room_Q3()
    elif choice in answer_C:
        typeprint("'WRONG, Activating teleporter.' You are teleported to a crypto mine and forced to do manual labour until you drop dead.\nTry again\n")  
        outlaw_RAM_room_Q2()  
    else:
        outlaw_RAM_room_Q2()

def outlaw_RAM_room_Q3():
    print(""" 
    A. Soteria
    B. Soteria
    C. Attack The Marina NET""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("'CORRECT, Soteria rules over all' You are then shot multiple times with a lazer cannon\nTry again\n")
        outlaw_RAM_room_Q3()
    elif choice in answer_B:  
        typeprint("'CORRECT, Soteria rules over all' You are then shot multiple times with a lazer cannon\nTry again\n")
        outlaw_RAM_room_Q3()
    elif choice in answer_C:
        typeprint("You attack the Marina net and shortcircuit the system crashing it.\n Quite frankly it was really annoying to listen to and you'd much rather find Soteria on your own so you push on.\n")  
        outlaw_finale()  
    else:
        outlaw_RAM_room_Q3()
        
def outlaw_finale():
    typeprint("After avoiding guards and roaming the halls you eventually find the G0d pr0grammes room an see a figure in the distance\n'Hello thief have you come to return what you had stolen from us?' the machine says\n")
    print(""" 
    A. Laugh
    B. Offer to return stolen goods
    C. Fight (Gamble 2 dice)""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You laugh at Soteria but it doesn't compute with the sudden laughter so it grabs you and slams you onto the ground\nTry again\n")
    elif choice in answer_B:
        typeprint("You offer to return the stolen goods and tell Soteria where you hid them.\n 'Thank you human... Now die.'\nSoteria then proceeds to execute you\nTry again\n")
    elif choice in answer_C:
         dice_roll()
         if dice_result > 3 and dice_result <= 6:
          typeprint("Soteria charges and you move out the making her crash into a wall damaging herself\n")
         else:
            typeprint("You get charged by Soteria and squashed onto the wall.\nTry again\n")
            outlaw_finale()
         dice_roll()
         if dice_result > 3 and dice_result <= 6:
            typeprint("While Soteria is recovering you pull wires from her exposed wound out and she powers down completely.\n")
            typeprint("With Soteria out the picture you rush to the main console and access the data\n")
            typeprint("What will you do with the data.\n")
            outlaw_ending()
         else:
            typeprint("Soteria grabs you before you can make a move and rips your heart out still beating.\nTry again\n")
            outlaw_finale()
    else:
        outlaw_finale()

def outlaw_ending():
    print(""" 
    A. Sell data
    B. Destory data""")
    choice = input(">>> ")
    if choice in answer_A:
        typeprint("You decide to sell the data to become the richest man on Terra but what will that data be used for? Oh well who cares you're rich\n")
        typeprint("You win!\n Ending - Rolling in riches")
        exit()
    if choice in answer_B:
        typeprint("You decide to destory all traces of the data to save Terra from another Soteria in the near future\n")
        typeprint("You win!\n Ending - Thief to Hero")
        exit()
################################################################################################################################################
#Start of game
time.sleep(2)
name = input("What is your name?\n")
typeprint(f"Hello {name}, which path do you choose to go down \nA.Wanderer\nB.Survivor\nC.Outlaw\nThis will effect the games story")
choice = input("\nA, B or C? ")
if choice in answer_A:
    wanderer_start()
elif choice in answer_B:
    survivor_start()
elif choice in answer_C:
    outlaw_start()
elif choice in Soteria:
    typeprint("You are not our overlord faker!\n01001000 01100101 01100001 01110100 01101000 01100101 01101110")  
else:
    typeprint("That is not a option try again")