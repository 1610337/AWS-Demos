
## **Distributed Load Testing on a Lambda function**

#### **Purpose of this repository:**
This project shows a quick way how to load test AWS Lambda as a service. That should allow us to understand Lambda concurrency limits (and how they can go up) and error handling of applications.

To do this small experiment we need two things: an application (on Lambda) to test and a tool for loadtests.


#### **Application to test**
In `/loadTestLambda` you can find the application we want to test. A simple Lambda function with a variable execution time exposed by an HTTP Endpoint through the API Gateway.
The result of that deployment should give you the Endpoint to test.

#### **Tool for Loadtests**
In `/deployTestingFramwork` you can find the tool I used to perform loadtests and some more information around it.


#### **Test result examples**
Below you can find some screenshots of some of the metrics during the loadtest. The first 4 screenshots show 2 loadtests that I performed. Feel free to dive deeper into some of the metrics and make your own conclusions. Those 4 screenshots come from a CloudWatch Dashboard which was partially setup by the load testing framework</br>
The last screenshot shows similar metrics from within the loadtesting application. </br> 

Average Response time             |  Concurrent Executions
:-------------------------:|:-------------------------:
![](images/avg_response_time.jpg)  |  ![](images/concurrent_executions.jpg )

Failed Lambdas             |  Successful Lambdas
:-------------------------:|:-------------------------:
![](images/failures.jpg)  |  ![](images/success.jpg )


![Setup](images/simple_test_results.jpg "Setup")
*Screenshot of LoadTesting Framework for the first load test (Lambda execution time was set to 2.5 seconds)*

