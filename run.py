"""
This module contains the main game
"""

import random


def fight_pause_and_continue():
    """
    Pauses the game and waits for the player's confirmation to continue.
    """
    while True:
        print(" You are about to fight, are you READY?")
        print("\n 1. Bring it on!")
        print("\n 2. No, i want my mommy!")
        choice = get_choice(2)
        if choice == 1:
            break
        elif choice == 2:
            print("\n Too bad, it is time to wear the big boy pants\n")
            break


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
            choice = int(input("\n Enter your choice: "))

            if 1 <= choice <= max_choice:
                print_horizontal_line()
                return choice
            else:
                print()  # Prints an empty line for separation
                print(f" Please enter a number between 1 and {max_choice}.")
        except ValueError:
            print()  # Prints an empty line for separation
            print(" Invalid input! Please enter a number.")


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
    - The name must be between 1 and 15 characters in length.
    - The name should not consist solely of whitespace.

    If the player enters only whitespace, the name will default to 'Hero'.

    Returns:
    - The name of the player's character.
    """
    print()  # Prints an empty line for separation
    while True:
        # strip() ensures there are no accidental or intentional whitespaces
        player_name = input(" What is the name of "
                            "this hero's story?\n").strip()
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


def print_player_potions():
    """
    Prints the player's available potions in the combat menu
    """
    print()  # Prints an empty line for separation
    for idx, (potion, details) in enumerate(player["Potions"].items(), 1):
        quantity = details["Quantity"]
        heal_amount = details["Heal Amount"]
        print(f"{idx}. {potion} ({quantity}): Heals {heal_amount}HP")
    print(" 4. Back to the Combat Menu!")


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
            print(f" You used a {selected_potion} and"
                  f" healed for {heal_amount}HP!")
            handle_overheal()
            return True  # Potion was used

        else:
            print()  # Prints an empty line for separation
            print(f" You don't have any {selected_potion} left!")


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
        "Name": "Goblin Dagger",
        "Type": "Weapon",
        "Atk": 5
    }
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
        print_horizontal_line()
        print(f" You have defeated the {self.enemy['Name']}!")
        self.handle_loot()

    def handle_loot(self):
        """
        Handles loot
        """
        self.player["Stats"]["Gold"] += self.enemy["Loot"]["Gold"]
        print(f" You got {self.enemy['Loot']['Gold']} Gold!")

        for loot_name in self.enemy["Loot"]["Items"]:
            item_detail = item_database.get(loot_name)
            if item_detail:
                self.equip_item(item_detail)

    def equip_item(self, item_detail):
        """
        Equips automatically better equipment
        """
        item_type = item_detail["Type"]
        item_name = item_detail["Name"]

        currently_equipped = self.player["Equipment"].get(item_type, None)

        def calculate_stat_change(new_item, old_item=None):
            """
            Calculates the stat change between the newly found item
            and the old equipped one if any is equipped
            """
            change = {}
            for stat, value in new_item.items():
                if stat != "Type" and "Name":
                    if old_item:
                        change[stat] = value - old_item.get(stat, 0)
                    else:
                        change[stat] = value

            return change

        if currently_equipped:
            stat_change = calculate_stat_change(
                item_detail, currently_equipped)

            if sum(stat_change.values()) > 0:
                self.player["Equipment"][item_type] = item_detail
                for stat, change in stat_change.items():
                    self.player["Stats"][stat] += change
                print(f"You found and equipped {item_name}")
            else:
                print(f" Found {item_detail}, but current"
                      " equipment is better!")
        else:
            self.player["Equipment"][item_type] = item_detail
            for stat, value in item_detail.items():
                if stat != "Type" and "Name":
                    self.player["Stats"][stat] += value
            print(f" Equipped {item_detail['Type']}!")

    def display_combat_info(self):
        """
        Compares stats of player and enemy
        """
        print("PLAYER\t\tENEMY")
        print_horizontal_line()
        print(f" Name: {self.player['Stats']['Name']}\tName: "
              f"{self.enemy['Name']}")
        print(f" HP: {self.player['Stats']['Max HP']}\t\tHP: "
              f"{self.enemy['Max HP']}")
        print(f" Attack: {self.player['Stats']['Atk']}\tAttack: "
              f"{self.enemy['Atk']}")
        print(f" Defence: {self.player['Stats']['Def']}\tDefence: "
              f"{self.enemy['Def']}")
        print(f" Crit: {self.player['Stats']['Crit']}\t\tCrit: "
              f"{self.enemy['Crit']}")
        print(f" \t\tRun: {self.enemy['Run']}")

    def player_combat_defeat(self):
        """
        Actions to take when the player is defeated in combat
        """
        print(f" The {self.enemy['Name']} hit you with a killing blow!")
        player_defeat()

    def combat_loop(self):
        """
        Handles combat
        """
        print(f" ======== COMBAT VS {self.enemy['Name'].upper()} ========")
        while (self.player['Stats']['Current HP'] > 0 and
               self.enemy['Current HP'] > 0):
            print("\n ENEMY IMAGE")
            print(f"\n{self.player['Stats']['Name']} HP:"
                  f" {self.player['Stats']['Current HP']}"
                  f"/{self.player['Stats']['Max HP']} |"
                  f" {self.enemy['Name']} HP:"
                  f" {self.enemy['Current HP']}"
                  f"/{self.enemy['Max HP']}")
            print("\n 1. Attack"
                  "\n 2. Item"
                  "\n 3. Info"
                  "\n 4. Run")
            choice = get_choice(4)
            if choice == 1:
                dmg_to_enemy = round((self.player['Stats']["Atk"] -
                                      self.enemy["Def"]) * dmg_roll())
                if dmg_to_enemy > 0:
                    self.enemy['Current HP'] -= dmg_to_enemy
                    print(f" You dealt {dmg_to_enemy} damage to the"
                          f" {self.enemy['Name']}!")
                    if self.enemy['Current HP'] <= 0:
                        self.player_combat_victory()
                else:
                    print(" You did no damage."
                          " The enemy's defense is too high!")

                if self.enemy['Current HP'] > 0:
                    dmg_to_player = round(
                        (self.enemy["Atk"] - self.player
                         ["Stats"]["Def"]) * dmg_roll()
                        )
                    if dmg_to_player > 0:
                        self.player["Stats"]["Current HP"] -= dmg_to_player
                        print(f" The {self.enemy['Name']}"
                              " dealt {dmg_to_player}"
                              " damage to you!")
                    else:
                        print(f" The {self.enemy['Name']} did no damage."
                              " Your defense is too high!")

                    if self.player['Stats']['Current HP'] <= 0:
                        self.player_combat_defeat()

            elif choice == 2:
                if use_potion():
                    dmg_to_player = round((self.enemy["Atk"] - self.player
                                          ["Stats"]["Def"]) * dmg_roll())
                    if dmg_to_player > 0:
                        self.player["Stats"]["Current HP"] -= dmg_to_player
                        print(f" The {self.enemy['Name']}"
                              " dealt {dmg_to_player}"
                              " damage to you!")
                    else:
                        print(f" The {self.enemy['Name']} did no damage."
                              " Your defense is too high!")

                    if self.player['Stats']['Current HP'] <= 0:
                        self.player_combat_defeat()

            elif choice == 3:
                self.display_combat_info()

            else:
                if player_run_away(self.enemy['Run']):
                    print(" You successfully ran away!")
                    return  # Exits the combat loop

                else:
                    print(f" The {self.enemy['Name']} blocked your way."
                          " You couldn't escape.")
                    dmg_to_player = round((self.enemy["Atk"] - self.player
                                          ["Stats"]["Def"]) * dmg_roll())
                    if dmg_to_player > 0:
                        self.player["Stats"]["Current HP"] -= dmg_to_player
                        print(f" The {self.enemy['Name']}"
                              f" dealt {dmg_to_player}"
                              " damage to you!")
                    else:
                        print(f" The {self.enemy['Name']} did no damage."
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
        main()
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
    print("===== STATS =====")
    print(f"Name: {player['Stats']['Name']}")
    print(f"HP: {player['Stats']['Max HP']}")
    print(f"Attack: {player['Stats']['Atk']}")
    print(f"Defence: {player['Stats']['Def']}")
    print(f"Crit: {player['Stats']['Crit']}")
    print(f"Gold: {player['Stats']['Gold']}")
    print_horizontal_line()
    print("===== POTIONS =====")
    print(
          f"Potion: {player['Potions']['Potion']['Quantity']}"
          f"\t Heal Amount: {player['Potions']['Potion']['Heal Amount']}")
    print(
          f"Mega Potion: {player['Potions']['Mega Potion']['Quantity']}"
          f"\t Heal Amount: {player['Potions']['Mega Potion']['Heal Amount']}")
    print(
          f"Ultra Potion: {player['Potions']['Ultra Potion']['Quantity']}"
          f"\t Heal Amount:"
          f" {player['Potions']['Ultra Potion']['Heal Amount']}")
    print_horizontal_line()
    print("===== EQUIPMENT =====")

    weapon_name = (
        player['Equipment']['Weapon']['Name']
        if player['Equipment']['Weapon']
        else 'None'
    )
    weapon_stat = (
        player['Equipment']['Weapon']['Atk']
        if player['Equipment']['Weapon']
        else '0'
    )

    helmet_name = (
        player['Equipment']['Head']['Name']
        if player['Equipment']['Head']
        else 'None'
    )
    helmet_stat = (
        player['Equipment']['Head']['Def']
        if player['Equipment']['Head']
        else '0'
    )

    body_name = (
        player['Equipment']['Body']['Name']
        if player['Equipment']['Body']
        else 'None'
    )
    body_stat = (
        player['Equipment']['Body']['Def']
        if player['Equipment']['Body']
        else '0'
    )

    legs_name = (
        player['Equipment']['Legs']['Name']
        if player['Equipment']['Legs']
        else 'None'
    )
    legs_stat = (
        player['Equipment']['Legs']['Def']
        if player['Equipment']['Legs']
        else '0'
    )

    boots_name = (
        player['Equipment']['Boots']['Name']
        if player['Equipment']['Boots']
        else 'None'
    )
    boots_stat = (
        player['Equipment']['Boots']['Def']
        if player['Equipment']['Boots']
        else '0'
    )

    hands_name = (
        player['Equipment']['Hands']['Name']
        if player['Equipment']['Hands']
        else 'None'
    )
    hands_stat = (
        player['Equipment']['Hands']['Def']
        if player['Equipment']['Hands']
        else '0'
    )

    print(f"Weapon: {weapon_name}\t Attack: +{weapon_stat}")
    print(f"Head: {helmet_name}\t Defence: +{helmet_stat}")
    print(f"Body: {body_name}\t Defence: +{body_stat}")
    print(f"Legs: {legs_name}\t Defence: +{legs_stat}")
    print(f"Boots: {boots_name}\t Defence: +{boots_stat}")
    print(f"Hands: {hands_name}\t Defence: +{hands_stat}")


def intro():
    """
    Provides the initial game introduction to the player.

    Prompts the player with the choice of starting the game,
    reading the rules or exiting the game.
    """
    reset_game(player, enemy)
    print(" 📜 Welcome to Text-Land!"
          "\n In a realm where words wield power and choices shape destinies,"
          " you find yourself at the crossroads of fate."
          "\n A mysterious world filled with unknown dangers,"
          " captivating stories, and hidden treasures beckons you."
          "\n As you embark on this epic journey, remember:"
          " every choice matters!"
          "\n Your decisions will carve out your path, lead you to treasures, "
          "pit you against formidable foes, and present riddles that challenge"
          " your intellect."
          "\n But fear not, in Text-Land, even the most ordinary adventurers"
          " can become legends."
          "\n Do you have what it takes to conquer the challenges,"
          " decipher the"
          " mysteries, and emerge as the hero of Text-Land?"
          "\n Or will you be its Doom?"
          "\n 1. 🛡️  Enter your name and begin your adventure."
          "\n 2. 📘 Read about the rules of Text-Land."
          "\n 3. 🚪 Exit to the real world.")

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
    print_horizontal_line()
    print(" Blinking awake, you find yourself by a serene lake."
          " How did you end up here? Your memory's a blur."
          "\n As you're piecing things together, a distant"
          " scream of help shatters the tranquility."
          "\n Something's not right!"
          "\n What will you do?")
    while True:
        print("\n 1. Run towards the screams"
              "\n 2. The screams dont concern you."
              " You rather go back to sleep."
              "\n 3. Player Info")

        choice = get_choice(3)
        if choice == 1:
            fight_pause_and_continue()
            battle = Combat(player, enemy["Goblin"])
            battle.combat_loop()
            break
        elif choice == 2:
            first_scene_game_over()
        elif choice == 3:
            print_player_info_menu(player)


def first_scene_game_over():
    """
    Calls the game over screen if the player chooses
    the second option of the first scene
    """
    print(" You ignored the screams of help and went back to sleep..."
          "\n Zzz...Zzz..Zz AAGH!"
          "\n You suddenly wake up to a stinging pain in your chest!"
          "\n You see a Goblin in front of you grinning"
          " with a malicious smile."
          "\n As your eyes wander you notice the goblin's"
          " blade in your heart.."
          "\n You go back to sleep....this time forever......")
    player_defeat()


def second_scene():
    """
    This is going to be the second scene
    """
    print("\n Ths is the second scene")
    while True:
        print("(1)"
              "2")
        choice = get_choice(2)
        if choice == 1:
            print("You chose 1")
        elif choice == 2:
            print_player_info_menu(player)


def main():
    """
    Starts the game
    """
    intro()
    first_scene()
    second_scene()


main()
