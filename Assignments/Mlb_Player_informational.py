import requests
import json
import speech_recognition as s_r
from pprint import pprint
import pyttsx3
import threading
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id)


my_mic = s_r.Microphone()
r = s_r.Recognizer()

def find_in_dict(dict, stat):
    return dict.get("sport_career_hitting").get("queryResults").get("row").get(stat)

def find_in_bio(dict, stat):
    return dict.get("player_info").get("queryResults").get("row").get(stat)

#Creating a list of answers that are plausable
list_of_answers = ["batting", "gidp", "bats", "runs", "left", "babip", "rbi", "slugging"]
""""
I want to make my program possible to search up information of any baseball player in history and to get the basic 
stats about this person. Because the current stats API is not active anymore, I decided to do career stats which do
not change as much
"""

def find_bio_out():
    if "from".lower() in response_list:
        print("\n" + player_name + " is from: " + find_in_bio(stats, "birth_city") + ", " + find_in_bio(stats, "birth_country"))
    elif "nickname".lower() in response_list:
        print("\n" + player_name + "'s nickname is: " + find_in_bio(stats, "name_nick"))
    elif "team".lower() in response_list:
        print("\n" + player_name + "is on the: " + find_in_bio(stats, "team_name"))


#if statements prints below
def find_out():
    if "batting".lower() in response_list:
        engine.say(player_name + "'s career batting average is: " + find_in_dict(stats,"avg") )
        engine.runAndWait()
        print( "\n" + player_name + "'s career batting average is: " + find_in_dict(stats,"avg") + "\n")
    elif "gidp".lower() in response_list:
        engine.say(player_name + ("'s career ground-outs into double plays are: ") + find_in_dict(stats,"gidp"))
        engine.runAndWait()
        print( "\n" + player_name + ("'s career ground-outs into double plays are: ") + find_in_dict(stats,"gidp") + "\n")
    elif "walk-off".lower() in response_list:
        engine.say(player_name + " has " + find_in_dict(stats,"wo") + " career walk-offs.")
        engine.runAndWait()
        print( "\n" + player_name + " has " + find_in_dict(stats,"wo") + " career walk-offs." + "\n")
    elif "bats".lower() in response_list:
        engine.say(player_name + "'s career at bat is: " + find_in_dict(stats,"ab"))
        engine.runAndWait()
        print( "\n" + player_name + "'s career at bat is: " + find_in_dict(stats,"ab") + "\n")
    elif "runs".lower() in response_list:
        engine.say(player_name + "'s career home runs are: " + find_in_dict(stats, "hr"))
        engine.runAndWait()
        print( "\n" + player_name + "'s career home runs are: " + find_in_dict(stats, "hr") + "\n")
    elif "left".lower() in response_list:
        engine.say(player_name + "'s career left-on-base are: " + find_in_dict(stats, "lob"))
        engine.runAndWait()
        print( "\n" + player_name + "'s career left-on-base are: " + find_in_dict(stats, "lob") + "\n")
    elif "babip".lower() in response_list:
        engine.say(player_name + "'s career batting average with a ball in play is: " + find_in_dict(stats, "babip"))
        engine.runAndWait()
        print( "\n" + player_name + "'s career batting average with a ball in play is: " + find_in_dict(stats, "babip") + "\n")
    elif "rbi".lower() in response_list:
        engine.say(player_name + "'s career rbi is: " + find_in_dict(stats, "rbi"))
        engine.runAndWait()
        print( "\n" + player_name + "'s career rbi is: " + find_in_dict(stats, "rbi") + "\n")
    elif "slugging".lower() in response_list:
        engine.say(player_name + "'s career slugging average is: " + find_in_dict(stats, "slg"))
        engine.runAndWait()
        print( "\n" + player_name + "'s career slugging average is: " + find_in_dict(stats, "slg") + "\n")
    elif "base".lower() in response_list:
        engine.say(player_name + "'s career on-base percentage is: " + str(find_in_dict(stats, "obp")))
        engine.runAndWait()
        print( "\n" + player_name + "'s career on-base percentage is: " + str(find_in_dict(stats, "obp")) + "\n")
    else:
        engine.say("please enter a valid response.")
        engine.runAndWait()
        print("please enter a valid response.")

def welcomesaying(e):
    print("Welcome to the MLB Chatbot, you can ask me a variety of things about specific players")
e = threading.Event()
t = threading.Thread(target=welcomesaying, args=(e,))
t.start()
engine.say("Welcome to the MLB Chatbot, you can ask me a variety of things about specific players")
engine.runAndWait()

def batnbasesaying(e):
    print("You can ask about carreer batting and career baserunning stats, chances are, I will know. (leave out pitching stats)")
e = threading.Event()
t = threading.Thread(target=batnbasesaying, args=(e,))
t.start()
engine.say("You can ask about batting and baserunning stats or profile, chances are, I will know. (leave out pitching stats)")
engine.runAndWait()

engine.say("Here is a list of everything you can ask me:")
engine.runAndWait()
print("Here is a list of everything you can ask me:\n ")
print("career at bats \ncareer gidp \ncareer on-base percentage \ncarreer walk-offs \ncareer home runs \ncareer left on bases \ncareer babip \ncareer rbi \ncareer slugging")
engine.say("I also know")
engine.runAndWait()
print("hometown \nnicknames \nteam \n ")
print(" ")
#UI asking questions code
while True:
    while True:
        engine.say("Is the player you're asking about active or retired?")
        engine.runAndWait()
        with my_mic as source:
            r.adjust_for_ambient_noise(source)
            print("Say 'active' or 'retired'")
            audio = r.listen(source)
            try:
                active_or_history = r.recognize_google(audio)
                print(r.recognize_google(audio))
            except:
                active_or_history = input("Is the player you're asking about active or retired?: \n")
        if active_or_history.lower() in ["current", "active"]:
            y_or_n =  "Y"
            break
        elif active_or_history.lower() in ["historical", "retired", "old",]:
            y_or_n = "N"
            break
        else:
            print("That's not a valid response")
    engine.say("Who would you like to know about?")
    engine.runAndWait()
    with my_mic as source:
        r.adjust_for_ambient_noise(source)
        print("Say which player you would like to know")
        audio = r.listen(source)
        try:
            player_name = r.recognize_google(audio)
            print(r.recognize_google(audio))
        except:
            player_name = input("Who would you like to know about?: \n")
    player_api = requests.get(
        "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='" + y_or_n + "'&name_part='" + player_name + "%25'")
    data_dict = json.loads(player_api.text)
    if data_dict.get("search_player_all").get('queryResults').get('totalSize') == "0":
        engine.say("player not detected")
        engine.runAndWait()
        print("Player not detected")
        break
    else:
        player_id = data_dict.get("search_player_all").get("queryResults").get("row").get("player_id")
    engine.say("Would you like to know Bio, or stats about " + player_name + "?: " + "\n")
    engine.runAndWait()
    with my_mic as source:
        r.adjust_for_ambient_noise(source)
        print("Say Bio or Stat")
        audio = r.listen(source)
        try:
            if_or_if = r.recognize_google(audio)
            print(r.recognize_google(audio))
        except:
            if_or_if = input("Bio or stats?: \n")
    if if_or_if.lower() in {"stats", "stat"}:
        engine.say("What stat line would you like to know?")
        engine.runAndWait()
        with my_mic as source:
            r.adjust_for_ambient_noise(source)
            print("Say what stat line you would like to know")
            audio = r.listen(source)
            try:
                response = r.recognize_google(audio)
                print(r.recognize_google(audio))
            except:
                hitting_stats = input("What stat would you like to know?: \n")
        # Going into second to get stats
        hitting_statsapi = requests.get(
            "http://lookup-service-prod.mlb.com/json/named.sport_career_hitting.bam?league_list_id='mlb'&game_type='R'&player_id='" + player_id + "'")
        # pprint(json.loads(hitting_statsapi.text))
        stats = json.loads(hitting_statsapi.text)
        response_list = response.split()
        response_list = [r.lower() for r in response_list]
        find_out()
    elif if_or_if.lower() in {"bio", "info", "information"}:
        engine.say("What would you like to know about " + player_name + ("?"))
        engine.runAndWait()
        with my_mic as source:
            r.adjust_for_ambient_noise(source)
            print("Say what you would like to know")
            audio = r.listen(source)
            try:
                user_response = r.recognize_google(audio)
                print(r.recognize_google(audio))
            except:
                user_response = input("What would you like to know about " + player_name + ("?:\n"))
        user_response = input("What would you like to know about " + player_name + ("?: "))
        response_list = user_response.split()
        response_list = [r.lower() for r in response_list]
        hitting_statsapi = requests.get(
            "http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='" + player_id + "'")
        stats = json.loads(hitting_statsapi.text)
        find_bio_out()
#asking abt another player
    engine.say("would you like to know about another player?")
    engine.runAndWait()
    yes_or_no = input("\nWould you like to know about another player?: ")
    if yes_or_no.lower() == "no":
        engine.say("okay")
        engine.runAndWait()

        break
    else:
        engine.say("okay")
        engine.runAndWait()
        print('\n')
        response_list = {}
