import os
API_ID = int(os.getenv("6200062"))
API_HASH = os.getenv("c6367e505084b613cd60d80182e4d4d5")
BOT_TOKEN = os.getenv("1702065748:AAFNB91DxmL_9GXAl2p3taJFlLkoB1yHYdE")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
