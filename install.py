
import time
from langstyle import config
from langstyle.install import database
from langstyle.install import english_word

log_service = config.service_factory.get_log_service()

# create database
log_service.debug("begin create database")
database.drop_and_create()
log_service.debug("finish create database")

# populate words
log_service.debug("begin populate words")
start_time = time.time()
english_word.chinese_english_words()
log_service.debug(str(time.time()-start_time) + " seconds")
log_service.debug("finish populate words")

# populate english characters
log_service.debug("begin populate english characters")
start_time = time.time()
#english_word.populate_cet_characters()
log_service.debug(str(time.time()-start_time) + " seconds")
log_service.debug("finish populate english characters")

# populate english sounds
log_service.debug("begin populate english sounds")
start_time = time.time()
#english_word.populate_sounds()
log_service.debug(str(time.time()-start_time) + " seconds")
log_service.debug("finish populate english sounds")

# populate images
log_service.debug("begin populate english images")
start_time = time.time()
english_word.populate_images()
log_service.debug(str(time.time()-start_time) + " seconds")
log_service.debug("finish populate english images")

