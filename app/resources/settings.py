from os import getenv


BASE_URL = getenv("BASE_URL", "/v1/trackers")
COOKIE_MAX_AGE = 60*60*72
DOMAIN = "localhost"
PATH = "/v1/trackers/item"
