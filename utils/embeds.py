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

from datetime import datetime
import random
from typing import (
    Any,
    List,
    Optional,
    Tuple,
    Union
)


from discord import Colour, Embed, EmbedField, Colour


def make_embed(*,
    title: str,
    colour: Union[Colour, int] = Colour.random(),
    description: Optional[str] = Embed.Empty,
    image_url: Optional[str] = Embed.Empty,
    thumb_url: Optional[str] = Embed.Empty,
    footer_text: Optional[str] = None,
    footer_icon: Optional[str] = Embed.Empty,
    author_name: Optional[str] = None,
    author_url: Optional[str] = Embed.Empty,
    author_icon: Optional[str] = Embed.Empty,
    timestamp: bool = True,
    fields: Optional[List[Union[Tuple[str, Any, bool], EmbedField]]] = None
    ) -> Embed:
    """Creates and returns a Discord embed with the provided parameters.
    Args:
        title: Embed title.
        colour: Colour or raw 16-bit int representing embed accent color.
        description: Embed body text.
        image_url: URL for main image, if desired, (Bottom-Center)
        thumb_url: URL for thumbnail image, if desired. (Upper-Right)
        footer_text: Text for the embed footer.
        footer_icon: URL for icon within embed footer.
        author_name: Text to use for embed author field. (At Top)
        author_url: URL to use for the author field.
        author_icon: URL to use for the author field icon.
        timestamp: Boolean indicating whether to add the current time to the embed.
        fields: List of tuples or EmbedFields, each denoting a field to
            be added to the embed. If entry is a tuple, values are as follows:
            0 -> Name | 1 -> Value | 2 -> Inline (bool)
    Returns:
        The finished embed object.
    """

    embed = Embed(
        colour = colour,
        title = title,
        description = description
    )

    embed.set_thumbnail(url=thumb_url)
    embed.set_image(url=image_url)

    if footer_text is not None:
        embed.set_footer(text=footer_text, icon_url=footer_icon)

    if author_name is not None:
        embed.set_author(name=author_name, url=author_url, icon_url=author_icon)

    if timestamp:
        embed.timestamp = datetime.now()

    if fields is not None:
        for i in fields:
            if isinstance(i, tuple):
                embed.add_field(name=i[0], value=str(i[1]), inline=i[2])
            else:
                embed.fields.append(i)

    return embed
    