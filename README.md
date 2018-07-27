# oltp_olap_monitoring
Monitoring a real-time OLTP to OLAP data pipeline

- When companies want to run analytics on transactions in real-time, the overall health of the pipeline needs to be monitored and the failure scenarios needs to be handled.

- Solution steps:

1. Generate e-commerce datasets in real-time.

2. Set up 2 databases in PostgreSQL and Druid, host them with EC2 on AWS.

3. Build a pipeline connects by Kafka.

4. Monitor the overall health of the system, visualize the monitoring results. 
To be more specific:
- Kafka: server, producer, consumer, broker
- EC2(Cloudwatch)
- PostgreSQL: Read&Write query throughput and performance, replication, resource utilization
- Druid: query/time, query/wait/time, segment/scan/pending, query/success/count, query/failed/count

5. Analysis the failure scenarios of the data pipeline, auto-recovery if possible.
Possible failure scenarios & Auto-recovery:
- EC2 down
- Kafka streams fail( Implementing a resilient Kafka cluster) : All/parts clusters are down

6. Aggregate the metrics data (also real-time) from Prometheus and Cloudwatch on Graphana, do analytics and visualization.
