import time, random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import discord
from discord.ext import commands


#  Создание бота
token = "ВАШ ТОКЕН"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

#  Создание хром-драйвера
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

sad_phrases = ['Посмотрите на что способны люди', "Вот что бывает из-за плохого отношения к природе",
               "Экология - это важно", "Сортируйте отходы, это важно", "Вот почему нужно беречь природу",
               "Дважды подумайте, прежде чем выкинуть мусор в неположенном месте"]


@bot.command(name='show')
async def show_categories(ctx, number):

    if not number.isdigit():
        await ctx.send('После show вы должны вписать число!')
    else:
        driver.get("https://www.istockphoto.com/ru/search/2/image?phrase=загрязнение+окружающей+среды")
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, features="html.parser")

        pictures_divs_list = soup.find_all('div', class_='ABVClgVJTdOPXmIa63fN')
        pictures_list = []

        for picture_div in pictures_divs_list:
            picture_a = picture_div.find('a', class_='Up7tj_EQVFh6e6sV17Ud')
            picture_href = picture_a.find('img', class_='yGh0CfFS4AMLWjEE9W7v').get('src')

            pictures_list.append(picture_href)

        await ctx.send(random.choice(sad_phrases))

        for i in range(int(number)):
            await ctx.send(random.choice(pictures_list))


bot.run(token)
