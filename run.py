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
                print()  # Prints an empty line for separation
                print(f"Please enter a number between 1 and {max_choice}.")
        except ValueError:
            print()  # Prints an empty line for separation
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
    print()  # Prints an empty line for separation
    while True:
        # strip() ensures there are no accidental or intentional whitespaces
        player_name = input("What is the name of this hero's story?\n").strip()
        # Checks if name is empty and assigns "Hero"
        if not player_name:
            player["Stats"]["Name"] = "Hero"
            break
        # Checks if name length is between 1 and 10 charachters
        elif 1 <= len(player_name) <= 10:
            player["Stats"]["Name"] = player_name
            break
        else:
            print("Please enter a name between 1 and 10 characters.")


def print_player_potions():
    """
    Prints the player's available potions in the combat menu
    """
    print()  # Prints an empty line for separation
    for idx, (potion, details) in enumerate(player["Potions"].items(), 1):
        quantity = details["Quantity"]
        heal_amount = details["Heal Amount"]
        print(f"{idx}. {potion} ({quantity}): Heals {heal_amount}HP")
    print("4. Back to the Combat Menu!")


def handle_overheal():
    """
    If player heals over the Max HP, sets the current HP to the Max HP value
    """
    if player["Stats"]["Current HP"] > player["Stats"]["Max HP"]:
        player["Stats"]["Current HP"] = player["Stats"]["Max HP"]


def use_potion():
    """
    Allows the player to use a potion during combat.

    Returns:
    - True if a potion is used.
    - False if no potion is used.
    """
    while True:
        print_player_potions()
        choice = get_choice(4)

        if choice == 4:  # If player chooses to go back to the combat menu
            return False  # No potion was used

        potion_names = list(player["Potions"].keys())
        selected_potion = potion_names[choice - 1]

        if player["Potions"][selected_potion]["Quantity"] > 0:
            heal_amount = player["Potions"][selected_potion]["Heal Amount"]
            player["Stats"]["Current HP"] += heal_amount
            player["Potions"][selected_potion]["Quantity"] -= 1
            print()  # Prints an empty line for separation
            print(f"You used a {selected_potion} and"
                  f" healed for {heal_amount}HP!")
            handle_overheal()
            return True  # Potion was used

        else:
            print()  # Prints an empty line for separation
            print(f"You don't have any {selected_potion} left!")


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
            print_player_info_menu(player)


enemy = {
    "Goblin": {
        "Name": "Goblin",
        "HP": 50,
        "Atk": 20,
        "Def": 8,
        "Crit": 3,
    }
}

player = {
    "Stats": {
        "Name": "Unknown",
        "Max HP": 100,
        "Current HP": 100,
        "Atk": 15,
        "Def": 15,
        "Crit": 5,
    },
    "Potions": {
        "Potion": {"Quantity": 1, "Heal Amount": 20},
        "Mega Potion": {"Quantity": 0, "Heal Amount": 50},
        "Ultra Potion": {"Quantity": 0, "Heal Amount": 100},
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


# def choose_info(current_enemy):
#     """
#     Prints out the info options
#     """
#     while True:
#         choice = get_choice(3)
#         print()  # Prints an empty line for separation
#         print("Info about who?")
#         print("\n1. Player")
#         print("2. Enemy")
#         print("3. Go back to the Combat Menu.")

#         if choice == 1:
#             print_player_info_menu(player)
#             return False


# def print_enemy_info(enemy):
#     """
#     Prints the stats of the enemy.
#     """
#     print("\n=== ENEMY INFO ===\n")
#     for key, value in enemy.items():
#         print(f"{key} : {value}")
#     print()  # Prints an empty line for separation


# def combat(enemy):
#     """
#     Handles Combat
#     """
#     global player
#     print(f"========COMBAT VS {enemy['Name']}========")
#     while player['Stats']['Current HP'] > 0 and enemy['HP'] > 0:
#         print(f"\n{player['Stats']['Name']} HP:"
#               f" {player['Stats']['Current HP']}"
#               f"/{player['Stats']['Max HP']} |"
#               f" {enemy['Name']} HP: {enemy['HP']}"
#               "\n1. Attack"
#               "\n2. Item"
#               "\n3. Info"
#               "\n4. Run")
#         choice = get_choice(4)
#         if choice == 1:
#             dmg_to_enemy = round((player['Stats']["Atk"] - enemy["Def"])
#                                  * dmg_roll())
#             if dmg_to_enemy > 0:
#                 enemy["HP"] -= dmg_to_enemy
#                 print(f"You dealt {dmg_to_enemy} damage to the"
#                       f" {enemy['Name']}!")
#             else:
#                 print("You did no damage. The enemy's defense is too high!")

#             if enemy["HP"] > 0:
#                 dmg_to_player = round(
#                     (enemy["Atk"] - player["Stats"]["Def"]) * dmg_roll()
#                     )
#                 if dmg_to_player > 0:
#                     player["Stats"]["Current HP"] -= dmg_to_player
#                     print(f"The {enemy['Name']} dealt {dmg_to_player}",
#                           "damage to you!")
#                 else:
#                     print(f"The {enemy['Name']} did no damage. Your defense"
#                           " is too high!")

#         elif choice == 2:
#             if use_potion():
#                 dmg_to_player = round((enemy["Atk"] - player["Stats"]["Def"])
#                                       * dmg_roll())
#                 if dmg_to_player > 0:
#                     player["Stats"]["Current HP"] -= dmg_to_player
#                     print(f"The {enemy['Name']} dealt {dmg_to_player}"
#                           " damage to you!")
#                 else:
#                     print(f"The {enemy['Name']} did no damage."
#                           " Your defense is too high!")

#         elif choice == 3:
#             print("wait")

#         else:
#             print("RUN")


class Combat:
    """
    Handles the Combat
    """
    def __init__(self, player, enemy):
        """
        Something
        """
        self.player = player
        self.enemy = enemy

    def choose_info(self):
        """
        Prints out the info options.
        """
        while True:
            print("Info about who?")
            print("\n1. Player")
            print("2. Enemy")
            print("3. Go back to the Combat Menu.")
            choice = get_choice(3)

            if choice == 1:
                self.print_player_info()

            elif choice == 2:
                self.print_enemy_info()

            elif choice == 3:
                return

    def print_player_info(self):
        """
        Print player information
        """
        print()  # Prints an empty line for separation
        print("=== PLAYER INFO ===")
        print_horizontal_line()
        for main_key, main_value in self.player.items():
            print(main_key + ":\n")
            for key, value in main_value.items():
                if isinstance(value, dict):
                    print(f"{key}:")
                    for sub_key, sub_value in value.items():
                        print(f"{sub_key} : {sub_value}")
                    print()  # Prints an empty line for separation
                else:
                    print(f"{key} : {value}")
            print_horizontal_line()

    def print_enemy_info(self):
        """
        Print enemy information
        """
        print("\n=== ENEMY INFO ===\n")
        print()  # Prints an empty line for separation
        for key, value in enemy.items():
            print(f"{key} : {value}")
        print()  # Prints an empty line for separation

    def combat_loop(self):
        """
        Handles combat
        """
        print(f"========COMBAT VS {self.enemy['Name']}========")
        while self.player['Stats']['Current HP'] > 0 and self.enemy['HP'] > 0:
            print(f"\n{self.player['Stats']['Name']} HP:"
                  f" {self.player['Stats']['Current HP']}"
                  f"/{self.player['Stats']['Max HP']} |"
                  f" {self.enemy['Name']} HP: {self.enemy['HP']}"
                  "\n1. Attack"
                  "\n2. Item"
                  "\n3. Info"
                  "\n4. Run")
            choice = get_choice(4)
            if choice == 1:
                dmg_to_enemy = round((self.player['Stats']["Atk"] -
                                      self.enemy["Def"]) * dmg_roll())
                if dmg_to_enemy > 0:
                    self.enemy["HP"] -= dmg_to_enemy
                    print(f"You dealt {dmg_to_enemy} damage to the"
                          f" {self.enemy['Name']}!")
                else:
                    print("You did no damage."
                          " The enemy's defense is too high!")

                if self.enemy["HP"] > 0:
                    dmg_to_player = round(
                        (self.enemy["Atk"] - self.player
                         ["Stats"]["Def"]) * dmg_roll()
                        )
                    if dmg_to_player > 0:
                        self.player["Stats"]["Current HP"] -= dmg_to_player
                        print(f"The {self.enemy['Name']} dealt {dmg_to_player}"
                              " damage to you!")
                    else:
                        print(f"The {self.enemy['Name']} did no damage."
                              " Your defense is too high!")

            elif choice == 2:
                if use_potion():
                    dmg_to_player = round((self.enemy["Atk"] - self.player
                                          ["Stats"]["Def"]) * dmg_roll())
                    if dmg_to_player > 0:
                        self.player["Stats"]["Current HP"] -= dmg_to_player
                        print(f"The {self.enemy['Name']} dealt {dmg_to_player}"
                              " damage to you!")
                    else:
                        print(f"The {self.enemy['Name']} did no damage."
                              " Your defense is too high!")

            elif choice == 3:
                self.choose_info()

            else:
                print("RUN")


def start_battle(player, enemy_name):
    """
    Checks if the enemy name exists in the enemies dictionary
    """
    if enemy_name in enemy:
        battle = Combat(player, enemy[enemy_name])
        battle.combat_loop()
    else:
        print("There was an error starting the battle,"
              " you got lucky this time!")


def print_horizontal_line():
    """
    Prints 40 dashes on the screen
    """
    print("-" * 40)


def print_player_info_menu(player):
    """
    This is used to avoid repeating the same code
    """
    print_horizontal_line()
    for main_key, main_value in player.items():
        print(main_key + ":\n")
        for key, value in main_value.items():
            if isinstance(value, dict):  # If the value is another dictionary
                print(f"{key}:")
                for sub_key, sub_value in value.items():
                    print(f"{sub_key} : {sub_value}")
                print()  # Prints an empty line for separation
            else:
                print(f"{key} : {value}")
        print_horizontal_line()


def main():
    """
    Starts the game
    """
    intro()
    first_scene()
    battle = Combat(player, enemy["Goblin"])
    battle.combat_loop()


main()
