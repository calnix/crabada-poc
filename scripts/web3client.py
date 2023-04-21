import json, time
from brownie.network.contract import Contract
from brownie import accounts, web3, config
from scripts.aws import get_pk

def create_contract():
    with open("./scripts/IdleGameAbi.json") as file:
        contract_abi = json.load(file)
    contract_address = "0x82a85407BD612f52577909F4A58bfC6873f14DA8"
    contract = Contract.from_abi("IdleGame", contract_address, contract_abi)
    return contract

# account
account = accounts.add(get_pk())

# max avax
max_avax = 0.01

def close_game(gameId, contract):
    # check gas
    close_gas()
    # tx - close game
    print("... Team 1: close_game ...")
    tx = contract.closeGame(gameId, {'from': account}) # this works!
    tx.wait(1)
    # if game has not ended ->  ValueError: Gas estimation failed: 'execution reverted: GAME:TOO EARLY'
    print("... Team 1: Closed game ...")


def start_game(contract,teamId=24182): #team1 = 24182
    #check gas
    start_gas()
    # start game
    print("... Team 1: start_game ...")
    start_tx = contract.startGame(teamId, {'from': account})
    start_tx.wait(1)
    print("... Team 1: Started game ...")



# gas mgmt
def close_gas():
    #print(web3.eth.gasPrice) -> returns GWEI - 1e9 wei | 48364216040 -> 48.36 GWEi
    while True:
        curr_avax =  128001 * (web3.eth.gasPrice / 10**18) 
        if curr_avax <= max_avax:
            print(f"...Current avax needed {curr_avax}...")
            print(f"...Max avax set to {max_avax}...")
            break
        else: 
            time.sleep(5)
    return (curr_avax <= max_avax)

    
def start_gas():
    #print(web3.eth.gasPrice) -> returns GWEI - 1e9 wei | 48364216040 -> 48.36 GWEi
    while True:
        curr_avax =  211862  * (web3.eth.gasPrice / 10**18) 
        if curr_avax <= max_avax:
            print(f"...Current avax needed {curr_avax}...")
            print(f"...Max avax set to {max_avax}...")
            break
        else: 
            time.sleep(5)
    return (curr_avax <= max_avax)


    