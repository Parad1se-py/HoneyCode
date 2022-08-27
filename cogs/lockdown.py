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


class Lockdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} is ready!')

    @commands.slash_command(
        name='lock',
        description='Lock any channel.',
        usage='/lock [channel] [reason]'
    )
    @commands.has_permissions(
        manage_channels=True
    )
    async def lock(
        self,
        ctx: ApplicationContext,
        channel: Option(discord.channel, required=False) = None
    ):

        if not channel:
            channel = ctx.channel

        await ctx.respond(
            embed = make_embed(
                title = f"Locked {channel.name}",
                description=None,
                color = discord.Colour.yellow()
            )
        )

def setup(bot):
    bot.add_cog(Lockdown(bot))