# Gas & Fees

actual fee is: gasUsed \* baseFee (converted to 9 decimals)
https://snowtrace.io/tx/0x10bfa494e68ae3f5bbe3de38c26d72cd50a7122ba42b7e98cd8a5466b1f77c36

- total gas units: 128,001

# Getting baseFee

print(web3.eth.gasPrice)

- returns in 9 dp. as WEi (29331592115)
- to get Gwei, which is reflected in gas trackers online print(web3.eth.gasPrice / 10\*\*9) -> 29.33 (GWei/nAVAX)
- to get baseFee(in avax), 29.33 (GWei/nAVAX) / 10\*\*9 ->
- https://snowtrace.io/unitconverter | https://cointool.app/unitConverter/eth

# Dont want actual fee to exceed 0.07

gasUsed _ baseFee <= 0.07
128001 _ baseFee(in avax) <= 0.07
128001 \* (web3.eth.gasPrice / 10**9 / 10**9) <= 0.07

# Json stuff

## JSON

# type 1

# https://idle-api.crabada.com/public/idle/mines?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&page=1&status=open&limit=8

# ran while mine was underway: http.json

# ran while there was no mine:

{'error_code': None, 'message': None, 'result': {'totalRecord': 0, 'totalPages': 1, 'page': 1, 'limit': 8, 'data': []}}

# https://idle-api.crabada.com/public/idle/teams?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&limit=300&page=1&is_team_available=1

# ran while mine was underway:

{'error_code': None, 'message': None, 'result': {'totalRecord': 0, 'totalPages': 1, 'page': 1, 'limit': 300, 'data': None, 'team_size': 3}}

# ran while there was no mine:

{'error_code': None, 'message': None, 'result': {'totalRecord': 1, 'totalPages': 1, 'page': 1, 'limit': 300, 'data': [{'team_id': 24182, 'looting_point': 12, 'owner': '0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa', 'crabada_id_1': 57181, 'crabada_1_photo': '57181.png', 'crabada_1_hp': 125, 'crabada_1_speed': 29, 'crabada_1_armor': 25, 'crabada_1_damage': 71, 'crabada_1_critical': 52, 'crabada_1_is_origin': 0, 'crabada_1_is_genesis': 0, 'crabada_1_legend_number': 0, 'crabada_id_2': 57647, 'crabada_2_photo': '57647.png', 'crabada_2_hp': 125, 'crabada_2_speed': 29, 'crabada_2_armor': 25, 'crabada_2_damage': 71, 'crabada_2_critical': 52, 'crabada_2_is_origin': 0, 'crabada_2_is_genesis': 0, 'crabada_2_legend_number': 0, 'crabada_id_3': 19608, 'crabada_3_photo': '19608.png', 'crabada_3_hp': 148, 'crabada_3_speed': 27, 'crabada_3_armor': 35, 'crabada_3_damage': 54, 'crabada_3_critical': 39, 'crabada_3_is_origin': 0, 'crabada_3_is_genesis': 0, 'crabada_3_legend_number': 0, 'battle_point': 679, 'lock_expired_at': None, 'time_point': 228, 'mine_point': 228, 'game_type': None, 'mine_start_time': None, 'mine_end_time': None, 'game_id': None, 'game_start_time': None, 'game_end_time': None, 'process_status': None, 'game_round': None, 'status': 'AVAILABLE', 'faction': 'LUX', 'crabada_1_class': 3, 'crabada_2_class': 3, 'crabada_3_class': 4, 'crabada_1_type': 1, 'crabada_2_type': 1, 'crabada_3_type': 1}], 'team_size': 3}}

# https://idle-api.crabada.com/public/idle/teams?user_address=0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa&limit=300&page=1&is_team_available=0

# ran while mine was underway:

{'error_code': None, 'message': None, 'result': {'totalRecord': 1, 'totalPages': 1, 'page': 1, 'limit': 300, 'data': [{'team_id': 24182, 'looting_point': 12, 'owner': '0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa', 'crabada_id_1': 57181, 'crabada_1_photo': '57181.png', 'crabada_1_hp': 125, 'crabada_1_speed': 29, 'crabada_1_armor': 25, 'crabada_1_damage': 71, 'crabada_1_critical': 52, 'crabada_1_is_origin': 0, 'crabada_1_is_genesis': 0, 'crabada_1_legend_number': 0, 'crabada_id_2': 57647, 'crabada_2_photo': '57647.png', 'crabada_2_hp': 125, 'crabada_2_speed': 29, 'crabada_2_armor': 25, 'crabada_2_damage': 71, 'crabada_2_critical': 52, 'crabada_2_is_origin': 0, 'crabada_2_is_genesis': 0, 'crabada_2_legend_number': 0, 'crabada_id_3': 19608, 'crabada_3_photo': '19608.png', 'crabada_3_hp': 148, 'crabada_3_speed': 27, 'crabada_3_armor': 35, 'crabada_3_damage': 54, 'crabada_3_critical': 39, 'crabada_3_is_origin': 0, 'crabada_3_is_genesis': 0, 'crabada_3_legend_number': 0, 'battle_point': 679, 'lock_expired_at': None, 'time_point': 228, 'mine_point': 228, 'game_type': 'mining', 'mine_start_time': 1650251307, 'mine_end_time': 1650265707, 'game_id': 4610556, 'game_start_time': 1650251307, 'game_end_time': 1650265707, 'process_status': 'attack', 'game_round': 0, 'status': 'MINING', 'faction': 'LUX', 'crabada_1_class': 3, 'crabada_2_class': 3, 'crabada_3_class': 4, 'crabada_1_type': 1, 'crabada_2_type': 1, 'crabada_3_type': 1}], 'team_size': 3}}

# ran while there was no mine:

{'error_code': None, 'message': None, 'result': {'totalRecord': 1, 'totalPages': 1, 'page': 1, 'limit': 300, 'data': [{'team_id': 24182, 'looting_point': 12, 'owner': '0xfea275521354c1f1fbc1cd32bfd6d9b407df7bfa', 'crabada_id_1': 57181, 'crabada_1_photo': '57181.png', 'crabada_1_hp': 125, 'crabada_1_speed': 29, 'crabada_1_armor': 25, 'crabada_1_damage': 71, 'crabada_1_critical': 52, 'crabada_1_is_origin': 0, 'crabada_1_is_genesis': 0, 'crabada_1_legend_number': 0, 'crabada_id_2': 57647, 'crabada_2_photo': '57647.png', 'crabada_2_hp': 125, 'crabada_2_speed': 29, 'crabada_2_armor': 25, 'crabada_2_damage': 71, 'crabada_2_critical': 52, 'crabada_2_is_origin': 0, 'crabada_2_is_genesis': 0, 'crabada_2_legend_number': 0, 'crabada_id_3': 19608, 'crabada_3_photo': '19608.png', 'crabada_3_hp': 148, 'crabada_3_speed': 27, 'crabada_3_armor': 35, 'crabada_3_damage': 54, 'crabada_3_critical': 39, 'crabada_3_is_origin': 0, 'crabada_3_is_genesis': 0, 'crabada_3_legend_number': 0, 'battle_point': 679, 'lock_expired_at': None, 'time_point': 228, 'mine_point': 228, 'game_type': None, 'mine_start_time': None, 'mine_end_time': None, 'game_id': None, 'game_start_time': None, 'game_end_time': None, 'process_status': None, 'game_round': None, 'status': 'AVAILABLE', 'faction': 'LUX', 'crabada_1_class': 3, 'crabada_2_class': 3, 'crabada_3_class': 4, 'crabada_1_type': 1, 'crabada_2_type': 1, 'crabada_3_type': 1}], 'team_size': 3}}
