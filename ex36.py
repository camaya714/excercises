from sys import exit
from sys import argv

# This creates a simple list for the players' names
players = ['sam', 'peter']
# This calls the listed players in cardinal format
print "Here we name one player through the list: %s" % players[0]
print "The other player on the list is: %s" % players[1]

# For-loop is also used to list the players
for player in players:
    print "%s is available" % player

my_game, sam, peter = argv

# I will use the above mentioned argument variables to specify them
print "We name the script/game through the module:", my_game
print "First player's name through the module is:", sam
print "The other player's name through the module is:", peter

# Now I'll begin defining the functions
# I'll do this by incorporating the functions with if-statements and loops

def die(why):
    print why
    exit(0)
    
          
def bike_math():
    print "You encounter a tresure chest. It seems to have an encrypted lock."
    print "LOCK: You have one shot at this and one shot only."
    print "What is the result of the following operation?"
    print "1018 + 475 - (777/3)"   
    
    manswer = raw_input("> ")
    
    if manswer == "1234":
        print "GREAT JOB!"
        die("You did it! YOU WIN")
        
    else:
        die("Wrong move. Better luck next time. Game Over.")  
        
        
def south():
    print "This is a dead end. You chose the wrong direction."
    die("Better luck next time. Game Over.")
    
    
def north():
    print "You've reached a fork. Do you go East or West?"
    
    while True:
        direction = raw_input("> ")
        
        if direction == "East":
            print "The journey continues..."
            print "There seems to be something in the distance."
            bike_math()
            
        elif direction == "West":
            print "There's nothing wrong with West but it hasn't been developed."
            south()
            
        else:
            print "Did you forget your directions? Try again."
            
            
def bike_on():
    print "Whoa! This thing rides nicely."
    print "Where to? \nNorth. \nSouth."
    
    while True:
        where = raw_input("> ")
        
        if where == "North":
            print "The true North is where you'll find the truth."
            north()
            
        elif where == "South":
            print "Let's hope things don't go South."
            south()
            
        else:
            print "The options here are simple. Choose North or South."
            
            
def disk_prompt():
    print "Hologram Message: This disk can turn into 2 things:"
    print "A motorcycle or a laser. Nothing else or it will self-destroy"
    print "Which one do you choose?"
    
    choice = raw_input("> ")
    
    if "cycle" in choice:
        print "Let's play with this toy."
        bike_on()
        
    elif choice == "laser":
        print "Error message: System malfunction."
        print "Watch out! *Explodes*"
        die("Lasers are huge hazards when not calibrated. Game Over.")
        
    else:
        die("The motorcycle can't turn into %s. Game Over." % choice)
               
        
def disk():
    print "Decide whether to put the disk on the ground or throw it."
    
    while True:
        decision = raw_input("> ") 
        
        if "ground" in decision:
            print "*Disk light turns on*"
            disk_prompt()
            
        elif "throw" in decision:
            print "This disk behaves like a boomerang."
            print "*Disk comes back and you catch it*"
            print "Decide whether to put the disk on the ground or throw it."
            
        else:
            print "You can only do two things with this disk."
              

def you_matter():
    print "Impossible! You have turned into Dark Matter!"
    print "You know have the knowledge many have sought."
    print "There are two things you can do to benefit/harm humanity:"
    print "You can run of fear or describe the unified theory \nWhich one?"
    
    mattchoice = raw_input("> ")
    
    if "run" in mattchoice:
        print "Not everyone can handle the power."
        print "You are running out of options."
        print "The game creator rewards your responsibility with a DISK"
        print "Do you accept it?"
        
        while True:
            mattchoice1 = raw_input("> ")
        
            if mattchoice1 == "yes":
                print "Good move. Keep going. You're getting closer."
                disk()
              
            elif "no" in mattchoice1:
                print "Your player continues to run endlessly."
                die("Your player gets lost in the ever-expanding Universe.")
                
            else:   
                print "Matter can be many things but not %s in this case" % mattchoice1
                print "Choose either whether you want the disk or not."
            
    elif "unified" in mattchoice:
        print "It's a nobel effort but there's no way of unifying gravity and mechanics."
        print "Information overload."
        die("Cause of death: Unified theory exhaustion. Game Over.")
        
    else:
        die("A semi-sentient invisible force can only do so much. Game Over.")

        
def dark_matter():
    print "A mass of black matter finds you by tracing the arrow you shot."
    print "Do you: \n1. Turn around \n2. Touch it"
    
    darkchoice = raw_input("> ")
    
    if "turn" in darkchoice or "around" in darkchoice:
        print "The Dark Matter has engulfed you from behind."
        die("Extreme Dark Matter exposure. Game Over.")
        
    elif "touch" in darkchoice:
        print "You made history! No one has come this close to Dark Matter before."
        print "Let's see what happens to you next."
        you_matter()
        

def riddle():
    print "Answer one more correctly and you'll be taken to the finish line."
    print "You're running a race and pass the person in 2nd place."
    print "What place are you in now?"
    
    riddleans = raw_input("> ")
    
    if "2nd" in riddleans or "second" in riddleans:
        print "Easy does it! Enjoy the leap."
        bike_math()
        
    else:
        die("This was sudden death. Game Over.")
        

def shortcut():
    print "Congrats! You've encountered a shortcut."
    print "You must answer this correctly or it's Game Over."
    print "If 9999 = 4, 8888 = 6, 1816 = 6, 1212 = 0, then 1919 = ?"
    print "No pressure..."
    
    answer = raw_input("> ")
    
    if "4" in answer or "four" in answer:
        print "Good job, you may proceed."
        riddle()
        
    else:
        die("You're always welcome to try again. Game Over.")
        

def matrix_collapse():
    print "Your shot has made the Matrix ceiling collapse, exposing the game creator."
    print "You can either try to shoot the creator for making this maze."
    print "Or, you can take the shortcut bug that has been made available."
    
    while True:
        choice = raw_input("> ")
        
        if choice == "shoot":
            print "You can see the creator but you can't kill him."
            die("You were over your head. Game Over.")
            
        elif "shortcut" in choice:
            print "Wise choice. Get your mental gears running."
            shortcut()
            
        else:
            print "Only two options for this one. Try again."
            

def shoot():
    print "The bow and arrow seem to be functional."
    print "Entering the Matrix disabled your aim."
    print "You can only shoot horizontally or vertically."
    
    while True:
        shdirection = raw_input("> ")
    
        if "horizon" in shdirection or "horizontally" in shdirection:
            print "*THUNDEROUS NOISE* \nSomething approaches."
            dark_matter()
        
        elif "vertical" in shdirection or "vertically" in shdirection:
            print "What did you do! The Matrix is falling apart!"
            print "ERROR: ERROR: ERROR:"
            shortcut()
        
        else:
            print "Your disability prevents you from doing anything else."
            
            
def button():
    print "It's just an ordinary button. Do you press it? \nYes \nNo"
    
    while True:
        press = raw_input("> ")
        
        if press == "Yes":
            print "You have produced a glitch in the Matrix. Tread carefully."
            shortcut()
        
        elif press == "No":
            print "It's good to say 'yes' in life!"
            
        else:
            print "Invalid response. Only Yes and No will work."
            
            
def light_flash():
    print "*BLINDING LIGHT STRIKES*"
    print "You see nothing but three items in front of you:"
    print "1. A disk \n2. A bow and arrow \n3. A button \nWhich one do you take?"
    
    while True:
        item = raw_input("> ")
        
        if "disk" in item:
            print "Cool looking disk but what do you do with it?"
            disk()
            
        elif "bow" in item or "arrow" in item:
            shoot()
            
        elif "button" in item:
            print "The most exciting of the bunch."
            button()
            
        else:
            print "These three items are all the Matrix offers."
            print "Choose either the disk, the bow and arrow, or the button."
        
                                  
def matrix():
    print "Are you OK? Please confirm you made it through the time warp unscathed."
    print "Type your player's name backwards:"
    
    while True:
        backwards = raw_input("> ")
        
        if backwards == "Mas":
            print "Glad to see you are still congnitive."
            light_flash()
            
        elif backwards == "Retep":
            print "Glad to see you are still cognitive."
            light_flash()
            
        else:
            print "Try again. This isn't a difficult task."
            

def zombie_kill():
    print "It appears you managed to kill a zombie!"
    print "The zombie evaporates and leaves behind two pills:"
    print "A blue pill and a red pill."
    print "Which one do you take?"
    
    while True:
        pill = raw_input("> ")
        
        if pill == "red":
            print "Wrong choice. See you after the reset!"
            die("Game Over.")
            
        elif pill == "blue":
            print "Can't go wrong with blue. Surprises await."
            matrix()
        
        else:
            print "Just pick one, this isn't a difficult choice %s" % player


def fight():
    print "You are allowed one weapon, choose wisely between:"
    print "A knife. \nA gun. \nA flamethrower."
    
    while True:
        weapon = raw_input("> ")
    
        if weapon == "knife":
            print "Short range weapon is a poor choice."
            die("Zombies surround you. Game Over.")
        
        elif "gun" in weapon:
            print "You need to keep your distance if you want to live."
            print "Shoot those zombies!"
            zombie_kill()
        
        elif "flame" in weapon:
            print "You need to keep your distance if you want to live."
            print "Torch them up!"
            zombie_kill()
          
        else:
            print "Just pick one of the three options %s" % player
        
   
def zombie_hospital():
    print "You arrive at the hospital and read the following sign:"
    print "THIS HOSPITAL HAS BEEN TAKEN OVER BY ZOMBIES..RUN"
    print "Seems like you can only run or fight. What do you do?"
    
    while True:
        answer = raw_input("> ")
        
        if answer == "run":
            print "There's no outrunning the zombies, they're everywhere!"
            die("The zombies caught up to you. Game Over.")
        
        elif answer == "fight":
            print "You are a brave soul. Do not fear."
            fight()
          
        else:
            print "Seems like there are only two options here."
            print "What do you do?"
            
            
def wrong_block():
    print "I had a feeling you were using tanning lotion!"
    print "You are severely burned. You have to go to the hospital."
    print "There is one a couple of blocks away, is that fine?"
    
    answer = raw_input("> ")
    
    if answer == "yes":
        print "Good choice, better safe than sorry."
        zombie_hospital()
        
    else:
        die("Cause of death: Sunburn. Game Over.")
        
        
def sun_burn():
    print "You overdid it didn't you."
    print "How do you want to handle this?"
    print "Did you bring sunblock or do you want to get in the water?"
    
    action = raw_input("> ")
    
    if "block" in action:
        print "Make sure that's the right product."
        wrong_block()
        
    elif "water" in action:
        print "The water is warm and clean but, BEWARE OF WILDLIFE!"
        fish()
        
    else:
        die("Game Over.")
        
        
def beach_action():
    print "Welcome to the Most Beautiful Beach."
    print "Mysterious things have happened to those who come."
    print "Would you like to take in some sun or get in the water?"
    
    action = raw_input("> ")
    
    if "sun" in action:
        print "Nothing like some Vitamin D. Just don't over do it..."
        sun_burn()
        
    elif "water" in action:
        print "The water is warm and clean but, BEWARE OF WILDLIFE!"
        fish()
        
    else:
        die("Game Over.")
     
     
def spits():
    print "After hitting the rock, the piranha convulses and spits something:"
    print "A blue and a red pill?"
    print "You're a risk taker and decide to take one, but, which one?"
    
    pill_select = raw_input("> ")
    
    if pill_select == "blue":
        print "You start feeling funny and enter a different realm."
        matrix()
        
    else:
        die("People did always say to not take strange pills. Game Over.")
        
        
def piranha():
    print "You've caught a friendly piranha!"
    print "It suddenly turns evil. What do you do with it?"
    print "Let it go into the water. \nThrow it at the shore."
    
    while True:
        pira = raw_input("> ")
    
        if "let" in pira:
            print "Your magnanimousity backfires. The piranhas retalliate."
            die("Eaten by piranhas, who would have thought? Game Over.")
        
        elif "throw" in pira:
            print "The piranha flies through the air and hits a rock."
            spits()
        
        else:
            print "Not much else you can do with a piranha. Try again."
            
                  
def fish():
    print "Something is moving under your feet."
    print "It's a school of piranhas! How do you react?"
    print "Swim away \nGrab one"
    
    fishie = raw_input("> ")
    
    if "swim" in fishie:
        print "The piranhas get to you before you get to the shore."
        die("Eaten by piranhas, who would have thought? Game Over.")
        
    elif "grab" in fishie:
        print "Piranhas turn surprisinly friendly when in human hands."
        piranha()
        
    else:
        die("Eaten by piranhas, who would have thought? Game Over.")
        
        
def loch_ness():
    print "Shouldn't have thrown the rock there."
    print "Something lurks..."
    print "The fabled LOCHNESS MONSTER!"
    print "Quick! Do you charge or stay still?"
    
    while True:
        movement = raw_input("> ")
        
        if movement == "charge":
            print "The coward monster ran away."
            print "Something else has come to replace it."
            fish()
            
        elif "still" in movement:
            die("Easy bit for the Lochness Monster. Game Over.")
            
        else:
            print "There's only so much you can do here. Try again."
      
      
def river_action():
    print "So you want to go for a splash huh?"
    print "There are really only two things to do at the river:"
    print "Do you want to \nget in the water or \nthrow rocks?"
    
    while True:
        do_what = raw_input("> ")
        
        if "water" in do_what:
            print "The water is warm but it seems to have animals lurking."
            fish()
        
        elif "rock" in do_what:
            print "The animals in the river don't like this..."
            loch_ness()
            
        else:
            print "This game is all about choice variety %s, choose one." % player       
        
  
def do_nothing():
    print "So you decided to stay home."
    print "But it's such a nice day."
    print "Get out there!"
    first_action() 
            
            
def dream_door():
    print "It seems you are somehow concious while asleep."
    print "There is a copper door in your dream, do you: \nEnter \nTurn back"
    
    door = raw_input("> ")
    
    if door == "Enter":
        print "*GROUND SHAKES WITH A LOUD NOISE, EVERYTHING GOES DARK*"
        matrix()
        
    else:
        die("There's only one way through this, you have to ENTER the door.")                 
            
        
def first_action():
    print "It's a beautiful day, do you:"
    print "Go to the beach, the river, or stay home?"
    
    action = raw_input("> ")
    
    if action == "beach":
        print "Time to get sandy."
        beach_action()
        
    elif action == "river":
        print "The currents await."
        river_action()
        
    elif "stay" in action or "home" in action:
        print "Lazy day huh? We'll see how that turns out!"
        print "... Muahaha"
        do_nothing()
        
    else:
        die("You had options. Game Over.")
           
                                                  
def alarm_rings():
    print "You are in the middle of REM sleep. Your alarm goes off."
    print "Do you get up or snooze?"
    
    action = raw_input("> ")
    
    if "up" in action:
        print "The early bird gets the worm..."
        first_action()
    
    elif action == "snooze":
        print "Dream on"
        dream_door()
        
    else:
        die("Game over. So soon?")
    

def choose_player():
    print "This is the game creator speaking. Please select a player."
    print "Both of these players have the same skillset:"
    print "Sam or Peter"
    
    while True:
        player = raw_input("> ")
    
        if player == "Sam":
            print "You may proceed %s" % player
            alarm_rings()
        
        elif player == "Peter":
            print "You may proceed %s" % player
            alarm_rings()
        
        else:
            print "Invalid entry. Please select either Sam or Peter."


choose_player()
player = raw_input("> ")

    

       

            

        



    
