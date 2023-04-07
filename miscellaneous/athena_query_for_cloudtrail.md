
Query all API calls from IAM user Alice from CloudTrail Logs in S3 within a specific time

``` sql
SELECT eventName
FROM cloudtrail_logs_cloudtrail_ORIGIN
WHERE useridentity.username = 'Alice'
and eventtime >= '2023-01-10T00:00:00Z'
and eventtime < '2023-01-11T00:00:00Z'
GROUP BY eventName;
```