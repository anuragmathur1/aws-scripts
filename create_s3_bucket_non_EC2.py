#!/usr/bin/python
from boto3.session import Session
import boto3

session = Session(aws_access_key_id='xxxxxxxxxx', aws_secret_access_key='xxxxxxxxxx')

s3 = session.resource('s3')

## create a connection to boto3

s3.create_bucket(Bucket='anuraglatestbucket-2')
