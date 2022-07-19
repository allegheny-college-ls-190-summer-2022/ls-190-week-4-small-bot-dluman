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
    # Test if message is too long, quit if so, print stats
    if len(message) > 240: # <-- if message is too long (i.e. more than 240 chars)
        # The print statements are just "tracing" code
        print(len(message), message) # <-- print both values with space between
        print("It's too long!")
        return # <-- Because I return here, nothing else happens
    
    # If message is not too long, go ahead
    
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
    
if __name__ == "__main__":
    main()
