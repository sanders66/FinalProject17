from sys import exit
#Used to exit the game when you either drop out or reach 0 life points

class Student(object):
#This is the main class in which the user will work. It creates the average student in MHS
    def __init__(self):
    #you start with 100 life points
        self.life_points = 100

#Drop out function to be used throughout the game in between grades
#Essentially lets you quit the game
    def drop_out(self):
        print("You leave the school and go to your town high school")
        print("The rest is up to you...")
        print("Game Over")
        exit()

#Dead function for when lifepoints reach 0. You lose the game
    def dead(self):
        print("You fail school and are forced to drop out, leaving you in an extreme state of depression.")
        print("You end up working at Walmart for the rest of your life.")
        print("You also live with your mother.")
        print("Rip")
        print("Game Over")

    #Freshman Year Situations

    def freshman_1(self):
        print("Congratulations! You have been selected by Magnet High School to be a student in the Class of 2019!")
        print("You are given 100 life points. Now try to get through high school without losing them!")
        print("Enough of that though...")
        print("You're a freshman, you need new clothes, new stuff... You need a backpack!")
        print("Mom takes you to the store and a rolly backpack is on sale!")
        print("Do you buy it?")
        print(" ")

        decision = input("> ")
        #Takes an input from the user
        #User has to put yes or no

        if "yes" in decision:
            loss = 10
            print("You buy the backpack. First day of school 7 people trip on it and one of them gets a concussion. Not good...")
            print(f"You now only have {self.life_points - loss} points left")
            print(" ")

        elif "no" in decision:
            loss = 0
            print("Smart choice. You spare people of broken ankles. You buy a different backpack but no one cares because it's just a backpack.")
            print(f"You have {self.life_points - loss} life points")
            print(" ")

        else:
            loss = 0
            print("please enter a valid input")
            print("...")
            print("REFRESHING SITUATION")
            print("...")
            s.freshman_1()

        self.life_points -= loss
        #Updates your life point total after each function

    #Freshman Year Decisions Part 2

    def freshman_2(self):
        print("Alright...")
        print("You're sitting in the front row of your bio class...")
        print("But you didn't get much sleep last night..")
        print("It's first period and you're tired...")
        print("Do you sleep?")
        print(" ")

        decision = input("> ")

        if "yes" in decision:
            loss = -5
            print("You take a nap and your teacher doesn't notice. Good job")
            print(f"You have {self.life_points - loss} life points")
            print(" ")

        elif "no" in decision:
            loss = 10
            print("Your teacher wouldn't have noticed...")
            print("You just lost valuable sleep!")
            print(f"You have {self.life_points - loss} life points")
            print(" ")

        else:
            loss = 0
            print("please enter a valid input")
            print("...")
            print("REFRESHING SITUATION")
            print("...")
            s.freshman_2()

        self.life_points -= loss

    def freshman_3(self):
        print("Okay this one is simple...")
        print("It's freshman year finals!")
        print("You either study hard, cram during the period before each test, or go home and watch netflix")
        print("What's your choice?")
        print(" ")

        decision = input("> ")

        if "study" in decision:
            loss = -10
            print("Wow you're pretty responsible!")
            print("You're building some good habits")
            print(f"You have {self.life_points - loss} life points now")
            print("Good work")
            print(" ")

        elif "cram" in decision:
            loss = 5
            print("You didn't do too bad...")
            print("But that's not a good habit to have")
            print(f"You have {self.life_points - loss} life points")
            print(" ")

        elif "netflix" or "home" in decision:
            loss = -1
            print("Honestly that's a fair choice")
            print("+1")
            print(f"You have {self.life_points - loss} life points")
            print(" ")

        else:
            loss = 0
            print("please enter a valid input")
            print("...")
            print("REFRESHING SITUATION")
            print("...")
            s.freshman_3()

        self.life_points -= loss

    #Sophomore Year Begins, New set of decisions

    def sophomore_1(self):
        print("Wow.. You made it past freshman year")
        print("That's the easiest part though")
        print("There are more tough decisions to be made!")
        print(" ")
        print("First off...")
        print("You think maybe this school just isn't for you...")
        print("Summit High School is looking kinda nice!")
        print("Do you drop out?")
        print(" ")

        decision = input("> ")

        if "yes" in decision:
            s.drop_out()
            #This lets the user quit the game...

        elif "no" or "stay" in decision:
            print("You stay in Magnet...")
            print("For now at least.")
            print(" ")
            print(" ")
            #No life point loss or gain for this decision

        else:
            print("please enter a valid input")
            print("...")
            print("REFRESHING SITUATION")
            print("...")
            s.sophomore_1()

    #Sophomore Year Part 2

    def sophomore_2(self):
        print("Okay so it's sophomore year now...")
        print("You're in English class and your teacher presents a MEME project")
        print("Wow! A meme project! Something you know all about!")
        print("This should be easy!")
        print("Do you make something that's actually slightly funny, something kind of clever but still pretty trash, or is your sense of humor non-existent")
        print(" ")

        decision = input("> ")

        if "funny" in decision:
            loss = 15
            print("Everyone finds it funny...")
            print("Except... your teacher")
            print("Let's just say... you lost a lot of points on your grade")
            print("It wasn't worth it")
            print(f"You now have {self.life_points - loss} life points")
            print(" ")

        elif "clever" in decision:
            loss = -5
            print("Honestly no one laughs but you get a good grade")
            print("+5")
            print(f"You've got {self.life_points - loss} life points now")
            print(" ")

        elif "sense" in decision:
            loss = 0
            print("You for real?")
            print("...")
            print("Okay")
            print(" ")
            #No penalty because the user is a weirdo

        else:
            loss = 0
            print("please enter a valid input")
            print("...")
            print("REFRESHING SITUATION")
            print("...")
            s.sophomore_2()

        self.life_points -= loss
        #Lifepoint update

    #Sophomore Part 3

    def sophomore_3(self):
        print("Alright...")
        print("Sophomore year continues, but nobody is perfect..")
        print("You're not doing too well in physics and you need that grade boost.")
        print("Do you cheat on your physics test?")
        print(" ")

        decision = input("> ")

        if "yes" in decision:
            loss = 40
            print("Everything goes wrong")
            print("The teacher catches you")
            print("You have to speak to the principal")
            print("Now this is on your record")
            print("However, you do well for the rest of the year, and the failing grade on the test does not affect you too much.")
            print("You somehow survive...")
            print(f"You've got {self.life_points - loss} life points now")
            print(" ")

        elif "no" in decision:
            loss = -5
            print("Phew..")
            print("You dodge a bullet!")
            print("Your teacher would have definitely caught you...")
            print("That would not have been good.")
            print(f"You've got {self.life_points - loss} life points now")
            print(" ")

        else:
            loss = 0
            print("please enter a valid input")
            print("...")
            print("REFRESHING SITUATION")
            print("...")
            s.sophomore_3()

        self.life_points -= loss

    #Sophomore Year ends and Junior year begins

    def junior_1(self):
        print("Wow... Time really flies.")
        print("You're finally a Junior")
        print("You think you're a big man now.")
        print("However.........")
        print(" ")
        print("Cranford High School is lookin kind of nice")
        print("Do you drop out?")
        print(" ")

        decision = input("> ")

        if "yes" in decision:
            s.drop_out()
            #Essentially quits the game

        if "no" in decision:
            print("Wow, you're quite resilient.")
            print(" ")
            #There is no life point loss here, no need for life point update

    #Junior year part 2

    def junior_2(self):
        print("Alright, enough about dropping out.")
        print("You're positive that you belong in this school.")
        print("First marking period is a big one... You know what that means")
        print("Yes, speakeasy is here.")
        print("You get the group you want, but...")
        print("Do you let your group do all the work, singlehandedly develop Al Capone the musical, work equally, or go on a vacation literally the exact day of speakeasy?")
        print(" ")

        decision = input("> ")

        if "group" in decision:
            loss = 10
            print("Your group does well...")
            print("But during the performance you stumble really hard and cost your group a small deduction.")
            print("Although you look like fool, you don't do too bad grade-wise")
            print(" ")

            self.life_points -= loss

        if "capone" in decision:
            loss = -10
            print("Your group learns their lines effectively.")
            print("You just made possibly the best speakeasy skit in Magnet High School history.")
            print("You might be remembered for this for a long time.")
            print("For about 24 hours, you're a legend, gaining hundreds of views on Snapchat.")
            print(" ")

            self.life_points -= loss

        if "equal" in decision:
            loss = -4
            print("You guys don't do anything amazing but you get a good grade.")
            print("Here, take 4 free points for doing well on a big project")
            print(" ")

            self.life_points -= loss

        if "vacation" in decision:
            loss = 5
            print("wow")
            print(" ")
            print("Your group is annoyed")
            print("Honestly though... can they even blame you")
            print("You don't lose any points because... well... you're on vacation.")
            print("-5 for reputation.")
            print(" ")

            self.life_points -= loss

    #Junior Year part 3

    def junior_3(self):
        print("Another perk of being a Junior is being a part of Mr. Sanservino's class")
        print("Every night, you're supposed to read about 10 pages of the text book.")
        print("He mentions that there may be a pop quiz on the reading during any class.")
        print("Do you read each night?")
        print(" ")

        decision = input("> ")

        if "yes" in decision:
            loss = -5
            print("You read and take notes each night and do fairly well on every quiz")
            print("This leads you to good habits and you do well in his class")
            print(f"You have {self.life_points - loss} life points now.")
            print(" ")

        if "no" in decision:
            loss = 20
            print("You make a grave mistake...")
            print("You manage to get five 0s in one marking period...")
            print("This leads to bad habits and you never recover your grade in his class.")
            print(" ")

        self.life_points -= loss

    #Lifepoint test function
    #Does not need to be used after every function because it is not mathematically possible to lose yet
    def lifepointtest(self):
        if self.life_points > 0:
            print(f"You have {self.life_points} life points now!")
            print(" ")
        else:
            print("YOU HAVE NO LIFE POINTS LEFT!")
            s.dead()
        #This is how the game is lost

    def junior_4(self):
        print("You're usually good with your ID..")
        print("But you seem to have lost it!")
        print("You come into school, get a nice bright, green temporary ID, and sign your name on the LOP sheet.")
        print("Loss of Priviledges are served in AIT during 5th period.")
        print("Do you go and serve your LOP?")
        print(" ")

        decision = input("> ")

        if "yes" in decision:
            print("Wow what a loser")
            print("...")
            print("Just kidding")
            print("You're not getting any points though.")
            print(" ")
            #No loss in life
        if "no" in decision:
            loss = 20
            print("They hunt you down.")
            print("You try to run but you cant.")
            print("You get a central detention.")
            print("Big L")
            print(" ")

        self.life_points -= loss

    def junior_5(self):
        print("Wow, look how far you got!")
        print("In order to complete the game...")
        print("Please download the Senior Year DLC package at the Magnet Island")
        print("Use discount code Merkl for 5% off")
        print(" ")
        print(" ")

#BUY DLC FOR SENIOR YEAR
#THE END

s = Student()
s.freshman_1()
s.freshman_2()
s.freshman_3()
s.sophomore_1()
s.sophomore_2()
s.sophomore_3()
s.junior_1()
s.junior_2()
s.lifepointtest()
s.junior_3()
s.lifepointtest()
s.junior_4()
s.lifepointtest()
s.junior_5()