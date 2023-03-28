import boto3

def read_object_from_s3(bucket_name, object_key):
    """
    Downloads an object from S3 given the bucket name and object key provided as arguments.
    Returns the downloaded object data as bytes.
    """
    # create S3 client
    s3_client = boto3.client('s3')
    
    # read object data
    object_data = s3_client.get_object(Bucket=bucket_name, Key=object_key)['Body'].read()
    
    return object_data

if __name__ == '__main__':
    # set bucket name and object key
    bucket_name = 'my-bucket'
    object_key = 'example_file.txt'

    # download file from S3 bucket
    file_contents = read_object_from_s3(bucket_name, object_key)

    # write file to disk
    with open('downloaded_file.txt', 'wb') as file:
        file.write(file_contents)

    # print success message
    print('File downloaded successfully')