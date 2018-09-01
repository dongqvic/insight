from __future__ import print_function

import sys
import json
import os
import time
import datetime
import random
from kafka import KafkaConsumer
import psycopg2

KAFKA_TOPIC = 'producer'
KAFKA_BROKERS = ["34.216.43.1:9092","52.27.206.120:9092","54.244.196.222:9092"]
conn = psycopg2.connect(database='postgres_rds', user = 'postgres_master',password = 'postgres',host = 'postgres-rds.cbgshh8oysg5.us-west-2.rds.amazonaws.com', port='5432')

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKERS,
                         auto_offset_reset='earliest')
# Create a table with 
cur = conn.cursor()
cur.execute(
"""CREATE TABLE review ( \
reviewerID text, asin text, reviewerName text, helpful text, \
reviewerText text, overall text, summary text, unixReviewerTime text, reviewTime text)\
;""")

# The table is with schema fields
fields = [
    'reviewerID',
    'asin',
    'reviewerName',
    'helpful',
    'reviewText',
    'overall',
    'summary',
    'unixReviewTime',
    'reviewTime'
]

try:
    for message in consumer:
        print(type(message))
        print(message)

        msg = message.value.decode('utf-8')
        print (type(msg))
        print (msg)

        #msg_up = json.loads(msg)
        #print(type(msg_up))
        #print(msg_up)
        for i in msg:
            my_data = [i[field] for field in fields]
            cur.execute("INSERT INTO review VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);", (reviewerID,asin,reviewerName,helpful,reviewText,overall,summary,unixReviewTime,reviewTime))
    # commit changes
    conn.commit()
    # Close the connection
    conn.close()
except:
    pass
