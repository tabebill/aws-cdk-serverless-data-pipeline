from aws_cdk import (
    App,
    Stack,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_s3 as s3,
    aws_iam as iam,
    aws_lambda_event_sources as lambda_event_sources
)
from constructs import Construct 

class TestCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the S3 bucket
        backup_bucket = s3.Bucket(
            self, 'backup'
        )

        # Create the IAM role
        lambda_role = iam.Role(
            self, 'LambdaRole',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole')
            ]
        )

        # Create a Lambda function construct
        lambda_function = _lambda.Function(
            self, 'MyLambdaFunction',
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler='index.handler',
            role=lambda_role,
            environment={
                'BUCKET_NAME': backup_bucket.bucket_name,
                'CSV_FILE_NAME': 'backup.csv'
            },
            code=_lambda.Code.from_asset('lambda')
        )

        # Add S3 permissions to the Lambda IAM role
        lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    's3:GetObject',
                    's3:PutObject'
                ],
                resources=[backup_bucket.bucket_arn + '/*']
            )
        )

        # Create the DynamoDB table
        dynamodb_table = dynamodb.Table(
            self, 'MyTable',
            table_name='my_table',
            partition_key=dynamodb.Attribute(name='id', type=dynamodb.AttributeType.STRING),
            stream=dynamodb.StreamViewType.NEW_IMAGE
        )

        # Add DynamoDB table stream as an event source for the Lambda function
        lambda_function.add_event_source(
            lambda_event_sources.DynamoEventSource(
                table=dynamodb_table,
                starting_position=_lambda.StartingPosition.LATEST
            )
        )

app = App()
TestCdkStack(app, "TestCdkStack",)
app.synth()
