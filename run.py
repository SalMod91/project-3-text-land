"""
This module contains the main game
"""


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
        player_name()
    else:
        intro()


def player_name():
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
        name = input("What is the name of this hero's story?\n").strip()
        # Checks if name is empty and assigns "Hero"
        if not name:
            return "Hero"
        # Checks if name length is between 1 and 10 charachters
        elif 1 <= len(name) <= 10:
            return name
        else:
            print("Please enter a name between 1 and 10 characters.")


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
          "\n\n1. 🛡️   Enter your name and begin your adventure."
          "\n2. 📘 Read about the rules of Text-Land."
          "\n3. 🚪 Exit to the real world.")

    choice = get_choice(3)
    if choice == 1:
        player_name()

    elif choice == 2:
        rules()

    else:
        print("Not everyone is suited to be a Hero \U0001F44E Goodbye!")


def main():
    """
    Starts the game
    """
    intro()


main()
