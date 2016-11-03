import urllib.request
import json
import time
import tweet_it
on = True
name = "your name"
old_uts = 0
while on:
    json_data = urllib.request.urlopen("http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=LASTFM-USERNAME-TO-FOLLOW&limit=1&api_key=LASTFM-API-KEY&format=json").read()
    obj = json.loads(json_data.decode())
    new_uts = (obj['recenttracks']['track'][1]['date'])
    if new_uts != old_uts:
        tweet_contents = name + " is currently listening to " + obj['recenttracks']['track'][0]['name'] + " by " + obj['recenttracks']['track'][0]['artist']['#text']
        tweet_it.tweet_song(tweet_contents)
    else:
        print("same song is playing ", obj['recenttracks']['track'][1]['date'])
    old_uts = new_uts
    time.sleep(300)



