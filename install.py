
import time
from langstyle import config
from langstyle.install import database
from langstyle.install import english_character

log_service = config.service_factory.get_log_service()

# create database
log_service.debug("begin create database")
database.drop_and_create()
log_service.debug("finish create database")

# populate english characters
log_service.debug("begin populate english characters")
start_time = time.time()
english_character.populate_cet_characters()
log_service.debug(str(time.time()-start_time) + " seconds")
log_service.debug("finish populate english characters")