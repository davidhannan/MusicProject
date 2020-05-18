import requests

API_KEY = "58c0e3631080b2ca7566ca24c47baf09"
URL = "http://ws.audioscrobbler.com/2.0/"



def getSimilarTracks(fArtist, fTrackName):
    resp = requests.get(URL + "?method=track.getsimilar&artist="+fArtist+"&track="+fTrackName+"&api_key="+API_KEY+"&format=json")

    if resp.status_code == 200:
        data = resp.json()
        nameData = data['similartracks']['track']
        return nameData


def getSimilarArtists(artist):
    print(artist)
    print(URL + "?method=artist.getsimilar&artist="+artist+"&api_key="+API_KEY+"&format=json")
    resp = requests.get(URL + "?method=artist.getsimilar&artist="+artist+"&api_key="+API_KEY+"&format=json")
    if resp.status_code == 200:
        data = resp.json()
        nameData = data['similarartists']['artist']
        return nameData
