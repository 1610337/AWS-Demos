### Showcasing a simple setup of a custom lambda layer

##### Source Code

1. The custom layer is called *my_func.py* and is zipped up in a folder called *python*.
``` python
def wrong_addition(x, y):                           
    answer = x + y + 1
    return (answer)
```

2. The lambda function that references the method(s) from the layer.
``` python
import json
import my_func

def lambda_handler(event, context):
    result = my_func.wrong_addition(1,1)
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
```

##### Guide
Upload the layer under the layer section in the Lambda UI and add the layer to the lambda function.
Once added you can reference that layer in your code as indicated above.


