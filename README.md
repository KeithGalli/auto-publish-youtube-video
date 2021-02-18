## Overview

This is the source code that if zipped and uploaded to an AWS Lambda function, can automatically publish a video when it hits 1000 subscribers.

## Setup

### 1. Get Code Locally

To access all of the files I recommend you fork this repo and then clone it locally. Instructions on how to do this can be found here: https://help.github.com/en/github/getting-started-with-github/fork-a-repo

The other option is to click the green "clone or download" button and then click "Download ZIP". You then should extract all of the files to the location you want to edit your code.

### 2. Get YouTube API Credentials

I recommend following along with Corey Schafer's [YouTube API OAuth Tutorial](https://youtu.be/vQQEaSnQ_bs) to set yourself up with the proper credentials to access the API.

Once you have your credentials, I encourage you to play around with the YouTube API functionality using the API documentation as reference. This will help you see what your possibilities are :).

You will need to save your user_credentials.json file & your token.pickle file to the directory where you have saved the code from this repo locally.

Environment variables defined in this code will need to be set/replaced with your own values.

### 3. Upload code to Lambda

Follow along with my [Schedule & Automatically Run Python Code](https://youtu.be/aqnJvXOIr6g) tutorial to learn the basic on creating a Lambda Function.

It will also be beneficial to play around with boto3 library in Lambda a bit before attempting to upload this code to your function.

Install the YouTube API Libraries locally by running the following command in your project folder:

``` pip install -r requirements.txt -t ./resources ```

Zip the files in your resources folder with your source code files and upload resulting zip package to Lambda (this is also demonstrated in my [Schedule & Automatically Run Python Code](https://youtu.be/aqnJvXOIr6g) tutorial)

Enjoy!
