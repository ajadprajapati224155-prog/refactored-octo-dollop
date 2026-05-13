#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from pymongo import MongoClient

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7934788301:AAE70WxZS1WfNrbeDRRjb1XD-h4SxtDcAXw")
    API_ID = int(os.environ["API_ID", 24037760]
    API_HASH = os.environ["API_HASH", "dccc3070f1c12ab155011f14c3d6ae6a"]
    AUTH_USERS = "7834875502"
    MONGO_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://mpsystem05:ZzYGIZ0a4PCUQkKm@cluster0.eppygqi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
