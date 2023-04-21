from brownie import web3


def main():
    print(web3.eth.gasPrice) 
    #nAvax
    print(web3.eth.gasPrice/ 10**9) 

    gasUsed = 128001
    base_fee_gwei = web3.eth.gasPrice   #in avax: (41.952730216 navax / 1000000000 = 0.000000041952730216  AVAX)
    avax = (base_fee_gwei) * gasUsed
    print(F"avax USED {avax}")
