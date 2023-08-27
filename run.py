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
        print("Enter your name")
    else:
        intro()


def intro():
    """
    Prints out the intro
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
        print("Input your name")

    elif choice == 2:
        rules()

    else:
        print("Not everyone is suited to be a Hero \U0001F44E Goodbye!")


intro()
