#!/usr/bin/env python3

import discord
from discord.ext import commands

with open("tokenfile","r") as tokenfile:
	token = tokenfile.read()

client = commands.Bot(command_prefix="c!")
client.remove_command("help")

def cringeify(text,length,plurality):
	if len(text) > length:
		rtext = f"{text[:length - 3]}..."
	else:
		rtext = text
	isword = "is" if not plurality else "are"
	return f"{rtext} {isword} cringe"

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
	await ctx.send(f"{cringeify(ctext,1970,False)}")

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
	await ctx.send(f"saying {cringeify(ctext,1978,False)}")

@client.command()
async def arecringe(ctx,*text):
	if text != ():
		ctext = " ".join(text)
	else:
		async for message in ctx.channel.history(limit=2):
			if message == ctx.message:
				continue
			ctext = message.content
	await ctx.send(f"{cringeify(ctext,1971,True)}")

@client.command()
async def help(ctx):
	await ctx.send("theres:\n1. c!saidcringe for saying that saying something is cringe\n2. c!iscringe for saying something is cringe\n3. c!arecringe for saying somethings are cringe")

@client.command()
async def naenae(ctx):
	await ctx.send("https://i.redd.it/arvlnfkgv8921.jpg")

client.run(token)

