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
                print(f" 🚫 Please enter a number between 1 and {max_choice}.")
        except ValueError:
            print()  # Prints an empty line for separation
            print(" 🚫 Invalid input! Please enter a number.")


def rules():
    """
    Prints the rules of the game and then redirects the user either
    back to the intro or to the start of the game.
    """
    print(" These are the rules, will be add later",
          "\n\n 1. 🛡️  I am ready to start my adventure!",
          "\n\n 2. 📜 Bring me back to the Menu.")
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


player_critical_messages = [
    " 💥 YOU DEALT A POWERFUL CRITICAL BLOW!",
    " 💥 YOU DEALT A DEVASTATING CRITICAL BLOW!",
    " 💥 YOU DEALT AN IMPRESSIVE CRITICAL BLOW!",
    " 💥 YOU DEALT A CRITICAL HIT!",
    " 💥 THE ECHOES OF YOUR POWERFUL CRITICAL HIT RESOUND!",
    " 💥 THE AIR CRACKLES WITH ENERGY FROM YOUR CRITICAL HIT!"
]


enemy_critical_messages = [
    " 💥 THE ENEMY CLARIFIES YOUR MORTALITY WITH A SINGLE"
    "  CRITICAL STRIKE!",
    " 💥 THE ENEMY DEALT TO YOU A CRITICAL INJURY!",
    " 💥 THE ENEMY STRIKES WITH UNBRIDLED FURY!",
    " 💥 A CHILLING CRITICAL BLOW FROM THE ENEMY!",
    " 💥 THE ENEMY LANDS A VICIOUS CRITICAL HIT!",
    " 💥 THE ENEMY UNLEASHES A SURGE OF POWER,"
    " CRITICALLY STRIKING YOU!",
    " 💥 THE AIR TENSES AS THE ENEMY'S"
    " CRITICAL ATTACK LANDS!",
    " 💥 YOU REEL FROM THE OVERWHELMING FORCE OF THE ENEMY'S"
    " CRITICAL BLOW!"
]


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


def reset_enemy(enemy):
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
                "Items": ["Goblin Dagger"]
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
        print("\n 👊 1. Bring it on!")
        print("\n 😭 2. No, i want my mommy!")
        choice = get_choice(2)
        if choice == 1:
            break
        elif choice == 2:
            print("\n Too bad, it is time to wear the big boy pants!\n")
            break


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
        reset_enemy(enemy)

    def handle_loot(self):
        """
        Handles loot
        """
        self.player["Stats"]["Gold"] += self.enemy["Loot"]["Gold"]
        print(f" You got {self.enemy['Loot']['Gold']} Gold 💰!")

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
                if stat != "Type" and stat != "Name":
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
                print(f"🎉 You found and equipped {item_name} 🎉")
            else:
                print(f" Found {item_name}({item_detail['Type']}), but current"
                      " equipment is better!")
        else:
            self.player["Equipment"][item_type] = item_detail
            for stat, value in item_detail.items():
                if stat != "Type" and stat != "Name":
                    self.player["Stats"][stat] += value
            print(f" 🎉 You found and equipped {item_name}"
                  f"({item_detail['Type']})! 🎉")

    def print_player_potions(self):
        """
        Prints the player's available potions in the combat menu
        """
        print()  # Prints an empty line for separation
        for idx, (potion, details) in enumerate(
                self.player["Potions"].items(), 1):
            quantity = details["Quantity"]
            heal_amount = details["Heal Amount"]
            print(f" 🧪 {idx}. {potion} ({quantity}): Heals {heal_amount}HP")
        print(" 🔄 4. Back to the Combat Menu!")

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
                      f" healed for {heal_amount}HP"
                      f" back to {self.player['Stats']['Current HP']} ❤️!")
                return True  # Potion was used

            else:
                print()  # Prints an empty line for separation
                print(f" 🚫 You don't have any {selected_potion} left!")

    def display_combat_info(self):
        """
        Compares stats of player and enemy
        """
        print("PLAYER\t\tENEMY")
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
                  " 🛡️🛡️🛡️ Your defense is too high!")

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
                  "\n 🧪 2. Item"
                  "\n 📜 3. Info"
                  "\n 💨 4. Run")
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
                    print(" 🚫 You did no damage."
                          " The enemy's defense is too high!")

                if self.enemy['Current HP'] > 0:
                    self.enemy_attack()

            elif choice == 2:
                if self.use_potion():
                    self.enemy_attack()

            elif choice == 3:
                self.display_combat_info()

            else:
                if player_run_away(self.enemy['Run']):
                    print(" 💨 You successfully ran away!")
                    return  # Exits the combat loop

                else:
                    print(f" 🚫 The {self.enemy['Name']} blocked your way."
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
    print()  # Prints an empty line for separation
    print(" " + "-" * 39)


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
          " captivating stories, and hidden treasures beckons you.")
    print(" As you embark on this epic journey, remember:"
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
          "\n\n 1. 🛡️  Enter your name and begin your adventure."
          "\n\n 2. 📘 Read about the rules of Text-Land."
          "\n\n 3. 🚪 Exit to the real world.")

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
    print("\n Blinking awake, you find yourself by a serene lake."
          " How did you end up here? Your memory's a blur."
          "\n As you're piecing things together, a distant"
          " scream of help shatters the tranquility."
          "\n Something's not right!"
          "\n What will you do?")
    while True:
        print("\n 👣 1. Investigate the source of the scream."
              "\n\n 💤 2. The screams dont concern you."
              " You rather go back to sleep."
              "\n\n 📖 3. Player Info")

        choice = get_choice(3)
        if choice == 1:

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
    This is going to be the second scene wich serves
    as an introduction to the combat mechanic.
    The fight is intended to be easy to win.
    """
    print("\n Rushing towards the scream, you discover a goblin threatening"
          " a merchant beside his cart dragged by a horse."
          '\n Goblin: "Hand over your gold, human!"'
          '\n Merchant (spotting you and with hopeful eyes): "Stranger!'
          ' Please, help me!"'
          "\n The goblin, hearing the merchant's plea, whirls around to"
          " face you, his eyes narrowed.")
    print("\n Goblin: \"Mind your own business,\" he snarls,"
          " \"or you're next!\"")
    while True:
        print("\n ⚔️  1. Charge the goblin head on!"
              "\n\n 🤷 2. The goblin is right, this is not your problem."
              "\n\n 📖 3. Player Info")
        choice = get_choice(3)

        if choice == 1:
            print("\n The merchant's eyes widen in hope as you take a stance "
                  "between him and the menacing creature."
                  "\n With a determined glint in your eyes, you charge towards"
                  " the goblin.")
            fight_pause_and_continue()
            battle = Combat(player, enemy["Goblin"])
            battle.combat_loop()
            break
        elif choice == 2:
            print("\n As you decide to turn around, hoping to distance "
                  "yourself from the goblin's aggression,")
            print("\n the soft padding of its feet grows rapidly louder"
                  "behind you. You glance over your shoulder.")
            print('\n You see just in time the goblin\'s wicked grin,'
                  ' eyes alight with malicious intent.')
            print('\n "Thought you could ignore me, did you?" the goblin'
                  '  sneers. Easier prey than I thought!"')
            print('\n With no other choice, you brace yourself'
                  " to fend off the goblin's surprise assault.")
            fight_pause_and_continue()
            battle = Combat(player, enemy["Goblin"])
            battle.combat_loop()
            break
        elif choice == 3:
            print_player_info_menu(player)


def third_scene():
    """
    This is going to be the third scene after defeating the goblin
    """
    print_horizontal_line()
    print("\n Catching his breath, the merchant straightens up and beams at "
          'you.\n "Thank you, kind stranger. Without your intervention, '
          'I fear what that goblin would have done to me."'
          """\n He extends a hand in gratitude, "The name's Elidor"""
          " Silversmile, but folk around these parts call me"
          '\n Elidor Coinstride, on account of my dealings and wares."')
    print()  # Prints an empty line for separation
    print("\n Taking a moment to observe Elidor, it's clear that"
          " he has Halfling origins. Standing shorter than most."
          "\n His stature is a bit rotund, giving him a cherubic "
          "appearance.\n Pointy ears peek out from beneath a cascade of white "
          "hair, accentuated by prominent sideburns that frame his face."
          "\n Beside him stands a magnificent white horse, its gray mane"
          " flowing gracefully. \n The contrast between the majestic steed and"
          " the diminutive merchant creates a heartwarming scene."
          """\n "A beautiful creature, isn't she?" Elidor remarks, noticing"""
          """ your admiration. \n "She's been """
          'my loyal companion for years, traveling through thick and thin."')
    while True:
        print_horizontal_line()
        print()  # Prints an empty line for separation
        print(' 🐴 1. "She is indeed beautiful, how are you faring?'
              '\n\n 🤲 2. "I\'m glad you\'re safe, but a reward for my troubles'
              ' would be appreciated."')
        choice = get_choice(2)
        if choice == 1:
            print("\n Elidor looks at you gratefully and says, "
                  '"Thank you for asking, kind traveler.'
                  "\n It\'s not every day you find someone so considerate. "
                  "We are both well, thanks to you.\n The road has been hard,"
                  " but having Medea, my horse, by my side makes it easier."
                  '\n Please, take this as a token of my gratitude.'
                  "\n He hands you a small pouch of coins.")
            player["Stats"]["Gold"] += 50
            print("\n You obtained 50 Gold 💰!"
                  " You can carry gold in your pouch from now on.")
            print()  # Prints an empty line for separation
            break
        elif choice == 2:
            print("\n The halfling seems a bit taken aback by your forwardness"
                  '.\n After a moment of hesitation, he says, '
                  '"Well, I suppose it\'s fair to ask for compensation after '
                  'such a deed.\n He reluctantly "'
                  " hands you a slightly large pouch of coins.")
            player["Stats"]["Gold"] += 75
            print("\n You obtained (basically extorted..) 75 Gold 💰!"
                  " You can carry gold in your pouch from now on.")
            print()  # Prints an empty line for separation
            break


def fourth_scene():
    """
    This is the fourth scene in wich the merchant will join,
    this will start the branches of the story and serves as
    an end to the "tutorial" like face.
    """
    print_horizontal_line()
    print("\n As you continue to converse, Elidor starts packing up his cart. "
          "The clinking of vials and the rustling of cloth can be heard.")
    print('\n \"You know, I\'m headed to the city of Veradia. '
          "It's a big, bustling place and I've some important business there.")
    print("\n Delivering a certain... package, so to speak. It's a long "
          "journey and, after the goblin incident, I realize I could use "
          "some protection.")
    print("\n Given how adeptly you handled that goblin,"
          " would you be interested in "
          "accompanying me?\n I'm willing to pay for your services and, "
          "of course, my shop's at your disposal for resupply.\"")
    print()  # Prints an empty line for separation
    print("\n You ponder on his request. You really don't have any idea where"
          " you are or where you're headed.\n Would it be such a bad idea to"
          " accompany him?")

    while True:
        print("\n\n 👍 1. \"Certainly, Elidor. It'll be my pleasure to"
              " accompany you.\"")
        print("\n\n 👎 2. \"Thanks for the offer, but I must go my own way.\"")
        choice = get_choice(2)

        if choice == 1:
            print("\n Elidor grins, looking visibly relieved. \"Excellent!"
                  " With your combat skills "
                  "and my... ahem, 'tricks of the trade', I'm sure we'll make"
                  " it to the city safely.\"")
            break
        elif choice == 2:
            print("\n Elidor raises an eyebrow, looking a tad confused."
                  " \"Well, if you don't want to come with me, "
                  "\n then it only makes sense that I'll have to go with you!"
                  " Let's set forth, friend.\""
                  "\n You try to piece together the logic of what Elidor just"
                  " said and come up blank."
                  "Before you can even react, he's already on his way, "
                  "mounting Medea and waving for you to follow."
                  "Wasn't he supposed to follow you?")
            break

    print("\n \"By the way,\" Elidor interjects, \"I usually rely on my "
          "intuition for travel, but seeing as you're my protector now, "
          "I'll leave the decisions up to you."
          "There's a small town on the way; we should aim to reach it next. "
          "You decide which way we should take"
          ' to best reach our destination."')


def fifth_scene():
    """
    Fifth Scene
    """
    print_horizontal_line()
    print("\n As you and Elidor travel together, the path ahead"
          "forks into three distinct routes.")
    print("\n To the right, the gentle sound of a river is heard"
          " and the shimmering water can be seen in the distance.") 
    print("\n Straight ahead lies the main road, well-trodden and marked with"
          " milestones indicating the way to the closest town.")
    print("\n The left path dives deep into a dense, dark forest. Amongst the "
          "trees, tall grasses sway gently, \n reaching up to a person's"
          " height, shading the path from the midday sun.")

    while True:
        print("\n 🌊 1. Head towards the river route.")
        print("\n\n 🛣️ 2. Stick to the main road.")
        print("\n\n 🌲 3. Venture into the forest.")
        print("\n\n 📖 4. Player Info")
        choice = get_choice(4)

        if choice == 1:
            print("\n With the river by your side offering a soothing ambiance"
                  ", you and Elidor start your journey on the river route.")
            print("\n Elidor seems pleased with the decision, the fresh scent "
                  "of the river lifting his spirits.")
            break
        elif choice == 2:
            print("\n Deciding to stick to what seems safest, you and Elidor"
                  " continue on the main road.")
            break
        elif choice == 3:
            print("\n Feeling adventurous, you decide to delve into"
                  " the woods.")
            print("Were it not for Medea, Elidor would be completely "
                  "obscured by the tall grass.")
            break
        elif choice == 4:
            print_player_info_menu(player)


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
