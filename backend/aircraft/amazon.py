import boto3

# https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html
# https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-python-example_code-sns.html

client = None
# f = open("backend_keys.txt", "r")
# key_id = f.readline().rstrip('\n')
# access_key = f.readline().rstrip('\n')
# print(key_id)
# print(access_key)

def init_sms():
    f = open("backend_keys.txt", "r")
    key_id = f.readline().rstrip('\n')
    access_key = f.readline().rstrip('\n')

    # Create an SNS client
    global client
    client = boto3.client(
        "sns",
        aws_access_key_id=key_id,
        aws_secret_access_key=access_key,
        region_name="us-west-2"
    )

def send_sms(msg):

    # Send your sms message.
    client.publish(
        PhoneNumber="+11111111111",
        Message=msg
    )

init_sms()
msg = "an aircraft was detected nearby"
send_sms(msg)