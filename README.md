# AWS CDK Serverless Data Pipeline

A serverless data pipeline in AWS using the AWS Cloud Development Kit (CDK). 
Easily provision and orchestrate AWS services to build scalable, reliable, and cost-effective data pipelines for your applications.

## Table of Contents
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Requirements](#requirements)
- [Usage](#usage)
  - [CDK Commands](##cdk-commands)
  - [Cleanup](##cleanup)
- [Tools Used](#tools-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, follow these steps:

1. **Install AWS CLI**:

   If you haven't already, you'll need to install the AWS Command Line Interface (CLI). You can download and install it from the [official AWS CLI documentation](https://aws.amazon.com/cli/).

2. **Install Python**:

   This project requires Python to run. You can download the latest version of Python from the [official Python website](https://www.python.org/downloads/). Make sure to add Python to your system's PATH during installation.

3. **Install Node.js and npm**:

   The AWS CDK requires Node.js and npm (Node Package Manager). You can download and install them from the [official Node.js website](https://nodejs.org/).

4. **Install AWS CDK**:

   You need to install the AWS Cloud Development Kit (CDK) globally using npm. Run the following command:

   ```bash
   npm install -g aws-cdk
   ```

5. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-project.git
   ```

6. Install the required Python dependencies using pip:

   ```bash
   cd your-project
   pip install -r requirements.txt
   ```

## Prerequisites

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

   ```
   bash
   $ python3 -m venv .venv
   ```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

   ```
   bash
   $ source .venv/bin/activate
   ```

If you are a Windows platform, you would activate the virtualenv like this:

   ```
   bash
   % .venv\Scripts\activate.bat

## Requirements

Make sure you have the following dependencies installed before running the project:

- [aws-cdk-lib](https://pypi.org/project/aws-cdk-lib/): Version 2.81.0
- [constructs](https://pypi.org/project/constructs/): Version >=10.0.0,<11.0.0
- [boto3](https://pypi.org/project/boto3/): (latest version)

You can install them using the following command:

   ```bash
   cd aws-cdk-serverless-data-pipeline
   pip install -r requirements.txt
   ```

## Usage

### CDK Commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

After setting up the project, you can use the AWS CDK commands to manage your deployment.

- **Synthesize CloudFormation Templates**:

   To generate CloudFormation templates for your CDK app, use the following command:

   ```bash
   cdk synth
   ```

- **Review Changes Before Deploying**:

   Before deploying changes, you can preview the changes using:

   ```bash
   cdk diff
   ```

- **Deploy Your Stack**:

   To deploy your stack and create AWS resources, run:

   ```bash
   cdk deploy
   ```

### Cleanup

To remove the AWS resources created by the CDK stack, you can use the following command:

   ```bash
   cdk destroy
   ```

Make sure to review and confirm the changes before proceeding with the destroy command.

## Tools Used

This project leverages several tools and technologies to streamline data processing workflows:

- **AWS CDK**: The AWS Cloud Development Kit is used to define and provision AWS infrastructure resources programmatically. With AWS CDK, you can use familiar programming languages to model your cloud resources.

- **Amazon DynamoDB**: DynamoDB is a fully managed NoSQL database service by AWS. In this project, it is used to store and manage structured data efficiently.

- **AWS Lambda**: AWS Lambda is a serverless compute service that allows you to run code in response to events. Lambda functions are used for data processing and event-driven architecture.

- **Amazon S3**: Amazon Simple Storage Service (S3) is a scalable object storage service. In this project, it is used for data storage and archiving.

- **AWS CLI**: The AWS Command Line Interface is a unified tool to manage AWS services from the command line. It's used for interacting with AWS resources, including provisioning and deploying.

These tools, along with the AWS CDK constructs, provide a powerful and scalable foundation for building and managing serverless data pipelines in AWS.


## Contributing
Contributions to this project are welcome! If you have ideas for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the GNU license - see the [LICENSE](https://github.com/collective/example.p4p5/blob/master/LICENSE.GPL) file for details.

```

This updated README.md includes information on CDK commands for managing deployments and a section on cleaning up AWS resources using `cdk destroy`. Adjust the placeholders and details as needed for your specific project.