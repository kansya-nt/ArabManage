class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 20609170
    API_HASH = "cd0fa6d4f7c452ec5617bb0b1e4dc479"

    MUST_JOIN = "Berlinmusic_support"

    CASH_API_KEY = "J1BBEIOV38CZ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://zntgdebh:C_9TO4_Yaae7WAEMxRyyBzjqYQvwn1fA@pom.db.elephantsql.com/zntgdebh"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002049500040)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://kansya:1234@db-mongodb-sgp1-52558-1312a8db.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-sgp1-52558"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/file/163b8234f53e007e8f884.jpg"

    SUPPORT_CHAT = "Berlinmusic_support"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6742240257:AAHH7RDQILs6eHQFtdXwy02eLFsuNheQsx0"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "EYQXWAI8GT4M"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6024180996  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [6024180996]  # User id of sudo users
    DEV_USERS = [6024180996]  # User id of dev users
    DEMONS = [6024180996]  # User id of support users
    TIGERS = [6024180996]  # User id of tiger users
    WOLVES = [6024180996]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
