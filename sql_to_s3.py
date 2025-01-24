import pandas as pd
import pymysql
import boto3

# Database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='havefun1783',
    database='fortinos_s1_retail'
)

# SQL Query to fetch data for store 1 and January 2023
query = """
SELECT 
    *
FROM 
    Orders
WHERE 
    (OrderDate >= '2023-01-01' AND OrderDate <= '2023-01-31')
    AND 
    (storeID = 's1');
"""

# Execute query and load data into a DataFrame
with connection.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=columns)

# Close the database connection
connection.close()

# Save DataFrame to CSV
output_file = 'jan2023_s1.csv'
df.to_csv(output_file, index=False)

# S3 upload
bucket_name = 's1-ontario-ca-central-1'
folder_name = '2023/'
s3_file_name = f"{folder_name}{output_file}"

# Initialize Boto3 S3 client
s3 = boto3.client('s3')

try:
    # Upload file to S3
    s3.upload_file(output_file, bucket_name, s3_file_name)
    print(f"File uploaded successfully to {bucket_name}/{s3_file_name}")
except Exception as e:
    print(f"Error uploading file: {e}")
