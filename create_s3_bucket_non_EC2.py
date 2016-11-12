#!/usr/bin/python
from boto3.session import Session
import boto3

session = Session(aws_access_key_id='AKIAJHXEMWF22W2ECNUA', aws_secret_access_key='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')

s3 = session.resource('s3')

## create a connection to boto3

s3.create_bucket(Bucket='anuraglatestbucket-2')
