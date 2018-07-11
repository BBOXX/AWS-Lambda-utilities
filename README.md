# Aim of this project

The aim of this project is to provide utilities to speep up development of python projects using aws lambda by reducing the update of the lambda function to one command.
This is particularly useful for projects that require several iterations of deployment which would make building the zip package as required by aws a painful and repetitive task.
The main functionality offered is the automatic zip package building and update of the lambda function.

## Assumptions

- Your project python files are all at the root of your project folder as required by aws lambda.
- You have IAM access keys with permissions to the Lambda service, needed to configure the aws CLI (not mandatory).
- You have a Lambda function already created for your project.

# Quickstart

## Installation

Clone the repo and copy over the lamda_tools directory and its contents at the root of your project (your_project/lambda_tools)

If you have not done so, you will need to set up aws CLI following these guides from the docs: 
- https://docs.aws.amazon.com/cli/latest/userguide/installing.html
- https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

## Configuration

In the lambda_tools/zipper.py file, you will find several constants that may need to be updated for your project.
Each is explained in the file and should be straightforward to update if necessary.

You will also need to update the shell file lambda_tools/push_function.zip with your lambda function name.

## Usage
If your system is shell file compatible, running the push_function.sh will create the zip package and update the lambda function.

Otherwise, you can cd in the lambda_tools and run:
```
python zipper.py
```
which will create the lambda zip file at the location configured and you can push it via aws CLI or drag and drop it from the lambda service console on their website.


