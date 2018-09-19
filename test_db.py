"""
Contain the functions for run application.
"""

import psycopg2
from urllib.parse import urlparse


info_db = urlparse(
            "postgres://hzajnzutyyndog:ab2cffd9f9a694f816728c6ca5133b21d6006156cf84a586be566e61a2e88cf7@ec2-54-247-98-162.eu-west-1.compute.amazonaws.com:5432/df6ko6h1vmn5gf")

username = info_db.username
password = info_db.password
database = info_db.path[1:]
hostname = info_db.hostname
connexion = psycopg2.connect(
    database=database,
    user=username,
    password=password,
    host=hostname
)

import pdb ; pdb.set_trace()
