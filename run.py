"""
This module contains the main game
"""

import random


def get_choice(max_choice):
    """
    Prompts the player to make a valid choice withing a given range.

    Parameters:
    - max_choice: Maximum valid choice number.

    Returns:
    - An integer chosen by the player.

    Exceptions:
    - Raises a message if the input is not a valid number in range.
    """
    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if 1 <= choice <= max_choice:
                return choice
            else:
                print(f"Please enter a number between 1 and {max_choice}.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def rules():
    """
    Prints the rules of the game and then redirects the user either
    back to the intro or to the start of the game.
    """
    print("These are the rules, will be add later",
          "\n1. 🛡️  I am ready to start my adventure!",
          "\n2. 📜 Bring me back to the Menu.")
    choice = get_choice(2)
    if choice == 1:
        player_name_choice()
    else:
        intro()


def player_name_choice():
    """
    Prompts the player to input their character's name.

    The function will continue to prompt the player until they provide a
    valid name, adhering to the following conditions:
    - The name must be between 1 and 10 characters in length.
    - The name should not consist solely of whitespace.

    If the player enters only whitespace, the name will default to 'Hero'.

    Returns:
    - The name of the player's character.
    """
    while True:
        # strip() ensures there are no accidental or intentional whitespaces
        player_name = input("What is the name of this hero's story?\n").strip()
        # Checks if name is empty and assigns "Hero"
        if not player_name:
            player["Stats"]["Name"] = "Hero"
            break
        # Checks if name length is between 1 and 10 charachters
        elif 1 <= len(player_name) <= 10:
            player["Name"] = player_name
            break
        else:
            print("Please enter a name between 1 and 10 characters.")


def print_player_info(player):
    """
    This is used to avoid repeating the same code
    """
    print("\n")

    for main_key, main_value in player.items():
        print(main_key + ":")
        for key, value in main_value.items():
            print(f"{key} : {value}")
        print()  # Prints an empty line for separation


def intro():
    """
    Provides the initial game introduction to the player.

    Prompts the player with the choice of starting the game,
    reading the rules or exiting the game.
    """
    print("📜 Welcome to Text-Land!"
          "\n\nIn a realm where words wield power and choices shape destinies,"
          " you find yourself at the crossroads of fate."
          "\nA mysterious world filled with unknown dangers,"
          " captivating stories, and hidden treasures beckons you."
          "\n\nAs you embark on this epic journey, remember:"
          " every choice matters!"
          "\nYour decisions will carve out your path, lead you to treasures, "
          "pit you against formidable foes, and present riddles that challenge"
          " your intellect."
          "\n\nBut fear not, in Text-Land, even the most ordinary adventurers"
          " can become legends."
          "\nDo you have what it takes to conquer the challenges, decipher the"
          " mysteries, and emerge as the hero of Text-Land?"
          "\n\nOr will you be its Doom?"
          "\n\n1. 🛡️  Enter your name and begin your adventure."
          "\n2. 📘 Read about the rules of Text-Land."
          "\n3. 🚪 Exit to the real world.")

    choice = get_choice(3)
    if choice == 1:
        player_name_choice()

    elif choice == 2:
        rules()

    else:
        print("Not everyone is suited to be a Hero \U0001F44E Goodbye!")
        exit()


def first_scene():
    """
    This is going to be the first scene
    """
    print("\nThis is the first scene")
    while True:
        print("\n1. Go towards the screams\n"
              "2. Player Info")

        choice = get_choice(2)
        if choice == 1:
            print("Done")
            break
        else:
            print_player_info(player)


enemy = {
    "Goblin": {
        "Name": "Goblin",
        "HP": 50,
        "Atk": 20,
        "Def": 10,
        "Crit": 3,  # 3% chance
    }
}

player = {
    "Stats": {
        "Name": {None},
        "HP": 100,
        "Atk": 25,
        "Def": 15,
        "Crit": 5,  # 5% chance
    },
    "Potions": {
        "Potion": 0,
        "Mega Potion": 0,
        "Ultra Potion": 0,
    }
}


def dmg_roll():
    """
    Rolls a random multiplier between 0.8 and 1.2

    Returns:
    - A random float between 0.8 and 1.2.
    """
    multiplier = ((random .randint(0, 40) - 20) + 100) / 100
    return multiplier


def combat(enemy):
    """
    Handles Combat
    """
    global player
    print(f"========COMBAT VS {enemy['Name']}========")
    while player["HP"] > 0 and enemy["HP"] > 0:
        print(f"\n Player HP: {player['HP']} | Enemy HP: {enemy['HP']}"
              "\n1. Attack"
              "\n2. Item"
              "\n3. Info"
              "\n4. Run")
        choice = get_choice(4)
        if choice == 1:
            dmg_to_enemy = round((player["Atk"] - enemy["Def"]) * dmg_roll())
            if dmg_to_enemy > 0:
                enemy["HP"] -= dmg_to_enemy
                print(f"You dealt {dmg_to_enemy} damage to the"
                      f" {enemy['Name']}!")
            else:
                print("You did no damage. The enemy's defense is too high!")

            if enemy["HP"] > 0:
                dmg_to_player = round(
                    (enemy["Atk"] - player["Def"]) * dmg_roll()
                    )
                if dmg_to_player > 0:
                    player["HP"] -= dmg_to_player
                    print(f"The {enemy['Name']} dealt {dmg_to_player}",
                          "damage to you!")
                else:
                    print(f"The {enemy['Name']} did no damage. Your defense is"
                          "too high!")

        elif choice == 2:
            print("Item")

        elif choice == 3:
            print("Choice 3")

        else:
            print("RUN")


def main():
    """
    Starts the game
    """
    intro()
    first_scene()
    combat(enemy["Goblin"])


main()
