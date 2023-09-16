## Introduction

# 🎮 WELCOME TO TEXT-LAND 🎮
Welcome to Text-Land, the Text-Based Adventure Game reminiscent to the days of retro gaming!

Dive into an immersive world that combines the charm of classic text-based games with the depth of RPG elements. Every step you take is driven by lore, every decision influenced by narratives rooted in rich histories and mysteries.

Enchanting Forests: Traverse deep woods filled with secrets.

Treacherous Rivers: Navigate waters where every turn could be your last.

Dangerous Roads: Journey across lands where friend and foe are often indistinguishable.

Your choices won't just determine your path—they'll write the legends of Text-Land.                                                                     
Embrace the nostalgia, but stay sharp: in this game, choices truly matter.

Play it here: 🎮 [TEXT-LAND](https://text-land-6fba33f8e155.herokuapp.com/)

![Responsive Screenshot](/assets/images/responsive.PNG)

## Content Table
- [Introduction](#introduction)
- [UX](#ux)
  - [Site Purpose](#site-purpose)
  - [Site Goal](#site-goal)
  - [Audience](#audience)
  - [Current User Goals](#current-user-goals)
  - [New User Goals](#new-user-goals)
- [Features](#features)
  - [Choices](#choices)
  - [Rules](#rules)
  - [Personalized Naming](#personalized-naming)
  - [Player Info](#player-info)
  - [Combat System](#combat-system)
  - [Branching Paths](#branching-paths)
  - [Future Features](#future-features)
- [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [Unfixed Bugs](#unfixed-bugs)
- [Thought Of Process](#thought-of-process)
  - [Regrets](#regrets)
  - [Wireframes](#wire-frames)
- [Technologies Used](#technologies-used)
  - [Main Languages Used](#main-languages-used)
  - [Frameworks, Libraries, Programs](#frameworks-libraries-and-programs-used)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

## UX

### Site Purpose:

The primary purpose of Text-Land is to provide users with an interactive, text-based gaming experience that transports them to a world of adventure, decision-making, and unforeseen outcomes.

### Site Goal:
To ensure that each player's journey is unique through a series of choices and consequences, offering different paths and endings, making each gameplay session a novel experience.

### Audience:
Nostalgic Gamers: Those who have fond memories of the golden age of text-based games and are looking for a modern twist on their beloved classics.

Modern RPG Fans: Players who enjoy role-playing games with a rich narrative and the power of choice, steering their own story.

Casual Gamers: With its easy-to-understand mechanics and intriguing stories, Text-Land is perfect for those looking to enjoy a game during breaks or spare time without the commitment of heavy gameplay.

### Current User Goals:
Given the branching nature of the story, users hope to revisit the game multiple times to explore alternative paths and endings.

Each journey through Text-Land offers a fresh experience. The paths taken and monsters encountered vary in the items they present, ensuring that every adventure feels new and unpredictable.

### New user Goals:
- New users will be able to grasp the game's premise, mechanics, and objectives within minutes of starting.
- The narrative will captivate and pull new users into the world of Text-Land, motivating them to delve deeper into the adventure.
- Encourages a sense of curiosity. Users will want to explore different paths and outcomes, realizing that every choice can lead to a distinct adventure.
- The initial experience has been designed to be intriguing enough that new users want to come back, explore different storylines, or improve their outcomes.

## Features

### Choices:

Accompanied by illustrative emojis, the gameplay mechanics revolve around making choices that will steer the course of the adventure.

The choice function is undeniably the brain of this program.

- Intuitive Interface: 
Designed for simplicity and clarity, the game interface makes it apparent how the choice system functions.
- Foolproof Input System:
For numbers outside the choice range: Users receive a prompt warning, indicating the need to input a value within the available decision range.
For non-numerical inputs: A warning message instructs players to provide a numeric value, clarifying which specific number corresponds to each choice option.

- Emoji-Backed Decisions: Enhancing the visual comprehension, every choice is symbolized with an emoji, providing an additional layer to understand the consequences or themes of each decision. This ensures a more engaging and intuitive user experience.

![Choices](/assets/images/choices.PNG)

### Rules:

- Immediate Access: Right from the start, players can delve into the rules, ensuring they have a firm grasp of the gameplay mechanics before embarking on their adventure.

- Clear Explanation on Choices: The guide elucidates how the choice-driven gameplay operates, ensuring players know what to anticipate from their decisions.

- Combat Insight: It provides an in-depth look into the combat statistics, offering players clarity on how combat scenarios unfold and how different combat-related features impact their journey. This knowledge equips players with the strategic depth required to make informed decisions during confrontations.

![Rules](/assets/images/rules.PNG)

### Personalized Naming:
- Custom Player Identity: Players are given the opportunity to immerse themselves more deeply into the adventure by personalizing their character with a name of their choice.

- Inclusive Naming: I've even allowed numerical inputs in the naming process. After all, we wouldn't want to discriminate against Elon Musk's son, would we? 😄

- Default Naming: If players choose not to provide a name or accidentally submit an empty value, the game automatically dubs them as "Hero", ensuring a smooth experience and maintaining the narrative flow.

![Name](/assets/images/name.PNG)

### Player Info:
- Informed Decision Making: Throughout the adventure, players have near-constant access to their character's crucial stats, potions, and equipment. 

- Strategic Planning: By having immediate insights into their character's strengths, weaknesses, and available resources, players can effectively strategize for upcoming challenges and encounters.
- Immersive Experience: This continuous access to character information enhances immersion, as players are always aware of their hero's current state.

![Player Info](/assets/images/player-info-option.PNG)
![Player Stats/Potion](/assets/images/player-info-stat-potion.PNG)
![Player Equipment](/assets/images/player-info-stat-equip.PNG)

### Combat System:
An in-depth Look of the Combat function.
- Foundation of the Game: The combat class is undeniably the centerpiece of Text-Land. If the Choice function is the brain, then the Combat class is the heart. Meticulously crafted, this function epitomizes the essence of the game and its strategic RPG elements. It is my Magnum Opus.

- The Initial Vision: The aspiration was to integrate ASCII art for each adversary, enhancing the immersive experience for players. While the initial design included the concealment of enemy HP, revealing it only upon acquisition of the "Magnifying Glass", time constraints led to some revisions. However, the infrastructure for these planned features, like the Pandora's box function, remains embedded in the code for potential future enhancements.

- Dynamic Enemy Display: The combat function's versatility shines as it can fetch and display varying enemy names from the dictionary. This ensures that the combat experience remains fresh and unpredictable with the possibility of introducing new enemies seamlessly.

- Mana and Magic: Initially, the design encompassed a mana system governing elemental attacks and healing abilities. Envisioned were elemental resistances to deepen the combat dynamics. 
The idea is to give the player an initial amount of 10 mana while the spell cost of each ability would be 5 mana. The player would be able to recover 1 mana each turn. This would introduce elemental resistances (physical, fire, ice, nature) wich each enemy having a multiplier between 0.3 and 2.0 that would server as an ulterior way of calculating damage and adding strategic depth. The code for this design is saved in my notes, however, this ambitious feature awaits future integration, as time did not allow me to test it enough to be implemented in the final draft before the submission.
![Combat](/assets/images/combat.PNG)

Player Options:

- Attack: The damage mechanics are straightforward yet offer depth. Attack power is determined by the difference between the attacker's ATK and defender's DEF, adjusted by a damage roll between 80% and 120% of the difference to add an element of unpredictability.

- Crit Mechanic: Introducing an additional layer of strategy, the critical hits vary between the player and enemies. Players, upon landing a crit, deal augmented damage bypassing a portion of the enemy's defense. Conversely, enemy crits are more frequent but only amplify the damage. A random message gets triggered for player and enemy upon a critical strike taken from a list of messages.

- Items: Players can peruse through their inventory, viewing the quantities and healing capabilities of various potions. This is done by iterating through the items in the player's dictionary.

![Combat Item](/assets/images/combat-potions.PNG)

- Info: For the strategists, this option lays out a comparative analysis of player and enemy stats.

![Combat Info](/assets/images/combat-info.PNG)
- Run: Escaping battles is a gamble. Each adversary possesses a unique 'run' stat, representing the success probability of a player's escape attempt. Failure to flee leaves the player vulnerable to an enemy strike.

![Combat Run](/assets/images/combat-run.PNG)

- Battle Outcome Determination: The combat system meticulously logs the result of each skirmish. Victory or retreat, each decision impacts the narrative, leading to branching paths and varying outcomes.

- Enemy Dictionary Reset: The combat system resets the enemy dictionaries allowing to battle the same enemy again. 

- Loot System: Victories in combat can be rewarding. Post-battle, the function sifts through the defeated enemy's inventory, granting gold and potential equipment upgrades to the player based on drop rates.

- Auto-Equip Mechanism in Combat:
Within the combat function, there's an intelligent system in place that evaluates the attributes of looted items. Should the player emerge victorious from a skirmish and acquire an item, the function automatically performs a comparison between the player's current equipment and the newly obtained item. If the new item proves superior, the system seamlessly auto-equips it for the player, ensuring they always have the best gear equipped without manually sifting through their inventory. This feature prioritizes player efficiency and optimizes their combat readiness for forthcoming challenges.

![Combat Victory](/assets/images/combat-victory.PNG)

### Branching Paths:
The narrative framework of this project was originally conceptualized to be an introductory or tutorial phase, with the initial town marking the first significant juncture in the player's journey. From this point, the storyline was intended to diverge dramatically, offering players distinct paths that would influence their alignment towards either good or evil.

However, due to constraints in development time, the scope was refined to conclude at the first town. Nevertheless, even within this limited framework, players will encounter a triad of distinct pathways, each with its unique sequence of events and treasures to uncover. This ensures that each playthrough offers a fresh experience, and encourages exploration of all routes to fully appreciate the depth of the story.

![Branching Story](/assets/images/story%20wireframe.PNG)

### Future Features:
- ASCII ART for enemies and important messages
- Retro 8 bit music
- Special items that enhance gameplay differently than raw statistics
- Magic
- Elemental resistances and attacks
- Advance the plot as initially planned

## Testing 
Given the vast expanse of choices and possible outcomes in this project, the traditional approach of implementing a testing table, which I have employed in past projects, becomes infeasible. Especially with the tight constraints of time, aiming to finalize everything just a couple of hours prior to the deadline.

That being said, rigorous testing has been a staple throughout the development process. Every scenario has been meticulously played through multiple times to ensure the desired outcomes are achieved, and any potential bugs are ironed out. This iterative testing approach guarantees that the final product offers players a seamless and enjoyable experience.

### Validator Testing:

CI Python Linter:
![CI Linter](/assets/images/CI-linter.PNG)

### Unfixed Bugs

- One peculiar bug managed to elude resolution during the testing phase. Specifically, when the player defeats Petalback, there are rare occurrences where the enemy revives with a health range of just one attack. Intriguingly, this anomalous behavior is confined solely to this particular enemy. Despite the enemy dictionary resetting and the loop breaking as intended, this unexpected revival takes place. The exact conditions to replicate this bug consistently remain elusive.

Multiple attempts were made to rectify this, including adjusting the reset function and its positioning, but the issue persists. Fortunately, its occurrence is infrequent, and even when it does manifest, it's limited to just a singular revival, thus not critically affecting gameplay. Given its rarity and the non-critical nature, the decision was made to deprioritize its resolution for the time being.

## Thought Process

The inception of this project stemmed from a desire to grapple with  certain concepts that had proven challenging during my learning journey. There were two primary concepts I aimed to delve deeper into: classes and dictionaries.

Class: Embarking on this project, I found it deeply ironic that the element which had been a consistent thorn in my side during the course, ended up being the backbone of my entire game. Classes were initially my Achilles' heel. Their complexity and depth had been a constant challenge throughout my learning journey. However, as I delved deeper into their structure and capabilities, they transformed from being my most formidable obstacle to the very foundation of this project.

Dictionaries: Much like classes, dictionaries began as another point of contention but soon showcased their immense potential. Their adaptability offered the scalability the project demanded, allowing for:

Seamless Customization: Thanks to these enemies turned allies i have now the ability in this project to integrate new scenarios, enemies, or items without tampering with the foundational code. 

Intuitive Expansion with Magic Attacks and Resistances: One of the proudest features of this project is its inherent capability for easy expansion, especially when it comes to complex systems like magical combat.

Elemental Resistances: The foundational design allows for the effortless inclusion of elemental resistances. By simply appending the resistance stats to enemies within the dictionary, the combat class autonomously pulls and applies them during combat scenarios.

Magic Attacks: Similarly, the structure is primed to accommodate magic attacks. Their integration doesn't demand a revamp of the core mechanics but merely the addition of the relevant details into the existing dictionaries.

Self-Sufficiency in Expansion: The overarching design principle was to create a system that’s self-reliant. By laying down a robust and versatile foundation, the game can be expanded upon endlessly such as:
- Adding Enemies & Items: New adversaries or collectibles can be woven into the narrative with ease, demanding no changes to the core but simply enhancing the game’s content.

- Scenario Incorporation: The game’s true strength lies in its adaptability. As it stands, my primary responsibility to evolve the game revolves around crafting new scenarios. The existing infrastructure is adept at absorbing, processing, and presenting these new tales, making the storytelling process seamless and unbounded.

Reusable and Expandable Code: A key philosophy I adhered to was ensuring the code's longevity recognizing the potential for future growth.
New equipment slots like amulets or rings can be smoothly integrated by simply adding them to the player's dictionary, emphasizing the project's forward-compatible design.

In summation, this project became a powerful reminder of the twists and turns of learning. What was once a point of consternation transformed into the linchpin of my project, underscoring the unpredictable beauty of the educational journey.

### Regrets
While I am proud of what I've achieved, I acknowledge the potential refinements. A glaring area for optimization lies in the refactoring of the code.

Lore Organization: Print statements, predominantly those narrating the lore, can be organized better. Transferring them to a separate module or file would streamline the main code, enhancing readability and maintenance.

Incorporation of ASCII Art: Aesthetics play a crucial role in game immersion. My original vision encompassed the integration of ASCII art, sourced from a dedicated file, to vividly represent enemies. This visual element would have undoubtedly elevated the user experience.

Dynamic Text Presentation: Another feature that regrettably didn't make the cut was the dynamic speed of text display. Instead of an immediate print, a gradual reveal would have intensified the storytelling.

Colored Text: This small but impactful tweak would've assisted in distinguishing different game elements, creating a richer visual landscape.

While certain features were sidelined due to time constraints, it's crucial to note that it was a matter of time, not capability.

Upon the conclusion of the course, I aim to revisit and revamp this project, integrating graphical libraries to transition from a solely text-based experience to a visually richer one.

As I delved deeper into this project, 8-bit music from various platforms became my muse, fueling my creative narrative drive. The auditory element holds immense power in shaping a gamer's journey, and it’s a matter of personal sorrow that I couldn't harness this medium to elevate the project's ambiance. In a dream scenario, each twist and turn of the story would be underscored by these retro tunes, making the adventure both a visual and auditory delight.

In wrapping up, while this project might have its limitations as it stands, it embodies my learning journey, my aspirations, and a promise of what it can evolve into with time and dedication.

### Wire Frames
Contained within the subsequent wireframe is the raw, unfiltered visualization of my concept. While it may appear chaotic and unrefined, it captures the genuine essence of the developmental process. I consciously chose not to polish these initial sketches, wanting to retain and present the authentic emotion and fervor that birthed this project.

In many ways, these sketches offer a candid window into the whirlwind of ideas, dilemmas, and epiphanies that marked the genesis of the game. The seeming disorder is emblematic of the organic, free-flowing thought process that, over time, coalesced into a structured game narrative.

Much of the initial sketch was inspired by the Pokemon Games. The 80%-120% damage roll is a damage calculation from the Pkmn games.
Note how i accepted the utility of the Dictionaries but i refused to use classes.
It is visible in the commits how i later had to give up the Combat function to make space for a combat class when i slowly started adding too many functionalities related to combat.
![Initial Sketch](/assets/images/initial-sketch.PNG)

Some of implemented ideas and some still to apply. 

Spoiler alert: Elidor will betray you in the end.
![Ideas Fly](/assets/images/ideas-thrown.PNG)

## Technologies Used
### Main Languages Used
Python
### Frameworks, Libraries and Programs Used
- LucidChart - for planning and overview of the scenes
- Random package - used to give some variety to the combat and scenarios
- GitPod - used CI Python Essentials Template
- GitHub - used to store my repository for submission.
## Deployment 
The project was deployed to Heroku. The steps to deploy are as follows:
- log in to heroku
- create a new app
- chose my region
- create app (again)
- navigate to settings
- add build packs in the following order: Python, nodejs
- chose GitHub as deployment method
- connected to the repository with the CI python essentials template
- connected GitHub and Heroku
- chose to enable automatic deploys
- The live link can be found both [HERE](https://text-land-6fba33f8e155.herokuapp.com/) and in the introduction of this document
## Credits 
How to use docstring - https://www.geeksforgeeks.org/python-docstrings/

How to use slowprint (wich hasn't been used) - https://replit.com/talk/learn/The-Slow-Print/44741

All the code for this project was crafted, "fine-tuned" (this word doesn't exactly fit with the mess i created but i need to stay professional and write fancy words), and brought to life by yours truly.

As has become tradition in every project I undertake, Lauren, my mentor, keeps getting used as a way to ventilate (at this point more like the shoulder where i go and cry) and is once again my fountain of youth.
Instead of keeping me young she keeps me motivated and blesses me with new knowledge. 
And just for posterity's sake (and a touch of humor), imagine the irony of having to read this one day if i end up hating her... :D