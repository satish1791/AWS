import json
#psycopg2 library to connect to a PostgreSQL database and execute SQL queries
# to retrieve and activate subscriptions
import psycopg2

#event object passed to the Lambda function by the API Gateway. It contains 
# information about the HTTP request, such as the HTTP method, headers, 
# and request body (if present).
#The context object passed to the Lambda function by the AWS Lambda runtime. It 
# contains information about the execution environment, such as the AWS request ID
# and function name
def handler(event, context):
    http_method = event['httpMethod']
    if http_method == 'GET':
        # Handle GET requests
#The ID of the device for which to retrieve or activate the subscription
        device_id = event['queryStringParameters']['device_id']
#status of the subscription for the specified device_id. This is retrieved from 
# the database using the get_subscription_status function.
        subscription_status = get_subscription_status(device_id)
        response = {
            'statusCode': 200,
            'body': json.dumps({'subscription_status': subscription_status})
        }
    elif http_method == 'POST':
        # Handle POST requests
        request_body = json.loads(event['body'])
        device_id = request_body['device_id']
#parameters needed to activate a subscription.
        subscription_type = request_body['subscription_type']
#The type of subscription to activate for the specified device_id. This is 
# extracted from the request body of a POST request.        
        activate_subscription(device_id, subscription_type)
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Subscription activated successfully'})
        }
    else:
        # Handle other requests
        response = {
            'statusCode': 405,
            'body': json.dumps({'message': 'Method not allowed'})
        }

    return response

#The get_subscription_status function executes a SELECT query to retrieve the 
# subscription status for the specified device_id, and the activate_subscription
# function executes an INSERT query to activate the subscription for the specified
# device_id and subscription_type.
def get_subscription_status(device_id):
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host="db.testautomation.com",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    # Execute SELECT query
    cur = conn.cursor()
    cur.execute("SELECT subscription_status FROM subscriptions WHERE device_id=%s", (device_id,))
    # Fetch result and close connection
    subscription_status = cur.fetchone()[0]
    cur.close()
    conn.close()
    return subscription_status

def activate_subscription(device_id, subscription_type):
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host="db.testautomation.com",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    # Execute INSERT query
    cur = conn.cursor()
    cur.execute("INSERT INTO subscriptions (device_id, subscription_type, subscription_status) VALUES (%s, %s, 'active')", (device_id, subscription_type))
    conn.commit()
    # Close connection
    cur.close()
    conn.close()
