#!/usr/bin/env python3

import discord
from discord.ext import commands

with open("tokenfile","r") as tokenfile:
	token = tokenfile.read()

client = commands.Bot(command_prefix="c!")
client.remove_command("help")

def cringeify(text,length):
	if len(text) > length:
		rtext = f"{text[:length - 3]}..."
	else:
		rtext = text
	return f"{rtext} is cringe"

@client.event
async def on_ready():
	print(f"logged in as {client.user}")
	game = discord.Game("with cringe nae nae babys")
	await client.change_presence(status=discord.Status.online, activity=game)
	print(f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=65536&scope=bot")
	for guild in client.guilds:
		print(f"In guild: {guild.name}") 

@client.command()
async def iscringe(ctx,*text):
	if text != ():
		ctext = " ".join(text)
	else:
		async for message in ctx.channel.history(limit=2):
			if message == ctx.message:
				continue
			ctext = message.content
	await ctx.send(f"{cringeify(ctext,1970)}")

@client.command()
async def saidcringe(ctx,*text):
	if text != ():
		ctext = " ".join(text)
	else:
		async for message in ctx.channel.history(limit=2):
			if message == ctx.message:
				continue
			ctext = message.content
	ctext = f"\"{ctext}\""
	await ctx.send(f"saying {cringeify(ctext,1978)}")

@client.command()
async def help(ctx):
	await ctx.send("use c!iscringe to mark something as cringe")

@client.command()
async def naenae(ctx):
	await ctx.send("https://i.redd.it/arvlnfkgv8921.jpg")

client.run(token)

