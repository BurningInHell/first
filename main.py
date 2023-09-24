import discord , random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот который хочет помочь вас научить оберегать природу')
@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока, пока!')
@bot.command()
async def helpsea(ctx):
    await ctx.send(f'https://unsdg.un.org/ru/latest/stories/tri-deystvennykh-sposoba-pomoch-sokhranit-nashi-okeany')
@bot.command()
async def helplitter(ctx):
    await ctx.send(f'https://ria.ru/20220829/utilizatsiya-1812880941.html')
@bot.command()
async def treas(ctx):
    await ctx.send(f'https://news.un.org/ru/story/2020/05/1378752')
@bot.event
async def on_ready():
    print(f'Бот запущен, помощь по боту $help')
@bot.command()
async def help1(ctx):
    await ctx.send(f'Команда $helpsea - помощь по сохранению океанов, $helplitter - помощь по утилизациии мусора, $treas - вред вырубки деревьев, $hello - приветсвие, $bye - прощание, $an_mem - мемы')
@bot.command()
async def an_mem(ctx):
    image_name = random.choice(os.listdir('mem_world'))
    with open(f'images_animals/{image_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("")
