import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands

bot_prefix = "d."
bot = commands.Bot(command_prefix=bot_prefix)

def char_create():
	X = []
	for i in range(6):
		c = []
		for t in range(4):
			c.append(random.randint(1,6))
		c.remove(min(c))
		X.append(c[0]+c[1]+c[2])
	return X
@bot.event
async def on_ready():
    print("Bot en ligne")
    print("Nom: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))

@bot.command(pass_context=True)
async def commandes(ctx):
    await bot.say(" Les commandes sont : \n\t\t\t\t\t\t\t\t\t\td.commandes\n\t\t\t\t\t\t\t\t\t\td.d20 : lance un dé 20 ")

@bot.command(pass_context=True)
async def d20(ctx):
    await bot.say("tu as roulé : " + str(random.randint(1,20)))
	
@bot.command(pass_context=True)
async def perso(ctx):
	X=char_create()
	await bot.say(str(X[0])+"\n"+str(X[1])+"\n"+str(X[2])+"\n"+str(X[3])+"\n"+str(X[4])+"\n"+str(X[5]))	

bot.run("NDU0NjI5MzQ1Mjk4NzQzMjk2.DfzrCQ.QW_EJt_bjBWQfywSzkMmcOGuk3A")