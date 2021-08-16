import time
import telepot
from telepot.loop import MessageLoop

token = "398259524:AAHMXMTVrXDfNd-E9tAsA1eRp-u4LopefLI"
bot = telepot.Bot(token)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg['text']
    bot.sendMessage(chat_id, text)

MessageLoop(bot, handle).run_as_thread()
while True:
    time.sleep(10)
