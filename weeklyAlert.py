import discord
from discord.ext import tasks
from datetime import datetime 
import asyncio

def strRead(_path):
    _strInTxt = ""
    with open(_path, "r", encoding = "UTF-8") as f:
        _strInTxt = f.read()
    f.close()
    return _strInTxt

# 接続に必要なオブジェクトを生成
intents = discord.Intents.default()
client = discord.Client(intents = intents)

# 起動時の処理
@client.event
async def on_ready():
    print('ログインしました')
    timeCheck.start()

# アクセストークン
TOKEN = strRead("/home/raspi/ダウンロード/BotToken.txt")

# チャンネルID
channel_id = int(strRead("/home/raspi/ダウンロード/ChannelID.txt"))

# メッセージを送る
async def SendMessage():
    channel = client.get_channel(channel_id)
    _message = strRead("/home/raspi/ダウンロード/Message.txt")
    await channel.send(_message)

# ループ
@tasks.loop(seconds=30)
async def timeCheck():
    # 現在の時刻
    now = datetime.now()
    if now.weekday() == 0 and now.hour == 12 and now.minute == 30:
        await SendMessage()
        #該当時間だった場合は２重に投稿しないよう待機
        await asyncio.sleep(60)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

