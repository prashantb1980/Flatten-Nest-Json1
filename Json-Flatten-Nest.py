import json
import flatten_json as ls

def lambda_handler(event, context):

    
    #fetch the event body that has the input json coming from the website
    
    json_body = event['body']
    
    #Converts string to Json python dictionary
    json_body1 = json.loads(json_body)
    
    #invoke the flatten built in function.
    if event['requestContext'] ['stage' ] == 'Flatten' :
        output_json = ls.flatten(json_body1,".")
        
    if event['requestContext'] ['stage' ] == 'Nest' :
        output_json = ls.unflatten(json_body1,".")

    response = {
        'isBase64Encoded': False,
        'statusCode': 200, 
        'headers': { 
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
        },
        'body': json.dumps(output_json)  
        }
 
    return response 