import os

class Config:

    BOT_TOKEN = os.environ["5685905647:AAH1D3MtLQWWfowH7A-faWLRlHYmlwvd44U"]                                 # Get From https://t.me/BotFather

    API_ID = int(os.environ["1747534"])                                  # Get from https://my.telegram.org/apps

    API_HASH = os.environ["5a2684512006853f2e48aca9652d83ea"]                                   # Get from https://my.telegram.org/apps

    CLIENT_ID = os.environ["CLIENT_ID"]                                 # Get from https://console.developers.google.com/apis/credentials

    CLIENT_SECRET = os.environ["CLIENT_SECRET"]                         # Get from https://console.developers.google.com/apis/credentials

    BOT_OWNER = int(os.environ["BOT_OWNER"])                            # Bot owner's telegram id You can get with rose or marie

    AUTH_USERS = [BOT_OWNER,813878981]+[int(user) for user in os.environ["AUTH_USERS"].split(",") if os.environ["AUTH_USERS"]]
                                                                        # Id of other users who want to use your bot

    CRED_FILE = "auth_token.txt"                                        # Credentials file



