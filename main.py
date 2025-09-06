import math
import random
import time
import ASCII

from colors import END, BOLD, clear, close
import colors as color

level = 0
basehp = 100
hp = 100
tempoaryhp = 0
xp = 0

#clear()
print(f"{color.BLACKBG}{color.WHITE}{ASCII.welcomebanner}{END}")
print("\n\n\nHello, brave adventurer! Welcome to the land of LampZenia! In this world you will embark on many quests throughout this world, leveling up as you go. Enjoy!")

time.sleep(5)
clear()

playername = input("What would you like your name to be?\n")

level = 0
basehp = 100
hp = 100
tempoaryhp = 0

option = input(f"Hello, {playername}! Have you played before?\n").lower()
if option == "yes": skip = True
else: skip = False
clear()
if not skip:
  print("TUTORIAL:")
  input("Lampzenia is a fantasy RPG based on some rules of magic set in the ERAGON and CHILDREN OF RAGANROCK sieries. (Click enter for next line)")
  clear()
  print("TUTORIAL:")
  input("You can go around, and you will encounter monsters wich you can try to deafeat in a D&D style combat system. As you defeat monters, you will gain treasure and more spells or weapons to fight more monsters as you level up with XP points. (Click enter for next line)")
  clear()
  print("TUTORIAL:")
  input("Press return to enter combat")
  clear()
  while not option == "attack":
    clear()
    print("TUTORIAL - COMBAT:")
    option =input("You have 100 hp, 0 thp and are level 0.\nWhat would you like to do (select attack)?\n\t- attack\n\t- doge\n\t- use an item\n").lower()
  clear()
  print("TUTORIAL - COMBAT:")
  input("Using your greatsword, you slash at the dragon, dealing a fatal blow! (Click enter to continue)")
  clear()
  level += 1
  for second in range(5):
    print(f"You leveled up! (Now level {level}!) (continue in {5-(second)})")
    clear()
    time.sleep(0.999999)
  input("You have finished the tutorial! (Enter to continue)")
  
def itemcheck_name(item_id):
  items = {
    "0001": "Test item",
    "0002": "Healing potion",
    "0003": "Greater healing potion",
    "0004": "Potion of instant harming",
    "0005": "Greater potion of instant harming",
    "0006": "Orb of empowerment",
    "0007": "Staff of ice power",
    "0008": "Staff of fire power",
    "0009": "Staff of poison power",
    "0010": "Staff of astral power",
    "0011": "Staff of destructive power",
    "0012": "Staff of void power",
    "0013": "Orb of power",
    "0014": "Orb of prison",
    "0015": "Orb of travel",
    "0016": "Orb of dimensional travel",
    "0017": "Level potion",
    "0018": "Greater level potion"
  };
  if item_id in items: return items[item_id]
  else: return "Invalid item"
def itemcheck_use(item_id):
  items = {
    "0001": "Test item",
    "0002": "Healing potion",
    "0003": "Greater healing potion",
    "0004": "Potion of instant harming",
    "0005": "Greater potion of instant harming",
    "0006": "Orb of empowerment",
    "0007": "Staff of ice power",
    "0008": "Staff of fire power",
    "0009": "Staff of poison power",
    "0010": "Staff of astral power",
    "0011": "Staff of destructive power",
    "0012": "Staff of void power",
    "0013": "Orb of power",
    "0014": "Orb of prison",
    "0015": "Orb of travel",
    "0016": "Orb of dimensional travel",
    "0017": "Level potion",
    "0018": "Greater level potion"
  };
  key = [k for k, v in items.items() if v == "Test item"][0];
  return key;
  
def encounter(c_name, c_hp, c_ac, disadvantage, player_name, player_ac, player_hp, player_level, player_thp, player_items, player_weapons, player_spells, player_blinded=False, player_noattack=False, player_shocked=False):
  def weaponcheck(ac, weapon):
    weapon_dmg = {"greatsword":80, "shortsword":10, "rapier":25, "scimitar":20, "dagger":10, "whip":5, "morningstar":15, "spear":30, "halberd":65, "greataxe":75};
    if random.randint(1, 20) >= ac: return weapon_dmg[weapon];
    return 0;
  while True:
    player_maxhp = player_hp
    player_turn = True
    player_options = ["Attack", "Heal", "Use an item", "Look for an advantage", "Look around", "Sleep", "Run away", "Cast a spell", "Hide"]
    player_options_check = [playeroptions.lower() for playeroptions in player_options]
    player_weapons_check = [playerweapons.lower() for playerweapons in player_weapons]
    if player_noattack: player_options.remove("Attack")
    if player_blinded:
      player_options.remove("Look for an advantage")
      player_options.remove("Look around")
    if player_shocked:
      player_options.remove("Look for an advantage")
      player_options.remove("Look around")
      player_options.remove("Sleep")
      player_options.remove("Run away")
      player_options.remove("Cast a spell")
      player_options.remove("Hide")
      player_turn = False
    print(f"{color.BOLD}{color.RED}Entering combat...")
    time.sleep(1.5)
    clear()
    openingmessage = random.randint(1, 3)
    if openingmessage == 1: print(f"{color.BOLD}{color.RED}You find a {c_name} lying on the floor!\n")
    elif openingmessage == 2: print(f"{color.BOLD}{color.RED}You spin around just in time to see a {c_name}!\n")
    elif openingmessage == 3: print(f"{color.BOLD}{color.RED}Suddenly, a {c_name} creeps up behind you!\n")
    close()
    while player_turn:
      print(f"What would you like to do? You have {color.BOLD}{color.RED}{player_hp} hp{END}, and {color.BOLD}{color.BLUE}{player_thp} shield hp{END}.")
      for item in player_options: print(f"— {item}")
      option = input("\n→ ").lower()
      clear()
      if option in player_options_check:
        if option == "attack":
          print("What would you like to attack with?")
          for item in player_weapons: print(f"— {item}")
          print("— Go back")
          option = input("\n→ ").lower()
          if option == "go back":
            print(f"{color.GREEN}Going back...")
            close()
          elif option in player_weapons_check:
            weaponcheck(c_ac, option)
          else: print("I am not sure what you mean!")
          # Continue attack script later
        elif option == "hide":
          yn_option = input(f"Would you like to try stealth (disadvantage: {disadvantage})?").lower()
          if option == "yes":
            if disadvantage:
              roll = random.randint(1, 20)
            else:
              roll1 = random.randint(1, 20)
              roll2 = random.randint(1, 20)
              max()
        elif option == "heal":
          if player_hp + round(player_hp/3) > player_maxhp: print("You are not damaged enough to heal!")
          else:
            print("Healing...")
            player_hp += player_hp/10*player_level
        elif option == "use an item":
          print("What item would you like to use?")
          for item in player_items: print(f"— {itemcheck_name(item)}")
          print("— Go back")
          option = input("\n→ ").lower()
          if option == "go back":
            print(f"{color.GREEN}Going back...")
            close()
          elif option in player_items:
            if option == "0001":
              print("Hello world!")
            elif option == "0002":
              if player_hp + round(player_hp/5) > player_maxhp: print("You are not damaged enough to heal!")
              else: print("Healing...")
            player_hp += round(player_hp/7)*player_level
          else: print("I am not sure what you mean!")
      else: print("I am not sure what you mean!")
      time.sleep(2)
      clear()
  
# while True:
encounter("big wad of plastic", 10, 15, False, "hi", 10, 100, 1, 0, ["0001"], ["greatsword"], ["0001", "3847"])
# encounter(str, int, bool, str, int, int, int, lst, lst, lst)
