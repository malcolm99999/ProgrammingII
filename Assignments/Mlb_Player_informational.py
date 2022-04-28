import requests
import json
from pprint import pprint
def find_in_dict(dict, stat):
    return dict.get("sport_career_hitting").get("queryResults").get("row").get(stat)

#Creating a list of answers that are plausable
list_of_answers = ["batting", "gidp", "bats", "runs", "left", "babip", "rbi", "slugging"]
""""
I want to make my program possible to search up information of any baseball player in history and to get the basic 
stats about this person. Because the current stats API is not active anymore, I decided to do career stats which do
not change as much
"""


#if statements prints below
def find_out():
    if "batting".lower() in response_list:
        print(player_name + "'s career batting average is: " + find_in_dict(stats,"avg") + "\n")
    if "gidp".lower() in response_list:
        print(player_name + ("'s career ground-outs into double plays are: ") + find_in_dict(stats,"gidp") + "\n")
    if "bats".lower() in response_list:
        print(player_name + "'s career at bat is: " + find_in_dict(stats,"ab") + "\n")
    if "runs".lower() in response_list:
        print(player_name + "'s career home runs are: " + find_in_dict(stats, "hr") + "\n")
    if "left".lower() in response_list:
        print(player_name + "'s career left-on-base are: " + find_in_dict(stats, "lob") + "\n")
    if "babip".lower() in response_list:
         print(player_name + "'s career batting average with a ball in play is: " + find_in_dict(stats, "babip") + "\n")
    if "rbi".lower() in response_list:
        print(player_name + "'s career rbi is: " + find_in_dict(stats, "rbi") + "\n")
    if "slugging".lower() in response_list:
        print(player_name + "'s career slugging average is: " + find_in_dict(stats, "slg") + "\n")
    if user_response not in list_of_answers:
        print("Please select a valid choice")

print("Welcome to the MLB Chatbot, you can ask me a variety of things about specifc players")
print("You can ask about batting and baserunning stats or profile, chances are, I will know. (leave out pitching stats)")
print("Here is a list of everything you can ask me:\n "
      "career at bats \n career gidp \n career home runs \n career left on bases \n career babip \n career rbi \n career slugging")
print("\n")

#UI asking questions code
while True:
    while True:
        active_or_history = input("Is the player you're asking about active or retired?: ")
        if active_or_history.lower() in ["current", "active"]:
            y_or_n =  "Y"
            break
        elif active_or_history.lower() in ["historical", "retired", "old",]:
            y_or_n = "N"
            break
        else:
            print("That's not a valid response")
    player_name = input("Who would you like to know about?: ")
    user_response = input("What would you like to know?: ")

#going into first API to get the user ID
    response_list = user_response.split()
    player_api = requests.get( "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='"+ y_or_n + "'&name_part='" + player_name +"%25'")
    data_dict = json.loads(player_api.text)
    if data_dict.get("search_player_all").get('queryResults').get('totalSize') == "0":
        print("Player not detected")
    else:
        player_id = data_dict.get("search_player_all").get("queryResults").get("row").get("player_id")
#Going into second to get stats
        hitting_statsapi = requests.get("http://lookup-service-prod.mlb.com/json/named.sport_career_hitting.bam?league_list_id='mlb'&game_type='R'&player_id='" + player_id + "'")
    #pprint(json.loads(hitting_statsapi.text))
        stats = json.loads(hitting_statsapi.text)
        find_out()
#asking abt another player
    yes_or_no = input("Would you like to know about another player?: ")
    if yes_or_no.lower() == "no":
        break
    else:
        print('\n')