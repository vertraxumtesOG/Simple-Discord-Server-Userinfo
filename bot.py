#DONT REMOVE CREDITS
#Importet Stuff 
import discord
from discord.ext import commands, tasks
import pytz
from datetime import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='%', intents=intents)
#Consolelog
@bot.event
async def on_ready():
    print(f'Bot is Online as {bot.user.name}! coded by vetraxumtes')
#Serverinfo
@bot.command(name='serverinfo')
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=f"**»** Informations about **{ctx.guild.name}**",
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name=":shield: » Name", value=f"{ctx.guild.name}", inline=True)
  embed.add_field(name=":earth_africa: » ID ", value=f"{ctx.guild.id}") 
  embed.add_field(name=":man_office_worker: » Owner", value=owner, inline=True)
  embed.add_field(name=":bust_in_silhouette: » Member", value=memberCount, inline=True)
  embed.add_field(name=":art: » Erstellt am ", value=ctx.guild.created_at.__format__('%d.%m.%Y '), inline=True)
  embed.add_field(name=":performing_arts: » Roles", value=f"{len(ctx.guild.roles)}")
  embed.add_field(name=":loud_sound: » Channels", value=f"{len(ctx.guild.channels)}")
  embed.add_field(name=":file_folder: » Categories", value=f"{len(ctx.guild.categories)}")
  embed.add_field(name=":rocket: » Boosts", value=f"{ctx.guild.premium_subscription_count}")
  embed.set_footer(text=f'Chip × Serverinfo', icon_url="https://cdn.discordapp.com/avatars/910534177848438846/f020c3d542931050c32e6143699e5253.webp?size=1024")

  await ctx.send(embed=embed)
#Userinfo
@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member = None):
    if member == None:
      member = ctx.author
    de = pytz.timezone('Europe/Berlin')
    embed = discord.Embed(title=f'**»** Informations about {member.display_name}',
                          description='', color=discord.Colour.blue())

    embed.add_field(name='👥 » Name', value=f'{member.name}#{member.discriminator}', inline=True)
    embed.add_field(name= '🤖 » Bot', value=f'{("Yes" if member.bot else "No")}', inline=True)
    embed.add_field(name='👨‍🎨 » Nickname', value=f'{(member.nick if member.nick else "Not set")}', inline=True)
    embed.add_field(name='🌎 » Server joined', value=f'{member.joined_at.strftime("%d.%m.%Y")}', inline=True)
    embed.add_field(name='🚀 » Discord joined', value=f'{member.created_at.strftime("%d.%m.%Y")}', inline=True)
    embed.add_field(name='🎭 » Roles', value=f'{len(member.roles)}', inline=True)
    embed.add_field(name='🎭 » Highstes Role', value=f'{member.top_role.name}', inline=True)
    embed.add_field(name='🎨 » Role Color', value=f'{member.color}', inline=True)
    embed.add_field(name='💎 » Booster', value=f'{("Yes" if member.premium_since else "No")}', inline=True)
    embed.set_footer(text=f'Chip × Userinfo', icon_url="https://cdn.discordapp.com/avatars/910534177848438846/f020c3d542931050c32e6143699e5253.webp?size=1024")
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)  
  


#Login
bot.run("TOKEN")

#by vertraxumtes
#DONT REMOVE CREDITS