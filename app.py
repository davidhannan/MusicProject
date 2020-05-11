import requests

API_KEY = "58c0e3631080b2ca7566ca24c47baf09"
URL = "http://ws.audioscrobbler.com/2.0/"

artist = "Tame Impala"
trackName = "Alter Ego"

resp = requests.get(URL + "?method=track.getsimilar&artist="+artist+"&track="+trackName+"&api_key="+API_KEY+"&format=json")

if resp.status_code == 200:
    data = resp.json()
    nameData = data['similartracks']['track']
    for track in nameData:
        print('{} by {}'.format(track['name'], track['artist']['name']))
