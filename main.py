# -*- coding: utf-8 -*-
#    Copyright 2022 Parad1se

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import discord
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	owner_ids = data["owner_ids"]

# Intents
intents = discord.Intents.all()
# The bot
bot = discord.Bot(intents = intents, owner_ids = owner_ids)


@bot.slash_command(guild_ids=[765869842451398667])
async def load(ctx, name):
    if ctx.author.id not in owner_ids:
        return
    bot.load_extension(f'cogs.{name}')
    await ctx.respond(f'Loaded {name}')

@bot.slash_command(guild_ids=[765869842451398667])
async def unloaded(ctx, name):
    if ctx.author.id not in owner_ids:
        return
    bot.unload_extension(f'cogs.{name}')
    await ctx.respond(f'Unloaded {name}')
    
@bot.slash_command(guild_ids=[765869842451398667])
async def reload(ctx, name):
	if ctx.author.id not in owner_ids:
		return
	bot.unload_extension(f'cogs.{name}')
	bot.load_extension(f'cogs.{name}')
	await ctx.respond(f'Reloaded {name}')


# Load cogs
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}', store=False)


@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	print(f"Discord Version: {discord.__version__}")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "Watching over servers!"))

# Run the bot
bot.run(os.getenv("TOKEN"))