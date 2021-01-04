import json
from webexteamssdk import WebexTeamsAPI, Webhook
from flask import Flask, request

from env_var import Database, Cluster, Collection, bot_token, target_url
from pymongo import MongoClient

app = Flask(__name__)

api = WebexTeamsAPI(access_token=bot_token)

def get_employees():
    """
    Connect to database and get employee list
    """
    cluster = MongoClient(Database)
    db = cluster[Cluster]
    collection = db[Collection]
    employees = list(collection.find())
    return employees

def get_json_card(filepath):
    """
    Get content of Json card
    """
    with open(filepath, 'r') as f:
        json_card = json.loads(f.read())
        f.close()
    return json_card


def send_notification():
    """
    Send adaptive card notification in webex teams to all employees
    """
    for e in get_employees():
        to = e["email"]
        print(to)
        api.messages.create(
            toPersonEmail=to,
            text="Card Message: If you see this your client cannot render cards",
            attachments=[{
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": get_json_card("card.json")
            }],
        )


def create_webhook():
    """
    Create the Webex Teams webhooks we need for our bot
    """
    print("Creating Message Created Webhook...")
    webhook = api.webhooks.create(
        name = "Test webhook",
        resource = "attachmentActions",
        event="created",
        targetUrl= target_url
    )
    return webhook


def delete_webhooks():
    """
    List all webhooks and delete the webhooks
    """
    for webhook in api.webhooks.list():
        print("Deleting Webhook:", webhook.name, webhook.targetUrl)
        api.webhooks.delete(webhook.id)
    return "All webhooks have been deleted"


@app.route('/webhook', methods=['POST'])
def webhook_received():
    """
    Recieve the card responses
    """
    if request.method == 'POST':
        webhook = Webhook(request.json)
        respond_to_button_press(webhook)
    return "Webhook Recieved", 200


def respond_to_button_press(webhook):
    """
    Respond to a button press on the card we posted
    """
    room = api.rooms.get(webhook.data.roomId)
    attachment_action = api.attachment_actions.get(webhook.data.id)
    response = dict(attachment_action.inputs)
    selection = response["selection"]
    try:
        comment = response["comment"]
    except:
        comment = " "
        
    person = api.people.get(webhook.data.personId)
    person_email = person.emails #can be used to save response to database
    
    message_id = attachment_action.messageId
    api.messages.create(
        room.id,
        parentId=message_id,
        markdown= "Thanks for your feedback! We have saved your response"
    )
