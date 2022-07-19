import datetime
import json
import random
import tweepy

def load_keys():
    """Load keys file"""
    # Find the file and open it
    file = open("../.secrets/keys.json")
    # Parse JSON
    keys = json.load(file)
    # Return results
    return keys

def tweet(message):
    """Handles authentication and tweeting."""
    # Get keys from file
    keys = load_keys()
    # "Log in"
    auth = tweepy.OAuthHandler(
        keys["API"], 
        keys["API_SECRET"]
    )
    auth.set_access_token(
        keys["ACCESS"], 
        keys["ACCESS_SECRET"]
    )
    api = tweepy.API(auth)
    # Post message
    api.update_status(message)
    
def get_year():
    now = datetime.datetime.now()
    date = now.date()
    return date.strftime("%Y")
    
def main():
    #         File path,                      File mode
    fh = open("_data/divination/zodiac.json", "r")
    zodiac = json.load(fh)
    #     dictionary --> associative array (key => value)
    eastern_zodiac = zodiac["eastern_zodiac"]
    for zodiac in eastern_zodiac:
        zodiac_year = eastern_zodiac[zodiac]["years"]
        if get_year() not in zodiac_year:
            tweet(f"It is not the year of the {zodiac}")
            break
    # TODO: Implement your bot in the main function
    #       provided here and dont forget to tweet!
    pass    # <-- delete or comment this line out when done
    
if __name__ == "__main__":
    main()
