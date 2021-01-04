# GVE_Devnet_ResponsiveWebexBot

| :exclamation:  External repository notice   |
|:---------------------------|
| This repository is now mirrored at "PLEASE UPDATE HERE - add External repo URL after code review is completed"  Please inform a https://github.com/gve-sw/ organization admin of any changes to mirror them to the external repo |
## Contacts
* Eda Akturk (eakturk@cisco.com)

## Solution Components
*  Python 3.8
*  Cisco Webex
* MongoDB

## Installation/Configuration

#### Clone the repo :
```$ git clone (link)```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

Now you have your virtual environment setup and ready

#### Install the libraries :

```$ pip install -r requirements.txt```


## Setup: 

*Create Cisco Webex Bot*
1. Create a Webex Chatbot from https://developer.webex.com/my-apps/new/bot.

2. Add your Bot Token to env_var 
```
bot_token = " "
```

*Connect to Database*
3. Download and install MongoDb. 

4. Create collection in your MongoDb. 

5. Add Database, Cluster and Collection variables to env_var. 
```
Database = " "
Cluster = " "
Collection = " "
```

*Webhook Receiver*

6. You need a web server that will receive the webhooks from Webex in order to reply and save the responses. Add your webhook reciver to env_var. Heroku (https://www.heroku.com/), Pythonanywhere (https://www.pythonanywhere.com/) are options that can be used. 
```
target_url = " "
```

*Create Webhooks*

7. Webhooks need to be created for Webex in order for the Bot to recive replies from users. Documentation on webhooks can be found [here.](https://developer.webex.com/docs/api/v1/webhooks)

8. Run the function "create_webhook" from app.py on you python console. 
```
create_webhook()
```

9. When you want to remove the webhook you can run the delete_webhooks function  from app.py on you python console which will delete all the existing webhooks. 

```
delete_webhooks()
```

## Usage: 

Create your json file for the notification. More details on Webex Cards can be found [here.](https://developer.webex.com/docs/api/guides/cards) 

In order to send the card to list of poeple from the database run the "send_notification" function. 

```
send_notification()
```

# Screenshots

![/IMAGES/bot_message.png](/IMAGES/bot_message.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
