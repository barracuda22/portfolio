import time

wizard = "Wizard" 
elf = "Elf"
human = "Human"

charMap = {
    "Wizard":{"Health":70,"Damage":150},
    "Elf":{"Health":100,"Damage":100},
    "Human":{"Health":150,"Damage":20}
} # dictionary mapping all the characters to attributes

dragon_hp = 300
dragon_damage = 50
choice = 0
character = ""
my_character = ""

# defines a function that lists the characters and receives the players input
def characterDialogue():
    print("Choose a character!")
    print("1.  Wizard")
    print("2.  Elf")
    print("3.  Human")
    choice = input("Choose your character: ")
    return choice # returns chosen character as string

# sets the character variable to what the player chose
def getCharacter(char: str):
    for c in charMap:
        if c.lower() == char.lower():
            character = (char[0].upper() + char[1:].lower()) # uses string indices to correct the name
            return character
    print("Unknown character!")
    exit() # Exits the terminal

# provides the stats about the character that the player chose
def getStats(char: str):
    for c in charMap:
        if char == c:
            print("Health - " + str(charMap.get(c).get("Health")))
            print("Damage - " + str(charMap.get(c).get("Damage")))

# gets any character's health from a string
def getMyHealth(char: str):
    for c in charMap:
        if char == c:
            return charMap.get(c).get("Health")

# gets any character's damage from a string
def getMyDMG(char: str):
    for c in charMap:
        if char == c:
            return charMap.get(c).get("Damage")

# defines all variables needed for the game
chosen = characterDialogue()
characterChoice = getCharacter(chosen)
print("You have chosen " + characterChoice)
getStats(characterChoice)
my_character = characterChoice
my_hp = getMyHealth(my_character)
my_dmg = getMyDMG(my_character)
input("Press enter to begin!")
print("")

# starts the fight between the dragon and the player's character
while True:
    if dragon_hp <= 0:
        print("VICTORY!")
        break
    elif my_hp <= 0:
        print("GAME OVER!")
        break

    dragon_hp = dragon_hp - my_dmg
    print(my_character + " stroke an attack at the dragon!")
    print("The dragon is now at " + str(dragon_hp) + " health!")
    if dragon_hp <= 0:
        print("VICTORY!")
        break
    elif my_hp <= 0:
        print("GAME OVER!")
        break
    time.sleep(0.5)
    my_hp = my_hp - dragon_damage
    print("")
    print(f"The dragon stroke back at the {my_character}")
    print("You are now at " + str(my_hp) + " health!")
    input("Press enter to continue!")
    print("")
    if dragon_hp <= 0:
        print("VICTORY!")
        break
    elif my_hp <= 0:
        print("GAME OVER!")
        break
    time.sleep(0.5)