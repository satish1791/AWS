#Create an AWS Lambda function using AWS CLI: First, we need to create an AWS Lambda function to host the subscription microservice 

aws lambda create-function --function-name subscription-microservice --runtime
python3.8 --handler app.handler --memory-size 128 --timeout 30 --zip-file 
fileb://subscription-microservice.zip

#create an API Gateway REST API to route incoming requests to the Lambda function. 
#We can also do this using the AWS Management Console or the AWS CLI.

aws apigateway create-rest-api --name subscription-microservice

#create a resource and method in the API to route requests to the Lambda function.

aws apigateway create-resource --rest-api-id vaz7da96z6 --parent-id root
--path-part subscription
aws apigateway put-method --rest-api-id vaz7da96z6 --resource-id 6sxz2j
--http-method GET --authorization-type NONE
aws apigateway put-integration --rest-api-id vaz7da96z6 --resource-id 
6sxz2j --http-method GET --type AWS_PROXY --integration-http-method POST --uri arn:aws:apigateway:eu-central-1:lambda:path/2022-12-31/functions/arn:aws:lambda:eu-central-1:123456789012:function:subscription-microservice/invocations

#deploy the API to make it publicly accessible
aws apigateway create-deployment --rest-api-id vaz7da96z6--stage-name production

#to update the Lambda function code to handle requests from the API Gateway REST API

After running these commands, you should have a new API Gateway endpoint at a URL like https://vaz7da96z6.execute-api.eu-central-1.amazonaws.com/production/subscription

