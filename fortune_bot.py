import tweepy
import fortune
import os
from auth import api_xame, api_uva, api_mevu, api, api_zark, api_lufi, api_woba


bots = [api_xame, api_uva, api_mevu, api, api_zark, api_lufi, api_woba]
coun = 0

def une(api):
	fortune = os.popen("fortune alts/fortunes").read()
	while len(fortune) < 280:
		api.update_status(fortune)
		coun += 1
		
for bot in bots:
	une(bot)
	coun+=1
	print(f"{coun} fortuna postada")
