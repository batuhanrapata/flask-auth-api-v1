import requests
import os
import random
import string
from bson.objectid import ObjectId
from resources.db import get_db


col=get_db("user")


api_key = os.environ.get("MAILGUN_API_KEY")
domain = os.environ.get("MAILGUN_DOMAIN")


def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))


def send_reset_mail(email,user_id):
    otp = generate_otp()
    requests.post(
        "https://api.mailgun.net/v3/sandboxa49efa1327944ef6bfcaa532f41b6130.mailgun.org/messages",
        auth=("api", api_key),
        data={"from": "Mailgun Sandbox <postmaster@sandboxa49efa1327944ef6bfcaa532f41b6130.mailgun.org>",
              "to": [email],
              "subject": "Your OTP is " + otp + "",
              "template": "otp",
              "h:X-Mailgun-Variables": '{ "code" : "' + otp + '"}'})
    #current user otp to db
    col.update_one({'_id': ObjectId(user_id)}, {'$set': {'otp': otp}})



def verify_reset_otp(sender_otp,user_id):
    return sender_otp==col.find_one({'_id': ObjectId(user_id)})['otp']
