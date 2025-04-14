
import random
import os


animal_list=["rabbit", "donkey", "giraffe", "leopard", "buffalo", "chicken", "hamster", "jaguar", "lizard", "octopus","parrot", "peacock", "squirrel", "pelican", "antelope", "lobster", "pigeon","wombat", "badger", "alpaca", "walrus", "cheetah", "gazelle", "jackal", "ocelot", "raccoon", "seahorse", "reindeer","hyena", "turkey", "bison", "panda", "otter", "monkey", "sloth", "koala", "snail",    "turtle", "weasel", "frogs", "mole", "gecko"]

geography_list=["paris", "london", "tokyo", "cairo", "berlin", "madrid", "oslo", "sydney", "nairobi", "vienna", "canada", "brazil", "germany", "egypt", "kenya", "france", "norway", "italy", "mexico", "japan","island", "desert", "ocean", "valley", "mountain", "volcano", "glacier", "river", "lagoon", "fjord","savanna", "tundra", "delta", "peninsula", "plateau", "canyon", "coast", "bay", "reef", "plain", "seoul", "beijing", "moscow", "jakarta", "havana", "athens", "lisbon", "stockholm", "baghdad", "boston", "map"]

video_games=[ "mario", "zelda", "sonic", "link", "luigi", "samus", "pikachu", "ragnarok", "doom","fortnite", "minecraft", "roblox", "halo", "portal", "tetris", "pacman", "metroid", "witcher", "skyrim","joystick", "console", "arcade", "boss", "respawn", "inventory", "level", "quest", "mission", "avatar", "loot", "experience", "powerup", "combo", "checkpoint", "stealth", "armor", "weapon", "mana","health", "grenade", "sniper", "sandbox", "racing", "platformer", "fps", "rpg", "enemy", "ally", "map"]

movies_list=["inception", "avatar", "batman", "gladiator", "matrix", "jaws", "rocky", "titanic", "joker", "frozen", "aladdin", "shrek", "casablanca", "eternal", "parasite", "braveheart", "bond","godzilla", "elsa", "vader","cinema", "hollywood", "director", "script", "actor", "actress", "stunt", "sequel", "trilogy", "remake","genre", "popcorn", "trailer", "screen", "camera", "blockbuster","villain", "hero", "credits", "scene", "studio", "premiere", "marvel", "pixar", "disney", "universal", "thriller", "comedy", "drama", "action"]

objects_list=["laptop", "pencil", "wallet", "bottle", "mirror", "blanket", "glasses", "notebook", "backpack", "charger","window", "remote", "toaster", "cupboard", "dresser", "camera", "keychain","shampoo", "bedroom", "cushion","earbuds", "headset", "blanket", "marker", "speaker", "monitor", "keyboard", "stapler", "scissors", "bucket", "hanger", "toothbrush", "tissue", "napkin", "bicycle", "helmet", "flashlight", "basket", "curtain", "fridge","mattress", "candle", "notepad", "ruler", "mirror", "broom", "ladder", "sponge", "tablet", "shoe"]

fruits_list=["apple", "banana", "cherry", "orange", "melon", "peach", "grapes", "kiwi", "mango", "plum", "pear", "lemon", "lime", "papaya", "coconut", "berry", "guava", "mandarin", "nectar", "pomegranate", "dragonfruit", "watermelon", "tangerine", "avocado", "starfruit", "passionfruit", "blackberry", "raspberry", "elderberry", "blueberry", "cranberry"]

housetools_list=["hammer", "screwdriver", "wrench", "pliers", "drill", "tape", "level", "axe", "saw", "chisel", "screw", "nail", "bradawl", "spade", "shovel", "spanner", "trowel", "hacksaw", "sander", "torch", "pliers", "cutter", "vice", "pallet", "clamps", "stapler", "brush", "ladder", "duster", "glue", "bucket", "pouch", "screwkit", "welding", "vacuum", "gloves", "cordless", "paint", "scissors", "plumb", "tongs", "scraper", "mop", "drillbit", "hose", "cleaver", "grinder", "toolbox", "trowel"]


random_list= ["rabbit", "donkey", "giraffe", "leopard", "buffalo", "chicken", "hamster", "jaguar", "lizard", "octopus","parrot", "peacock", "squirrel", "pelican", "antelope", "lobster", "pigeon","wombat", "badger", "alpaca", "walrus", "cheetah", "gazelle", "jackal", "ocelot", "raccoon", "seahorse", "reindeer","hyena", "turkey", "bison", "panda", "otter", "monkey", "sloth", "koala", "snail",    "turtle", "weasel", "frogs", "mole", "gecko", "paris", "london", "tokyo", "cairo", "berlin", "madrid", "oslo", "sydney", "nairobi", "vienna", "canada", "brazil", "germany", "egypt", "kenya", "france", "norway", "italy", "mexico", "japan","island", "desert", "ocean", "valley", "mountain", "volcano", "glacier", "river", "lagoon", "fjord","savanna", "tundra", "delta", "peninsula", "plateau", "canyon", "coast", "bay", "reef", "plain", "seoul", "beijing", "moscow", "jakarta", "havana", "athens", "lisbon", "stockholm", "baghdad", "boston", "mario", "zelda", "sonic", "link", "luigi", "samus", "pikachu", "ragnarok", "doom","fortnite", "minecraft", "roblox", "halo", "portal", "tetris", "pacman", "metroid", "witcher", "skyrim","joystick", "console", "arcade", "boss", "respawn", "inventory", "level", "quest", "mission", "avatar", "loot", "experience", "powerup", "combo", "checkpoint", "stealth", "armor", "weapon", "mana","health", "grenade", "sniper", "sandbox", "racing", "platformer", "fps", "rpg", "enemy", "ally", "map", "inception", "avatar", "batman", "gladiator", "matrix", "jaws", "rocky", "titanic", "joker", "frozen", "aladdin", "shrek", "casablanca", "eternal", "parasite", "braveheart", "bond","godzilla", "elsa", "vader","cinema", "hollywood", "director", "script", "actor", "actress", "stunt", "sequel", "trilogy", "remake","genre", "popcorn", "trailer", "screen", "camera", "blockbuster","villain", "hero", "credits", "scene", "studio", "premiere", "marvel", "pixar", "disney", "universal", "thriller", "comedy", "drama", "action","laptop", "pencil", "wallet", "bottle", "mirror", "blanket", "glasses", "notebook", "backpack", "charger","window", "remote", "toaster", "cupboard", "dresser", "camera", "keychain","shampoo", "bedroom", "cushion","earbuds", "headset", "blanket", "marker", "speaker", "monitor", "keyboard", "stapler", "scissors", "bucket", "hanger", "toothbrush", "tissue", "napkin", "bicycle", "helmet", "flashlight", "basket", "curtain", "fridge","mattress", "candle", "notepad", "ruler", "mirror", "broom", "ladder", "sponge", "tablet", "shoe","apple", "banana", "cherry", "orange", "melon", "peach", "grapes", "kiwi", "mango", "plum", "pear", "lemon", "lime", "papaya", "coconut", "berry", "guava", "mandarin", "nectar", "pomegranate", "dragonfruit", "watermelon", "tangerine", "avocado", "starfruit", "passionfruit", "blackberry", "raspberry", "elderberry", "blueberry", "cranberry", "hammer", "screwdriver", "wrench", "pliers", "drill", "tape", "level", "axe", "saw", "chisel", "screw", "nail", "bradawl", "spade", "shovel", "spanner", "trowel", "hacksaw", "sander", "torch", "pliers", "cutter", "vice", "pallet", "clamps", "stapler", "brush", "ladder", "duster", "glue", "bucket", "pouch", "screwkit", "welding", "vacuum", "gloves", "cordless", "paint", "scissors", "plumb", "tongs", "scraper", "mop", "drillbit", "hose", "cleaver", "grinder", "toolbox", "trowel"]


words_list= []
word='_'
list_choice='_'

skip=False
score=0
v_counter=1
extra_chance=1
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "scoreshangman.txt")

def pick_list():
    global words_list
    global word
    global v_counter
    global list_choice
    print("________________________________________\nYou can choose from multiple categories of words.\nCategories:'animals', 'geography', 'movies', 'objects', 'fruits', 'housetools', 'video games'\nYou can also select 'random' for a extra x2 multiplier/streak to your score")
    list_choice=input('________________________________________\nWrite the name of the category would you like to choose? ')
    if list_choice.lower()=='animals':
        words_list=animal_list
    elif list_choice.lower()=='geography':
        words_list=geography_list
    elif list_choice.lower()=='movies':
        words_list=movies_list
    elif list_choice.lower()=='objects':
        words_list=objects_list
    elif list_choice.lower()=='fruits':
        words_list=fruits_list
    elif list_choice.lower()=='housetools':
        words_list=housetools_list
    elif list_choice.lower()=='random':
        words_list=random_list
    elif list_choice.lower()=='video games':
        words_list=video_games
    else:
        print('________________________________________\nInvalid selection, please input the name of the category.\n________________________________________')
        pick_list()
    if words_list==random_list:
        v_counter=v_counter+2
    word=random.choice(words_list)

def graph_word(word):  #making the !!!hidden!!! word structure 
    graph=[]
    i=0
    for x in word:
        i+=1
        graph.append('_')
    if i==len(word):
        return graph

def guess():
    guezz=input('....................................\nChoose a letter: ')
    return guezz.lower()

def check_input(a):  #request input from user and check if it is one letter !!!choice!!!
    if a != word:
        if len(a)!=1:
            print('Please input only one letter!')
            return check_input(guess())
        elif not a.isalpha():
                print('Please input one letter, not a number/symbol!')
                return check_input(guess())   
        else:
            return a
    else:
        return a 
        
def letter_count(x,a):  #this creates a list of positions where the letter is the word !!!position!!!
    i=0
    counter=[]
    while i< len(a):
        if x == a[i]:
            counter.append(i)
            i+=1
        else:
            i+=1
    else:
        return counter

def display_top_entries(): #display top 10 score
    global file_path
    # Open the file in read mode
    with open(file_path, "r") as file:
        # Read the first 10 lines
        lines = file.readlines()
        for i, line in enumerate(lines[:10]):
            print(f"{i+1}. {line.strip()}")

def replace_graph(hidden,position,choice): #puts the letter in the correct positions
    i=0
    while i< len(position):
        hidden[position[i]]=choice
        i+=1
    return hidden

def save_score():
    global score
    global player_name
    global file_path
    global current_directory
    if score>0:
        saving=input(f'________________________________________\nType "yes", or press enter to skip\nDo you want to save your score?: ')
        if saving.lower()=='yes':
            #with open("scoreshangman.txt", "a") as file:  # "a" = append mode
            with open(file_path, "a") as file:
                file.write(f"{player_name}: {score}\n")
                print('Your score has been saved!')
            # print("Current working directory:", os.getcwd())
            sort_scores_by_value()
            ask_top=('\n________________________________________\nType "yes", or press enter to skip\nDo you want to see the top score list?: ')
            if ask_top.lower()=='yes':
                display_top_entries()
        else: 
            return
    else:
        return

def tries(word):
    l=8
    mistakes=[]
    hidden = graph_word(word)
    global score
    global v_counter
    global extra_chance
    global list_choice
    while l>0:
        if '_' in hidden:
            print(f'Current category: {list_choice}')
            print('The current word is:', ' '.join(hidden))
            hang1(l)
            choice=check_input(guess())
            if choice==word: #check if the entire word is correct and score accordingly
                
                score=(score+100+(l*10))*v_counter
                print(f'Congrats! You won!!!\nYour current score is    {score}\n The full word is " {word} "\nYour current win streak is "{v_counter}"')
                return score
            
            elif choice in word:
                if choice in hidden:
                    print(f'You already tried {choice} and it was correct, try another letter.')
                else:
                    print('You guessed right!')
                    position=letter_count(choice,word)
                    hidden=replace_graph(hidden, position, choice) #choice=check_input(guess())
                    print(f'\nIncorret letters used: {' '.join(mistakes)}\nYou have {l} lives left!')
            else:
                if choice not in mistakes:
                    l-=1
                    mistakes.append(choice)
                    print(f"Incorrect, you have {l} lives left!\nIncorret letters used: {' '.join(mistakes)}")
                else:
                    print(f"You have already picked the letter {choice}\nIncorret letters used: {' '.join(mistakes)} \nYou have {l} lives left! ")
                
            #choice=check_input(guess())
                
        else:
            score=(score+100+(l*10))*v_counter
            print(f'Congrats! You won!!!\n________________________________________\nThe full word is " {word} "\nYour current score is    {score}\nYour current win streak is "{v_counter}"\n________________________________________')
            return score
    else:
         print(f'  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="""\nI am sorry, you lost!\n________________________________________\n    The correct word was " {word} "\n    Your final score was      {score} \n________________________________________')
         if score>10000 and extra_chance==1:
            retry=input(f'Do you want to keep half of your score and go another game?\nThis will also reset your multiplier\nWrite "yes" if you agree, otherwise a new game starts: ')
            if retry.lower()=='yes':
                score=int(score/2)
                v_counter=0
                extra_chance=0
                print(f'Your current score is now  {score}  \nYour current win streak is "{v_counter}"!')
                return
            else:
                save_score()
                score=0
                v_counter=0
                extra_chance=1
                sort_scores_by_value() 
                see_top()
                return
         else:
            save_score()
            score=0
            v_counter=0
            extra_chance=1
            sort_scores_by_value() 
            see_top()
            return 
         
        
def hang1(l): #ascii drawing the hangman
    if l==6:
        print('  +---+\n      |\n      |\n      |\n      |\n      |\n========="""')
    elif l==5:
        print('  +---+\n  |   |\n      |\n      |\n      |\n      |\n========="""')
    elif l==4:
        print('  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n========="""')
    elif l==3:
        print('  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n========="""')
    elif l==2:
        print('  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n========="""')
    elif l==1:
        print('  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n========="""')
    elif l==7:
        print('       \n       \n       \n       \n       \n       \n========="""')

def exerc(word): #initial text
    print("\n________________________________________\nLet's play some hangman!")
    tries(word)

def again():
    global v_counter
    global extra_chance
    global words_list
    global skip
    trying='_'
    #print(extra_chance, '|||||||||||||||||||||||||||')
    if extra_chance!=0:
        if skip==False:
            trying=input('\nIf you want to try again, write "again"!\nWrite "always" if you want to skip this prompt the for entire session\nOtherwise the game will close.\nYour input: ')
            if trying.lower()=="always":
                skip=True
                again()
    
    while trying.lower()=="again" or extra_chance==0 or skip==True:
        if extra_chance==0:
            extra_chance=2
        pick_list()
        v_counter=v_counter+1
        exerc(word)
        trying='_'
        again()
    else:
        if score>0:
            extra_chance=1
            print(f'You final score is: {score} ')
            save_score()
            sort_scores_by_value()
            see_top()
        return exit()   

def sort_scores_by_value():
    global file_path
    # Open the file in read mode
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass  # Just creates the file
    with open(file_path, "r") as file:
        # Read all lines from the file
        lines = file.readlines()

    # Create a list to hold tuples of (name, score)
    score_entries = []
    
    # Extract the name and score from each line
    for line in lines:
        # Remove leading/trailing spaces and split by ':'
        parts = line.strip().split(": ")
        if len(parts) == 2:
            name = parts[0]
            try:
                score = int(parts[1])  # Convert score to integer
                score_entries.append((name, score))  # Append as tuple
            except ValueError:
                continue  # Skip if the score is not an integer

    # Sort the entries by score in descending order
    score_entries.sort(key=lambda x: x[1], reverse=True)

    # Print the sorted entries (you can also save them back to the file)
#    print("Sorted scores:")
#    for i, (name, score) in enumerate(score_entries[:10]):  # Display top 10
#        print(f"{i + 1}. {name}: {score}")

    # Optionally, write the sorted entries back to the file
    with open(file_path, "w") as file:
        for name, score in score_entries:
            file.write(f"{name}: {score}\n")
    return

def see_top():
    ask_top=input('________________________________________\nType "yes", or press enter to skip\nDo you want to see the top score list?: ')
    if ask_top.lower()=='yes':
        display_top_entries()



player_name = input("________________________________________\nEnter your name: ")
sort_scores_by_value()
see_top()
pick_list()
exerc(word)     
again()

