import requests
from bs4 import BeautifulSoup
import time
import telepot
from telepot.loop import MessageLoop


def get_dividend_earning_rate(code):
    try:
        url = "http://finance.naver.com/item/main.nhn?code=" + code
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html5lib")
        tag = soup.select("#_dvr")
        return tag[0].text
    except:
        return 0


token = "398259524:AAHMXMTVrXDfNd-E9tAsA1eRp-u4LopefLI"
bot = telepot.Bot(token)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    code = msg['text']
    dvr = get_dividend_earning_rate(code)
    text = "배당 수익률은 {} 입니다.".format(dvr)
    bot.sendMessage(chat_id, text)


MessageLoop(bot, handle).run_as_thread()
while True:
    time.sleep(10)