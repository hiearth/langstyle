#!/usr/bin/env python3

import langstyle.server
import langstyle.install.database

#upgrade database
langstyle.install.database.drop_and_create()

langstyle.server.start()
