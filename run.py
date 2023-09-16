# pylint: disable=too-many-lines
"""
This is the main module for the text adventure game.
It contains all game functionalities, classes, and methods
required for the game's operation.

Everything from player creation, combat mechanics, to game
scenes are housed within this module.
"""

import random


def get_choice(max_choice):
    """
    Prompts the player to make a valid choice within a given range.

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
    print("\n Welcome to this text-adventure game!")
    print("\n 🖊️  How to Play:")
    print(" 1. Input choices by selecting the corresponding number.")
    print(" 2. Confirm your choice by pressing 'ENTER'.")
    print("\n 🚫  But, tread carefully! Every decision can tip the balance."
          "\n Take a")
    print(" wrong step and you might be drawn into combat.")
    print("\n 🛡️  Combat Basics:")
    print(" - Attack: The damage you inflict.")
    print(" - Defense: The damage you mitigate.")
    print(" - MAX HP: Your total health points.")
    print(" - Current HP: Your current health. Reach 0, and...well, you'll"
          " see.")
    print(" - Crit: % chance to deal a critical strike. A successful crit"
          " deals")
    print("   1.5x damage and bypasses 1/3 of the opponent's defense.")
    print("\n 🚨 Keep in mind! Enemies can critically hit too.\n Yet, they only"
          " deal 1.5x damage. You're special, after all!")
    print(" - Run: % chance to flee a battle.")
    print("\n 🌟 Pro Tip: Sometimes, retreat is the best strategy."
          "\n Not every battle is meant to be won.")
    print(" Maybe someone will also appreciate it if you do..")
    print("\n Did i forget something?")
    print(" If i did it is not oversight. It's a FEATURE! 😉")
    print(" Like adding a little layer of mistery.")
    print("\n Embark, dear adventurer. Good luck and enjoy the ride!")

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

random_elidor_messages = [
    " Ah, ready to give me back my gold?",
    " Looking for supplies? Check these out!",
    " Stock up for the journey ahead!",
    " Ready to spend some gold?"
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
    },
    "Troll Club": {
        "Name": "Troll Club",
        "Type": "Weapon",
        "Atk": 8,
        "Crit": 10
    },
    "Wet Boots": {
        "Name": "Wet Boots",
        "Type": "Boots",
        "Def": 2,
        "Max HP": 3
    },
    "Bandit Cloth": {
        "Name": "Bandit Cloth",
        "Type": "Body",
        "Def": 1,
        "Max HP": 2
    },
    "Bandit Boots": {
        "Name": "Bandit Boots",
        "Type": "Boots",
        "Def": 1,
        "Max HP": 2
    },
    "Bandit Hood": {
        "Name": "Bandit Hood",
        "Type": "Head",
        "Def": 1,
        "Max HP": 2
    },
    "Bandit Pants": {
        "Name": "Bandit Pants",
        "Type": "Legs",
        "Def": 1,
        "Max HP": 2
    },
}


# Pandora's items haven't been added yet. It will be a future feature.
pandora_items = {
    1: {"Name": 1, "Status": True},
    2: {"Name": 2, "Status": True},
    3: {"Name": 3, "Status": True},
    4: {"Name": 4, "Status": True},
    5: {"Name": 5, "Status": True},
    6: {"Name": 6, "Status": True},
    7: {"Name": 7, "Status": True},
    8: {"Name": 8, "Status": True},
    9: {"Name": 9, "Status": True},
    10: {"Name": 10, "Status": True}
}


def reset_player():
    """
    Resets the player dictionary
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
    Resets the enemy dictionary for the next combat encounter.
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
            "Max HP": 55,
            "Current HP": 55,
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
            "Def": 15,
            "Crit": 5,
            "Run": 0,

            "Loot": {
                "Gold": 50,
            }
        },
        "River Troll": {
            "Name": "River Troll",
            "Max HP": 70,
            "Current HP": 70,
            "Atk": 22,
            "Def": 13,
            "Crit": 2,
            "Run": 30,

            "Loot": {
                "Gold": 50,
                "Items": {
                    "Troll Club": 80,
                    "Wet Boots": 70
                }
            }
        },
        "Bandit": {
            "Name": "Bandit",
            "Max HP": 45,
            "Current HP": 45,
            "Atk": 22,
            "Def": 15,
            "Crit": 25,
            "Run": 0,

            "Loot": {
                "Gold": 30,
                "Items": {
                    "Bandit Cloth": 80,
                    "Bandit Boots": 70,
                    "Bandit Hood": 70,
                    "Bandit Pants": 50
                }
            }
        },
        "Town Guard": {
            "Name": "Town Guard",
            "Max HP": 90,
            "Current HP": 90,
            "Atk": 30,
            "Def": 45,
            "Crit": 25,
            "Run": 100,
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
    Pauses the game during combat scenarios, allowing the player
    to read the story text and continue when ready.
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
    This class manages the intricacies of combat logic, including
    calculating damage, loot, critical hits and more.
    """

    def __init__(self, player, enemy):  # pylint: disable=redefined-outer-name
        """
        Initializes the class with the provided player and enemy.

        Parameter:
        - Player: The player dictionary, used to gather the stats
        - Enemy: The enemy dictionary, used to gather the stats and loot
        """
        self.player = player
        self.enemy = enemy

    def player_combat_victory(self):
        """
        This function sets the global battle result to "Victory",
        displays a victory message to the player, processes the
        loot obtained from the victory.

        Returns:
        - A string "Victory" assigned to battle_result
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
        Iterates through the loot of enemy and
        if the drop rate is successful it
        appends the item to an empty list.

        Returns:
        - A list of items dropped by the enemy
        """
        dropped_items = []

        items = self.enemy.get("Loot", {}).get("Items", {})

        for item, drop_rate in items.items():
            if random.randint(1, 100) <= drop_rate:
                dropped_items.append(item)

        return dropped_items

    def handle_loot(self):
        """
        Adds the gold from the defeated enemy to the player's
        gold count and display a message about it.
        It checks for any items dropped by the enemy
        and calls the equip_item using it as an argument
        """
        self.player["Stats"]["Gold"] += self.enemy["Loot"]["Gold"]
        print()
        print(f" Elidor gave you {self.enemy['Loot']['Gold']} Gold 💰 !")

        dropped_items = self.check_drop()

        for loot_name in dropped_items:
            item_dropped = item_database.get(loot_name)
            self.equip_item(item_dropped)

    def equip_item(self, item_detail):
        """
        Automatically equips a better piece of equipment
        if the equipment item is superior to the currently
        equipped item of the same type

        Uses as argument the iterated items from
        handle_loot
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
        Displays a list of potions available to the player during combat.

        Iterates through the player's potion inventory and presents each
        potion with its healing amount and remaining quantity.
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
        Ensures player's current HP doesn't exceed the Max HP after healing.
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
        Displays a side-by-side comparison of the player's and enemy's combat
        stats.
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
        Handles the sequence of events when the player is defeated in combat.
        """
        print(f" The {self.enemy['Name']} hit you with a killing blow!")
        player_defeat()

    def enemy_attack(self):
        """
        Calculates and applies the damage the enemy deals to the player
        during combat.
        If player's health drops to zero or below, the player defeat sequence
        is initiated.
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
        Manages the combat loop sequence
        The loop continues until the player, or the enemy's health drops to 0,
        or the player successfully escapes.
        """
        print(f" ======== COMBAT VS {self.enemy['Name'].upper()} ========")
        while (self.player['Stats']['Current HP'] > 0 and
               self.enemy['Current HP'] > 0):
            print(f"\n IMAGE OF {self.enemy['Name'].upper()}")
            current_player_hp = int(self.player['Stats']['Current HP'])
            player_maxhp = int(self.player['Stats']['Max HP'])
            current_enemy_hp = int(self.enemy['Current HP'])
            enemy_maxhp = int(self.enemy['Max HP'])
            print(f"\n {self.player['Stats']['Name']} HP:"
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
    Handles the scenario when the player is defeated in the game.
    Provides the option to restart the game or exit.
    """
    print("\n 💀  YOU DIED 💀")
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
    Prints a detailed overview of the player's stats, available potions,
    and equipped items.
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
    Sets the scene for the game by introducing the player to their environment
    and immediate choices.
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
    This function serves as an early game-over scenario if the player
    chooses to ignore the external world and get back to sleep.

    Serves as an introduction to the possibility of a game over
    outside of combat.
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
    This function introduces the player to the combat mechanics of the game.
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
    Serves to establish the aftermath of the confrontation with the goblin
    and as an introduction to Elidor, a core part of the narrative.
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
     Presents the fourth scene in the game's narrative progression.
    Elidor the merchant will join and this will serve as an end to the
    "tutorial" like phase.
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
    Implements the mechanics for the Pandora Box item roll in the game.
    It generates a random roll to determine the item received

    If the player already own the rolled item they will receive 2 Ultra
    potions.

    If the player doesn't own the item it is added to its inventory.

    Note:
    This function sets the foundation for a more comprehensive loot box system,
    which could be expanded in future game versions to include a wider variety
    of items or effects.
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
    A shop mechanic where the player can purchase various items.
    It is available in most scenes throughout the game.
    """
    print(" ===== ELIDOR SHOP =====")
    print()
    print(f" Elidor: {random.choice(random_elidor_messages)}")
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
    Implements the fifth scene and introduction to branching paths.
    It serves as an end to the main function sequences, each branch
    becomes independent and will influence some outcomes.
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
    Processes the loot items found by the player outside of combat scenarios.

    Parameters:
    - *items_found: tuple of str

    If multiple items are used as arguments, the function iterates through
    them and calls an equip function for each of them.
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
    Handles the first scene of the river route.
    """
    print_horizontal_line()
    print(" As you walk alongside the river, the calmness of the water,\n "
          " along with the rhythmic sound of the current,"
          " gives you a sense of peace.")
    print(" The sun glitters on the water's surface, and the air is filled"
          " with the sweet\n scent of blooming flowers.")
    print("\n Elidor bends down, picks up a smooth, flat stone, and with"
          " a mischievous glint\n in his eyes, challenges you.")
    print('\n "How about a little contest? Let\'s see who can skip the stone'
          ' the furthest."')
    while True:
        print('\n 💪  1. "Sure, I\'m up for a challenge!"')
        print('\n\n 🌊  2. "No thanks, I\'d rather just enjoy the scenery."')
        print("\n\n 💰  3. Elidor Shop")
        print("\n\n 📖  4. Player Info")
        choice = get_choice(4)
        if choice == 1:
            print(" With a confident smirk, you take the stone from Elidor."
                  "\n Positioning yourself, you give it a strong flick of the "
                  "wrist.\n To your surprise, after the second skip, the stone"
                  " seems to hit something\n solid mid-air and drops into the"
                  " water with a splash.\n Both you and Elidor exchange"
                  " puzzled glances.")
            print("\n Approaching the spot, you extend your hand and feel an"
                  " invisible barrier."
                  "\n The air around it vibrates with magic.\n Elidor murmurs,"
                  '"It\'s an illusion spell...\n something is being concealed'
                  ' here."')
            print('\n "What should we do?"')
            while True:
                print("\n 🔍  1. Examine the hidden spot")
                print("\n\n 🚫  2. Walk away, it might be risky")
                choice = get_choice(2)
                if choice == 1:
                    print("\n After a moment of concentration, Elidor chants a"
                          " soft incantation,\n and the illusion starts to"
                          " fade, revealing a hidden alcove.\n You find "
                          "a mysterious, ancient-looking chest.")
                    print("\n Inside, you find a bejeweled Long Sword.")
                    print(" It may not be much but you feel like it could make"
                          " your life easier")
                    print("\n You ponder why someone would go through so much"
                          " trouble to hide a mere sword.")
                    handle_loot_world("Long Sword")
                    while True:
                        print('\n Elidor glances around warily and leans in to'
                              ' whisper,\n "We should leave quickly. The one '
                              'responsible for the illusion might return."')
                        print("\n 🚶  1. He is right, we should leave.")
                        choice = get_choice(1)
                        if choice == 1:
                            river_second_scene()
                            break
                    break
                elif choice == 2:
                    print('\n "There are things in this world best left'
                          ' undiscovered," Elidor murmurs,\n his gaze '
                          " lingering on the concealed spot for a moment"
                          "longer.")
                    print("\n You nod, feeling a mixture of relief and"
                          ' curiosity.\n "There\'s a reason it was hidden, "'
                          'you reason aloud,\n "and we might not want to know'
                          ' why."')
                    print("\n With a final glance over your shoulder, you and"
                          " Elidor continue,\n the gentle sounds of the river"
                          " soon drowning out the unease.\n The path may have"
                          " presented an unexpected mystery, but sometimes,\n"
                          " it's best to choose safety over curiosity.")
                    while True:
                        print("\n What to do now?")
                        print("\n 🚶  1. Let us leave this place behind")
                        choice = get_choice(1)
                        if choice == 1:
                            print(" With a nod to Elidor, you decide it's time"
                                  " to move on.\n The two of you gather your"
                                  " belongings,\n leaving the mysteries of the"
                                  " riverbank behind as you continue your"
                                  " journey.")
                            river_second_scene()
                            break
                    break
            break
        elif choice == 2:
            print(" You smile and shake your head, choosing instead to sit and"
                  " relax\n by the riverside."
                  "\n The journey continues peacefully as you absorb the"
                  " serenity around you.")
            river_second_scene()
            break
        elif choice == 3:
            elidor_shop()
        elif choice == 4:
            print_player_info_menu()


def river_second_scene():
    """
    Handles the second scene alongside the river during the player's journey.
    The choices made here can lead to combat or exploration.
    """
    print_horizontal_line()
    print(" Continuing your journey along the river, the scenery starts"
          " to shift.\n The once clear "
          "water now appears murky.")
    print("\n Birds chirp high in the trees, and the scent of wet"
          " earth fills the air.")
    print('\n Elidor slows his pace and remarks,\n "This part of the river'
          " is less familiar to me. We "
          'need to be cautious."')
    while True:
        print('\n 🌉  1. "I see a bridge in the distance. Let\'s cross there."')
        print("\n\n 🏞️  2. Let's set up camp and decide tomorrow.")
        print("\n\n 💰  3. Elidor Shop")
        print("\n\n 📖  4. Player Info")
        choice = get_choice(4)
        if choice == 1:
            print(" The two of you approach the bridge.\n It looks ancient,"
                  " with moss covering its stone sides.")
            print("\n As you step onto it, you notice the wooden planks"
                  " creaking under your weight.")
            print("\n Halfway across, Elidor stops, sensing something."
                  "\n Before you can react, the bridge is "
                  "ambushed by a river troll!")
            fight_pause_and_continue()
            reset_enemy()
            battle = Combat(player, enemy["River Troll"])
            battle.combat_loop()
            print_horizontal_line()
            print(" With the troll defeated, a sigh of relief washes over you."
                  "\n Their might is unmatched, but cunning always finds a"
                  " way.\n As you catch your breath, the distant silhouette of"
                  " a town emerges\n just beyond the bridge.")
            print(" Elidor's face brightens at the sight, and even Medea "
                  "seems to share\n a hint of relief. A proper rest awaits.")
            print(" Without hesitation, you all head towards the promise of"
                  " comfort\n that the town offers.")
            town_guard_scene()
            break
        elif choice == 2:
            print(" You and Elidor decide to set up camp. As night falls,"
                  " you both share stories around a campfire.")
            print("\n The gentle sounds of the river soothe you to sleep.")
            print_horizontal_line()
            river_rest_scene()
            break
        elif choice == 3:
            elidor_shop()
        elif choice == 4:
            print_player_info_menu()


def river_rest_scene():
    """
    Handles the third river scene where the player attempts to rest.
    There are 3 outcomes with each a chance of 33% to happen.
    Outcome 1: player heals 100% of Max HP.
    Outcome 2: player heals 50% of Max HP and gets ambushed.
    Outcome 3: player heals 20% of Max HP and gets ambushed.
    """
    rand_num = random.randint(1, 99)
    if 1 <= rand_num <= 33:
        print("\n You slept peacefully through the night and feel refreshed!")
        recovered_hp = player_rest(1.0)
        print(f"\n You rested and recovered {recovered_hp} ❤️  HP.")
        print(" As the sun shines, it reveals the distant silhouette of"
              " a town\n that emerges just beyond a bridge.")
        print(" Elidor's face brightens at the sight, and even Medea "
              "seems to share\n a hint of relief.")
        print('\n Elidor chuckles, "Just a bit further and we could\'ve had'
              ' proper beds!"\n But his smile says he cherished the time'
              ' shared with you and Medea.')
        print("\n With restored vigor you head towards the town's gate.")
        town_guard_scene()
    elif 34 <= rand_num <= 66:
        print(" Before dawn's first light, Medea's anxious whinnies rouse "
              "you and Elidor.")
        print(" Blinking away sleep, you quickly discern the cause:\n three"
              " bandits have surrounded your camp.")
        print(" You're groggy from interrupted rest, not at full strength,"
              "\n and now must defend yourselves!")
        recovered_hp = player_rest(0.5)
        print("\n Your rest was interrupted and therefore you only"
              f" recovered {recovered_hp} ❤️  HP.")
        fight_pause_and_continue()
        reset_enemy()
        battle = Combat(player, enemy["Bandit"])
        battle.combat_loop()
        print_horizontal_line()
        print_bandit_fight_1()
        fight_pause_and_continue()
        reset_enemy()
        battle = Combat(player, enemy["Bandit"])
        battle.combat_loop()
        print_horizontal_line()
        print_bandit_fight_2()
        river_last_scene()
    elif 67 <= rand_num <= 99:
        print(" No sooner had you closed your eyes for a night's rest,\n "
              "Medea's urgent neighs snap you awake.")
        print(" In the dim light, you spot three shadowy figures:\n bandits"
              " closing in on your camp!")
        print(" You've barely had a moment to rest, and now you must fend"
              " off an ambush\n with limited strength!")
        recovered_hp = player_rest(0.2)
        print("\n Your rest was interrupted and therefore you only"
              f" recovered {recovered_hp} ❤️  HP.")
        fight_pause_and_continue()
        reset_enemy()
        battle = Combat(player, enemy["Bandit"])
        battle.combat_loop()
        print_horizontal_line()
        print_bandit_fight_1()
        fight_pause_and_continue()
        reset_enemy()
        battle = Combat(player, enemy["Bandit"])
        battle.combat_loop()
        print_horizontal_line()
        print_bandit_fight_2()
        river_last_scene()


def river_last_scene():
    """
    Handles the aftermath of the bandit ambush at the river.
    """
    print_horizontal_line()
    print(" The weight of the ambush weighs on you,\n reminding you of the"
          " ever-present dangers on your journey.")
    print(" You share a nod with Elidor, signaling a mutual respect and"
          " understanding,\n then at the sun's first light you begin "
          "packing up camp.")
    print("\n You tenderly caress Medea, thanking her silently. The rising"
          " sun reveals\n a town in the distance, just beyond a bridge.")
    print("\n Physically and mentally drained, the group trudges towards the"
          " town's gates.")
    town_guard_scene()


def print_bandit_fight_1():
    """
    Narrates the unfolding events of the first phase of the bandit fight.
    """
    print(" With one bandit down, you now face the remaining two"
          " simultaneously.")
    print("\n Nearby, Medea fiercely protects Elidor. In her frenzy,"
          " she lands a")
    print(" mighty kick on a bandit, seemingly taking him out of"
          " the fight.")
    print("\n The last bandit, though lacking confidence, knows there's"
          " no way out.")
    print(" With a defiant yell, he charges, hell-bent on avenging his"
          " fallen comrade.")
    print("\n It's clear: if he's going down, he intends to take one"
          " of you with him."
          "\n It is up to you now to avoid this!")


def print_bandit_fight_2():
    """
    Narrates the unfolding events of the second phase of the bandit fight.
    """
    print(" After felling the final bandit, you exhale a weary sigh"
          " of relief.")
    print(" However, the luxury of rest eludes you now.")
    print(" On high alert, you await the sun's rays, yearning for the safety"
          " it brings.")


def main_road_path():
    """
    This function represents the main storyline along the main road.
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
          " encountered.\n Taller, adorned in menacing spiky armor,")
    print(" and wielding a colossal sword matching his formidable stature."
          "\n He must be the gang's chief. Defeating him"
          " could quell this bloodshed.")
    print("\n But there's no time for contemplation; the chief charges you,"
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
    This function represents the second scene along the main road path branch.
    """
    print_horizontal_line()
    print("\n After a few hours of walking along the main road,\n the outline"
          " of a town emerges on the horizon.")
    print("\n A fortified stone wall encircles it,\n with a large wooden gate"
          " marking the entrance.")
    print("\n As you and Elidor approach the town gate, a guard in polished"
          "\n armor steps forward, halting your progress.")
    print('\n "Halt! All newcomers must be inspected before entering",'
          "\n the guard states firmly.")
    print("\n While the guard is about to proceed with the inspection,\n his"
          " eyes fall on the chief's gauntlet you possess.")
    print('\n "Wait a minute... Is that the goblin chief\'s gauntlet?'
          ' Have you encountered\n the goblin gang?" he asks, curiosity'
          " evident in his voice.")

    while True:
        print("\n\n 👍  1. Tell him that you defeated the goblin chief.")
        print("\n 👎  2. Lie and tell him that you found the gauntlet.")
        choice = get_choice(2)

        if choice == 1:
            print("\n You and Elidor explain what happened to the guard.")
            print("\n The guard's face lights up with a broad smile."
                  '\n "Those goblins have been a thorn in our side for too'
                  ' long!\n They\'ve been raiding our commercial roads for'
                  ' months."')
            print("\n In recognition of your deed, the guard hands you a "
                  'pouch.\n "There was a bounty on the chief\'s head.'
                  ' This is yours now."')
            print("\n You obtained 100 Gold  💰  from the guard!")
            player["Stats"]["Gold"] += 100
            print("\n Furthermore, he hands you a special coupon."
                  '\n "This is for the town shop. They\'ll give you a good'
                  ' deal with this."')
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
                  ' you.\n Enter the town, but cause no trouble."')
            print("\n Although the guard's suspicions linger, you're granted "
                  "entry into the town."
                  "\n You step through the gate with a slight unease in your"
                  " step.")
            town_scene()
            break


def forest_path():
    """
    This function handles the forest scenario where you encounter a MYSTERIOUS
    creature.
    The player has the option to either attack the creature or continue on the
    path, with consequences based on the choice.
    If the battle is started it is still possible to flee in order to progress
    the "pacifist" path.
    """
    print_horizontal_line()
    print("\n While traversing the tall grass, the rustling of leaves draws"
          " your attention.")
    print("\n Emerging from the bushes is a small, yellow-furred creature"
          "\n with rosy cheeks and a lightning-shaped tail.")
    print("\n It looks startled, eyes wide as it assesses you.\n You're not"
          " sure if it's about to attack or bolt away.")
    print("\n As you cautiously approach the creature, you notice jolts of "
          "lightning\n emanating from its rosy cheeks,"
          " indicating its distress.")
    print("\n The fact that this creature can harness what appears to be"
          "\n elemental magic is a cause for concern.")
    while True:
        print("\n 🏹  1. Preemptively attack the creature."
              "\n      It is maybe better to be safe than sorry.")
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
    This function handles the second scene of the forest path and creates
    a scenario based on whether the player defeated the mysterious creature.

    Param:
    - defeated_creature: A boolean indicating whether the creature was slain.
    """
    if defeated_creature:
        print("\n The remnants of the battle linger in the air, and Sparky"
              " Tail's\n defeated form serves as a"
              " somber reminder of the confrontation.")
        print("\n You find yourself surrounded by tall grass, "
              "\n the direction you came from is clear."
              "\n The serenity of the forest contrasts with the adrenaline"
              "\n still coursing through your veins.")
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
              "\n Taller than most humans, with rough, greenish skin,\n he's"
              " dressed in a rather unconventional mix of attire."
              "\n Wearing a too-tight-for-him cap backward, his pointy ears"
              " poking through,\n and oversized cargo shorts that barely fit"
              " his bulky troll frame,\n he looks like someone who raided a"
              " teenager's closet.")
        print("\n Around his waist is a belt with numerous tiny cages,\n each "
              "containing what appears to be a miniature creature."
              "\n He holds a red and white orb-like object in one hand,\n"
              " which he periodically tosses up and down.")
        print('\n "Yo! Name\'s Brockmire, the Beast Master!" he declares with'
              ' a'
              ' flamboyant pose,\n "And... possibly the world\'s best Beast'
              ' Trainer!\n1 What brings you here in my turf?"')
        print_horizontal_line()
        while True:
            print("\n 🖐️  1. Greet him politely.")
            print("\n\n 🗡️  2. Boast about your recent kill.")
            print("\n\n 💰  3. Elidor Shop")
            print("\n\n 📖  4. Player Info")
            choice = get_choice(4)
            if choice == 1:
                print('\n "Oh, hey Brockmire," you greet cautiously,\n'
                      ' "We were just... uh, passing through?"')
                break
            elif choice == 2:
                print_horizontal_line()
                print('\n With pride swelling in your chest, you announce,'
                      '\n "You may be a beast trainer but I am a beast slayer!'
                      '\n Just moments ago, I bested a formidable creature!'
                      '\n It stood no chance against my prowess!"')
                break
            elif choice == 3:
                elidor_shop()
            elif choice == 4:
                print_player_info_menu()

        print('\n Brockmire responds, "Hm... Really?\n Because it seems'
              ' you\'ve encountered one of my precious critters.'
              '\n My Sparky Tail..."')
        print("\n The white orb begins to glow dimly, resonating with the"
              " residual energy\n left behind from your confrontation with"
              " the creature.")
        print(" A sinking feeling washes over you as you piece together"
              "\n that the creature was more than just a wild beast..\n"
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
                  "\n which materialize into a perplexing creature.\n It looks"
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
              "\n you can see Brockmire's anger intensifying."
              "\n He's not done yet!")
        print(" Clutching another one of those cages,\n Brockmire's hand"
              " trembles with a mix of fury and anticipation.")
        print(" The last battle took a toll on you, and the thought of facing"
              " another of Brockmire's creatures sends a shiver"
              " down your spine.")
        print(" Making a split-second decision, you dash towards him,"
              "\n hoping to catch him off-guard and prevent another battle.")
        print("\n In the split second it took you to lunge at him,"
              "\n Brockmire vanished into the dense underbrush,"
              "\n leaving only the faintest rustle as evidence of his escape.")
        print(" You stand amidst the tall grass, your breathing heavy\n and"
              " the cool forest air filling your lungs."
              "\n The immediate silence feels almost deafening after the"
              " heated confrontation.\n Gazing around, the tranquility of the"
              " forest seems almost surreal,\n making you question the reality"
              " of the battles you've just experienced.")
        print(" A fleeting thought crosses your mind:\n Could things"
              " have been handled differently?"
              "\n But now, there's only the path ahead and the choices yet to"
              " come.")
        print_horizontal_line()
        while True:
            print("\n 🛌  1. Take a moment to rest.")
            print("\n 🚶  2. With caution in your steps, continue forward,"
                  "\n     unwilling to tempt fate with another unexpected"
                  " encounter.")
            print("\n 💰  3. Elidor Shop ")
            print("\n 📖  4. Player Info")
            choice = get_choice(4)
            if choice == 1:
                print("\n You find a quiet spot amidst the undergrowth,"
                      "\n a patch of soft moss beckoning you.")
                print(" Sitting down, you let the serene environment envelop"
                      " you,\n "
                      "momentarily shutting out the memories"
                      " of recent events.")
                print("\n After a few moments of tranquility, Elidor's voice"
                      " breaks the silence.")
                print('"You know, we\'ve been through quite a lot in such a'
                      ' short time," he muses.'
                      '\n "It\'s unfortunate how certain events unfolded,\n'
                      ' but please know that I don\'t blame you.'
                      '\n Truth be told, had I been in your shoes, I might'
                      ' have reacted the same way."')
                print("\n His words bring a semblance of comfort,"
                      "\n reaffirming the bond the two of you share.")
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
    This function represents the end scene of the forest path branch.
    """
    print_horizontal_line()
    print("\n As you tread cautiously, the dense canopy of the forest"
          " begins to thin."
          "\n The muted sounds of wildlife are gradually replaced\n by "
          "a distant hum of activity."
          "\n A few more steps and the forest edge reveals itself,\n"
          " presenting a breathtaking vista:\n a quaint town, its"
          " rooftops bathed in the soft glow of the setting sun."
          "\n People can be seen moving about, and the distant chime of a bell"
          " signals the day's end.\n Relief washes over you; civilization is "
          "finally within reach.")
    while True:
        print("\n 🚶  1. With anticipation in your heart,\n you decide to"
              " journey towards the bustling town ahead!")
        print("\n\n 💰  2. Elidor Shop")
        print("\n\n 📖  3. Player Info")
        choice = get_choice(3)
        if choice == 1:
            print(" You head towards the town")
            town_guard_scene()
            break
        elif choice == 2:
            elidor_shop()
        elif choice == 3:
            print_player_info_menu()


def town_guard_scene():
    """
    This function handles the scenario when the player arrives at the town's
    outer perimeter.
    It involves interactions with a town guard.
    If the player does comply the temporarily final scene will play.
    If the player does not comply then an alternative scene will play.
    """
    print_horizontal_line()
    print("\n You reach the outer perimeter of the town.")
    print("\n A fortified stone wall encircles it, with a large wooden gate"
          " marking the entrance.")
    print("\n As you and Elidor approach the town gate,\n a guard in polished"
          " armor steps forward,\n halting your progress.")
    print('\n "Halt! All newcomers must be inspected before entering",'
          "\n the guard states firmly.")
    while True:
        print("\n ✋  1. Comply with the guard's request")
        print("\n\n 🖕  2. Challenge the guard's authority")
        print("\n\n 💰  3. Elidor Shop")
        print("\n\n 📖  4. Player Info")
        choice = get_choice(4)
        if choice == 1:
            print('\n "We\'re merely passing through," you explain,\n'
                  ' "We have a delivery for the city of Veradia."')
            print("\n\n Elidor nods in agreement.")
            print("\n\n The guard looks skeptically at both of you before"
                  " inspecting Elidor's cart.")
            print("\n After a thorough check, he finds nothing amiss.")
            print('\n "Everything seems to be in order," he says with a nod,'
                  ' "Proceed into the town."')
            print("\n With a sense of relief, you and Elidor enter the town,"
                  "\n ready to explore and rest.")
            town_scene()
        elif choice == 2:
            print('\n "What\'s the matter, tin head? Too scared to let a'
                  'couple of travelers through\n without'
                  'flexing your muscles?"'
                  "  you taunt, defiance evident in your voice.")
            print("\n Elidor shoots you a wary glance, but the guard seems"
                  " unexpectedly pleased.")
            print('\n "I was hoping you\'d say something like that," he smirks'
                  ' ,\n unsheathing his weapon.\n "It\'s been a rough week,'
                  ' and I could'
                  ' really use an excuse to blow off\n some steam...'
                  ' legally."')
            print(' "You, good sir, are under ARREST!"')
            print("\n At the sight of his gleaming blade, regret fills you."
                  "\n The thought of battle seems bleak now.")
            print(" You contemplate fleeing, but his smug expression suggests"
                  " he won't\n let you escape that easily.")
            fight_pause_and_continue()
            reset_enemy()
            battle = Combat(player, enemy["Town Guard"])
            battle.combat_loop()
            if battle_result == "Victory":
                town_scene_defiance(True)
                break
            elif battle_result == "Run":
                town_scene_defiance(False)
                break
        elif choice == 3:
            elidor_shop()
        elif choice == 4:
            print_player_info_menu()


def town_scene():
    """
    This function represents the arrival to the town.
    It is temporarily the end of the game.
    """
    print_horizontal_line()
    print("\n HELLOOOOOO, dear Assessor!")
    print(" Yes, it's me, THE DEVELOPER!")
    print(" Bold to name myself Developer already, am i right?!?")
    print(" Anyways, thanks for diving into my game!")
    print(" I hope you had a sliver of the fun playing it as I did"
          " creating it.")
    print(" I ambitiously envisioned a vast plot.\n Everything up to the town"
          " was just the tutorial!")
    print(" However, time wasn't my ally, so I had to use the town"
          "\n to conclude my project early.")
    print(" Once I expand on it, I'd love for you to revisit. Exciting"
          " features await! :D")
    print("\n\n\n PS: In case you chose the main road:"
          "\n     Sorry that i didn't let you use the Coupon =D")
    quit()


def town_scene_defiance(guard_battle):
    """
    Handles the outcome of the battle with the town guard, depending on whether
    the player wins, loses or runs from the battle.

    Parameter:
    - guard_battle: A boolean indicating whether the player won or ran.

    """
    if guard_battle is False:
        print(" Well, you didn't get far...")
        print(" You've been captured, but at least you're still breathing.")
        print(' "Lost your voice, have you?" the guard taunts, gripping you'
              ' with one'
              " hand while his sword points at your neck with the other.")
        print(" Elidor urgently pleads for leniency, but the guard remains"
              " unmoved.")
        print(' "It\'s a 50 gold fine for resisting the king\'s authority," he'
              ' sneers,'
              "\n 'Or it's the dungeon for you.'")
        while True:
            print("\n 💵  1. Reluctantly hand over the gold.")
            print("\n\n 🖕  2. Insult him even more")
            choice = get_choice(2)
            if choice == 1:
                if player["Stats"]["Gold"] >= 50:
                    player["Stats"]["Gold"] -= 50
                    print(' "This better be all of it," the guard grumbles,'
                          "\n counting the coins before stepping aside.")
                    print(" You enter the town, lighter in gold but relieved"
                          " to avoid further trouble.")
                    town_scene()
                    break
                else:
                    taken_gold = player["Stats"]["Gold"]
                    player["Stats"]["Gold"] = 0
                    print(f' "Only {taken_gold} gold? Pathetic," the guard'
                          " sneers, snatching the coins from your hand.")
                    print(' "I suppose it will have to do. Consider yourself'
                          ' lucky I\'m in a generous mood today."')
                    print(" You're allowed into the town, but now you're"
                          " completely broke.")
                    town_scene()
                break
            elif choice == 2:
                print(' "You really have a death wish, don\'t you?" the guard'
                      ' sneers.')
                print("\n Without another word, he and a few other guards grab"
                      " you.")
                print(" They drag you into the dungeon, where you meet your"
                      " grim fate.")
                player_defeat()
                break

    elif guard_battle is True:
        print("\n Wait... WHAT?! How did you...?!")
        print("\n Ah, I see you there, dear User. It's me, THE DEVELOPER!")
        print(" Either you've mastered the fine art of cheating, or Lady"
              " Luck truly favored you with some insane crits.")
        print(" Well, I'll admit it. I bit off more than I could chew and the"
              " deadline is breathing down my neck.")
        print(" So, alas, this journey ends here. Thanks for playing my game,"
              " you crafty CHEATER!")
        print("\n After I'll submit this, there's so much more in store!"
              "  We're talking a LOOOOOOOOT more plot and features like"
              " ✨MAGIC✨.")
        print("\n So, circle back and give it another whirl when it's ready."
              " Thanks for playing!\n BYEEEEEEEEE!")
        player_defeat()


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
