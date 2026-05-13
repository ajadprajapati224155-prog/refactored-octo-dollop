#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from pymongo import MongoClient

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8647304259:AAEjFvIQXYJUN952IFst04JTQQhygzEcQZo")
    API_ID = int(os.environ["API_ID", 35279304]
    API_HASH = os.environ["API_HASH", "49ea7646f4251b3ca5a7798c61bb5e9f"]
    AUTH_USERS = "6824252172"
    MONGO_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://privatefiles224155_db_user:mypassword123@cluster0.nrephhv.mongodb.net/?appName=Cluster0")
    
