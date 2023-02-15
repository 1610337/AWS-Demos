%flink.ssql(type=update);

DROP TABLE IF EXISTS main_table;
CREATE TABLE main_table (
    user_id INTEGER,
    device_id VARCHAR(10),
    client_event VARCHAR(10),
    client_timestamp TIMESTAMP(3), --VARCHAR(32)
    WATERMARK FOR client_timestamp AS client_timestamp - INTERVAL '5' SECOND
)
PARTITIONED BY (user_id)
WITH (
    'connector' = 'kinesis',
    'stream' = 'SOURCE_STREAM',
    'aws.region' = 'us-east-1',
    'scan.stream.initpos' = 'LATEST',
    'format' = 'json',
    'json.timestamp-format.standard' = 'ISO-8601'
);


SELECT window_start, window_end, client_event, COUNT(client_event) as no_of_clicks
FROM TABLE(
TUMBLE(TABLE main_table, DESCRIPTOR(client_timestamp), INTERVAL '1' MINUTES))
GROUP BY client_event, window_start, window_end;