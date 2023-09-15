# pylint: disable=too-many-lines
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
            choice = int(input("\n Enter your choice: "))

            if 1 <= choice <= max_choice:
                print_horizontal_line()
                return choice
            else:
                print()  # Prints an empty line for separation
                print(f" 🚫  Please enter a number between 1 and {max_choice}.")
        except ValueError:
            print()  # Prints an empty line for separation
            print(" 🚫  Invalid input! Please enter a number.")


def rules():
    """
    Prints the rules of the game and then redirects the user either
    back to the intro or to the start of the game.
    """
    print(" These are the rules, will be add later",
          "\n\n 1. 🛡️  I am ready to start my adventure!",
          "\n\n 2. 📜  Bring me back to the Menu.")
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
            print(" Please enter a name between 1 and 10 characters.")


enemy = {}

player = {}

battle_result = ""  # pylint: disable=invalid-name

shop_coupon = False  # pylint: disable=invalid-name

player_critical_messages = [
    " 💥  YOU DEALT A POWERFUL CRITICAL BLOW!",
    " 💥  YOU DEALT A DEVASTATING CRITICAL BLOW!",
    " 💥  YOU DEALT AN IMPRESSIVE CRITICAL BLOW!",
    " 💥  YOU DEALT A CRITICAL HIT!",
    " 💥  THE ECHOES OF YOUR POWERFUL CRITICAL HIT RESOUND!",
    " 💥  THE AIR CRACKLES WITH ENERGY FROM YOUR CRITICAL HIT!"
]


enemy_critical_messages = [
    " 💥  THE ENEMY CLARIFIES YOUR MORTALITY WITH A SINGLE"
    " CRITICAL STRIKE!",
    " 💥  THE ENEMY DEALT TO YOU A CRITICAL INJURY!",
    " 💥  THE ENEMY STRIKES WITH UNBRIDLED FURY!",
    " 💥  A CHILLING CRITICAL BLOW FROM THE ENEMY!",
    " 💥  THE ENEMY LANDS A VICIOUS CRITICAL HIT!",
    " 💥  THE ENEMY UNLEASHES A SURGE OF POWER,"
    " CRITICALLY STRIKING YOU!",
    " 💥  THE AIR TENSES AS THE ENEMY'S"
    " CRITICAL ATTACK LANDS!",
    " 💥  YOU REEL FROM THE OVERWHELMING FORCE OF THE ENEMY'S"
    " CRITICAL BLOW!"
]


item_database = {
    "Goblin Dagger": {
        "Name": "Goblin Dagger",
        "Type": "Weapon",
        "Atk": 5,
        "Crit": 10
    },
    "Goblin Boots": {
        "Name": "Goblin Boots",
        "Type": "Boots",
        "Def": 1,
        "Max HP": 2
    },
    "Small Buckler": {
        "Name": "Small Buckler",
        "Type": "Shield",
        "Def": 2,
        "Max HP": 3
    },
    "Chief Gloves": {
        "Name": "Chief Gloves",
        "Type": "Hands",
        "Def": 5,
        "Max HP": 5
    },
    "Long Sword": {
        "Name": "Long Sword",
        "Type": "Weapon",
        "Atk": 10,
        "Crit": 10
    }
}


pandora_items = {
    1: {"Name": 1, "Status": False},
    2: {"Name": 2, "Status": False},
    3: {"Name": 3, "Status": False},
    4: {"Name": 4, "Status": False},
    5: {"Name": 5, "Status": False},
    6: {"Name": 6, "Status": False},
    7: {"Name": 7, "Status": False},
    8: {"Name": 8, "Status": False},
    9: {"Name": 9, "Status": False},
    10: {"Name": 10, "Status": False}
}


def reset_player():
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
            "Shield": None,
            "Head": None,
            "Body": None,
            "Legs": None,
            "Boots": None,
            "Hands": None
        }
    }

    player.clear()
    player.update(starting_player)


def reset_enemy():
    """
    Resets the enemy dictionary after every fight
    """
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
                "Items": {
                    "Goblin Boots": 30,
                    "Goblin Dagger": 100,
                    "Small Buckler": 30
                }
            }
        },
        "Goblin Chief": {
            "Name": "Goblin Chief",
            "Max HP": 60,
            "Current HP": 60,
            "Atk": 30,
            "Def": 10,
            "Crit": 3,
            "Run": 0,

            "Loot": {
                "Gold": 15,
                "Items": {
                    "Chief Gloves": 100
                }
            }
        },
        "Sparky Tail": {
            "Name": "Sparky Tail",
            "Max HP": 30,
            "Current HP": 30,
            "Atk": 20,
            "Def": 10,
            "Crit": 20,
            "Run": 100,

            "Loot": {
                "Gold": 30,
            }
        },
        "Petalback": {
            "Name": "Petalback",
            "Max HP": 70,
            "Current HP": 70,
            "Atk": 25,
            "Def": 13,
            "Crit": 5,
            "Run": 0,

            "Loot": {
                "Gold": 50,
            }
        }
    }

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


def critical_hit(character):
    """
    Determines if the critical is True of False

    Parameter:
    - Either the player or enemy dictionary

    Returns:
    - A boolean with True or False value
    """
    if "Stats" in character:
        crit_chance = character["Stats"]["Crit"]
    else:
        crit_chance = character["Crit"]

    return random.random() < crit_chance / 100


def fight_pause_and_continue():
    """
    Pauses the game and waits for the player's confirmation to continue.
    """
    while True:
        print_horizontal_line()
        print("\n You are about to fight, are you READY?")
        print("\n 👊  1. Bring it on!")
        print("\n 😭  2. No, i want my mommy!")
        choice = get_choice(2)
        if choice == 1:
            break
        elif choice == 2:
            print("\n Too bad, it is time to wear the big boy pants!"
                  "  👖\n")
            break


class Combat:
    """
    Handles the Combat
    """

    def __init__(self, player, enemy):  # pylint: disable=redefined-outer-name
        """
        Something
        """
        self.player = player
        self.enemy = enemy

    def player_combat_victory(self):
        """
        Actions to take when the player defeats the enemy in combat
        """
        global battle_result  # pylint: disable=global-statement
        battle_result = "Victory"
        print()
        print("===== VICTORY =====")
        print()
        print(f" You have defeated the {self.enemy['Name']}!")
        self.handle_loot()
        return battle_result

    def check_drop(self):
        """
        Checks if players drops loot
        """
        dropped_items = []

        items = self.enemy.get("Loot", {}).get("Items", {})

        for item, drop_rate in items.items():
            if random.randint(1, 100) <= drop_rate:
                dropped_items.append(item)

        return dropped_items

    def handle_loot(self):
        """
        Handles loot
        """
        self.player["Stats"]["Gold"] += self.enemy["Loot"]["Gold"]
        print(f" Elidor gave you {self.enemy['Loot']['Gold']} Gold 💰 !")

        dropped_items = self.check_drop()

        for loot_name in dropped_items:
            item_dropped = item_database.get(loot_name)
            self.equip_item(item_dropped)

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
                if stat != "Type" and stat != "Name" and stat != "Droprate":
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
                print()
                print(f" 🎉  You found and equipped {item_name}  🎉")
            else:
                print()
                print(f" 🚫  Found {item_name}({item_detail['Type']}), but "
                      " current equipment is better!")
        else:
            self.player["Equipment"][item_type] = item_detail
            for stat, value in item_detail.items():
                if stat != "Type" and stat != "Name" and stat != "Droprate":
                    self.player["Stats"][stat] += value
            print()
            print(f" 🎉  You found and equipped {item_name}"
                  f"({item_detail['Type']})!  🎉")

    def print_player_potions(self):
        """
        Prints the player's available potions in the combat menu
        """
        print()  # Prints an empty line for separation
        for idx, (potion, details) in enumerate(
                self.player["Potions"].items(), 1):
            quantity = details["Quantity"]
            heal_amount = details["Heal Amount"]
            print(f" 🧪  {idx}. {potion} ({quantity}): Heals {heal_amount}HP")
        print(" 🔄  4. Back to the Combat Menu!")

    def handle_overheal(self):
        """
        If player heals over the Max HP, sets the current HP
        to the Max HP value
        """
        if self.player["Stats"]["Current HP"] > self.player["Stats"]["Max HP"]:
            self.player["Stats"]["Current HP"] = self.player["Stats"]["Max HP"]

    def use_potion(self):
        """
        Allows the player to use a potion during combat.

        Returns:
        - True if a potion is used.
        - False if no potion is used.
        """
        while True:
            self.print_player_potions()
            choice = get_choice(4)

            if choice == 4:  # If player chooses to go back to the combat menu
                return False  # No potion was used

            potion_names = list(player["Potions"].keys())
            selected_potion = potion_names[choice - 1]

            if player["Potions"][selected_potion]["Quantity"] > 0:
                heal_amount = player["Potions"][selected_potion]["Heal Amount"]
                player["Stats"]["Current HP"] += heal_amount
                self.handle_overheal()
                player["Potions"][selected_potion]["Quantity"] -= 1
                print()  # Prints an empty line for separation
                print(f" You used a {selected_potion} and"
                      f" healed for {heal_amount} HP"
                      f" back to {self.player['Stats']['Current HP']} ❤️  !")
                return True  # Potion was used

            else:
                print()  # Prints an empty line for separation
                print(f" 🚫  You don't have any {selected_potion} left!")

    def display_combat_info(self):
        """
        Compares stats of player and enemy
        """
        print("PLAYER\t\t\tENEMY")
        print_horizontal_line()
        print(f" Name: {self.player['Stats']['Name']}\t\tName: "
              f"{self.enemy['Name']}")
        print(f" HP: {self.player['Stats']['Max HP']}\t\tHP: "
              f"{self.enemy['Max HP']}")
        print(f" Attack: {self.player['Stats']['Atk']}\t\tAttack: "
              f"{self.enemy['Atk']}")
        print(f" Defence: {self.player['Stats']['Def']}\t\tDefence: "
              f"{self.enemy['Def']}")
        print(f" Crit: {self.player['Stats']['Crit']}\t\tCrit: "
              f"{self.enemy['Crit']}")
        print(f" \t\t\tRun: {self.enemy['Run']}")

    def player_combat_defeat(self):
        """
        Actions to take when the player is defeated in combat
        """
        print(f" The {self.enemy['Name']} hit you with a killing blow!")
        player_defeat()

    def enemy_attack(self):
        """
        Handles the enemy's attack on the player.
        """
        dmg_to_player = round(
            (self.enemy["Atk"] - self.player
             ["Stats"]["Def"]) * self.dmg_roll()
        )
        if critical_hit(self.enemy):
            dmg_to_player = round(dmg_to_player * 1.5)
            print(random.choice(enemy_critical_messages))
        if dmg_to_player > 0:
            self.player["Stats"]["Current HP"] -= dmg_to_player
            print(f" 🛡️  The {self.enemy['Name']}"
                  f" dealt {dmg_to_player}"
                  " damage to you!")
        else:
            print(f" The {self.enemy['Name']} did no damage."
                  " 🛡️🛡️🛡️  Your defense is too high!")

        if self.player['Stats']['Current HP'] <= 0:
            self.player_combat_defeat()

    def dmg_roll(self):
        """
        Rolls a random multiplier between 0.8 and 1.2

        Returns:
        - A random float between 0.8 and 1.2.
        """
        multiplier = ((random .randint(0, 40) - 20) + 100) / 100
        return multiplier

    def combat_loop(self):
        """
        Handles combat
        """
        print(f" ======== COMBAT VS {self.enemy['Name'].upper()} ========")
        while (self.player['Stats']['Current HP'] > 0 and
               self.enemy['Current HP'] > 0):
            print("\n ENEMY IMAGE")
            current_player_hp = int(self.player['Stats']['Current HP'])
            player_maxhp = int(self.player['Stats']['Max HP'])
            current_enemy_hp = int(self.enemy['Current HP'])
            enemy_maxhp = int(self.enemy['Max HP'])
            print(f"\n{self.player['Stats']['Name']} HP:"
                  f" {current_player_hp}"
                  f"/{player_maxhp} ❤️  |"
                  f" {self.enemy['Name']} HP:"
                  f" {current_enemy_hp}"
                  f"/{enemy_maxhp} 🖤")
            print("\n 🗡️  1. Attack"
                  "\n 🧪  2. Item"
                  "\n 📜  3. Info"
                  "\n 💨  4. Run")
            choice = get_choice(4)
            if choice == 1:
                if critical_hit(self.player):
                    dmg_to_enemy = round(
                        (self.player['Stats']["Atk"] - (self.enemy["Def"] *
                         2/3)) * self.dmg_roll())
                    dmg_to_enemy = round(dmg_to_enemy * 1.5)
                    print(random.choice(player_critical_messages))
                else:
                    dmg_to_enemy = round(
                        (self.player['Stats']["Atk"] - self.enemy["Def"])
                        * self.dmg_roll())

                if dmg_to_enemy > 0:
                    self.enemy['Current HP'] -= dmg_to_enemy
                    print(f" 🗡️  You dealt {dmg_to_enemy} damage to the"
                          f" {self.enemy['Name']}!")
                    if self.enemy['Current HP'] <= 0:
                        self.player_combat_victory()
                else:
                    print(" 🚫  You did no damage."
                          " The enemy's defense is too high!")

                if self.enemy['Current HP'] > 0:
                    self.enemy_attack()

            elif choice == 2:
                if self.use_potion():
                    self.enemy_attack()

            elif choice == 3:
                self.display_combat_info()

            elif choice == 4:
                if player_run_away(self.enemy['Run']):
                    print(" 💨  You successfully ran away!")
                    print_horizontal_line()
                    global battle_result  # pylint: disable=global-statement
                    battle_result = "Run"
                    return battle_result  # Exits the combat loop

                else:
                    print(f" 🚫  The {self.enemy['Name']} blocked your way."
                          " You couldn't escape.")
                    self.enemy_attack()


def player_defeat():
    """
    Displays the dead message and asks the player if they'd like to retry
    """
    print("\n 💀 YOU DIED 💀")
    print("\n Continue?"
          "\n 👍 1. Yes!"
          "\n 👎 2. No..I give up..")
    choice = get_choice(2)
    if choice == 1:
        main()
    elif choice == 2:
        print(" Not everyone is suited to be a Hero \U0001F44E Goodbye!")
        exit()


def print_horizontal_line():
    """
    Prints 40 dashes on the screen effectively creating a visual line that
    separates content
    """
    print()  # Prints an empty line for separation
    print(" " + "-" * 39)
    print()  # Prints an empty line for separation


def print_player_info_menu():
    """
    This is used to avoid repeating the same code
    """
    print(" ===== STATS =====")
    print(f" Name: {player['Stats']['Name']}")
    print(f" Max HP: {player['Stats']['Max HP']}")
    print(f" Current HP: {player['Stats']['Current HP']}")
    print(f" Attack: {player['Stats']['Atk']}")
    print(f" Defence: {player['Stats']['Def']}")
    print(f" Crit: {player['Stats']['Crit']}")
    print(f" Gold: {player['Stats']['Gold']}")
    print_horizontal_line()
    print(" ===== POTIONS =====")
    print(
        f" Potion: {player['Potions']['Potion']['Quantity']}"
        f"\t\t Heal Amount: {player['Potions']['Potion']['Heal Amount']}")
    print(
        f" Mega Potion: {player['Potions']['Mega Potion']['Quantity']}"
        f"\t\t Heal Amount: "
        f"{player['Potions']['Mega Potion']['Heal Amount']}")
    print(
        f" Ultra Potion: {player['Potions']['Ultra Potion']['Quantity']}"
        f"\t Heal Amount:"
        f" {player['Potions']['Ultra Potion']['Heal Amount']}")
    print_horizontal_line()
    print(" ===== EQUIPMENT =====")
    print()  # Prints an empty line for separation

    weapon_name = (
        player['Equipment']['Weapon']['Name']
        if player['Equipment']['Weapon']
        else 'No Equipment'
    )

    weapon_atk_stat = (
        player['Equipment']['Weapon']['Atk']
        if player['Equipment']['Weapon']
        else '0'
    )

    weapon_crit_stat = (
        player['Equipment']['Weapon']['Crit']
        if player['Equipment']['Weapon']
        else '0'
    )

    shield_name = (
        player['Equipment']['Shield']['Name']
        if player['Equipment']['Shield']
        else 'No Equipment'
    )

    shield_def_stat = (
        player['Equipment']['Shield']['Def']
        if player['Equipment']['Shield']
        else '0'
    )

    shield_hp_stat = (
        player['Equipment']['Shield']['Max HP']
        if player['Equipment']['Shield']
        else '0'
    )

    helmet_name = (
        player['Equipment']['Head']['Name']
        if player['Equipment']['Head']
        else 'No Equipment'
    )

    helmet_def_stat = (
        player['Equipment']['Head']['Def']
        if player['Equipment']['Head']
        else '0'
    )

    helmet_hp_stat = (
        player['Equipment']['Head']['Max HP']
        if player['Equipment']['Head']
        else '0'
    )

    body_name = (
        player['Equipment']['Body']['Name']
        if player['Equipment']['Body']
        else 'No Equipment'
    )

    body_def_stat = (
        player['Equipment']['Body']['Def']
        if player['Equipment']['Body']
        else '0'
    )

    body_hp_stat = (
        player['Equipment']['Body']['Max HP']
        if player['Equipment']['Body']
        else '0'
    )

    legs_name = (
        player['Equipment']['Legs']['Name']
        if player['Equipment']['Legs']
        else 'No Equipment'
    )

    legs_def_stat = (
        player['Equipment']['Legs']['Def']
        if player['Equipment']['Legs']
        else '0'
    )

    legs_hp_stat = (
        player['Equipment']['Legs']['Max HP']
        if player['Equipment']['Legs']
        else '0'
    )

    boots_name = (
        player['Equipment']['Boots']['Name']
        if player['Equipment']['Boots']
        else 'No Equipment'
    )
    boots_def_stat = (
        player['Equipment']['Boots']['Def']
        if player['Equipment']['Boots']
        else '0'
    )

    boots_hp_stat = (
        player['Equipment']['Boots']['Max HP']
        if player['Equipment']['Boots']
        else '0'
    )

    hands_name = (
        player['Equipment']['Hands']['Name']
        if player['Equipment']['Hands']
        else 'No Equipment'
    )

    hands_def_stat = (
        player['Equipment']['Hands']['Def']
        if player['Equipment']['Hands']
        else '0'
    )

    hands_hp_stat = (
        player['Equipment']['Hands']['Max HP']
        if player['Equipment']['Hands']
        else '0'
    )

    print(f" Weapon: {weapon_name}\t\t Attack: +{weapon_atk_stat}")
    print(f"\t\t\t\t Crit: +{weapon_crit_stat}")
    print(f"\n Shield: {shield_name}\t\t Defence: +{shield_def_stat}")
    print(f"\t\t\t\t Max HP: +{shield_hp_stat}")
    print(f"\n Head: {helmet_name}\t\t Defence: +{helmet_def_stat}")
    print(f"\t\t\t\t Max HP: +{helmet_hp_stat}")
    print(f"\n Body: {body_name}\t\t Defence: +{body_def_stat}")
    print(f"\t\t\t\t Max HP: +{body_hp_stat}")
    print(f"\n Legs: {legs_name}\t\t Defence: +{legs_def_stat}")
    print(f"\t\t\t\t Max HP: +{legs_hp_stat}")
    print(f"\n Boots: {boots_name}\t\t Defence: +{boots_def_stat}")
    print(f"\t\t\t\t Max HP: +{boots_hp_stat}")
    print(f"\n Hands: {hands_name}\t\t Defence: +{hands_def_stat}")
    print(f"\t\t\t\t Max HP: +{hands_hp_stat}")


def player_rest(percentage_recovery):
    """
    When the option to rest is available, this function allows the player
    to recover a specified percentage of their Max HP without exceeding
    the Max HP value.

    Parameters:
    - percentage_recovery: float representing the amount of Max HP healed
                           For Example: 0.5 = 50% of Max HP healed.

    Returns:
    - An integer wich represent the amount of HP healed
    """
    current_hp = player["Stats"]["Current HP"]
    max_hp = player["Stats"]["Max HP"]
    hp_recovery = round(max_hp * percentage_recovery)

    # Ensures that the current HP doesn't exceed max HP
    new_hp = min(current_hp + hp_recovery, max_hp)

    hp_healed = new_hp - current_hp
    player["Stats"]["Current HP"] = new_hp

    return hp_healed


def intro():
    """
    Provides the initial game introduction to the player.

    Prompts the player with the choice of starting the game,
    reading the rules or exiting the game.
    """
    reset_player()
    reset_enemy()
    print(" 📜  Welcome to Text-Land!"
          "\n In a realm where words wield power and choices shape destinies,"
          "\n you find yourself at the crossroads of fate."
          "\n A mysterious world filled with unknown dangers,"
          " captivating stories,\n and hidden treasures beckons you.")
    print(" As you embark on this epic journey, remember:"
          " every choice matters!"
          "\n Your decisions will carve out your path, lead you to treasures,"
          "\n pit you against formidable foes, and present riddles"
          "\n that challenge your intellect."
          "\n But fear not, in Text-Land, even the most ordinary adventurers"
          "\n can become legends."
          "\n Do you have what it takes to conquer the challenges,"
          " decipher the"
          " mysteries,\n and emerge as the hero of Text-Land?"
          "\n Or will you be its Doom?"
          "\n\n 1. 🛡️  Enter your name and begin your adventure."
          "\n\n 2. 📘  Read about the rules of Text-Land."
          "\n\n 3. 🚪  Exit to the real world.")

    choice = get_choice(3)
    if choice == 1:
        player_name_choice()

    elif choice == 2:
        rules()

    else:
        print(" Not everyone is suited to be a Hero \U0001F44E Goodbye!")
        exit()


def first_scene():
    """
    This is going to be the first scene and
    serves as an introduction to the choice system
    """
    print_horizontal_line()
    print(" Blinking awake, you find yourself by a serene lake."
          " How did you end up here?"
          "\n Your memory's a blur.\n As you're piecing things together,"
          " a distant scream of help shatters\n the tranquility."
          " Something's not right!"
          "\n What will you do?")
    while True:
        print("\n 👣  1. Investigate the source of the scream."
              "\n\n 💤  2. The screams dont concern you."
              " You rather go back to sleep."
              "\n\n 📖  3. Player Info")

        choice = get_choice(3)
        if choice == 1:

            break
        elif choice == 2:
            first_scene_game_over()
        elif choice == 3:
            print_player_info_menu()


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
    This is going to be the second scene wich serves
    as an introduction to the combat mechanic.
    The fight is intended to be easy to win.
    """
    print(" Rushing towards the scream, you discover a goblin threatening"
          " a merchant beside his cart dragged by a horse."
          '\n Goblin: "Hand over your gold, human!"'
          '\n Merchant (spotting you and with hopeful eyes): "Stranger!'
          ' Please, help me!"'
          "\n The goblin, hearing the merchant's plea, whirls around to"
          " face you,\n his eyes narrowed.")
    print("\n Goblin: \"Mind your own business,\" he snarls,"
          " \"or you're next!\"")
    while True:
        print("\n ⚔️  1. Charge the goblin head on!"
              "\n\n 🤷  2. The goblin is right, this is not your problem."
              "\n\n 📖  3. Player Info")
        choice = get_choice(3)

        if choice == 1:
            print("\n The merchant's eyes widen in hope as you take a stance "
                  "between him\n and the menacing creature."
                  "\n With a determined glint in your eyes, you charge towards"
                  " the goblin.")
            fight_pause_and_continue()
            reset_enemy()
            battle = Combat(player, enemy["Goblin"])
            battle.combat_loop()
            break
        elif choice == 2:
            print("\n As you decide to turn around, hoping to distance "
                  "yourself from the goblin,")
            print("\n the soft padding of its feet grows rapidly louder"
                  "behind you.\n You glance over your shoulder.")
            print('\n You see just in time the goblin\'s wicked grin,'
                  '\n eyes alight with malicious intent.')
            print('\n "Thought you could ignore me, did you?" the goblin'
                  '  sneers.\n Easier prey than I thought!"')
            print('\n With no other choice, you brace yourself'
                  " to fend off the goblin.")
            fight_pause_and_continue()
            reset_enemy()
            battle = Combat(player, enemy["Goblin"])
            battle.combat_loop()
            break
        elif choice == 3:
            print_player_info_menu()


def third_scene():
    """
    This is going to be the third scene after defeating the goblin
    """
    print_horizontal_line()
    print(" Catching his breath, the merchant straightens up and beams at "
          'you.\n "Thank you, kind stranger. Without your intervention, '
          '\n I fear what that goblin would have done to me."'
          """\n He extends a hand in gratitude, "The name's Elidor"""
          " Silversmile,\n but folk around these parts call me"
          '\n Elidor Coinstride, on account of my dealings and wares."')
    print()  # Prints an empty line for separation
    print("\n Taking a moment to observe Elidor, it's clear that"
          " he has Halfling origins.\n Standing shorter than most."
          "\n His stature is a bit rotund, giving him a cherubic "
          "appearance.\n Pointy ears peek out from beneath a cascade of white "
          "hair,\n accentuated by prominent sideburns that frame his face."
          "\n Beside him stands a magnificent white horse, its gray mane"
          " flowing gracefully. \n The contrast between the majestic steed and"
          " the diminutive merchant\n creates a heartwarming scene."
          """\n "A beautiful creature, isn't she?" Elidor remarks, noticing"""
          """ your admiration. \n "She's been """
          'my loyal companion for years, traveling through thick and thin."')
    while True:
        print_horizontal_line()
        print()  # Prints an empty line for separation
        print(' 🐴  1. "She is indeed beautiful, how are you faring?'
              '\n\n 🤲  2. "I\'m glad you\'re safe, but a reward'
              ' would be appreciated."')
        choice = get_choice(2)
        if choice == 1:
            print("\n Elidor looks at you gratefully and says, "
                  '"Thank you for asking, kind traveler.'
                  "\n It\'s not every day you find someone so considerate. "
                  "\n We are both well, thanks to you.\n The road has been"
                  " hard, but having Medea, my horse, by my side makes it"
                  ' easier.\n Please, take this as a token of my gratitude.'
                  "\n He hands you a small pouch of coins.")
            player["Stats"]["Gold"] += 50
            print("\n You obtained 50 Gold  💰 !"
                  " You can carry gold in your pouch from now on.")
            print()  # Prints an empty line for separation
            break
        elif choice == 2:
            print("\n The halfling seems a bit taken aback by your forwardness"
                  '.\n After a moment of hesitation, he says, '
                  '"Well, I suppose it\'s fair to ask for\n compensation after'
                  ' such a deed.\n He reluctantly'
                  " hands you a slightly large pouch of coins.")
            player["Stats"]["Gold"] += 75
            print("\n You obtained (basically extorted..) 75 Gold  💰 !"
                  "\n You can carry gold in your pouch from now on.")
            print()  # Prints an empty line for separation
            break


def fourth_scene():
    """
    This is the fourth scene in wich the merchant will join,
    this will serve as an end to the "tutorial" like phase.
    """
    print_horizontal_line()
    print(" As you continue to converse, Elidor starts packing up his cart. "
          "\n The clinking of vials and the rustling of cloth can be heard.")
    print('\n \"You know, I\'m headed to the city of Veradia. '
          "It's a big, bustling place\n and I've some important business"
          "there.")
    print("\n Delivering a certain... package, so to speak. It's a long "
          "journey and,\n after the goblin incident, I realize I could use "
          "some protection.")
    print("\n Given how adeptly you handled that goblin,"
          " would you be interested\n in "
          "accompanying me?\n I'm willing to pay for your services and, "
          "of course, my shop's at your\n disposal for resupply.\"")
    print()  # Prints an empty line for separation
    print("\n You ponder on his request. You really don't have any idea where"
          " you are\n or where you're headed.\n Would it be such a bad idea to"
          " accompany him?")

    while True:
        print("\n\n 👍  1. \"Certainly, Elidor. It'll be my pleasure to"
              " accompany you.\"")
        print("\n\n 👎  2. \"Thanks for the offer, but I must go my own way.\"")
        choice = get_choice(2)

        if choice == 1:
            print("\n Elidor grins, looking visibly relieved. \"Excellent!"
                  " With your combat skills "
                  "and\n my... ahem, 'tricks of the trade', I'm sure we'll"
                  " make it to the city safely.\"")
            break
        elif choice == 2:
            print("\n Elidor raises an eyebrow, looking a tad confused."
                  "\n \"Well, if you don't want to come with me, "
                  "then it only makes sense that\n I'll have to go with you!"
                  "\n Let's set forth, friend.\""
                  "\n You try to piece together the logic of what Elidor just"
                  " said and come up blank."
                  " Before you can even react, he's already on his way, "
                  "mounting Medea and waving\n for you to follow."
                  " Wasn't he supposed to follow you?")
            break

    print("\n \"By the way,\" Elidor interjects, \"I usually rely on my "
          "intuition for travel,\n but seeing as you're my protector now, "
          "I'll leave the decisions up to you."
          "\n There's a small town on the way; we should aim to reach it next."
          "\n You decide which way we should take"
          ' to best reach our destination."')


def pandora_box():
    """
    Rolls for an item from the Pandora Box
    """
    roll = random.randint(1, 10)

    chosen_pandora_item = pandora_items[roll]

    if chosen_pandora_item["Status"]:
        print(" The Pandora's Box gives you 2 Ultra Potions!")
        player["Potions"]["Ultra Potion"]["Quantity"] += 2
    else:
        chosen_pandora_item_name = chosen_pandora_item["Name"]
        print(" 🎉 The Pandora's Box grants you "
              f"the {chosen_pandora_item_name}! 🎉")
        print(" 📖 Check the Player's Info to see what it does.")
        chosen_pandora_item["Status"] = True


def elidor_shop():
    """
    A shop available to the player in most of the scenes
    """
    print(" ===== ELIDOR SHOP =====")
    print('\n Random elidor message')
    print_horizontal_line()
    while True:
        print(f" Player Gold: {player['Stats']['Gold']} 💰")
        print("\n 🧪 1. Potion(Heal 20): 20 Gold")
        print(" 🧪 2. Mega Potion(Heal 50): 40 Gold")
        print(" 🧪 3. Ultra Potion(Heal 150): 100 Gold")
        print(" 📦 4. Pandora's Box (Random Item): 200 Gold")
        print(" 🔙 5. Go back")
        choice = get_choice(5)
        if choice == 1:
            if player["Stats"]["Gold"] >= 20:
                player["Stats"]["Gold"] -= 20
                player["Potions"]["Potion"]["Quantity"] += 1
                print(" You purchased a Potion!")
            else:
                print(" ❌ You don't have enough Gold.")
        elif choice == 2:
            if player["Stats"]["Gold"] >= 40:
                player["Stats"]["Gold"] -= 40
                player["Potions"]["Mega Potion"]["Quantity"] += 1
                print(" You purchased a Mega Potion!")
            else:
                print(" ❌ You don't have enough Gold.")
        elif choice == 3:
            if player["Stats"]["Gold"] >= 100:
                player["Stats"]["Gold"] -= 100
                player["Potions"]["Potion"]["Quantity"] += 1
                print(" You purchased an Ultra Potion!")
            else:
                print(" ❌ You don't have enough Gold.")
        elif choice == 4:
            if player["Stats"]["Gold"] >= 200:
                player["Stats"]["Gold"] -= 200
                pandora_box()
                print(" You tried your luck with Pandora's Box!")
            else:
                print(" ❌ You don't have enough Gold.")
        elif choice == 5:
            break


def fifth_scene():
    """
    Fifth Scene in wich branches into 3 different paths
    """
    print_horizontal_line()
    print("\n As you and Elidor travel together, the path ahead"
          "forks into three\n distinct routes.")
    print("\n To the right, the gentle sound of a river is heard"
          " and the shimmering water\n can be seen in the distance.")
    print("\n Straight ahead lies the main road, well-trodden and marked with"
          " milestones\n indicating the way to the closest town.")
    print("\n The left path dives deep into a dense, dark forest. Amongst the "
          "trees,\n tall grasses sway gently, reaching up to a person's"
          " height,\n shading the path from the midday sun.")

    while True:
        print("\n 🌊  1. Head towards the river route.")
        print("\n\n 🛣️  2. Stick to the main road.")
        print("\n\n 🌲  3. Venture into the forest.")
        print("\n\n 💰  4. Elidor Shop")
        print("\n\n 📖  5. Player Info")
        choice = get_choice(5)

        if choice == 1:
            print("\n With the river by your side offering a soothing ambiance"
                  ", you and Elidor start your journey on the river route.")
            print("\n Elidor seems pleased with the decision, the fresh scent "
                  "of the river lifting his spirits.")
            river_first_scene()
            break
        elif choice == 2:
            print("\n Deciding to stick to what seems safest, you and Elidor"
                  "\n continue on the main road.")
            main_road_path()
            break
        elif choice == 3:
            print("\n Feeling adventurous, you decide to delve into"
                  " the woods.")
            print(" Were it not for Medea, Elidor would be completely "
                  "obscured by the tall grass.")
            forest_path()
            break
        elif choice == 4:
            elidor_shop()
        elif choice == 5:
            print_player_info_menu()


def handle_loot_world(*items_found):
    """
    Handles loot found in the world
    outside of combat
    """
    for item_name in items_found:
        item_detail = item_database.get(item_name)
        equip_item(item_detail)


def equip_item(item_detail):
    """
    Equips automatically better equipment
    """
    item_type = item_detail["Type"]
    item_name = item_detail["Name"]

    currently_equipped = player["Equipment"].get(item_type, None)

    def calculate_stat_change(new_item, old_item=None):
        """
        Calculates the stat change between the newly found item
        and the old equipped one if any is equipped
        """
        change = {}
        for stat, value in new_item.items():
            if stat != "Type" and stat != "Name" and stat != "Droprate":
                if old_item:
                    change[stat] = value - old_item.get(stat, 0)
                else:
                    change[stat] = value

        return change

    if currently_equipped:
        stat_change = calculate_stat_change(
            item_detail, currently_equipped)

        if sum(stat_change.values()) > 0:
            player["Equipment"][item_type] = item_detail
            for stat, change in stat_change.items():
                player["Stats"][stat] += change
            print()
            print(f" 🎉  You found and equipped {item_name}  🎉")
        else:
            print()
            print(f" 🚫  Found {item_name}({item_detail['Type']}), but "
                  " current equipment is better!")
    else:
        player["Equipment"][item_type] = item_detail
        for stat, value in item_detail.items():
            if stat != "Type" and stat != "Name" and stat != "Droprate":
                player["Stats"][stat] += value
        print()
        print(f" 🎉  You found and equipped {item_name}"
              f"({item_detail['Type']})!  🎉")


def river_first_scene():
    """
    Handles the first scene in the river
    """
    print_horizontal_line()
    print(" As you walk alongside the river, the calmness of the water, along"
          " with the rhythmic sound of the current,"
          " gives you a sense of peace.")
    print(" The sun glitters on the water's surface, and the air is filled"
          " with the sweet scent of blooming flowers.")
    print("\n Elidor bends down, picks up a smooth, flat stone, and with"
          " a mischievous glint in his eyes, challenges you.")
    print('"How about a little contest? Let\'s see who can skip the stone'
          ' the furthest."')
    while True:
        print('\n 💪  1. "Sure, I\'m up for a challenge!"')
        print('\n\n 🌊 🌳  2. "No thanks, I\'d rather just enjoy the scenery."')
        print("\n\n 💰  3. Elidor Shop")
        print("\n\n 📖  4. Player Info")
        choice = get_choice(4)
        if choice == 1:
            print(" With a confident smirk, you take the stone from Elidor."
                  "\n Positioning yourself, you give it a strong flick of the "
                  "wrist.\n To your surprise, after the second skip, the stone"
                  " seems to hit something solid mid-air and drops into the"
                  " water with a splash.\n Both you and Elidor exchange"
                  " puzzled glances.")
            print("\n Approaching the spot, you extend your hand and feel an"
                  " invisible barrier."
                  "\n The air around it vibrates with magic. Elidor murmurs,"
                  '"It\'s an illusion spell... something is being concealed'
                  ' here."')
            print('\n "What should we do?"')
            while True:
                print("\n 🔍  1. Examine the hidden spot")
                print("\n\n 🚫  2. Walk away, it might be risky")
                print("\n\n 💰  3. Elidor Shop")
                print("\n\n 📖  4. Player Info")
                choice = get_choice(4)
                if choice == 1:
                    print("\n After a moment of concentration, Elidor chants a"
                          " soft incantation, and the illusion starts to fade,"
                          " revealing a hidden alcove.\n Inside, you find "
                          "a mysterious, ancient-looking chest.")
                    print("\n Inside, you find a bejeweled Long Sword.")
                    print(" It may not be much but you feel like it could make"
                          " your life easier")
                    print(" It might not be a marvelous treasure, but it feels"
                          " like it could be quite useful.")
                    print("\n You ponder why someone would go through so much"
                          " trouble to hide a mere sword.")
                    handle_loot_world("Long Sword")
                    while True:
                        print('\n Elidor glances around warily and leans in to'
                              ' whisper, "We should leave quickly. The one '
                              'responsible for the illusion might return."')
                        print("\n 🚶  1. He is right, we should leave.")
                        print("\n\n 💰  2. Elidor Shop")
                        print("\n\n 📖  3. Player Info")
                        choice = get_choice(3)
                        if choice == 1:
                            river_second_scene()
                            break
                        elif choice == 2:
                            elidor_shop()
                        elif choice == 3:
                            print_player_info_menu()
                    break
                elif choice == 2:
                    print('\n "There are things in this world best left'
                          ' undiscovered," Elidor murmurs, his gaze lingering'
                          " on the concealed spot for a moment longer.")
                    print("\n You nod, feeling a mixture of relief and"
                          ' curiosity. "There\'s a reason it was hidden, "'
                          'you reason aloud, "and we might not want to know'
                          ' why."')
                    print("\n With a final glance over your shoulder, you and"
                          " Elidor continue along the river, the gentle sounds"
                          " soon drowning out the unease. The path may have"
                          " presented an unexpected mystery, but sometimes,"
                          " it's best to choose safety over curiosity.")
                    while True:
                        print("\nn What to do now?")
                        print("\n 🚶  1. Let us leave this place behind")
                        print("\n\n 💰  2. Elidor Shop")
                        print("\n\n 📖  3. Player Info")
                        choice = get_choice(3)
                        if choice == 1:
                            print(" With a nod to Elidor, you decide it's time"
                                  " to move on. The two of you gather your"
                                  " belongings, leaving the mysteries of the"
                                  " riverbank behind as you continue your"
                                  " journey.")
                            river_second_scene()
                            break
                        elif choice == 2:
                            elidor_shop()
                        elif choice == 3:
                            print_player_info_menu()
                    break
                elif choice == 3:
                    elidor_shop()
                elif choice == 4:
                    print_player_info_menu()
        elif choice == 2:
            print(" You smile and shake your head, choosing instead to sit and"
                  " relax by the riverside."
                  "\n The journey continues peacefully as you absorb the"
                  " serenity around you.")
        elif choice == 3:
            elidor_shop()
        elif choice == 4:
            print_player_info_menu()

        break


def river_second_scene():
    """
    Second scene of river
    """
    print("This is the second scene")


def main_road_path():
    """
    This will be the main road branch function
    """
    print(" \n As you travel along the main road, you stumble upon a dramatic"
          " scene.")
    print(" A colorful caravan, ambushed by a gang of goblins,"
          "\n fights desperately for survival.")
    print("\n The goblins, noticing you, turn hostile, leaving you "
          "with no choice\n but to join the fray.")
    print(" As you fend off the goblins, a chilling realization "
          "dawns upon you.\n One of these goblins,"
          " the very same goblin you encountered before, "
          "\n was merely a member of this malevolent gang.")
    print("\n Now, they are here, part of this brutal assault.")
    print(" The caravan's fate hangs in the balance as the clash intensifies,")
    print(" and your actions will determine its outcome.")
    fight_pause_and_continue()
    reset_enemy()
    battle = Combat(player, enemy["Goblin"])
    battle.combat_loop()
    print_horizontal_line()
    print(" After you've slain one of their comrades,"
          " another goblin witnessed the scene.")
    print(" He is bent on avenging his comrade and"
          " ignores the caravan raid to charge you.")
    print(" Amidst the tense battle, Elidor swiftly tosses a potion your way"
          "\n and yells,"
          ' "This one\'s on the house, kiddo!"')
    player["Potions"]["Mega Potion"]["Quantity"] += 2
    print("\n 🎉 You obtained 2 Mega Potions! 🎉")
    print("\n Before you can utter a word to Elidor, the looming"
          " goblin is upon you!")
    fight_pause_and_continue()
    reset_enemy()
    battle = Combat(player, enemy["Goblin"])
    battle.combat_loop()
    print_horizontal_line()
    print(" With the fallen goblin at your feet, you gasp for breath, "
          "\n only to witness another goblin's cruel act.")
    print("\n This vile creature has just taken the life of one of the men"
          "\n and now menaces a defenseless woman.")
    print("\n Without hesitation, you summon your remaining strength "
          "\n and charge at the goblin, desperate to reach her in time.")
    fight_pause_and_continue()
    reset_enemy()
    battle = Combat(player, enemy["Goblin"])
    battle.combat_loop()
    print_horizontal_line()
    print(" With the goblin vanquished, your heart sinks as you realize"
          "\n he managed to wound the woman before your arrival.")
    print(" Elidor swiftly tends to her injury, and amidst the tension, "
          "\n a commanding shout pierces the air!")
    print('\n "You there, the assailant of my brethren.'
          ' I shall end your life!"')
    print("\n You pivot, and there stands a goblin, unlike any you've"
          "encountered.\n Taller, adorned in menacing spiky armor,")
    print(" and wielding a colossal sword matching his formidable stature."
          "\n He must be the gang's chief. Defeating him")
    print(" could quell this bloodshed.")
    print(" But there's no time for contemplation; the chief charges you,"
          "\n and a battle with this fearsome foe is inevitable.")
    fight_pause_and_continue()
    reset_enemy()
    battle = Combat(player, enemy["Goblin Chief"])
    battle.combat_loop()
    print_horizontal_line()
    print(" The caravan members gather around you, their faces etched"
          " with gratitude\n and sorrow.")
    print("\n What seems their leader steps forward and speaks with a heavy "
          'heart,\n "We come from faraway lands,'
          'seeking a better future in the nearby town.'
          "\n Our journey was fraught with peril, and we were ambushed")
    print("\n by those vile goblins. It was you who saved us,\n and for that, "
          'we are deeply thankful."')
    print(" The leader looks down sadly and continues, 'We had hoped to start"
          " anew,\n but we don't have much left.")
    print(" We can't offer you gold or riches, but know that our gratitude"
          " is boundless.'")
    print(" The caravan members share somber glances, and you see tears"
          " in their eyes.")
    print(' The leader concludes, "We\'ll stay behind to mourn our lost '
          'family members\n and tend to the wounded."')
    print(' "We don\'t want to hold you back.\n May the'
          ' road ahead be kind to you, brave traveler."')
    main_road_path_guard_scene()


def main_road_path_guard_scene():
    """
    Second scene of main road path branch
    """
    print_horizontal_line()
    print("\n After a few hours of walking along the main road, the outline of"
          " a town emerges on the horizon.")
    print("\n A fortified stone wall encircles it, with a large wooden gate"
          " marking the entrance.")
    print("\n As you and Elidor approach the town gate, a guard in polished"
          "\n armor steps forward, halting your progress.")
    print('\n "Halt! All newcomers must be inspected before entering",'
          " the guard states firmly.")
    print("\n While the guard is about to proceed with the inspection, his"
          " eyes fall on the chief's gauntlet you possess.")
    print('\n "Wait a minute... Is that the goblin chief\'s gauntlet?'
          ' Have you encountered the goblin gang?" he asks, curiosity evident'
          " in his voice.")

    while True:
        print("\n\n 👍  1. Confirm that you defeated the goblin chief.")
        print("\n 👎  2. Deny and say you found the gauntlet.")
        choice = get_choice(2)

        if choice == 1:
            print("\n You and Elidor explain what happened to the guard.")
            print("\n The guard's face lights up with a broad smile."
                  '" Those goblins have been a thorn in our side for too long!'
                  ' They\'ve been raiding our commercial roads for months."')
            print("\n In recognition of your deed, the guard hands you a pouch"
                  " containing 100 gold coins."
                  '"There was a bounty on the chief\'s head.'
                  ' This is yours now."')
            print("\n You obtained 100 Gold  💰  from the guard!")
            player["Stats"]["Gold"] += 100
            print("\n Furthermore, he hands you a special coupon."
                  'This is for the town shop. They\'ll give you a good deal'
                  ' with this."')
            print()
            print(" 🎉  You obtained a Shop Coupon!  🎉")
            print("\n With a warm gesture, the guard welcomes you into the"
                  " town.")
            global shop_coupon  # pylint: disable=global-statement
            shop_coupon = True
            town_scene()
            break
        elif choice == 2:
            print('\n "I just found it," you reply hesitantly.')
            print("\n The guard looks skeptical but decides not to push the"
                  ' matter further.\n "Very well, but we\'re keeping an eye'
                  ' on"'
                  ' you. Enter the town, but cause no trouble."')
            print("\n Although the guard's suspicions linger, you're granted "
                  "entry into the town."
                  "\n You step through the gate with a slight unease in your"
                  " step.")
            town_scene()
            break


def forest_path():
    """
    This handles the forest scenario
    """
    print_horizontal_line()
    print("\n While traversing the tall grass, the rustling of leaves draws"
          " your attention.")
    print("\n Emerging from the bushes is a small, yellow-furred creature with"
          " rosy cheeks and a lightning-shaped tail.")
    print("\n It looks startled, eyes wide as it assesses you. You're not"
          " sure if it's about to attack or bolt away.")
    print("\n As you cautiously approach the creature, you notice jolts of "
          "lightning emanating from its rosy cheeks, indicating its distress.")
    print("\n The fact that this creature can harness what appears to be"
          " elemental magic is a cause for concern.")
    while True:
        print("\n 🏹  1. Preemptively attack the creature."
              "\n        It is maybe better to be safe than sorry.")
        print("\n 🚶  2. Try to ignore it and continue on your path.")
        choice = get_choice(2)
        if choice == 1:
            print(" As you unsheath your weapon hesitantly,"
                  " doubt clouds your mind."
                  "\n Sensing your aggressive intent, the creature's cheeks"
                  " spark more intensely,"
                  "\n emitting a symphony of crackling lightning bolts."
                  "\n The decision seems to have been made for you."
                  "\n It's do or die now!!")
            fight_pause_and_continue()
            reset_enemy()
            battle = Combat(player, enemy["Sparky Tail"])
            battle.combat_loop()
            if battle_result == "Victory":
                forest_path_second_scene(True)
                break
            elif battle_result == "Run":
                forest_path_second_scene(False)
                break
        elif choice == 2:
            forest_path_second_scene(False)
            break


def forest_path_second_scene(defeated_creature):
    """
    Creates a scenario depending on the battle result
    """
    if defeated_creature:
        print("\n The remnants of the battle linger in the air, and Sparky"
              " Tail's defeated form serves as a"
              " somber reminder of the confrontation.")
        print("\n You find yourself surrounded by tall grass, "
              "the direction you came from is clear."
              "\n The serenity of the forest contrasts with the adrenaline"
              " still coursing through your veins.")
        while True:
            print_horizontal_line()
            print("\n 🚶  1. Push onward through the opposite side of the"
                  "     grassy area,\n hoping to find a way out.")
            print("\n\n 💰  2. Elidor Shop")
            print("\n\n 📖  3. Player Info")
            choice = get_choice(3)
            if choice == 1:
                print("\n Determined, you tread carefully, pushing the tall"
                      " grass aside,\n vigilant"
                      " for any signs of danger or another encounter.")
                break
            elif choice == 2:
                elidor_shop()
            elif choice == 3:
                print_player_info_menu()

        print("\n As you make your way through the forest, you suddenly hear "
              "a rustling...")
        print("\n From behind the dense foliage, a peculiar figure emerges."
              "\n Taller than most humans, with rough, greenish skin, he's"
              " dressed in a rather unconventional mix of attire."
              "\n Wearing a too-tight-for-him cap backward, his pointy ears"
              " poking through,\n and oversized cargo shorts that barely fit"
              " his bulky troll frame, he looks like someone who raided a"
              " teenager's closet.")
        print("\n Around his waist is a belt with numerous tiny cages, each "
              "containing what appears to be a miniature creature."
              "\n He holds a red and white orb-like object in one hand, which"
              " he periodically tosses up and down.")
        print('\n "Yo! Name\'s Brockmire, the Beast Master!" he declares with'
              ' a'
              ' flamboyant pose,\n "And... possibly the world\'s best Beast'
              ' Trainer! What brings you here in my turf?"')
        print_horizontal_line()
        while True:
            print("\n 🖐️  1. Greet him politely.")
            print("\n\n 🗡️  2. Boast about your recent kill.")
            print("\n\n 💰  3. Elidor Shop")
            print("\n\n 📖  4. Player Info")
            choice = get_choice(4)
            if choice == 1:
                print('\n "Oh, hey Brockmire," you greet cautiously,'
                      ' "We were just... uh, passing through?"')
                break
            elif choice == 2:
                print_horizontal_line()
                print('\n With pride swelling in your chest, you announce,'
                      ' "You may be a beast trainer but I am a beast slayer!'
                      '\n Just moments ago, I bested a formidable creature!'
                      '\n It stood no chance against my prowess!"')
                break
            elif choice == 3:
                elidor_shop()
            elif choice == 4:
                print_player_info_menu()

        print('\n Brockmire responds, "Hm... Really? Because it seems'
              ' you\'ve encountered one of my precious critters.'
              '\n My Sparky Tail..."')
        print("\n The white orb begins to glow dimly, resonating with the"
              " residual energy left behind from your confrontation with"
              " the creature.")
        print(" A sinking feeling washes over you as you piece together"
              " that the creature was more than just a wild beast..\n"
              " It was Brockmire's cherished companion. The air grows heavy"
              " with tension,\n Brockmire's eyes darkening with a mix of rage"
              " and sorrow.")
        print_horizontal_line()

        def display_message():
            """
            Test
            """
            print("\n Without another word, he reaches for one of the orbs "
                  "attached to his belt.\n With a deft motion, he releases its"
                  " contents,"
                  " which materialize into a perplexing creature.\n It looks"
                  " like"
                  " a hulking turtle, but instead of a protective shell,"
                  "a vibrant,\n  flower-like bloom emerges from its back.")

            print('\n "Meet Petalback," Brockmire murmurs with a sinister'
                  ' smile,'
                  '\n "And I assure you, it\'s not as gentle as Sparky Tail'
                  ' was."')

            print("\n\n With no other choice left, you brace for combat!")

        def fight_with_petalback():
            """
            Repeated code
            """
            display_message()
            fight_pause_and_continue()
            reset_enemy()
            battle = Combat(player, enemy["Petalback"])
            battle.combat_loop()
        while True:
            print('"\n 🗣  1. It attacked us first! We had to defend'
                  ' ourselves!"')
            print("\n 🤐  2. Remain silent, avoiding his intense gaze.")
            print('\n 🙏  3. "I\'m truly sorry. I didn\'t realize it belonged'
                  ' to someone. Can we make it up to you?"')
            print('\n 💪  4. "Your creature should\'ve been stronger if it'
                  ' didn\'t want to be defeated."')
            choice = get_choice(4)
            if choice == 1:
                print('\n "Defense, huh? In its own home? On its own turf?"'
                      '\n Brockmire questions, a hint of anger in his voice.')
                fight_with_petalback()
                break
            elif choice == 2:
                print('\n\n "Silence. Just as well. The forest tells me all I'
                      ' need to know," Brockmire hisses.')
                fight_with_petalback()
                break
            elif choice == 3:
                print('\n "Make it up? Heh, you\'ll pay with your life,"'
                      ' Brockmire smirks, his intentions becoming very clear.')
                fight_with_petalback()
                break
            elif choice == 4:
                print('\n "Is that so? Well, let\'s test the strength'
                      ' of my other critters then!"')
                fight_with_petalback()
                break
        print_horizontal_line()
        print(" As Petalback's lifeless form rests before you,"
              " you can see Brockmire's anger intensifying."
              "\n He's not done yet!")
        print(" Clutching another one of those cages, Brockmire's hand"
              " trembles with a mix of fury and anticipation.")
        print(" The last battle took a toll on you, and the thought of facing"
              " another of Brockmire's creatures sends a shiver"
              " down your spine.")
        print(" Making a split-second decision, you dash towards him,"
              " hoping to catch him off-guard and prevent another battle.")
        print("\n In the split second it took you to lunge at him,"
              " Brockmire vanished into the dense underbrush,"
              "\n leaving only the faintest rustle as evidence of his escape.")
        print(" You stand amidst the tall grass, your breathing heavy and the"
              " cool forest air filling your lungs."
              "\n The immediate silence feels almost deafening after the"
              " heated confrontation.\n Gazing around, the tranquility of the"
              " forest seems almost surreal,\n making you question the reality"
              " of the battles you've just experienced.")
        print(" A fleeting thought crosses your mind: Could things have been"
              " handled differently?"
              "\n But now, there's only the path ahead and the choices yet to"
              " come.")
        print_horizontal_line()
        while True:
            print("\n 🛌  1. Take a moment to rest.")
            print("\n 🚶  2. With caution in your steps, continue forward,"
                  "\n unwilling to tempt fate with another unexpected"
                  " encounter.")
            print("\n 💰  3. Elidor Shop ")
            print("\n 📖  4. Player Info")
            choice = get_choice(4)
            if choice == 1:
                print("\n You find a quiet spot amidst the undergrowth,"
                      " a patch of soft moss beckoning you.")
                print(" Sitting down, you let the serene environment envelop"
                      " you, "
                      "momentarily shutting out the memories"
                      " of recent events.")
                print("\n After a few moments of tranquility, Elidor's voice"
                      " breaks the silence.")
                print('"You know, we\'ve been through quite a lot in such a'
                      ' short time," he muses.'
                      '\n "It\'s unfortunate how certain events unfolded, but'
                      ' please know that I don\'t blame you.'
                      ' Truth be told, had I been in your shoes, I might have'
                      ' reacted the same way."')
                print("\n His words bring a semblance of comfort,"
                      " reaffirming the bond the two of you share.")
                recovered_hp = player_rest(0.5)
                print(f"\n You rested and recovered {recovered_hp} ❤️  HP.")
                forest_end_scene()
                break
            elif choice == 2:
                forest_end_scene()
                break
            elif choice == 3:
                elidor_shop()
            elif choice == 4:
                print_player_info_menu()
    elif not defeated_creature:
        print("\n You decide it's best to let the creature be.")
        print("\n As you move on, you notice it curiously trailing you"
              " from a distance.")
        while True:
            print_horizontal_line()
            print("\n 🚶  1. Push onward through the opposite side of the"
                  " grassy area,\n     hoping to find a way out.")
            print("\n\n 💰  2. Elidor Shop")
            print("\n\n 📖  3. Player Info")
            choice = get_choice(3)
            if choice == 1:
                print("\n Determined, you tread carefully, pushing the tall"
                      " grass aside,\n vigilant"
                      " for any signs of danger or another encounter.")
                break
        print("\n As you make your way through the forest, you suddenly hear "
              "a rustling...")
        print("\n From behind the dense foliage, a peculiar figure emerges."
              "\n Taller than most humans, with rough, greenish skin, he's"
              " dressed in a rather unconventional mix of attire."
              "\n Wearing a too-tight-for-him cap backward, his pointy ears"
              " poking through,\n and oversized cargo shorts that barely fit"
              " his bulky troll frame, he looks like someone who raided a"
              " teenager's closet.")
        print("\n Around his waist is a belt with numerous tiny cages, each "
              "containing what appears to be a miniature creature."
              "\n He holds a red and white orb-like object in one hand, which"
              " he periodically tosses up and down.")
        print('\n "Yo! Name\'s Brockmire, the BeastMaster!" he declares with a'
              ' flamboyant pose,\n "And... possibly the world\'s best Beast'
              ' Trainer! What brings you here in my turf?"')
        print_horizontal_line()
        while True:
            print("\n 💬  1. I came from..")
            print("\n\n 💬  2. I just want..")
            print("\n\n 💬  3. What..?!?")
            print("\n\n 💰  4. Elidor Shop")
            print("\n\n 📖  5. Player Info")
            choice = get_choice(5)
            if choice == 1 or choice == 2 or choice == 3:
                print("\n Before you can utter any more words, Brockmire's"
                      " eyes widen, and his excitement is palpable.")
                print(' "YOU BROUGHT SPARKY TAIL BACK TO ME?!?" he exclaims.')
                print('\n With genuine gratitude in his eyes, he continues,'
                      '\n "I lost him a while back. I can\'t thank you '
                      'enough."')
                print("\n Brockmire hands you a pouch containing 100 Gold")
                player["Stats"]["Gold"] += 100
                print("\n You obtained 100 Gold 💰  !")
                print('\n Brokmire: "Consider this a token of my'
                      ' appreciation," he'
                      " adds, with a hint of a smile.")
                break
            elif choice == 4:
                elidor_shop()
            elif choice == 5:
                print_player_info_menu()

        while True:
            print_horizontal_line()
            print('\n 🌲  1. "Thanks! Any idea where I should head next?"')
            print('\n\n 🌲  2. "Thanks! Is there a nearby town or'
                  ' settlement?"')
            print('\n\n 🌲  3. "Thanks! I\'m kind of lost. Which way'
                  ' should I go?"')
            choice = get_choice(3)

            if choice == 1 or choice == 2 or choice == 3:
                print("\n Brockmire points towards a well-trodden path"
                      " that's "
                      "faintly visible through the trees."
                      '\n "That\'s the way to the nearest town.'
                      ' Just keep following that path,'
                      '\n and you\'ll be there in no time."')
                print('\n \"Take care on your journey, and thanks again'
                      ' for'
                      ' bringing back Sparky Tail. Farewell!"'
                      "\n He waves, turning his attention back to the"
                      " critter"
                      " with a look of deep affection on his face.")
                break

        forest_end_scene()


def forest_end_scene():
    """
    Handles the end of the forest scene
    """
    print("\n 🌲  As you tread cautiously, the dense canopy of the forest"
          " begins to thin."
          " The muted sounds of wildlife are gradually replaced by "
          "a distant hum of activity."
          " A few more steps and the forest edge reveals itself, presenting a"
          " breathtaking vista: a quaint town, its rooftops bathed in the "
          "soft glow of the setting sun."
          " People can be seen moving about, and the distant chime of a bell"
          " signals the day's end. Relief washes over you; civilization is "
          "finally within reach.")
    while True:
        print("\n 🚶  1. With anticipation in your heart, you decide to journey"
              " towards the bustling town ahead!")
        print("\n\n 💰  2. Elidor Shop")
        print("\n\n 📖  3. Player Info")
        choice = get_choice(3)
        if choice == 1:
            print(" You head towards the town")
            town_guard_scene()
        elif choice == 2:
            elidor_shop()
        elif choice == 3:
            print_player_info_menu()


def town_guard_scene():
    """
    Handles scenario if coming from lake or forest
    """
    print("HALT YOU DUMBASS")


def town_scene():
    """
    Handles town scene
    """
    print(" TOWN")


def main():
    """
    Starts the game
    """
    intro()
    first_scene()
    second_scene()
    third_scene()
    fourth_scene()
    fifth_scene()


main()
