import runpy
import boto3
import os

S3_BUCKET_NAME = os.getenv('BUCKET_NAME')
S3_FILE_PATH = os.getenv('FILE_PATH')

s3_client = boto3.client('s3')

def get_file_name(file_path):
    
    dirs = file_path.split('/')
    
    return dirs[-1]

def handler(event, context):
    
    file_name = get_file_name(S3_FILE_PATH)
    file_lambda_path = '/tmp/' + file_name
    
    s3_client.download_file(S3_BUCKET_NAME, S3_FILE_PATH, file_lambda_path)
    
    runpy.run_path(file_lambda_path)