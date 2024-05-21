import boto3
import os
import subprocess
import psycopg2

# Configure AWS credentials
session = boto3.Session(profile_name='default')
s3 = session.client('s3')
rds = session.client('rds', region_name='us-east-1')  # Replace with your AWS region

# AWS S3 configurations
s3_bucket_name = 'bucket-assign-unique123'
s3_object_key = 's3://bucket-assign-unique123/WinfexStoreData.xlsx'

# AWS RDS configurations
rds_endpoint = 'mydb.c962ysc6eunu.us-east-1.rds.amazonaws.com'  # Replace with your RDS endpoint
rds_database = 'mydb'  # Replace with your RDS database name
rds_user = 'admin'  # Replace with your RDS user
rds_password = 'password!123'  # Replace with your RDS password

def read_from_s3():
    try:
        response = s3.get_object(Bucket=s3_bucket_name, Key=s3_object_key.split('://')[1])
        data = response['Body'].read().decode('utf-8')
        return data
    except Exception as e:
        print(f"Error reading from S3: {e}")
        return None

def push_to_rds(data):
    try:
        conn = psycopg2.connect(
            host=rds_endpoint,
            database=rds_database,
            user=rds_user,
            password=rds_password
        )
        cur = conn.cursor()
        # Use the data and insert/update records in your RDS table
        # Example: cur.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", (data1, data2))
        conn.commit()
        cur.close()
        print("Data pushed to RDS successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error pushing to RDS: {error}")
    finally:
        if conn is not None:
            conn.close()

def lambda_handler(event, context):
    data = read_from_s3()
    if data:
        push_to_rds(data)
    else:
        print("No data to process")