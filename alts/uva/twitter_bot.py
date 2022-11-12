# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from uva import MarkovBot

# Create class instance
win = winner()
tweetbot = MarkovBot()
day = datetime.today().day

# Run script
if day in [1, 6, 11, 16, 21, 26]:
  print("Uva is on vacation.")
  tweetbot.read('Freud_Dream_Psychology.txt')
  my_first_text = tweetbot.generate_text(25, seedword=[u'dream', u'psychoanalysis'])
  api.update_status('"'+my_first_text+'"')
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
