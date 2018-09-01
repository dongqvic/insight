import boto3
import botocore
import time
import threading, logging, time
from kafka import KafkaProducer
import smart_open
import json

class Producer(threading.Thread):
        daemon = True

        def run(self):
            producer = KafkaProducer(
                            bootstrap_servers=["34.216.43.1:9092","52.27.206.120:9092","54.244.196.222:9092"],
                            key_serializer=lambda m: m.encode('utf8'),
                            value_serializer=lambda m: json.dumps(m).encode('utf8'),
                        ) # Broker servers 
            bucket_name="reviews-data-insight" # define the bucket name on s3
            bucket = self.read_s3(bucket_name) # read messgaes from s3 buckets
            for json_obj in bucket.objects.all():
                    json_file = "s3://{0}/{1}".format(bucket_name, json_obj.key)
                    for msg in smart_open.smart_open(json_file, encoding='utf8' ):
                        #ts = time.time()
                        #json_str = json.dumps({'message':msg,'timestamp':ts})
                        # print(msg)
                        producer.send("producer", json.dumps(msg)) # define topic name
			producer.flush()
                        print(msg)

        def read_s3(self,bucket_name):
                s3 = boto3.resource('s3')

                try:
                        s3.meta.client.head_bucket(Bucket=bucket_name)
                except botocore.exceptions.ClientError as e:
                        return None
                else:
                        return s3.Bucket(bucket_name)

def main():
        producer = Producer()
        producer.daemon = True
        producer.start()
        while True:
                time.sleep(0.00002) # read from producer every __ seconds

if __name__ == "__main__":
        main()
