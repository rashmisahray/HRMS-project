import os
from pymongo import MongoClient
from dotenv import load_dotenv

import certifi

load_dotenv()

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/?retryWrites=true&w=majority&appName=Cluster0"

SECRET_KEY = os.getenv("SECRET_KEY", "hrms-secret-key-2026")
DATABASE_NAME = "hrms_db"

USERS = {
    "admin": {"password": os.getenv("ADMIN_PASSWORD"), "role": "admin", "name": "Admin User"},
    "hr": {"password": os.getenv("HR_PASSWORD"), "role": "hr", "name": "HR Manager"},
    "finance": {"password": os.getenv("FINANCE_PASSWORD"), "role": "finance", "name": "Finance Manager"},
    "depthead": {"password": os.getenv("DEPTHEAD_PASSWORD"), "role": "depthead", "name": "Department Head"},
}

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000, tlsCAFile=certifi.where())
db = client[DATABASE_NAME]
