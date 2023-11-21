import discord
import asyncio
import json
import random
import os
import time
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View, Select
import time
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} Is Online!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} Command('s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="menu", description="Shows Your Village")
async def menu(interaction : discord.Interaction):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    name = user.display_name
    pfp = user.display_avatar

    firehabitat = users[str(user.id)]["fire habitat"]
    seahabitat = users[str(user.id)]["sea habitat"]
    windhabitat = users[str(user.id)]["wind habitat"]
    poisonhabitat = users[str(user.id)]["poison habitat"]
    fireshard = users[str(user.id)]["fireshard"]
    seashard = users[str(user.id)]["seashard"]
    windshard = users[str(user.id)]["windshard"]
    poisonshard = users[str(user.id)]["poisonshard"]
    barracks = users[str(user.id)]["barracks"]
    breedingmountain = users[str(user.id)]["breeding mountain"]
    hatchery = users[str(user.id)]["hatchery"]
    bigfarm = users[str(user.id)]["big farm"]
    foodfarm = users[str(user.id)]["food farm"]
    greenhouse = users[str(user.id)]["greenhouse"]
    rank = users[str(user.id)]["rank"]
    wins = users[str(user.id)]["wins"]
    losses = users[str(user.id)]["losses"]
    winstreak = users[str(user.id)]["winstreak"]
    losstreak = users[str(user.id)]["losstreak"]

    em = discord.Embed(title=f" **{name} Menu**")
    em.set_thumbnail(url=f"{pfp}")
    if rank == 0:
        rankk = "❔"
        namee = "Unranked"
    elif rank == 1:
        rankk = "<:silver:1172309123958841365>"
        namee = "Silver 1"
    elif rank == 2:
        rankk = "<:silver:1172309123958841365>"
        namee = "Silver 2"
    elif rank == 3:
        rankk = "<:silver:1172309123958841365>"
        namee = "Silver 3"
    elif rank == 4:
        rankk = "<:silver:1172309123958841365>"
        namee = "Silver ELite"

    elif rank == 5:
        rankk = "<:gold:1172309131361792044>"
        namee = "Gold 1"
    elif rank == 6:
        rankk = "<:gold:1172309131361792044>"
        namee = "Gold 2"
    elif rank == 7:
        rankk = "<:gold:1172309131361792044>"
        namee = "Gold 3"
    elif rank == 8:
        rankk = "<:gold:1172309131361792044>"
        namee = "Gold Master"

    elif rank == 9:
        rankk = "<:emerald:1172309208637640755>"
        namee = "Emerald 1"
    elif rank == 10:
        rankk = "<:emerald:1172309208637640755>"
        namee = "Emerald Elite"
    elif rank == 11:
        rankk = "<:ruby:1172309180871360532>"
        namee = "Ruby Star"
    elif rank == 12:
        rankk = "<:ruby:1172309180871360532>"
        namee = "Ruby Champion"

    elif rank == 13:
        rankk = "<:diamond:1171942980756701226>"
        namee = "Diamond 1"
    elif rank == 14:
        rankk = "<:diamond:1171942980756701226>"
        namee = "Diamond 2"
    elif rank == 15:
        rankk = "<:diamond:1172309139670696017>"
        namee = "Diamond Supreme"

    em.add_field(name=f"**~~ Rank:**", value=f"> **{rankk} | {namee}**", inline=False)
    if firehabitat != 0:
        a1 = "<:fire:1171945582420570283>"
    else:
        a1 = ""
    if seahabitat != 0:
        a2 = "<:SEA:1174076658609823744>"
    else:
        a2 = ""
    if windhabitat != 0:
        a3 = "<:wind:1174076663500394588>"
    else:
        a3 = ""
    if poisonhabitat != 0:
        a4 = "<:poison:1174076652939128843>"
    else:
        a4 = ""
    if firehabitat == 0:
        if seahabitat == 0:
            if windhabitat == 0:
                if poisonhabitat == 0:
                    a = "<:no:1094219530714230846>"
    em.add_field(name=f"**~~ Island:**", value=f"> **<:nest:1173404399939366952> | Habitats: {a}{a1}{a2}{a3}{a4}**\n"
                                             f"> **<:swords:1173404980531691590> | Barracks: Lvl **\n"
                                             f"> **<:goldmine:1173405239420932178> | Mine: Lvl **", inline=True)
    em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
    em.set_footer(text="Use Buttons For Extra Information")
    await interaction.response.send_message(embed=em)



@bot.tree.command(name="village", description="Shows Your Village!")
async def village(interaction : discord.Interaction):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    name = user.display_name
    pfp = user.display_avatar

    rank = users[str(user.id)]["rank"]
    foodmarket = users[str(user.id)]["foodmarket"]
    egghatcher = users[str(user.id)]["egghatcher"]
    goldmine = users[str(user.id)]["goldmine"]
    barracks = users[str(user.id)]["barracks"]
    petmarket = users[str(user.id)]["petmarket"]
    wins = users[str(user.id)]["wins"]
    losses = users[str(user.id)]["losses"]
    winstreak = users[str(user.id)]["winstreak"]

    em = discord.Embed(title=f" **{name} Village:**")
    em.set_thumbnail(url=f"{pfp}")
    if rank == 0:
        rank4 = "❔"
        name2 = "Unranked"
    elif rank == 1:
        rank2 = "<:silver:1172309123958841365>"
        name2 = "Silver 1"
    elif rank == 2:
        rank4 = "<:silver:1172309123958841365>"
        name2 = "Silver 2"
    elif rank == 3:
        rank4 = "<:silver:1172309123958841365>"
        name2 = "Silver 3"
    elif rank == 4:
        rank4 = "<:silver:1172309123958841365>"
        name2 = "Silver ELite"

    elif rank == 5:
        rank4 = "<:gold:1172309131361792044>"
        name2 = "Gold 1"
    elif rank == 6:
        rank4 = "<:gold:1172309131361792044>"
        name2 = "Gold 2"
    elif rank == 7:
        rank4 = "<:gold:1172309131361792044>"
        name2 = "Gold 3"
    elif rank == 8:
        rank4 = "<:gold:1172309131361792044>"
        name2 = "Gold Master"

    elif rank == 9:
        rank4 = "<:emerald:1172309208637640755>"
        name2 = "Emerald 1"
    elif rank == 10:
        rank4 = "<:emerald:1172309208637640755>"
        name2 = "Emerald Elite"
    elif rank == 11:
        rank4 = "<:ruby:1172309180871360532>"
        name2 = "Ruby Star"
    elif rank == 12:
        rank4 = "<:ruby:1172309180871360532>"
        name2 = "Ruby Champion"

    elif rank == 13:
        rank4 = "<:diamond:1171942980756701226>"
        name2 = "Diamond 1"
    elif rank == 14:
        rank4 = "<:diamond:1171942980756701226>"
        name2 = "Diamond 2"
    elif rank == 15:
        rank4 = "<:diamond:1172309139670696017>"
        name2 = "Diamond Supreme"

    em.add_field(name=f"**~~ Rank:**", value=f"> **{rank4} | {name2}**", inline=False)
    em.add_field(name=f"**~~ Village:**", value=f"> **<:nest:1173404399939366952> | Hatcher: Lvl {egghatcher}**\n"
                                             f"> **<:swords:1173404980531691590> | Barracks: Lvl {barracks}**\n"
                                             f"> **<:goldmine:1173405239420932178> | Mine: Lvl {goldmine}**", inline=True)
    em.add_field(name=f"**~~ Markets:**", value=f"> **<:market:1173408503336013836> | Food: Lvl {foodmarket}**\n"
                                                f"> **<:finale:1173409358189711410> | Pets: Lvl {petmarket}**", inline=True)
    em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
    em.set_footer(text="Use Buttons For Extra Information")
    select = Select(placeholder="Choose What You Want To Discover!" ,options=[
        discord.SelectOption(label="Your Statistics", emoji="<:trophy:1172308359186223104>", description="Shows Your Statistics Of Pet Wars And Your Rank"),
        discord.SelectOption(label="Your Village", emoji="<:townhall:1173394719699652710>", description="Shows And Explains Your Village In Depth!"),
        discord.SelectOption(label="Your Market", emoji="<:finale:1173409358189711410>", description="Shows And Explains Your Market In Depth!")
    ])
    async def callback1(interaction):
        if select.values[0] == "Your Statistics":
            em2 = discord.Embed(title=f" **Your Statistics:**")
            em2.set_thumbnail(url=f"{pfp}")
            if rank == 0:
                rank2 = "❔"
                name2 = "Unranked"
            elif rank == 1:
                rank2 = "<:silver:1172309123958841365>"
                name2 = "Silver 1"
            elif rank == 2:
                rank2 = "<:silver:1172309123958841365>"
                name2 = "Silver 2"
            elif rank == 3:
                rank2 = "<:silver:1172309123958841365>"
                name2 = "Silver 3"
            elif rank == 4:
                rank2 = "<:silver:1172309123958841365>"
                name2 = "Silver ELite"

            elif rank == 5:
                rank2 = "<:gold:1172309131361792044>"
                name2 = "Gold 1"
            elif rank == 6:
                rank2 = "<:gold:1172309131361792044>"
                name2 = "Gold 2"
            elif rank == 7:
                rank2 = "<:gold:1172309131361792044>"
                name2 = "Gold 3"
            elif rank == 8:
                rank2 = "<:gold:1172309131361792044>"
                name2 = "Gold Master"

            elif rank == 9:
                rank2 = "<:emerald:1172309208637640755>"
                name2 = "Emerald 1"
            elif rank == 10:
                rank2 = "<:emerald:1172309208637640755>"
                name2 = "Emerald Elite"
            elif rank == 11:
                rank2 = "<:ruby:1172309180871360532>"
                name2 = "Ruby Star"
            elif rank == 12:
                rank2 = "<:ruby:1172309180871360532>"
                name2 = "Ruby Champion"

            elif rank == 13:
                rank2 = "<:diamond:1171942980756701226>"
                name2 = "Diamond 1"
            elif rank == 14:
                rank2 = "<:diamond:1171942980756701226>"
                name2 = "Diamond 2"
            elif rank == 15:
                rank2 = "<:diamond:1172309139670696017>"
                name2 = "Diamond Supreme"
            em2.add_field(name=f"**~~ Your Rank:**", value=f"> **{rank2} | {name2}**",inline=True)
            em2.add_field(name=f"**~~ Your Stats:**", value=f"> **<:yes:1094219485453500426> | Wins: {wins}**\n"
                                                            f"> **<:no:1094219530714230846> | Losses: {losses}**\n"
                                                            f"> **<:trophy:1172308359186223104> | Winstreak: {winstreak}**", inline=True)
            em2.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
            await interaction.response.edit_message(embed=em2)
        elif select.values[0] == "Your Village":
            em2 = discord.Embed(title=f" **Your Village:**")
            em2.set_thumbnail(url=f"{pfp}")
            if egghatcher == 1:
                lvlup1 = "Lvl 2 = Rank 2 Eggs!"
            elif egghatcher == 2:
                lvlup1 = "Lvl 3 = Rank 3 Eggs!"
            elif egghatcher == 3:
                lvlup1 = "Lvl 4 = Rank 4 Eggs!"
            em2.add_field(name=f"**~~ Hatcher:**", value=f"> **<:nest:1173404399939366952> | Lvl {egghatcher}**\n"
                                                         f"> **{lvlup1}**",inline=True)
            if goldmine == 1:
                lvlup2 = "Lvl 2 = 720 Gold/ Day!"
            elif goldmine == 2:
                lvlup2 = "Lvl 3 = 1080 Gold/Day!"
            elif goldmine == 3:
                lvlup2 = "Lvl 4 = 2160 Gold/Day!"
            em2.add_field(name=f"**~~ Mine:**", value=f"> **<:goldmine:1173405239420932178> | Lvl {goldmine}**\n"
                                                      f"> **{lvlup2}**", inline=True)
            if barracks == 1:
                lvlup3 = "Lvl 2 = Allows 2 Dragons In War!"
            elif barracks == 2:
                lvlup3 = "Lvl 3 = Allows 3 Dragons In War!"
            em2.add_field(name=f"**~~ Barracks:**", value=f"> **<:swords:1173404980531691590>| Lvl {barracks}**\n"
                                                          f"> **{lvlup3}**", inline=False)
            em2.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
            await interaction.response.edit_message(embed=em2)

    select.callback = callback1
    view = View()
    view.add_item(select)
    await interaction.response.send_message(embed=em, view=view)




@bot.tree.command(name="balance", description="Shows Your Overall Stats!")
async def balance(interaction: discord.Interaction):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    coins = users[str(user.id)]["coins"]
    diamonds = users[str(user.id)]["diamonds"]
    diamondproduce = users[str(user.id)]["diamondproduce"]
    level = users[str(user.id)]["level"]
    progress = users[str(user.id)]["progress"]
    rebirth = users[str(user.id)]["rebirth"]

    member = interaction.user
    name = member.display_name
    pfp = member.display_avatar
    em = discord.Embed(title=" **My Balance:**")
    em.set_thumbnail(url=f"{pfp}")
    em.add_field(name="💵 | Wallet", value=f"> <:coin:1171943088529358970> **| Coins:** {coins}\n"
                                          f"> <:diamond:1171942980756701226> **| Diamonds:** {diamonds}")
    if premium != 0:
        a1 = "<:yes:1094219485453500426>"
    else:
        a1 = "<:no:1094219530714230846>"
    em.add_field(name="<:target:1171946146931933314> | Others", value=f"> <:crown:1171943237657821247> **| Rebirths:**{rebirth}\n"
                                          f"> <:diamondproduce:1171943469661569074> **| Production:** {diamondproduce}", inline=True)
    if progress == 0:
        b1 = "<:lr:1166486907178459177><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:rr:1166487001638371459>"
    elif progress == 1:
        b1 = "<:lg:1166487046077030581><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:rr:1166487001638371459>"
    elif progress == 2:
        b1 = "<:lg:1166487046077030581><:mg:1166487077270081656><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:rr:1166487001638371459>"
    elif progress == 3:
        b1 = "<:lg:1166487046077030581><:mg:1166487077270081656><:mg:1166487077270081656><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:rr:1166487001638371459>"
    elif progress == 4:
        b1 = "<:lg:1166487046077030581><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:rr:1166487001638371459>"
    elif progress == 5:
        b1 = "<:lg:1166487046077030581><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:rr:1166487001638371459>"
    elif progress == 6:
        b1 = "<:lg:1166487046077030581><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mr:1166486964325851186><:mr:1166486964325851186><:mr:1166486964325851186><:rr:1166487001638371459>"
    elif progress == 7:
        b1 = "<:lg:1166487046077030581><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mr:1166486964325851186><:mr:1166486964325851186><:rr:1166487001638371459>"
    elif progress == 8:
        b1 = "<:lg:1166487046077030581><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mr:1166486964325851186><:rr:1166487001638371459>"
    elif progress == 9:
        b1 = "<:lg:1166487046077030581><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:rr:1166487001638371459>"
    else:
        b1 = "<:lg:1166487046077030581><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:mg:1166487077270081656><:rg:1166487102138089472>"
    em.add_field(name=" <:fire:1171945582420570283> | Level ", value=f"> <:heart:1171944876041064469> **| Level:**  {level}\n"
                                           f"> <:stars:1171945319467069490> **| Progress:** \n"
                                           f"*---* {b1} *---*", inline=False)
    em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
    em.set_footer(text="More Information About These: ( /rebirth ) ( /free )")
    await interaction.response.send_message(embed=em)
@bot.tree.command(name="rebirth", description="All About Rebirths ( Info / To Do A Rebirth ) !")
async def rebirth(interaction: discord.Interaction):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    coins = users[str(user.id)]["coins"]
    diamonds = users[str(user.id)]["diamonds"]
    premium = users[str(user.id)]["premium"]
    level = users[str(user.id)]["level"]
    progress = users[str(user.id)]["progress"]
    rebirth = users[str(user.id)]["rebirth"]
    nextrebirth = users[str(user.id)]["nextrebirth"]
    diamondproduce = users[str(user.id)]["diamondproduce"]
    member = interaction.user
    name = member.display_name
    pfp = member.display_avatar
    em = discord.Embed(title="**Rebirth's:**", color=discord.Color.random())
    em.set_thumbnail(url=f"{pfp}")
    em.add_field(name="🧾 | Information:", value=f"> 💰 **| Cost: {nextrebirth} Coins**\n"
                                                f"> 🖊️ **| Increases Level Up Potential**")
    em.add_field(name="🔮 | Rebirth:", value=f"> 🔁 **| Rebirths:** {rebirth}\n"
                                            f"> 🧿 **| Increases Diamond Production**", inline=False)
    em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
    em.set_footer(text="Check More Statistics ( /balance )")

    button1 = Button(label="Confirm Rebirth", style=discord.ButtonStyle.green)
    button2 = Button(label="Cancel Rebirth", style=discord.ButtonStyle.red)

    async def button_callback1(interaction):
        if interaction.user != user:
            return False
        else:
            coins2 = users[str(user.id)]["coins"]
            diamonds2 = users[str(user.id)]["diamonds"]
            premium2 = users[str(user.id)]["premium"]
            level2 = users[str(user.id)]["level"]
            progress2 = users[str(user.id)]["progress"]
            rebirth2 = users[str(user.id)]["rebirth"]
            nextrebirth2 = users[str(user.id)]["nextrebirth"]
            diamondproduce2 = users[str(user.id)]["diamondproduce"]
            if coins2 >= nextrebirth2:
                e = discord.Embed(title="**Rebirth Successful:**", color=discord.Color.green())
                users[str(user.id)]["coins"] -= nextrebirth2
                users[str(user.id)]["diamondproduce"] += 1
                users[str(user.id)]["rebirth"] += 1
                users[str(user.id)]["nextrebirth"] += nextrebirth2
                e.add_field(name="🪙 | Coins Information", value=f"> 🪙 | Coins Spent: {nextrebirth2}\n"
                                                                f"> 🪙 | Coins Left: {coins - nextrebirth2}")
                e.add_field(name="🔁 | Rebirth Information", value=f"> 🔁 | Rebirths: {rebirth2 + 1}", inline=True)
                e.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
                e.set_footer(text="Check More Statistics ( /balance )")
                await interaction.response.edit_message(embed=e, view=None)
                with open("bank.json", "w") as f:
                    json.dump(users, f)
            elif coins2 < nextrebirth2:
                hi = discord.Embed(title="**Rebirth Failed:**", color=discord.Color.red())
                hi.add_field(name="🪙 | Coin Information", value=f"> 🪙 | Coins Needed: {nextrebirth2}\n"
                                                                f"> 🪙 | Coins: {coins2}")
                hi.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
                hi.set_footer(text="Check More Statistics ( /balance )")
                await interaction.response.edit_message(embed=hi, view=None)
    async def button_callback2(interaction):
        if interaction.user != user:
            return False
        else:
            await interaction.response.edit_message(view=None)

    button1.callback = button_callback1
    button2.callback = button_callback2
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    await interaction.response.send_message(embed=em, view=view)
@bot.tree.command(name="premium", description="All About The Premium Upgrade !")
async def premium(interaction: discord.Interaction):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    coins = users[str(user.id)]["coins"]
    diamonds = users[str(user.id)]["diamonds"]
    premium = users[str(user.id)]["premium"]
    level = users[str(user.id)]["level"]
    progress = users[str(user.id)]["progress"]
    rebirth = users[str(user.id)]["rebirth"]
    member = interaction.user
    name = member.display_name
    pfp = member.display_avatar
    em = discord.Embed(title="**Premium Upgrade:**", color = discord.Color.random())
    em.set_thumbnail(url=f"{pfp}")
    em.add_field(name="🧾 | Information:", value=f"> 💎 **| Cost: 1000 Diamonds**\n"
                                                f"> 🖊️ **| Give You Access To /weekly**")
    if premium != 0:
        a1 = "✅"
    else:
        a1 = "❌"
    em.add_field(name="🔮 | Premium:", value=f"> 🔁 **| Premium:** {a1}", inline=False)
    em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
    em.set_footer(text="Check More Statistics ( /balance )")
    button1 = Button(label="Confirm Premium", style=discord.ButtonStyle.green)
    button2 = Button(label="Cancel Premium", style=discord.ButtonStyle.red)
    async def button_callback1(interaction):
        if interaction.user != user:
            return False
        else:
            if premium == 0:
                if diamonds >= 1000:
                    e = discord.Embed(title="**Premium Successful:**", color=discord.Color.green())
                    users[str(user.id)]["premium"] += 1
                    users[str(user.id)]["diamonds"] -= 1000
                    e.add_field(name="💎 | Diamonds Information", value=f"> 💎 **| Diamonds Spent:** 1000\n"
                                                                    f"> 💎 **| Diamonds Left:** {diamonds-1000}")
                    e.add_field(name="🔁 | Premium Information", value=f"> 👑 **| Premium:** ✅", inline=True)
                    e.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
                    e.set_footer(text="Check More Statistics ( /balance )")
                    await interaction.response.edit_message(embed=e, view=None)
                    with open("bank.json", "w") as f:
                        json.dump(users, f)
                elif diamonds < 1000:
                    hi = discord.Embed(title="**Premium Failed:**", color=discord.Color.red())
                    hi.add_field(name="💎 | Diamond Information", value=f"> 💎 **| Diamonds Needed:** 1000\n"
                                                                       f"> 💎 **| Diamonds:** {diamonds}")
                    hi.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
                    hi.set_footer(text="Check More Statistics ( /balance )")
                    await interaction.response.edit_message(embed=hi, view=None)
            else:
                member = interaction.user
                name = member.display_name
                pfp = member.display_avatar
                i = discord.Embed(title="**Premium Already Owned:**", color=discord.Color.red())
                i.add_field(name="💎 | Premium", value=f"> 💎 **| Premium:** ✅\n"
                                                      f"> 💎 **| Diamonds:** {diamonds}")
                i.set_thumbnail(url=f"{pfp}")
                i.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
                i.set_footer(text="Check More Statistics ( /balance )")
                await interaction.response.edit_message(embed=i, view=None)

    async def button_callback2(interaction):
        if interaction.user != user:
            return False
        else:
            await interaction.response.edit_message(view=None)
    button1.callback = button_callback1
    button2.callback = button_callback2
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    await interaction.response.send_message(embed=em, view=view)
@bot.tree.command(name="slots", description="Slots - Type Of Gambling Method!")
@app_commands.describe(betamount = "How Much Coins Do You Want To Bet?")
async def slots(interaction: discord.Interaction, betamount: int):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    coins = users[str(user.id)]["coins"]
    diamonds = users[str(user.id)]["diamonds"]
    level = users[str(user.id)]["level"]
    progress100 = users[str(user.id)]["100progress"]
    progress = users[str(user.id)]["progress"]
    rebirth = users[str(user.id)]["rebirth"]
    nextrebirth = users[str(user.id)]["nextrebirth"]
    diamondproduce = users[str(user.id)]["diamondproduce"]
    progresscount = users[str(user.id)]["progresscount"]
    member = interaction.user
    name = member.display_name
    pfp = member.display_avatar
    a = 0
    if betamount <= 0:
        em = discord.Embed(title="** Slots: **", color=discord.Color.random())
        em.set_thumbnail(url=f"{pfp}")
        em.add_field(name="🎰 | Slots Failure", value=f"> 🪙 **| Minimum 1 Coin**")
        em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
        em.set_footer(text="Slots Is A Gambling Gamemode")
        a = 1
        await interaction.response.send_message(embed=em)
    b = 0
    if a == 0:
        if betamount > coins:
            em = discord.Embed(title="** Slots: **", color=discord.Color.red())
            em.set_thumbnail(url=f"{pfp}")
            em.add_field(name="🎰 | Slots Failure", value=f"> 🪙 **| Bet:** {betamount}\n" 
                                                         f"> 🪙 **| Coins:** {coins}")
            em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
            em.set_footer(text="Slots Is A Gambling Gamemode")
            b = 1
            await interaction.response.send_message(embed=em)
        if b == 0:
            em = discord.Embed(title="** Slots: **", color=discord.Color.red())
            em.set_thumbnail(url=f"{pfp}")
            em.add_field(name="🎰 | Slots", value=f"> 🪙 **| Bet:** {betamount}\n"
                                                 f"> 💎 **| Do You Wish To Continue?**")
            em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
            em.set_footer(text="Slots Is A Gambling Gamemode")

            button1 = Button(label="Confirm Game", style=discord.ButtonStyle.green)
            button2 = Button(label="Cancel Game", style=discord.ButtonStyle.red)

            async def button_callback1(interaction):
                if interaction.user != user:
                    return False
                else:
                    list = ["<:7slot:1166770943344001074>","<:starslot:1166770965892567153>","<:lemonslot:1166770979809271818>","<:cherryslot:1166770994921340948>"]
                    r1 = random.randint(0,3)
                    r2 = random.randint(0,3)
                    r3 = random.randint(0,3)
                    pick1 = list[r1]
                    pick2 = list[r2]
                    pick3 = list[r3]
                    e = discord.Embed(title="**Slot Game Result:**", color=discord.Color.green())
                    if pick1 == pick2 == pick3:
                        if pick1 == list[0]:
                            users[str(user.id)]["coins"] += (betamount*14)
                            e.add_field(name="🎰 | Slot Game", value=f"> 🪙 **| Slot:** {pick1} {pick2} {pick3}\n"
                                                                    f"> 🪙 **| Coins Earnt:** {betamount*14}\n"
                                                                    f"> 🪙 **| New Coin Amount:** {coins-(betamount*14)}")
                        else:
                            users[str(user.id)]["coins"] += (betamount*8)
                            e.add_field(name="🎰 | Slot Game", value=f"> 🪙 **| Slot:** {pick1} {pick2} {pick3}\n"
                                                                    f"> 🪙 **| Coins Earnt:** {betamount*8}\n"
                                                                    f"> 🪙 **| New Coin Amount:** {coins+(betamount*8)}")
                    else:
                        users[str(user.id)]["coins"] -= betamount
                        e.add_field(name="🎰 | Slot Game", value=f"> 🪙 **| Slot:** {pick1} {pick2} {pick3}\n"
                                                                f"> 🪙 **| Coins Lost:** {betamount}\n"
                                                                f"> 🪙 **| New Coin Amount:** {coins - betamount}")
                    users[str(user.id)]["100progress"] += betamount
                    yes = progress100 + betamount
                    if yes >= progresscount:
                        users[str(user.id)]["progress"] += 1
                        users[str(user.id)]["100progress"] = 0
                        if progress == 10:
                            users[str(user.id)]["progress"] = 0
                            users[str(user.id)]["level"] += 1
                            users[str(user.id)]["progresscount"] += 15

                    e.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
                    e.set_footer(text="Slots Is A Gambling Gamemode")
                    await interaction.response.edit_message(embed=e, view=None)
                    with open("bank.json", "w") as f:
                        json.dump(users, f)
            async def button_callback2(interaction):
                if interaction.user != user:
                    return False
                else:
                    await interaction.response.edit_message(view=None)

            button1.callback = button_callback1
            button2.callback = button_callback2
            view = View()
            view.add_item(button1)
            view.add_item(button2)
            await interaction.response.send_message(embed=em, view=view)

    with open("bank.json", "w") as f:
        json.dump(users, f)
@bot.tree.command(name="blackjack", description="Blackjack - Gambling Method")
@app_commands.describe(betamount = "How Much Coins Do You Want To Bet?")
async def slots(interaction: discord.Interaction, betamount: int):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    coins = users[str(user.id)]["coins"]
    diamonds = users[str(user.id)]["diamonds"]
    level = users[str(user.id)]["level"]
    progress100 = users[str(user.id)]["100progress"]
    progress = users[str(user.id)]["progress"]
    rebirth = users[str(user.id)]["rebirth"]
    nextrebirth = users[str(user.id)]["nextrebirth"]
    diamondproduce = users[str(user.id)]["diamondproduce"]
    progresscount = users[str(user.id)]["progresscount"]
    member = interaction.user
    name = member.display_name
    pfp = member.display_avatar
    a = 0
    if betamount <= 0:
        em = discord.Embed(title="** Blackjack: **", color=discord.Color.red())
        em.set_thumbnail(url=f"{pfp}")
        em.add_field(name="🃏 | Blackjack Failure", value=f"> 🪙 **| Minimum 1 Coin**")
        em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
        em.set_footer(text="Blackjack Is A Gambling Gamemode")
        a = 1
        await interaction.response.send_message(embed=em)
    b = 0
    if a == 0:
        if betamount > coins:
            em = discord.Embed(title="** Blackjack: **", color=discord.Color.red())
            em.set_thumbnail(url=f"{pfp}")
            em.add_field(name="🃏 | Blackjack Failure", value=f"> 🪙 **| Bet:** {betamount}\n" 
                                                         f"> 🪙 **| Coins:** {coins}")
            em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
            em.set_footer(text="Blackjack Is A Gambling Gamemode")
            b = 1
            await interaction.response.send_message(embed=em)
        if b == 0:
            em = discord.Embed(title="** Slots: **", color=discord.Color.red())
            em.set_thumbnail(url=f"{pfp}")
            em.add_field(name="🎰 | Slots", value=f"> 🪙 **| Bet:** {betamount}\n"
                                                 f"> 💎 **| Do You Wish To Continue?**")
            em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
            em.set_footer(text="Slots Is A Gambling Gamemode")

            button1 = Button(label="Confirm Game", style=discord.ButtonStyle.green)
            button2 = Button(label="Cancel Game", style=discord.ButtonStyle.red)

            async def button_callback1(interaction):
                if interaction.user != user:
                    return False
                else:
                    list = ["<:7slot:1166770943344001074>","<:starslot:1166770965892567153>","<:lemonslot:1166770979809271818>","<:cherryslot:1166770994921340948>"]
                    r1 = random.randint(0,3)
                    r2 = random.randint(0,3)
                    r3 = random.randint(0,3)
                    pick1 = list[r1]
                    pick2 = list[r2]
                    pick3 = list[r3]
                    e = discord.Embed(title="**Slot Game Result:**", color=discord.Color.green())
                    if pick1 == pick2 == pick3:
                        if pick1 == list[0]:
                            users[str(user.id)]["coins"] += (betamount*14)
                            e.add_field(name="🎰 | Slot Game", value=f"> 🪙 **| Slot:** {pick1} {pick2} {pick3}\n"
                                                                    f"> 🪙 **| Coins Earnt:** {betamount*14}\n"
                                                                    f"> 🪙 **| New Coin Amount:** {coins-(betamount*14)}")
                        else:
                            users[str(user.id)]["coins"] += (betamount*8)
                            e.add_field(name="🎰 | Slot Game", value=f"> 🪙 **| Slot:** {pick1} {pick2} {pick3}\n"
                                                                    f"> 🪙 **| Coins Earnt:** {betamount*8}\n"
                                                                    f"> 🪙 **| New Coin Amount:** {coins+(betamount*8)}")
                    else:
                        users[str(user.id)]["coins"] -= betamount
                        e.add_field(name="🎰 | Slot Game", value=f"> 🪙 **| Slot:** {pick1} {pick2} {pick3}\n"
                                                                f"> 🪙 **| Coins Lost:** {betamount}\n"
                                                                f"> 🪙 **| New Coin Amount:** {coins - betamount}")
                    users[str(user.id)]["100progress"] += betamount
                    yes = progress100 + betamount
                    if yes >= progresscount:
                        users[str(user.id)]["progress"] += 1
                        users[str(user.id)]["100progress"] = 0
                        if progress == 10:
                            users[str(user.id)]["progress"] = 0
                            users[str(user.id)]["level"] += 1
                            users[str(user.id)]["progresscount"] += 15

                    e.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
                    e.set_footer(text="Slots Is A Gambling Gamemode")
                    await interaction.response.edit_message(embed=e, view=None)
                    with open("bank.json", "w") as f:
                        json.dump(users, f)
            async def button_callback2(interaction):
                if interaction.user != user:
                    return False
                else:
                    await interaction.response.edit_message(view=None)

            button1.callback = button_callback1
            button2.callback = button_callback2
            view = View()
            view.add_item(button1)
            view.add_item(button2)
            await interaction.response.send_message(embed=em, view=view)

    with open("bank.json", "w") as f:
        json.dump(users, f)
@bot.tree.command(name="free")
@app_commands.describe(pack = "What Pack Do You Want To Buy?")
@app_commands.choices(pack = [
    discord.app_commands.Choice(name="Sea Pack ( 19 Coins )", value=1),
    discord.app_commands.Choice(name="Eagle Pack ( 19 Coins )", value=2),
    discord.app_commands.Choice(name="Fury Pack ( 19 Coins )", value=3)
])
async def free(interaction: discord.Interaction, pack: discord.app_commands.Choice[int]):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    coin_amt = users[str(user.id)]["coins"]

    with open("bank.json", "w") as f:
        json.dump(users, f)

async def open_account(user):
  users = await get_bank_data()
  if str(user.id) in users:
      return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["rank"] = 1
    users[str(user.id)]["foodmarket"] = 1
    users[str(user.id)]["egghatcher"] = 1
    users[str(user.id)]["goldmine"] = 1
    users[str(user.id)]["barracks"] = 1
    users[str(user.id)]["petmarket"] = 1
    users[str(user.id)]["wins"] = 1
    users[str(user.id)]["losses"] = 1
    users[str(user.id)]["winstreak"] = 1
    users[str(user.id)]["fire habitat"] = 0
    users[str(user.id)]["sea habitat"] = 0
    users[str(user.id)]["wind habitat"] = 0
    users[str(user.id)]["poison habitat"] = 0
    users[str(user.id)][""] = 0
    users[str(user.id)]["fireshard"] = 0
    users[str(user.id)]["seashard"] = 0
    users[str(user.id)]["windshard"] = 0
    users[str(user.id)]["poisonshard"] = 0
    users[str(user.id)][""] = 0
    users[str(user.id)]["barracks"] = 1
    users[str(user.id)]["breeding mountain"] = 1
    users[str(user.id)]["hatchery"] = 1
    users[str(user.id)][""] = 0
    users[str(user.id)]["big farm"] = 0
    users[str(user.id)]["food farm"] = 1
    users[str(user.id)]["greenhouse"] = 0
    users[str(user.id)][""] = 0
    users[str(user.id)]["rank"] = 0
    users[str(user.id)][""] = 0
    users[str(user.id)]["wins"] = 0
    users[str(user.id)]["losses"] = 0
    users[str(user.id)]["winstreak"] = 0
    users[str(user.id)]["losstreak"] = 0
  with open("bank.json","w") as f:
    json.dump(users,f)
  return True

async def get_bank_data():
    with open("bank.json", "r") as f:
      users = json.load(f)
    return users

bot.run("MTE3MTkwMDU3NjMwNTUyNDc3Nw.G9CkHe.gnJG-X7QUhzg2qRKFOrgSIw7s8wYc5CQbw4Bog")