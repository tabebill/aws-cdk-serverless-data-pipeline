import json
import boto3
import os

def handler(event, context):
    try:
        # Get the newly created items from the DynamoDB event
        records = event['Records']
        
        # Extract the necessary data from each record
        items = []
        for record in records:
            if record['eventName'] == 'INSERT':
                items.append(record['dynamodb']['NewImage'])
        
        # Prepare the CSV content
        csv_content = ""
        for item in items:
            csv_values = []
            for value in item.values():
                if 'S' in value:
                    csv_values.append(str(value['S']))
                elif 'N' in value:
                    csv_values.append(str(value['N']))
            csv_content += ','.join(csv_values) + '\n'
        
        # Write the CSV content to the backup file in S3
        s3_client = boto3.client('s3')
        bucket_name = os.environ['BUCKET_NAME']
        file_name = os.environ['CSV_FILE_NAME']
        
        # Check if the file already exists in the bucket
        try:
            s3_client.head_object(Bucket=bucket_name, Key=file_name)
            file_exists = True
        except:
            file_exists = False
        
        # If the file doesn't exist, create it
        if not file_exists:
            s3_client.put_object(
                Body='',
                Bucket=bucket_name,
                Key=file_name
            )
        
        # Append the CSV content to the backup file
        s3_client.put_object(
            Body=csv_content,
            Bucket=bucket_name,
            Key=file_name,
            ACL='bucket-owner-full-control',
            ContentType='text/csv'
        )
        
        return {
            'statusCode': 200,
            'body': 'Function executed successfully'
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Function execution failed: {str(e)}'
        }
