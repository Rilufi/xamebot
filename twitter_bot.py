# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from twitter_unfollow import unfollow

# Create class instance
win = winner()
unfollow = unfollow()

day = datetime.today().day

# Run script
if day in [4, 8, 13, 19, 25]:
  print("Rilufix is auditioning to be cast in Asterix and Obelix next movie.")
#  unfollow.unfollow()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
