import pandas as pd
import boto3

s3_client = boto3.client("s3")
sns_client = boto3.client("sns")
sns_arn = "arn:aws:sns:ap-south-1:231066899898:sns-topic-first"
def lambda_handler(event, context):
    print(event)
    try:
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        s3_file_key = event["Records"][0]["s3"]["object"]["key"]
        print(bucket_name)
        print(s3_file_key)
        res = s3_client.get_object(Bucket = bucket_name, Key = s3_file_key)
        print(res["Body"])
        df_s3_data = pd.read_csv(res["Body"] , sep=",")
        print(df_s3_data.head())
        msg = "Input S3 file processed Successfully"
        response = sns_client.publish(TargetArn = sns_arn , Message = msg, MessageStructure = "text")
        
    except Exception as err:
        print(err)
        msg = "Input S3 file processing f"
        response = sns_client.publish(TargetArn = sns_arn , Message = msg, MessageStructure = "text")
