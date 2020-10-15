TOKEN = 'NjgzMzU2MDYwMzkxODMzNjEw.XlqW7A._m2uZ2pdnVPEVcuicgD1Id-krp8'

import discord
import random
import json
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import data

def rolls(type):
    return str(random.randint(1, int(type)))

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.command()
async def attack(ctx):
    await ctx.send("`A strat for attack: \n" + data.attacks[random.randint(1, len(data.attacks)-1)] + "`")

@bot.command()
async def defense(ctx):
    await ctx.send("`A strat for defense: \n" + data.defenses[random.randint(1, len(data.defenses)-1)] + "`")

@bot.command()
async def any(ctx):
    await ctx.send("`A strat for both: \n" + data.anys[random.randint(1, len(data.anys)-1)] + "`")

@bot.command()
async def roll(ctx, args):
    if '-' not in str(args):
        if not args.isdigit():
            await ctx.send('The input must be a number! Ex. $roll 6-1, for a single d6.')
        else:
            await ctx.send("```Roll for: " + str(ctx.author) + ".\nYour d"+ str(args) + " is: " + rolls(args)  + "```")

    else:
        parts = str(args).split('-')
        if not parts[0].isdigit() or not parts[1].isdigit:
            await ctx.send('The input must be a number! Ex. $roll 6-1, for a single d6.')
        else:
            total = 0
            result = "```Roll for: {name}.\nDie: d{type}".format(name=str(ctx.author), type=str(parts[0]))
            for i in range(0, int(parts[1])):
                current_role = rolls(parts[0])
                result = result + "\nRoll #{count}: {result}".format(count=str(i+1), result=str(current_role))
                total = total + int(current_role)
            result = result + "\nTotal: {total}```".format(total=str(total))
            await ctx.send(result)

@bot.command()
async def help(ctx):
    await ctx.send("```Currently availible commands \
                     \n-For R6-\
                     \n$attack  \
                     \n$defense \
                     \n$any \
                     \n\
                     \n-For Dice-\
                     \n$roll <die:amount> ex $roll 6-1```")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Command "{cmd}" not found!'.format(cmd=str(ctx.message.content)))
        return
    raise error

bot.run(TOKEN)