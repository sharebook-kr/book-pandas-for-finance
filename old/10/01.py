import telepot

token = "398259524:AAHMXMTVrXDfNd-E9tAsA1eRp-u4LopefLI"
bot = telepot.Bot(token)

resp = bot.getMe()
print(resp)