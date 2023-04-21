# Crabada idle game auto player

- brownie run deploy.py
- private key stored in aws secrets: accessed via aws.py
- web2client.py: deprecated in favour of direct contract interactions
- web3client.py: builds and signs transactions accordingly to game state
- gas.py: to prevent execution during high-gas periods
- messaging.py: send notifications to pushover for mobile updates.

Note: delays are introduced as safeguards, as well as to allow the API to update accordingly.

## Features

- Automatically send crabs mining.
- Automatically claim rewards.
- Run the bot without human supervision.
