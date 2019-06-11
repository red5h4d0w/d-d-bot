import random
import discord
from discord.ext import commands
import sqlite3

bot_prefix = "d."
bot = commands.Bot(command_prefix=bot_prefix)

def id_already_exists(id):
	print(type(id))
	c.execute("SELECT * FROM discord WHERE ID=? ;", (id,))
	if c.fetchone() == None:
		return False
	return True

def read_token():
	'''Reads the token located in a text file'''
	with open("token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()

def char_create():
	X = []
	for _ in range(6):
		c = []
		for _ in range(4):
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
    await ctx.send(" Les commandes sont : \n\t\t\t\t\t\t\t\t\t\td.commandes\n\t\t\t\t\t\t\t\t\t\td.d20 : lance un dé 20 ")

@bot.command(pass_context=True)
async def roule(ctx, dés: str):
	"""Roule des dés en format dnd"""
	try:
		lancers, faces = map(int, dés.split('d'))
	except Exception:
		await ctx.send("Écrit sous la forme NdN stp")
		return
	résultats = []
	for _ in range(0, lancers):
		résultats.append(random.randint(1,faces))
	await ctx.send("tu as roulé : " + str(sum(résultats)))
	
@bot.event
async def on_message(message):
	id = message.author.id
	name = message.author.name
	if not id_already_exists(id):
		c.execute("INSERT INTO discord VALUES(:ID, :XP, :NAME )", {"ID": id, "XP": 0, "NAME": name})
	c.execute("UPDATE discord SET XP = XP + 1 WHERE ID=?", id)
	conn.commit()
	await bot.process_commands(message)
	
@bot.command(pass_context=True)
async def perso(ctx):
	X=char_create()
	await ctx.send(str(X[0])+"\n"+str(X[1])+"\n"+str(X[2])+"\n"+str(X[3])+"\n"+str(X[4])+"\n"+str(X[5]))	
if __name__ == "__main__":
	conn = sqlite3.connect("discord.db")
	c = conn.cursor()
	bot.run(read_token())