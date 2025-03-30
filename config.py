from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "21134445"))
API_HASH = environ.get("API_HASH", "231c18ea7273824491d6bf05425ab74e")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7506799376:AAGv3uinQM-bnU_hTHLhggOsL7_vnf0TpCg")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7763229951")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002107236622")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://bornhyper1:Bornhyper5911@cluster0.gmvpm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
