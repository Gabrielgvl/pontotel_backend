import logging
import os

DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/api")
HOST = os.getenv("APPLICATION_HOST", "192.168.2.17")
PORT = int(os.getenv("APPLICATION_PORT", "8080"))
SQLALCHEMY_TRACK_MODIFICATIONS = False
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", "OPHF3J94FCTPNKCC")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "pontosecreto")

DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "localhost")
POSTGRES = {
    "user": os.getenv("APPLICATION_POSTGRES_USER", "postgres"),
    "pw": os.getenv("APPLICATION_POSTGRES_PW", ""),
    "host": os.getenv("APPLICATION_POSTGRES_HOST", DB_CONTAINER),
    "port": os.getenv("APPLICATION_POSTGRES_PORT", 5432),
    "db": os.getenv("APPLICATION_POSTGRES_DB", "postgres"),
}
DB_URI = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
