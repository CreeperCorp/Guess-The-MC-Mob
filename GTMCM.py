import random
import textwrap

# Full list of Minecraft mobs (Java Edition 1.20, excluding variants/unused/test mobs)
mobs = [
# Passive Mobs
{"name": "Bat", "desc": "A small, flying creature found in caves.", "type": "Passive", "hint": "It hangs upside down and squeaks.", "icon": "🦇"},
{"name": "Cat", "desc": "A small, tameable feline, often found in villages.", "type": "Passive", "hint": "Scares away creepers.", "icon": "🐱"},
{"name": "Chicken", "desc": "A common farm animal that lays eggs.", "type": "Passive", "hint": "Drops feathers and eggs.", "icon": "🐔"},
{"name": "Cod", "desc": "A fish found in oceans and rivers.", "type": "Passive", "hint": "Brownish fish, can be caught with a bucket.", "icon": "🐟"},
{"name": "Cow", "desc": "A common farm animal, useful for leather and milk.", "type": "Passive", "hint": "Drops beef and leather.", "icon": "🐄"},
{"name": "Donkey", "desc": "A tameable animal that can carry chests.", "type": "Passive", "hint": "A horse's humble cousin.", "icon": "🫏"},
{"name": "Fox", "desc": "A small, fast, and sneaky animal found in taiga biomes.", "type": "Passive", "hint": "Likes to sleep and carries items in its mouth.", "icon": "🦊"},
{"name": "Frog", "desc": "A hopping amphibian found in swamps.", "type": "Passive", "hint": "Eats small slimes and magma cubes.", "icon": "🐸"},
{"name": "Glow Squid", "desc": "A glowing aquatic mob found in dark water.", "type": "Passive", "hint": "Drops glowing ink sacs.", "icon": "🦑"},
{"name": "Horse", "desc": "A fast, rideable animal that can be tamed.", "type": "Passive", "hint": "Can wear armor and jump high.", "icon": "🐎"},
{"name": "Mooshroom", "desc": "A red and white cow found in mushroom fields.", "type": "Passive", "hint": "Can be milked for mushroom stew.", "icon": "🐮🍄"},
{"name": "Mule", "desc": "A hybrid of horse and donkey, can carry chests.", "type": "Passive", "hint": "Cannot breed with its own kind.", "icon": "🐴🫏"},
{"name": "Ocelot", "desc": "A wild cat found in jungles.", "type": "Passive", "hint": "Was once tamed into cats.", "icon": "🐆"},
{"name": "Parrot", "desc": "A colorful bird that mimics mob sounds.", "type": "Passive", "hint": "Can dance to music.", "icon": "🦜"},
{"name": "Pig", "desc": "A pink farm animal, rideable with a saddle.", "type": "Passive", "hint": "Drops porkchops.", "icon": "🐖"},
{"name": "Pufferfish", "desc": "A spiky fish that inflates when threatened.", "type": "Passive", "hint": "Causes poisoning if touched.", "icon": "🐡"},
{"name": "Rabbit", "desc": "A small, quick animal that hops around.", "type": "Passive", "hint": "Can drop rabbit's foot.", "icon": "🐇"},
{"name": "Salmon", "desc": "A pinkish fish found in cold and river biomes.", "type": "Passive", "hint": "Can be caught with a bucket.", "icon": "🐟"},
{"name": "Sheep", "desc": "A woolly animal that can be sheared.", "type": "Passive", "hint": "Comes in many colors.", "icon": "🐑"},
{"name": "Skeleton Horse", "desc": "An undead horse, can be ridden.", "type": "Passive", "hint": "Summoned during thunderstorms.", "icon": "🐎💀"},
{"name": "Snow Golem", "desc": "A snowman mob that throws snowballs.", "type": "Passive", "hint": "Created by stacking snow blocks and a pumpkin.", "icon": "☃️"},
{"name": "Squid", "desc": "A common aquatic animal in oceans and rivers.", "type": "Passive", "hint": "Shoots ink when attacked.", "icon": "🦑"},
{"name": "Strider", "desc": "A lava-walking mob found in the Nether.", "type": "Passive", "hint": "Can be saddled and ridden.", "icon": "🦶🔥"},
{"name": "Tadpole", "desc": "A baby frog, grows into a frog over time.", "type": "Passive", "hint": "Smallest mob in the game.", "icon": "🐟🐸"},
{"name": "Tropical Fish", "desc": "A colorful fish found in warm oceans.", "type": "Passive", "hint": "Many types and colors.", "icon": "🐠"},
{"name": "Turtle", "desc": "A slow, shelled reptile that lays eggs.", "type": "Passive", "hint": "Drops scutes when growing up.", "icon": "🐢"},
{"name": "Villager", "desc": "A humanoid mob that trades and works in villages.", "type": "Passive", "hint": "Says 'Hrmm.'", "icon": "👨‍🌾"},
{"name": "Wandering Trader", "desc": "A traveling merchant with llamas.", "type": "Passive", "hint": "Trades random goods for emeralds.", "icon": "🧑‍🌾"},
{"name": "Bee", "desc": "A flying insect that pollinates flowers.", "type": "Passive", "hint": "Can sting and become angry.", "icon": "🐝"},
{"name": "Axolotl", "desc": "An amphibious creature found in lush caves.", "type": "Passive", "hint": "Regenerates health and helps fight underwater.", "icon": "🦎"},
{"name": "Goat", "desc": "A mountain-dwelling animal that can ram players.", "type": "Passive", "hint": "Drops horns.", "icon": "🐐"},
{"name": "Camel", "desc": "A rideable animal found in deserts.", "type": "Passive", "hint": "Can carry two players.", "icon": "🐫"},
# Neutral Mobs
{"name": "Dolphin", "desc": "A playful aquatic mammal.", "type": "Neutral", "hint": "Leads players to treasure.", "icon": "🐬"},
{"name": "Enderman", "desc": "A tall, teleporting mob that dislikes being stared at.", "type": "Neutral", "hint": "Carries blocks and hates water.", "icon": "👾"},
{"name": "Goat", "desc": "A mountain-dwelling mob that can ram you.", "type": "Neutral", "hint": "Drops horns.", "icon": "🐐"},
{"name": "Iron Golem", "desc": "A large, strong protector of villagers.", "type": "Neutral", "hint": "Created by villagers or players.", "icon": "🤖"},
{"name": "Llama", "desc": "A woolly pack animal that spits.", "type": "Neutral", "hint": "Used for transporting goods.", "icon": "🦙"},
{"name": "Panda", "desc": "A bamboo-eating bear found in jungles.", "type": "Neutral", "hint": "Rolls around and has different personalities.", "icon": "🐼"},
{"name": "Piglin", "desc": "A gold-loving Nether mob.", "type": "Neutral", "hint": "Attacks unless you wear gold armor.", "icon": "🐗"},
{"name": "Polar Bear", "desc": "A white bear found in snowy biomes.", "type": "Neutral", "hint": "Becomes hostile if cub is nearby.", "icon": "🐻‍❄️"},
{"name": "Trader Llama", "desc": "A special llama accompanying the Wandering Trader.", "type": "Neutral", "hint": "Tied to a trader.", "icon": "🦙"},
{"name": "Wolf", "desc": "A neutral mob that can be tamed into a loyal companion.", "type": "Neutral", "hint": "Tamed with bones.", "icon": "🐺"},
# Hostile Mobs
{"name": "Blaze", "desc": "A flying, fire-throwing mob found in Nether fortresses.", "type": "Hostile", "hint": "Drops blaze rods.", "icon": "🔥"},
{"name": "Cave Spider", "desc": "A poisonous variant of spider found in mineshafts.", "type": "Hostile", "hint": "Smaller and blue.", "icon": "🕷️"},
{"name": "Creeper", "desc": "A silent, green monster that explodes when it gets close.", "type": "Hostile", "hint": "Infamous for blowing up builds.", "icon": "💥"},
{"name": "Drowned", "desc": "An underwater zombie variant.", "type": "Hostile", "hint": "Can hold a trident.", "icon": "🧟‍♂️"},
{"name": "Elder Guardian", "desc": "A large, boss-like guardian found in ocean monuments.", "type": "Hostile", "hint": "Gives Mining Fatigue effect.", "icon": "🐟👑"},
{"name": "Endermite", "desc": "A small, rare mob spawned by Ender Pearls.", "type": "Hostile", "hint": "Similar to Silverfish.", "icon": "🐛"},
{"name": "Evoker", "desc": "A spell-casting illager that summons vexes.", "type": "Hostile", "hint": "Drops Totem of Undying.", "icon": "🧙‍♂️"},
{"name": "Ghast", "desc": "A floating, ghost-like mob that shoots fireballs.", "type": "Hostile", "hint": "Cries and lives in the Nether.", "icon": "👻"},
{"name": "Guardian", "desc": "A spiky fish defending ocean monuments.", "type": "Hostile", "hint": "Shoots lasers.", "icon": "🐡"},
{"name": "Hoglin", "desc": "A hostile pig-like mob in the Nether.", "type": "Hostile", "hint": "Drops porkchops.", "icon": "🐗"},
{"name": "Husk", "desc": "A desert-dwelling zombie variant.", "type": "Hostile", "hint": "Inflicts Hunger.", "icon": "🧟"},
{"name": "Illusioner", "desc": "A spell-casting illager that blinds and duplicates itself.", "type": "Hostile", "hint": "Unused in survival.", "icon": "🧙‍♂️"},
{"name": "Magma Cube", "desc": "A jumping, fiery cube found in the Nether.", "type": "Hostile", "hint": "Drops magma cream.", "icon": "🟥"},
{"name": "Phantom", "desc": "A flying mob that attacks tired players.", "type": "Hostile", "hint": "Drops phantom membranes.", "icon": "👻"},
{"name": "Piglin Brute", "desc": "A stronger, meaner piglin found in bastions.", "type": "Hostile", "hint": "Always hostile, even if you wear gold.", "icon": "🐗💪"},
{"name": "Pillager", "desc": "A crossbow-wielding illager.", "type": "Hostile", "hint": "Leads raids on villages.", "icon": "🏹"},
{"name": "Ravager", "desc": "A large, powerful beast ridden by pillagers.", "type": "Hostile", "hint": "Destroys crops.", "icon": "🐃"},
{"name": "Shulker", "desc": "A box-like mob that shoots levitation-inducing bullets.", "type": "Hostile", "hint": "Found in End cities.", "icon": "📦"},
{"name": "Silverfish", "desc": "A tiny, annoying mob found in strongholds.", "type": "Hostile", "hint": "Hides in stone blocks.", "icon": "🐛"},
{"name": "Skeleton", "desc": "A bony ranged attacker that shoots arrows.", "type": "Hostile", "hint": "Drops bones and arrows.", "icon": "🏹💀"},
{"name": "Slime", "desc": "A bouncing green mob that splits into smaller versions.", "type": "Hostile", "hint": "Drops slimeballs.", "icon": "🟩"},
{"name": "Spider", "desc": "A wall-climbing arthropod.", "type": "Hostile", "hint": "Drops string and spider eyes.", "icon": "🕷️"},
{"name": "Stray", "desc": "A skeleton variant found in snowy biomes.", "type": "Hostile", "hint": "Shoots slowness arrows.", "icon": "🏹❄️"},
{"name": "Vex", "desc": "A tiny, flying hostile mob summoned by evokers.", "type": "Hostile", "hint": "Passes through walls.", "icon": "🧚"},
{"name": "Vindicator", "desc": "An axe-wielding illager.", "type": "Hostile", "hint": "Shouts 'Hey-ya!' and charges.", "icon": "🪓"},
{"name": "Witch", "desc": "A potion-throwing mob found in swamps.", "type": "Hostile", "hint": "Drinks potions to heal.", "icon": "🧙‍♀️"},
{"name": "Wither Skeleton", "desc": "A tall, black skeleton found in the Nether.", "type": "Hostile", "hint": "Drops wither skulls.", "icon": "💀"},
{"name": "Zoglin", "desc": "A zombified hoglin.", "type": "Hostile", "hint": "Hostile to everything.", "icon": "🐗💀"},
{"name": "Zombie", "desc": "A slow-moving undead creature.", "type": "Hostile", "hint": "Burns in sunlight.", "icon": "🧟"},
{"name": "Zombie Villager", "desc": "A zombified villager.", "type": "Hostile", "hint": "Can be cured.", "icon": "🧟👨‍🌾"},
{"name": "Zombified Piglin", "desc": "A golden, undead pig creature in the Nether.", "type": "Hostile", "hint": "Neutral unless attacked.", "icon": "🐖💀"},
# Boss Mobs
{"name": "Ender Dragon", "desc": "The main boss of the End dimension.", "type": "Boss", "hint": "Destroys End crystals.", "icon": "🐉"},
{"name": "Wither", "desc": "A floating boss that shoots explosive skulls.", "type": "Boss", "hint": "Summoned with soul sand and wither skulls.", "icon": "☠️"},
{"name": "Warden", "desc": "A blind, powerful mob that detects vibrations.", "type": "Boss", "hint": "Lives in the Deep Dark.", "icon": "👹"}
]

print("="*50)
print("Welcome to Minecraft: Guess the Mob (All Mobs Edition)!")
print("="*50)
print("I will describe a Minecraft mob. Can you guess its name?")
print("Type 'quit' to exit at any time.")
print()

score = 0
rounds = 0

unplayed_indices = list(range(len(mobs)))
random.shuffle(unplayed_indices)

while unplayed_indices:
    idx = unplayed_indices.pop()
    mob = mobs[idx]
    print("\n--- New Challenge! ---")
    print("Mob type:", mob["type"])
    print("Description:", textwrap.fill(mob["desc"], width=60))

    guess = input("\nWhat is the name of this mob? ").strip()
    if guess.lower() == "quit":
        print("\nThanks for playing!")
        break

    rounds += 1

    if guess.lower() == mob["name"].lower():
        print("Correct! 🎉")
        score += 1
    else:
        print("Incorrect.")
        print(f"\nHint 1: Icon: {mob['icon']}")
        guess2 = input("Guess again: ").strip()
        if guess2.lower() == "quit":
            print("\nThanks for playing!")
            break
        if guess2.lower() == mob["name"].lower():
            print("Correct! 🎉")
            score += 1
            continue

        print(f"\nHint 2: {mob['hint']}")
        guess3 = input("Last try: ").strip()
        if guess3.lower() == "quit":
            print("\nThanks for playing!")
            break
        if guess3.lower() == mob["name"].lower():
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Sorry! The correct answer was: '{mob['name']}'.")

    print(f"Score: {score}/{rounds}")

    if score == len(mobs):
        print("\nCongratulations! You guessed every mob correctly — you beat the game! 🏆")
        break

if score < len(mobs):
    print(f"\nFinal Score: {score}/{rounds} rounds played.")
    print("Goodbye!")
