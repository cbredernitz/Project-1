import requests
import json
import random
import webbrowser


class Song(object):
    def __init__(self, song_dictionary):
        self.artist = song_dictionary["artistName"]
        self.track = song_dictionary["trackName"]
        self.album = song_dictionary["collectionName"]
        if song_dictionary["trackExplicitness"] == "notExplicit":
            self.explicit = False
        else:
            self.explicit = True
        if "trackViewUrl" in song_dictionary:
            self.track_url = song_dictionary["trackViewUrl"]
        else:
            self.track_url = None

    def __str__(self):
        return "{} by {} on {} whose URL is {}".format(self.track, self.artist, self.album, self.track_url)

    def __repr__(self):
        return "{} | Explicit: {}".format(self.track, self.explicit)

    def num_words_in_name(self):
        return len(self.album.split())

    def num_words_in_name_sans_determiners(self):
        return len([x for x in self.album.split() if (x.lower() != "the") and (x.lower() != "a")])

    def open_url_for_track(self):
        if self.track_url:
            webbrowser.open(self.track_url)
        else:
            print("Sorry, no such URL for this song: {}".format(self.track))


def random_song(list_of_song_objs):
    '''Function to get a random song from a list of song objects and return an identifiable tuple about the song'''
    song_picked = random.choice(list_of_song_objs)
    print(song_picked.track, song_picked.artist)# just return track name and artist tuple for identification
    return song_picked # return song object

def set_up_cache(cache_file_name="CACHE_FILE.txt"):
    try:
        f = open(cache_file_name)
        fstr = f.read()
        CACHE_DICTION = json.loads(fstr)
    except:
        CACHE_DICTION = {}
    return CACHE_DICTION

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)


def get_and_cache_songs(search_term):
    CACHE_DICTION = set_up_cache()
    baseurl = "https://itunes.apple.com/search"
    params = {}
    params["term"] = search_term
    params["entity"] = "song"
    unique_ident = params_unique_combination(baseurl, params)
    if unique_ident in CACHE_DICTION:
        return CACHE_DICTION[unique_ident]
    else:
        resp = requests.get(baseurl, params=params)
        resp_text = resp.text 
        python_resp = json.loads(resp_text)
        CACHE_DICTION[unique_ident] = python_resp
        return CACHE_DICTION[unique_ident]



if __name__ == '__main__':

    songs_resp = get_and_cache_songs("Want")
    song_objs = [Song(s) for s in songs_resp["results"]]
    single_song = random_song(song_objs)
    

