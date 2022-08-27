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

import asyncio

import discord
from discord.ext import commands
from discord import ApplicationContext, Member, Option

from utils import *


class BasicModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} is ready!')

    @commands.slash_command(
        name='kick',
        description='Kick any user below your & HoneyCode\'s hierarchy.',
        usage='/kick <user> [reason]'
    )
    @discord.default_permissions(
        kick_members=True
    )
    @commands.guild_only()
    async def kick(self, ctx: ApplicationContext, user: Option(Member, required=True, description='Person you want to kick.'), reason: Option(str, required=False, description='Reason to kicking user.') = "No Reason Provided."):
        await ctx.guild.kick(user, reason=reason)
        await ctx.respond(
            embed=make_embed(
                title=f'Successfully kicked {user.name}!',
                description=f'{user.name}#{user.discriminator} was kicked by {ctx.author.name}\nReason : *{reason}*',
                color=discord.Colour.yellow()
            )
        )

    @commands.slash_command(
        name='ban',
        description='Ban any user below your & HoneyCode\'s hierarchy.',
        usage='/ban <user> [reason]'
    )
    @discord.default_permissions(
        ban_members=True
    )
    @commands.guild_only()
    async def ban(self, ctx: ApplicationContext, user: Option(Member, required=True, description='Person you want to ban.'), reason: Option(str, required=False, description='Reason to banning user.') = "No Reason Provided."):
        await ctx.guild.ban(user, reason=reason)
        await ctx.respond(
            embed=make_embed(
                title=f'Successfully banned {user.name}!',
                description=f'{user.name}#{user.discriminator} was banned by {ctx.author.name}\nReason : *{reason}*',
                color=discord.Colour.yellow()
            )
        )

    @commands.slash_command(
        name='purge',
        description='Purge messages from a channel.',
        usage='/purge <messages=5> [channel]'
    )
    @discord.default_permissions(
        delete_messages=True
    )
    @commands.guild_only()
    async def purge(self, ctx: ApplicationContext, limit: Option(int, required=False, description='Amount of messags to purge.') = 5, channel: Option(discord.TextChannel, required=False, description='Channel to purge.') = None):
        if not channel:
            channel = ctx.channel
        
        await channel.purge(limit=limit)
        msg = await ctx.respond(
            embed=make_embed(
                title=f'{limit} messages successfully purged.',
                description=None,
                color=discord.Colour.yellow()
            )
        )
        asyncio.sleep(5)
        await msg.delete()

def setup(bot):
    bot.add_cog(BasicModCog(bot))