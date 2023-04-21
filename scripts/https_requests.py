import requests
from datetime import datetime
url = "https://idle-api.crabada.com/public/idle/teams?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&limit=300&page=1&is_team_available=1"
baseUri = "https://idle-api.crabada.com/public/idle"

# for mines:
url = baseUri + "/mines"

#params
#params = {"user_address": "0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa","limit"= "300", }

# get requ
#response = requests.get(url)
#print(response.text)

# modify useragent to make it look legit

def get_Status():
    url = "https://idle-api.crabada.com/public/idle/teams?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&limit=300&page=1&is_team_available=1"
    response = requests.get(url)
    resp = response.json()
    totalRecord = resp["result"]["totalRecord"]  #if 0:team not available, if 1: anai
    if totalRecord == 0:
        print("... There is a mine instance. Check if ended/claimable ...")
    elif totalRecord == 1:
        print("... Team is available. Send for mining ...")
    return totalRecord

def convert_time(end_time):
    ending_time = datetime.fromtimestamp(end_time)  
    time_left = ending_time - datetime.now()
    time_left_seconds = time_left.total_seconds()
    print(f"... Mine will end at {ending_time} ...")
    return time_left_seconds


def get_endtime_mineId():
    url = "https://idle-api.crabada.com/public/idle/mines?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&page=1&status=open&limit=8"
    response = requests.get(url)
    resp = response.json()
    totalRecord = resp["result"]["totalRecord"]
    if totalRecord == 1:
        end_time = resp["result"]["data"][0]["end_time"]
        game_id = resp["result"]["data"][0]["game_id"]
        print(f"End_time: {end_time}")
        print(f"Mine_ID: {game_id}")
        return end_time, game_id

    elif totalRecord == 0:
        print("... There are no active mines ...")
        return False, False
    
    else: 
        print("...totalRecord is neither 0 nor 1...")


def get_Status_test():
    urls = []
    urls.append('https://idle-api.crabada.com/public/idle/mines?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&page=1&status=open&limit=8') 
    urls.append('https://idle-api.crabada.com/public/idle/teams?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&limit=300&page=1&is_team_available=1')
    urls.append('https://idle-api.crabada.com/public/idle/teams?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&limit=300&page=1&is_team_available=0')

    for i in range(len(urls)):
        print(urls[i])
        response = requests.get(urls[i])
        resp = response.json()
        print(resp)
        print("......")

print(get_Status())

## JSON 
# type 1 
# https://idle-api.crabada.com/public/idle/mines?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&page=1&status=open&limit=8 
# http.json
# ran while mine was underway.


# https://idle-api.crabada.com/public/idle/teams?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&limit=300&page=1&is_team_available=1
# ran while mine was underway:
# {'error_code': None, 'message': None, 'result': {'totalRecord': 0, 'totalPages': 1, 'page': 1, 'limit': 300, 'data': None, 'team_size': 3}}
# ran while there was no mine:
# {'error_code': None, 'message': None, 'result': {'totalRecord': 1, 'totalPages': 1, 'page': 1, 'limit': 300, 'data': [{'team_id': 24182, 'looting_point': 12, 'owner': '0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa', 'crabada_id_1': 57181, 'crabada_1_photo': '57181.png', 'crabada_1_hp': 125, 'crabada_1_speed': 29, 'crabada_1_armor': 25, 'crabada_1_damage': 71, 'crabada_1_critical': 52, 'crabada_1_is_origin': 0, 'crabada_1_is_genesis': 0, 'crabada_1_legend_number': 0, 'crabada_id_2': 57647, 'crabada_2_photo': '57647.png', 'crabada_2_hp': 125, 'crabada_2_speed': 29, 'crabada_2_armor': 25, 'crabada_2_damage': 71, 'crabada_2_critical': 52, 'crabada_2_is_origin': 0, 'crabada_2_is_genesis': 0, 'crabada_2_legend_number': 0, 'crabada_id_3': 19608, 'crabada_3_photo': '19608.png', 'crabada_3_hp': 148, 'crabada_3_speed': 27, 'crabada_3_armor': 35, 'crabada_3_damage': 54, 'crabada_3_critical': 39, 'crabada_3_is_origin': 0, 'crabada_3_is_genesis': 0, 'crabada_3_legend_number': 0, 'battle_point': 679, 'lock_expired_at': None, 'time_point': 228, 'mine_point': 228, 'game_type': None, 'mine_start_time': None, 'mine_end_time': None, 'game_id': None, 'game_start_time': None, 'game_end_time': None, 'process_status': None, 'game_round': None, 'status': 'AVAILABLE', 'faction': 'LUX', 'crabada_1_class': 3, 'crabada_2_class': 3, 'crabada_3_class': 4, 'crabada_1_type': 1, 'crabada_2_type': 1, 'crabada_3_type': 1}], 'team_size': 3}}



# https://idle-api.crabada.com/public/idle/teams?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&limit=300&page=1&is_team_available=0
# ran while mine was underway:
# {'error_code': None, 'message': None, 'result': {'totalRecord': 1, 'totalPages': 1, 'page': 1, 'limit': 300, 'data': [{'team_id': 24182, 'looting_point': 12, 'owner': '0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa', 'crabada_id_1': 57181, 'crabada_1_photo': '57181.png', 'crabada_1_hp': 125, 'crabada_1_speed': 29, 'crabada_1_armor': 25, 'crabada_1_damage': 71, 'crabada_1_critical': 52, 'crabada_1_is_origin': 0, 'crabada_1_is_genesis': 0, 'crabada_1_legend_number': 0, 'crabada_id_2': 57647, 'crabada_2_photo': '57647.png', 'crabada_2_hp': 125, 'crabada_2_speed': 29, 'crabada_2_armor': 25, 'crabada_2_damage': 71, 'crabada_2_critical': 52, 'crabada_2_is_origin': 0, 'crabada_2_is_genesis': 0, 'crabada_2_legend_number': 0, 'crabada_id_3': 19608, 'crabada_3_photo': '19608.png', 'crabada_3_hp': 148, 'crabada_3_speed': 27, 'crabada_3_armor': 35, 'crabada_3_damage': 54, 'crabada_3_critical': 39, 'crabada_3_is_origin': 0, 'crabada_3_is_genesis': 0, 'crabada_3_legend_number': 0, 'battle_point': 679, 'lock_expired_at': None, 'time_point': 228, 'mine_point': 228, 'game_type': 'mining', 'mine_start_time': 1650251307, 'mine_end_time': 1650265707, 'game_id': 4610556, 'game_start_time': 1650251307, 'game_end_time': 1650265707, 'process_status': 'attack', 'game_round': 0, 'status': 'MINING', 'faction': 'LUX', 'crabada_1_class': 3, 'crabada_2_class': 3, 'crabada_3_class': 4, 'crabada_1_type': 1, 'crabada_2_type': 1, 'crabada_3_type': 1}], 'team_size': 3}}
# ran while there was no mine:
# {'error_code': None, 'message': None, 'result': {'totalRecord': 1, 'totalPages': 1, 'page': 1, 'limit': 300, 'data': [{'team_id': 24182, 'looting_point': 12, 'owner': '0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa', 'crabada_id_1': 57181, 'crabada_1_photo': '57181.png', 'crabada_1_hp': 125, 'crabada_1_speed': 29, 'crabada_1_armor': 25, 'crabada_1_damage': 71, 'crabada_1_critical': 52, 'crabada_1_is_origin': 0, 'crabada_1_is_genesis': 0, 'crabada_1_legend_number': 0, 'crabada_id_2': 57647, 'crabada_2_photo': '57647.png', 'crabada_2_hp': 125, 'crabada_2_speed': 29, 'crabada_2_armor': 25, 'crabada_2_damage': 71, 'crabada_2_critical': 52, 'crabada_2_is_origin': 0, 'crabada_2_is_genesis': 0, 'crabada_2_legend_number': 0, 'crabada_id_3': 19608, 'crabada_3_photo': '19608.png', 'crabada_3_hp': 148, 'crabada_3_speed': 27, 'crabada_3_armor': 35, 'crabada_3_damage': 54, 'crabada_3_critical': 39, 'crabada_3_is_origin': 0, 'crabada_3_is_genesis': 0, 'crabada_3_legend_number': 0, 'battle_point': 679, 'lock_expired_at': None, 'time_point': 228, 'mine_point': 228, 'game_type': None, 'mine_start_time': None, 'mine_end_time': None, 'game_id': None, 'game_start_time': None, 'game_end_time': None, 'process_status': None, 'game_round': None, 'status': 'AVAILABLE', 'faction': 'LUX', 'crabada_1_class': 3, 'crabada_2_class': 3, 'crabada_3_class': 4, 'crabada_1_type': 1, 'crabada_2_type': 1, 'crabada_3_type': 1}], 'team_size': 3}}


# use the first url
# if game_id present, 
# check is end_time has elapsed -. if so, close game
# if data is empty "data": [] -> start game