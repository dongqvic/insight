# oltp_olap_monitoring: Monitoring a real-time OLTP to OLAP data pipeline

# Business Cases:
Imagining an e-commerce website like Amazon, Spring, eBay storing everything in one databse, eg PostgreSQL for faster transaction purposes(Read/Write). During BlackFriday, customers who want search gifts are sending queries to PostgreSQL database while Data scientists who wanna predict real-time shopping trends also sending queries to the database. HIGH Stress to the OLTP database!

# Solution:
Syncronizing OLTP database(eg.PostgreSQL) with OLAP database(Amazon Redshift) in real-time and make sure the health condition of the pipeline by setting up monitoring system.

# Architecture: Basic: Kafka --> PostgreSQL --> kafka --> Redshift

# Solution steps:

1. Dataset: Amazon Review Dataset in .json.gz, stored in S3
 - Schema: reviewID, asin(productID), reviewerName, reviewText, helpful, overallrating, reviewTime

2. Set up 2 databases: PostgreSQL and Redshift, host them with EC2 x 2 ( 1 master, 1 worker).

3. Host 2 kafka with EC2 x 2.

4. Monitor the overall health of the system, visualize the monitoring results. 
Including:
- Kafka: server, producer, consumer, broker, zookeeper
- EC2 server behavior(Cloudwatch) [set up alert]
- PostgreSQL: Read&Write query throughput and performance, replication, resource utilization
- Redshift: query/time, query/wait/time, segment/scan/pending, query/success/count, query/failed/count

5. Analysis the failure scenarios of the data pipeline, auto-recovery if possible.
Possible failure scenarios & Auto-recovery:
- EC2 hosting PostgreSQL down ( using Airflow to scheduling batch processing for datastreams during down time)
- Kafka streams fail(Implementing a resilient Kafka cluster) : All/parts clusters are down

6. Aggregate the metrics data (also real-time) from Prometheus and Cloudwatch on Graphana, do analytics and visualization.

