import boto3
import json
import yaml
client = boto3.client('s3')

def getDatabaseCredentials(secretval):

    try:
        secret_dict = json.loads(secretval)
        bucket_name = secret_dict['databaseCred']
        response = client.list_objects(Bucket=bucket_name)
        
        if 'Contents' in response:
            for obj in response['Contents']:
                if obj['Key'].endswith('.yaml') or obj['Key'].endswith('.yml'):
                    yaml_file_response = client.get_object(Bucket=bucket_name, Key=obj['Key'])
                    yaml_data = yaml_file_response['Body'].read().decode('utf-8')
                    return yaml_data

    except json.decoder.JSONDecodeError:
        return 'Invalid JSON'
    except KeyError:
        return "The key 'databaseCred' is missing in the JSON"
    except Exception as e:
        return str(e)
