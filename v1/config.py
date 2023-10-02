# Password Request Params
import os

password_min_length = 8
password_max_length = 64

# DB
DB_URI = os.getenv("DB_URI")
ECHO_SQL = os.getenv("ECHO_SQL") == "1"