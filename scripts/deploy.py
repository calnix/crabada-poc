import time
from scripts.messaging import send_message
from scripts.web3client import create_contract, start_game, close_game
from scripts.https_requests import get_Status, convert_time, get_endtime_mineId

# contract
contract = create_contract()


# team id
team1_id = 24182


def main():
    while True:        
        
        # get game state
        team_status = get_Status()

        # Team is available. Send for mining
        if team_status == 1:
            start_game(contract, team1_id)
            time.sleep(60*3)

            # get game details
            (end_time, mining_id) = get_endtime_mineId()
            time_left_seconds = convert_time(end_time) 
           
            # inform limpeh
            print(f"... Team 1: Started Game. Ending in {end_time}...")
            send_message("... Team 1: Started Game  ...")

        
        # there exists an ongoing mine
        elif team_status == 0:        
            # get game details 
            (end_time, mining_id) = get_endtime_mineId()
            time_left_seconds = convert_time(end_time) + 10 
            
            # sleep if needed
            if time_left_seconds > 0:
                print(f"...Mine Status: On-going! Sleeping for {time_left_seconds} ...")
                time.sleep(time_left_seconds)

            # claim
            close_game(mining_id, contract)
            time.sleep(60*3)

            # inform limpeh
            send_message("... Team 1: Closed Game ...")

        else:
            print("we should not be here")
            send_message("... WE  SHOULD NOT BE HERE  ...")

            

      











# need to get mine id for each game.
# team id is fixed. 
# if multiple teams per account, then mine ID will be difficult/more complex to crawl , per team.
# bin/mining/closeMines.py