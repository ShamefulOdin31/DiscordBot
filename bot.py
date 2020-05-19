TOKEN = 'NjgzMzU2MDYwMzkxODMzNjEw.XlqW_g.sUxENy0XYQ8x8WuBUTR9zDNkSFQ'

import discord
import random

any = ["Iron Silence: Iron sights and suppressors only",
            "The blind man challenge: Turn brightness all the way down and run m870 recruits.",
            "Stock gun: No attachments allowed",
            "1 stand: Crouch, stand or prone only during the match.",
            "Lost in translation: Speak with your Operators accent",
            "AOL Messenger: No mics! You have to write in chat when you and where you spot and enemy and when you kill, plant, etc",
            "Freestyle: Whenever you die, you have to freestyle rap about how you died and say callouts by rapping.",
            "Day at the Range: Everyone get a shotgun and yell 'PULL!!!' whenever you fire at an enemy.",
            "Super detailed Callouts: Whenever you see an enemy don't say his name, but you must tell your teammates their height, estimated age, what they're wearing, which skin they have and shoe size etc.",
            "Crablike: Only use A and D to move. (disable W and S in the menu... or pull them out). Console use only left and right.",
            "Samurai: Knife Only.",
            "Time Out: Win (an entire match) through reaching the time limit. (At least 1 enemy must survive every round).",
            "Push it to the limit: Turn your mouse (or controller) DPI up to the limit.",
            "Low and Slow: Can only move if prone. (you also cannot vault over objects. You may crouch/stand to deploy gadgets only)",
            "Hospital: No killing, only injure and down the enemy team.",
            "Learn from the best: Imitate the top person (voice or actions).",
            "Captains Orders: Follow the lead of your captain. If he dies, the person who says 'I am captain now' fastest becomes the captain.",
            "Simon says: One person is Simon, the others have to follow and be killed uppon failure.",
            "Horse Rules: If a teammate goes down, kill them.",
            "I like this point of view: Lean left or right the entire round. (Console: Only when moving but you have to ADS)",
            "Ammo Conservation: All guns must be put to semi-auto",
            "The Imitation Game: All players must impersonate various famous celebrities during the round",
            "cl_righthand 0: Switch hands for your mouse and keyboard.",
            "Gladiator: Only one person may leave spawn. When that person dies, the next person leaves.",
            "Backwards headset: 180 your headset.",
            "Behind you!: You can only use the S key to move around.",
            "You always have to kill enemies with a drop shot."]

attack = ["Bunny Hop: During attack the attackers may only move their drone by jumping from start till end.",
            "Rush B: During attack the attackers may only use op's who are meant for rush such as: Blitz, Ash, IQ, Finka, Fuze, Lion.",
            "FBI OPEN UP!: While attacking you have a team of ash and thermite surrounded by recruits with shields only.",
            "Eyes or rush: You or your teammate has to be in the room with a drone otherwise you cannot use your gun until the last minute mark.",
            "Follow the leader: Everyone picks their operator, but everyone (except the player on the top of the team) changes their brightness all the way down and the leader directs everyone.",
            "Defend Wal-e: Twitch goes in with her drone and all attackers must make sure the drone stays alive.",
            "I’m the Capitão now: One player picks Capitão. He has to decide what loadout and/or character the others get. During the game, they will have to follow Capitão's orders.",
            "Mr. President: Choose one person to be the president and the other teammate need to protect the president and refer to him as the president. The person chosen as the president is only allowed to use pistols. Your mission ends when you complete the objective and the Mr. President survives. You all fail when he doesn't make it.",
            "Teenage mutant ninja turtles: Everyone uses recruit shield and can only crawl the whole game.",
            "The Phalanx: All choose riot shields, and you must stay in a line. DO NOT BREAK FORMATION!",
            "Easy going: No Sprinting, no ADS and no Prone",
            "Soviet Tactics: Only use 1 gun at a time. Everyone else follows the shooter. Once the shooter dies the next person may start using his weapon.",
            "Polite entry: Only enter through doors.",
            "Wide Open: Everyone takes breach charges, place them all around the objective room and breach at the same time.",
            "Don't harm Rapunzel: No rappeling",
            "Trigger Baggy: All attackers go recruit with spetnaz LMGS and must walk to the objective whilst shooting and tea bagging. You are ONLY allowed to stop tea bagging when you see an enemy, and your goal is to secure the area or complete the objective.",
            "Rambo Rush: All attackers go recruit and pick LMG and rush the objective and hip fire everywhere to kill everything.",
            "AFK Fake: All defenders don't move during prep phase, but as soon as the match starts kill drones and wait for enemy team to barge in.",
            "Penguins: All players must remain in one group and crouched at all times.",
            "Stormtroopers: Hipfire only; No shotguns.",
            "The Fapper Sapper: Must put a sock on your mouse hand before the round starts.",
            "WW2 Vets: 1911 Pistols only - Shields on back.",
            "007: Pistols only.",
            "Eagle Eye: Recruits using revolvers and shields.",
            "The long way: No breaching charges.",
            "Hero Mode: Only one person can enter the objective room at a time",
            "Follow the Leader: All players must use the same doorways / entry point",
            "Take a day off: All players must stay in spawn until the last 30 seconds",
            "No Ark for Noah: Objective must be spammed with flash bangs smoke and shields in one wave.",
            "Dakka Dakka Dakka!: Spetnatz recruit LMG only",
            "Team America - FBI: Must use only FBI operators and enter through the main entrance",
            "Window Washers: Must enter and exit any buildings through windows",
            "Bastille: Sharpshooter w/DMR w/ 4 shields",
            "Heavy Feet: Players are not allowed to move while shooting",
            "Tr8tor: Lowest scoring teammate must report teammate locations / strategies in all chat",
            "Canadian Warfare: Every kill must be marked with an 'I'm sorry' in all-chat",
            "Professional Help: MVP must die at the beginning of the round and direct their teammates through the round",
            "Karaoke: Bottom board decides on an inspirational song, team must sing along",
            "Blind Eye: No use of drones",
            "Pump Action: Attackers are only allowed to use Pump action shotguns. Any other type of weapon is not allowed! Breachable walls/doors or windows can only be shot open. Breaching them is not allowed.",
            "First Droned first surved: Every attacker has to drone the objective and stay within the objective room until. The first 2 drones that get destroyed or disrupted will get downed at the beginning of the round and revived.",
            "Kettle and Pummel: 4 Recruits with shields and 1 Sledge. The attacking team is only allowed to kill enemies by penning them up and letting sledge kill them with the hammer. Attackers have to ignore the objective. You are not allowed to return fire with fire arms! The round has to end by Sledge killing the last person with the Hammer!",
            "Headshots only: Attackers are only allowed to use Heavy Assault Rifles (G8A1 and 6P41) and can only kill enemies with 1 shot headshots. Only 2 frag grenades for the whole team! Wall breaching is not allowed! Armor panels can be opened with frag grenades. Wooden barricades have to be shot open!",
            "Tortoise: All pick recruits with riot shields. Prone only.",
            "Butt Stuff: When entering a room, you must enter backwards.",
            "The John Wayne: All pick a GIGN recruit with ballistic shield, revolver, breach charges and frag grenade. As soon as you spawn, press 1 to get your shield in your back and wield your revolver like a true hero.",
            "The most powerful guns in the world: All pick GIGN recruits with 417, revolver, breach charges and frag grenades. Deal out the damage.",
            "The blind shield wall: All pick American recruits with a shield, the 5.7, smoke grenades and stun grenades. Open a window (or door) and throw all the nades. Breach.",
            "LMG Aplenty: All pick Spetznaz recruits with LMG and go full auto on the breachable walls, floors, and doors.",
            "Death from above: All place breach charges on the ceiling of the objective room if it's breachable (like in Chalet) and detonate the five charges at once. Then, shoot from the room above.",
            "Auto-shotgun OP: All take an FBI recruit with the automatic shotgun and rush like hell.",
            "Eins Zwei Polizei: All GSG9, choose M870, G8A1 or shield. Rush in, no stopping.",
            "Maximum destruction: All destructive operators (Sledge, Buck, Ash, Thermite, one with breach charges). You can't use doors or Windows so you have to make your way in a line through all the walls to reach the objective.",
            "1 shot: Everyone picks an attacker with a revolver and 360 no scope the defending team with a revolver and they can only smoke the objective."]


defense = ["Defend the lord: While defending 1 must go as the lord tachanka him self and the other 4 are supposed to defend him at all cost.",
            "Showtime!: Have as many cameras as possible. Select Echo, Valkyrie, and Maestro along with two ops with bulletproof cameras. Have every angle covered.",
            "Operation Turtleshell: Pick Castle, Mute, Bandit, Jäger and Rook. Lock down and remain in the room.",
            "Pokemon Trainers: Your entire team is operators with impact grenades. You can use guns and gadgets, but the final blow on any kill must be made with the impact grenades. Next round you use the operators you killed. If you didn't captured anyone however, you become the Magikarp recruit. No weapon allowed, you have to get up and down around the enemy in attempt to inflict him some damage.",
            "Berlin Wall: Pick Spetsnaz with deployable shields and make a wall.",
            "Bring the Trash Outside: Map: House 1 defender as Jäger rushes outside to the dumpster at the start of the round via the main entrance. Jump in via a small pole on the right side. Once inside place all ADS's. Good luck, you're home!",
            "Small(er) caliber: Secondary/Pistol only (No Caviera)",
            "Drone Hunt: No one can reinforce until all drones are destroyed.",
            "Trump's Wall: Select operators (American class preferred) with deployable shields. Lay the shields down in a row to create a wall. NO ONE IS ALLOWED TO PASS!",
            "Wolfpack: Roam as a group",
            "Death from above: Can only shoot at people when you are above them (knifing is allowed when on the same level).",
            "Turtles: Everyone must equip a shield and once inside the building, go prone and shuffle around with their shield in their back.",
            "Shooting stand: Take all shotguns and shoot out all the walls on the objective and use pistols only",
            "False start: Don't start early! Only start preparing your defence once the preparation time is over.",
            "Chanka Fort: Team of 1 Chanka and 4 ops with deployable shields. Create a fort for Chanka and aid him.",
            "Stay out!: Choose up to 3 rooms which can't be entered during the match. If someone enters, kill him.",
            "Fake Out: Put all your defenses in a different objective room not the real room and have four people defend the empty room trying to trick the enemy team",
            "AFK Fake: Must remain motionless through drone phase.",
            "Stormtroopers: Hipfire only - No shotguns.",
            "The Iron Ruse: Fortify the wrong room.",
            "Spawn Camping: Cannot leave the objective room under any circumstance.",
            "Eyes Wide Shut: Destroy all cameras. No exceptions.",
            "Bring the fight to them: All defensive operators must leave the building once the match begins, and can only return if the objective is in immediate danger",
            "Toxic Room: Operators may not remain in the objective room unless taken",
            "Turret Terror: Only the turret and knives may be used",
            "Doctor's Orders: Whoever picks Doc commands the rest of the squad - All recruits",
            "Men of Iron: Only fully armored characters are allowed",
            "The Berlin Wall: Only barbed wire and shields",
            "With Open Arms: All barricades in a room that you are in must be ripped open",
            "You Must Construct Additional Pylons: No reinforced walls / ceilings",
            "Kill Confirmed: Every kill must be marked by the ENTIRE TEAM in all-chat",
            "Man Down: Every team death must be marked the ENTIRE TEAM in all-chat",
            "Deafened: Last surviving teammate must use only teammates making noise as audio",
            "Barebones: No gadgets allowed whatsoever - NO BARBED WIRE / C4 or ANYTHING",
            "CoD Attitude: Must teabag 3 times on any enemy kill before firing again",
            "To Be Worthy: Must get a kill before picking up armor",
            "No Retreat: No backing up during the round",
            "Karaoke: Bottom board decides song, team must sing along - MUST BE INSPIRATIONAL - up to team discretion",
            "P.E.: Players must always sprint when in motion",
            "Big Borders: You can't place barricades on the objective room walls, only the surrounding ones",
            "Blind Eye: No use of cameras",
            "Iron Curtain: Everyone has to take the GSG9 recruit and put barbwire in places the player wants them to be. You are only allowed to kill enemies that are stuck in the Barbwire.",
            "Good Deeds (Rook): At the beginning of the prep phase or action phase Rook has to put down his armor for the enemy to pick up.",
            "Good Deeds (Doc): If an enemy is in DBNO state Doc has to revive him and is not allowed to shoot him. He is only allowed to run away.",
            "No Shots: Only smoke is allowed to kill the enemy with his smoke bombs or bandit to electrocute them with barbwire and CED-1. Teammates can however, put down barbwire in order to help Bandit.",
            "Roman Formation Inside: Defenders have to take deployable shields, arrange them in a circle and all 5 have to stay in the objective room hidden behind the shields. No special gadgets are allowed! It is only allowed to change the position of your shield formation twice in the match.",
            "Roman Formation Outside: Defenders have to take deployable shields, run outside after the prep phase, arrange them in a circle and all 5 have to stay hidden behind the shields. Special Gadgets are allowed!",
            "Just Frames: Everyone pick FBI shotguns, and shoot out every wall, window and trapdoor.",
            "Auto-shotgun OP: All take Spetsnaz recruits with an automatic shotgun and open all the windows, trap doors and doors you can find during the preparation phase.",
            "Barbs, barbs everywhere: All pick GSG9 recruits with the carbine, barb wire and nitro cells. As Germans, you get 3 barb wires each. Cover the entire floor with it.",
            "The best defense is the attack: All pick SAS recruits with FMG, SMG and nitro. Stay as far away as possible from the objective room. As soon as the attackers plant the diffuser / get in the secure area or pick up the hostage, rush them.",
            "The .45 is king: All pick FBI recruits with an UMP45, an M45, nitros and go to war.",
            "It's a trap!: All take FBI recruits with the autoshotgun. Put C4 in each corner of the objective room, hide on the floor (but not in the objective room), as soon as they start securing or grab the hostage, detonate the C4 and rush them.",
            "I'm here, come get me!: All take GIGN recruits with the P90 and the pistol. Place barb wire all over the objective room. As soon as the attackers spawn, you must at least fire one shot every 3 seconds (count to 3, fire, count to 3, fire)."]

def rolls(type):
    return random.randint(1, type)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    messageAuthor = str(message.author)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$attack'):
        await message.channel.send("`A strat for attack: \n" + attack[random.randint(1, len(attack)-1)] + "`")

    if message.content.startswith('$any'):
        for x in range(1):
            await message.channel.send("`A strat for both: \n" + any[random.randint(1, len(any)-1)] + "`")

    if message.content.startswith('$defense'):
        for x in range(1):
            await message.channel.send("`A strat for defense: \n" + defense[random.randint(1, len(defense)-1)] + "`")

    if message.content.startswith('$help'):
        await message.channel.send("```Available commands for siege: \n$attack \n$defense \n$any```")

    if message.content == '$dnd':
        await message.channel.send("```Availible commands for DND: \n$d2 \n$d4 \n$d6 \n$d8 \n$d10 \n$d12 \n$d20 \n$d100```")

    if message.content.find('-') == -1:
        if message.content == '$d2':
            await message.channel.send("```Roll for: " + messageAuthor + "\nYour d2 roll is: " + str(rolls(2)) + "```")

        if  message.content == '$d4':
            await message.channel.send("```Roll for: " + messageAuthor + "\nYour d4 roll is: " + str(rolls(4)) + "```")

        if  message.content == '$d6':
            await message.channel.send("```Roll for: " + messageAuthor + "\nYour d6 roll is: " + str(rolls(6)) + "```")

        if  message.content == '$d8':
            await message.channel.send("```Roll for: " + messageAuthor + "\nYour d8 roll is: " + str(rolls(8)) + "```")

        if  message.content == '$d10':
            await message.channel.send("```Roll for: " + messageAuthor + "\nYour d10 roll is: " + str(rolls(10)) + "```")

        if  message.content == '$d12':
            await message.channel.send("```Roll for: " + messageAuthor + "\nYour d12 roll is: " + str(rolls(12)) + "```")

        if  message.content == '$d20':
            await message.channel.send("```Roll for: " + messageAuthor + "\nYour d20 roll is: " + str(rolls(20)) + "```")
        
        if  message.content == '$d100':
            await message.channel.send("```Roll for: " + messageAuthor + "\nYour d100 roll is: " + str(rolls(100)) + "```")

    else:
        content = str(message.content)
        output = "```Roll for: " + messageAuthor
        total = 0

        if content.startswith("$d2-") and content != "$d20":
            x = message.content.find('-') + 1
            amount = content[x:]
            for y in range(int(amount)):
                currentRoll = rolls(2)
                total += currentRoll
                output += "\nRoll #" + str(y + 1) + " Amount: "+ str(currentRoll)
            output += "\nTotal of all rolls: " + str(total) + "```"
            await message.channel.send(output)

        if content.startswith("$d4-"):
            x = message.content.find('-') + 1
            amount = content[x:]
            for y in range(int(amount)):
                currentRoll = rolls(4)
                total += currentRoll
                output += "\nRoll #" + str(y + 1) + " Amount: "+ str(currentRoll)
            output += "\nTotal of all rolls: " + str(total) + "```"
            await message.channel.send(output)

        if content.startswith("$d6-"):
            x = message.content.find('-') + 1
            amount = content[x:]
            for y in range(int(amount)):
                currentRoll = rolls(6)
                total += currentRoll
                output += "\nRoll #" + str(y + 1) + " Amount: "+ str(currentRoll)
            output += "\nTotal of all rolls: " + str(total) + "```"
            await message.channel.send(output)

        if content.startswith("$d8-"):
            x = message.content.find('-') + 1
            amount = content[x:]
            for y in range(int(amount)):
                currentRoll = rrolls(8)
                total += currentRoll
                output += "\nRoll #" + str(y + 1) + " Amount: "+ str(currentRoll)
            output += "\nTotal of all rolls: " + str(total) + "```"
            await message.channel.send(output)

        if content.startswith("$d10-"):
            x = message.content.find('-') + 1
            amount = content[x:]
            for y in range(int(amount)):
                currentRoll = rolls(10)
                total += currentRoll
                output += "\nRoll #" + str(y + 1) + " Amount: "+ str(currentRoll)
            output += "\nTotal of all rolls: " + str(total) + "```"
            await message.channel.send(output)

        if content.startswith("$d12-"):
            x = message.content.find('-') + 1
            amount = content[x:]
            for y in range(int(amount)):
                currentRoll = rolls(12)
                total += currentRoll
                output += "\nRoll #" + str(y + 1) + " Amount: "+ str(currentRoll)
            output += "\nTotal of all rolls: " + str(total) + "```"
            await message.channel.send(output)

        if content.startswith("$d20-"):
            x = message.content.find('-') + 1
            amount = content[x:]
            for y in range(int(amount)):
                currentRoll = rolls(20)
                total += currentRoll
                output += "\nRoll #" + str(y + 1) + " Amount: "+ str(currentRoll)
            output += "\nTotal of all rolls: " + str(total) + "```"
            await message.channel.send(output)

        if content.startswith("$d100-"):
            x = message.content.find('-') + 1
            amount = content[x:]
            for y in range(int(amount)):
                currentRoll = rolls(100)
                total += currentRoll
                output += "\nRoll #" + str(y + 1) + " Amount: "+ str(currentRoll)
            output += "\nTotal of all rolls: " + str(total) + "```"
            await message.channel.send(output)
    
    
        
client.run(TOKEN)