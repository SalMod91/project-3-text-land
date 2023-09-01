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
                print_horizontal_line()
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
        elif 1 <= len(player_name) <= 15:
            player["Stats"]["Name"] = player_name
            break
        else:
            print("Please enter a name between 1 and 10 characters.")

    first_scene()


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
    reset_game(player, enemy)
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
            battle = Combat(player, enemy["Goblin"])
            battle.combat_loop()
            break
        else:
            print_player_info_menu(player)


enemy = {
    "Goblin": {
        "Name": "Goblin",
        "Max HP": 50,
        "Current HP": 50,
        "Atk": 20,
        "Def": 8,
        "Crit": 3,
        "Run": 0,

        "Loot": {
            "Gold": 5,
            "Items": ["Goblin Dagger"]
        }
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
        "Gold": 0
    },
    "Potions": {
        "Potion": {"Quantity": 1, "Heal Amount": 20},
        "Mega Potion": {"Quantity": 0, "Heal Amount": 50},
        "Ultra Potion": {"Quantity": 0, "Heal Amount": 100},
    },
    "Equipment": {
        "Weapon": None,
        "Head": None,
        "Body": None,
        "Legs": None,
        "Boots": None,
        "Hands": None
    }
}


item_database = {
    "Goblin Dagger": {
        "Type": "Weapon",
        "Atk": 5
    }
}


equipment_stats = {
    "Goblin Dagger": {
        "Atk": 5
    }
}

player_equipment = {
    "Weapon": None,
    "Head": None,
    "Body": None,
    "Legs": None,
    "Boots": None,
    "Hands": None
}


def reset_game(player, enemy):
    """
    Resets the player dictionary and enemy dictionary
    """
    starting_player = {
        "Stats": {
            "Name": "Unknown",
            "Max HP": 100,
            "Current HP": 100,
            "Atk": 15,
            "Def": 15,
            "Crit": 5,
            "Gold": 0
        },
        "Potions": {
            "Potion": {"Quantity": 1, "Heal Amount": 20},
            "Mega Potion": {"Quantity": 0, "Heal Amount": 50},
            "Ultra Potion": {"Quantity": 0, "Heal Amount": 100},
        }
    }

    starting_equipment = {
        "Weapon": None,
        "Head": None,
        "Body": None,
        "Legs": None,
        "Boots": None,
        "Hands": None
    }

    starting_enemy = {
        "Goblin": {
            "Name": "Goblin",
            "Max HP": 50,
            "Current HP": 50,
            "Atk": 20,
            "Def": 8,
            "Crit": 3,
            "Run": 0,

            "Loot": {
                "Gold": 5,
                "Items": ["Goblin Dagger"]
            }
        }
    }

    player.clear()
    player.update(starting_player)

    player_equipment.clear()
    player_equipment.update(starting_equipment)

    enemy.clear()
    enemy.update(starting_enemy)


def player_run_away(enemy_run_stat):
    """
    Random Roll between 1 and 100 to determine if the player can run away

    Returns:
    - A boolean with True or False value
    """
    rand_int = random.randint(1, 100)
    if rand_int <= enemy_run_stat:
        return True
    else:
        return False


def dmg_roll():
    """
    Rolls a random multiplier between 0.8 and 1.2

    Returns:
    - A random float between 0.8 and 1.2.
    """
    multiplier = ((random .randint(0, 40) - 20) + 100) / 100
    return multiplier


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

    def player_combat_victory(self):
        """
        Actions to take when the player defeats the enemy in combat
        """
        print(f"You have defeated the {self.enemy['Name']}!")
        self.handle_loot()

    def handle_loot(self):
        """
        Handles loot
        """
        self.player["Stats"]["Gold"] += self.enemy["Loot"]["Gold"]
        print(f"You got {self.enemy['Loot']['Gold']} Gold!")

        for loot_name in self.enemy["Loot"]["Items"]:
            item_detail = item_database.get(loot_name)
            if item_detail:
                self.equip_item(item_detail)

    def equip_item(self, item_detail):
        """
        Equips automatically better equipment
        """
        item_type = item_detail["Type"]

        currently_equipped = self.player["Equipment"].get(item_type, None)

        if item_detail["Atk"] > currently_equipped["Atk"]:
            self.player["Stats"]["Atk"] -= currently_equipped["Atk"]
            self.player["Stats"]["Atk"] += item_detail["Atk"]
            self.player["Equipment"][item_type] = item_detail["Atk"]

    def display_combat_info(self):
        """
        Compares stats of player and enemy
        """
        print("PLAYER\t\tENEMY")
        print_horizontal_line()
        print(f"Name: {self.player['Stats']['Name']}\tName: "
              f"{self.enemy['Name']}")
        print(f"HP: {self.player['Stats']['Max HP']}\t\tHP: "
              f"{self.enemy['Max HP']}")
        print(f"Attack: {self.player['Stats']['Atk']}\tAttack: "
              f"{self.enemy['Atk']}")
        print(f"Defence: {self.player['Stats']['Def']}\tDefence: "
              f"{self.enemy['Def']}")
        print(f"Crit: {self.player['Stats']['Crit']}\t\tCrit: "
              f"{self.enemy['Crit']}")
        print(f"\t\tRun: {self.enemy['Run']}")

    def player_combat_defeat(self):
        """
        Actions to take when the player is defeated in combat
        """
        print(f"The {self.enemy['Name']} hit you with a killing blow!")
        player_defeat()

    def combat_loop(self):
        """
        Handles combat
        """
        print(f"======== COMBAT VS {self.enemy['Name'].upper()} ========")
        while (self.player['Stats']['Current HP'] > 0 and
               self.enemy['Current HP'] > 0):
            print("\nENEMY IMAGE")
            print(f"\n{self.player['Stats']['Name']} HP:"
                  f" {self.player['Stats']['Current HP']}"
                  f"/{self.player['Stats']['Max HP']} |"
                  f" {self.enemy['Name']} HP:"
                  f" {self.enemy['Current HP']}"
                  f"/{self.enemy['Max HP']}")
            print("\n1. Attack"
                  "\n2. Item"
                  "\n3. Info"
                  "\n4. Run")
            choice = get_choice(4)
            if choice == 1:
                dmg_to_enemy = round((self.player['Stats']["Atk"] -
                                      self.enemy["Def"]) * dmg_roll())
                if dmg_to_enemy > 0:
                    self.enemy['Current HP'] -= dmg_to_enemy
                    print(f"You dealt {dmg_to_enemy} damage to the"
                          f" {self.enemy['Name']}!")
                    if self.enemy['Current HP'] <= 0:
                        self.player_combat_victory()
                else:
                    print("You did no damage."
                          " The enemy's defense is too high!")

                if self.enemy['Current HP'] > 0:
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

                    if self.player['Stats']['Current HP'] <= 0:
                        self.player_combat_defeat()

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

                    if self.player['Stats']['Current HP'] <= 0:
                        self.player_combat_defeat()

            elif choice == 3:
                self.display_combat_info()

            else:
                if player_run_away(self.enemy['Run']):
                    print("You successfully ran away!")
                    return  # Exits the combat loop

                else:
                    print(f"The {self.enemy['Name']} blocked your way."
                          " You couldn't escape.")
                    dmg_to_player = round((self.enemy["Atk"] - self.player
                                          ["Stats"]["Def"]) * dmg_roll())
                    if dmg_to_player > 0:
                        self.player["Stats"]["Current HP"] -= dmg_to_player
                        print(f"The {self.enemy['Name']} dealt {dmg_to_player}"
                              " damage to you!")
                    else:
                        print(f"The {self.enemy['Name']} did no damage."
                              " Your defense is too high!")

                    if self.player['Stats']['Current HP'] <= 0:
                        self.player_combat_defeat()


def player_defeat():
    """
    Displays the dead message and asks the player if they'd like to retry
    """
    print("\nYOU DIED")
    print("\nContinue?"
          "\n1. Yes!"
          "\n2. No..I give up..")
    choice = get_choice(2)
    if choice == 1:
        intro()
    elif choice == 2:
        print("Not everyone is suited to be a Hero \U0001F44E Goodbye!")
        exit()


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
    Prints 40 dashes on the screen effectively creating a visual line that
    separates content
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


main()
