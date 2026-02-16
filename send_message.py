import requests
import os
import glob
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def send_text_message(to, message, phone_number_id):
    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": message}
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")

def send_message(to, message, phone_number_id):
    oldfileurl = "https://processintelligence.co/wp-content/uploads/2025/09/newsletter_2025_10_15_v1.pdf"
    folder_path = "C:\\PID\\YPCPL\\NewsLetter\\newsletter_pdf\\"
    list_of_files = glob.glob(os.path.join(folder_path, '*.pdf'))
    latest_file = max(list_of_files, key=os.path.getmtime)
    print(f"Sending file latest {latest_file}")
    onefilename = latest_file.replace(folder_path, "")
    print(f"Sending file {onefilename}")
    newfileurl = "https://reptiloid-unrobustly-michal.ngrok-free.dev/get_file/"+onefilename

    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "document",
        "document": {
            "link": newfileurl,
            "caption": message,
            "filename": onefilename
        }
        # "text": {"body": message}
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")

def send_backdated_message(to, message, date1, phone_number_id):
    print(f"Sending backdated message date {date1} to {to}.")
    datetime_object = datetime.strptime(date1, "%d/%m/%Y")
    date_string_yyyymmdd = datetime_object.strftime("%Y_%m_%d")
    print(f"Sending backdated message date_string_yyyymmdd {date_string_yyyymmdd}")
    newfileurl = "https://reptiloid-unrobustly-michal.ngrok-free.dev/get_file/playmaker_pulse_newsletter_"+date_string_yyyymmdd+"_v1.pdf"
    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "document",
        "document": {
            # "link": "https://processintelligence.co/wp-content/uploads/2025/09/newsletter_"+date_string_yyyymmdd+"_v1.pdf",
            "link": newfileurl,
            "caption": message,
            "filename": "newsletter_"+date_string_yyyymmdd+"_v1.pdf"
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")

def send_menu_message(to, message, phone_number_id):
    print("in menu message")

    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "INTERACTIVE",
        "interactive": {
            "type": "list",
            "header": {
                "type": "text",
                "text": "PlayMaker Services"
            },
            "body": {
                "text": message
            },
            "footer": {
                "text": "Tap a menu item to select."
            },
            "action": {
                "button": "View Data Menu",
                "sections": [
                    {
                        "title": "News Letter",
                        "rows": [
                            {
                                "id": "news_letter",
                                "title": "News Letter",  # max 24 char
                                "description": "Get News Letter."
                            }
                        ]
                    },
                    {
                        "title": "Live Data View",
                        "rows": [
                            {
                                "id": "tdy_machine_utilize",
                                "title": "Live Machine Utilization", # max 24 char
                                "description": "Check the Machine Health."
                            },
                            {
                                "id": "tdy_prod_plan",
                                "title": "Live Production Plan",
                                "description": "What will you Produce today."
                            },
                            {
                                "id": "tdy_prod_outage",
                                "title": "Live Production Outages",  # max 24 char
                                "description": "Check the Production Outages."
                            }
                        ]
                    },
                    {
                        "title": "Weekly Data View",
                        "rows": [
                            {
                                "id": "wkly_prediction",
                                "title": "Weekly Predictions",
                                "description": "Weekly Production Predictions."
                            },
                            {
                                "id": "wkly_slippages",
                                "title": "Weekly Slippages",
                                "description": "Check Current weekly Slippages."
                            }
                        ]
                    },
                    {
                        "title": "Monthly Data View",
                        "rows": [
                            {
                                "id": "mntly_blockages",
                                "title": "Monthly Blockages",
                                "description": "Monthly Production Blockages."
                            },
                            {
                                "id": "mntly_output",
                                "title": "Monthly Output",
                                "description": "Check Monthly Production Output."
                            }
                        ]
                    },
                    {
                        "title": "Customer Support",
                        "rows": [
                            {
                                "id": "contact_support",
                                "title": "Contact Support",
                                "description": "Speak with a customer service representative. on +919000000000"
                            },
                            {
                                "id": "faq",
                                "title": "Frequent Questions",
                                "description": "Find answers to common questions."
                            }
                        ]
                    }
                ]
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")


def send_ypcpl_menu_message(to, message, phone_number_id):
    print("in menu message")

    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "INTERACTIVE",
        "interactive": {
            "type": "list",
            "header": {
                "type": "text",
                "text": "PlayMaker Services"
            },
            "body": {
                "text": "Hello! What do you want to view?\n Please select an option from the menu below."
            },
            "footer": {
                "text": "Tap a menu item to select."
            },
            "action": {
                "button": "View Data Menu",
                "sections": [
                    {
                        "title": "Cost Per Part Summary",
                        "rows": [
                            {
                                "id": "cpp_summary",
                                "title": "View Cost Part Summary",  # max 24 char
                                "description": "Get Line Wise cost part summary."
                            }
                        ]
                    },
                    {
                        "title": "Cost Per Part Details",
                        "rows": [
                            {
                                "id": "cppd_main_menu",
                                "title": "Cost Per Part Details",  # max 24 char
                                "description": "Line Wise Cost Per Part Details."
                            }
                        ]
                    },
                    {
                        "title": "Shift Ratings",
                        "rows": [
                            {
                                "id": "shift_ratings",
                                "title": "Shift Ratings",  # max 24 char
                                "description": "Get Shift Ratings."
                            }
                        ]
                    },
                    {
                        "title": "Labour Performance",
                        "rows": [
                            {
                                "id": "lp_main_renew",
                                "title": "Labour Performance",  # max 24 char
                                "description": "Line Wise Labour Performance Details."
                            }
                        ]
                    },
                    {
                        "title": "Electricity Performance",
                        "rows": [
                            {
                                "id": "ep_main_menu",
                                "title": "Electricity Performance",  # max 24 char
                                "description": "Line Wise Electricity Performance Details."
                            }
                        ]
                    },
                    {
                        "title": "Get News Letter",
                        "rows": [
                            {
                                "id": "curr_news_letter",
                                "title": "Current News Letter",  # max 24 char
                                "description": "Get Latest News Letter."
                            },
                            {
                                "id": "news_letter",
                                "title": "Previous News Letter",  # max 24 char
                                "description": "Get Previous News Letter."
                            }
                        ]
                    }
                ]
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")

def send_ypcpl_lp_submenu_message(to, message, phone_number_id):
    print("in menu message")

    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "INTERACTIVE",
        "interactive": {
            "type": "list",
            "header": {
                "type": "text",
                "text": "PlayMaker Services"
            },
            "body": {
                "text": message
            },
            "footer": {
                "text": "Tap a menu item to select."
            },
            "action": {
                "button": "LP Sub Menu",
                "sections": [
                    {
                        "title": "Labour Performance",
                        "rows": [
                            {
                                "id": "lp_renew",
                                "title": "RE-NewStyling",  # max 24 char
                                "description": "RE-NewStyling Labour Performance Details."
                            },
                            {
                                "id": "lp_maxima",
                                "title": "Maxima",
                                "description": "Maxima Labour Performance Details."
                            }
                            ,
                            {
                                "id": "lp_zug",
                                "title": "ZUG",  # max 24 char
                                "description": "ZUG Labour Performance Details."
                            }
                        ]
                    }
                ]
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")


def send_ypcpl_ep_submenu_message(to, message, phone_number_id):
    print("in menu message")

    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "INTERACTIVE",
        "interactive": {
            "type": "list",
            "header": {
                "type": "text",
                "text": "PlayMaker Services"
            },
            "body": {
                "text": message
            },
            "footer": {
                "text": "Tap a menu item to select."
            },
            "action": {
                "button": "EP Sub Menu",
                "sections": [
                    {
                        "title": "Electricity Performance",
                        "rows": [
                            {
                                "id": "ep_renew",
                                "title": "RE-NewStyling",  # max 24 char
                                "description": "RE-NewStyling Electricity Performance Details."
                            },
                            {
                                "id": "ep_maxima",
                                "title": "Maxima",
                                "description": "Maxima Electricity Performance Details."
                            },
                            {
                                "id": "ep_zug",
                                "title": "ZUG",  # max 24 char
                                "description": "ZUG Electricity Performance Details."
                            }
                        ]
                    },
                ]
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")


def send_ypcpl_cppd_submenu_message(to, message, phone_number_id):
    print("in menu message")

    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "INTERACTIVE",
        "interactive": {
            "type": "list",
            "header":
                {
                "type": "text",
                "text": "PlayMaker Services"
            },
            "body": {
                "text": message
            },
            "footer": {
                "text": "Tap a menu item to select."
            },
            "action": {
                "button": "CPPD Sub Menu",
                "sections": [
                    {
                        "title": "Cost Per Part Details",
                        "rows": [
                            {
                                "id": "cppd_renew",
                                "title": "RE-NewStyling",  # max 24 char
                                "description": "RE-NewStyling Cost Per Part Details."
                            },
                            {
                                "id": "cppd_maxima",
                                "title": "Maxima",
                                "description": "Maxima Cost Per Part Details."
                            },
                            {
                                "id": "cppd_zug",
                                "title": "ZUG",  # max 24 char
                                "description": "ZUG Cost Per Part Details."
                            }
                        ]
                    },
                ]
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")


def send_carousel_message(to, message, phone_number_id):
    print("in send_carousel_message")
    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": to,
    "category": "SERVICE",
    "type": "template",
    "template": {
        "name": "carousel_template_media_cards_v1",
        "language": {
            "code": "en_US"
        }
    },
    "components": [{
            "type": "BODY",
            "text": "Rare succulents for sale! {{1}}, add these unique plants to your collection.",
            "example": {
                "body_text": [
                    [
                        "Pablo"
                    ]
                ]
            }
        },
        {
            "type": "CAROUSEL",
            "cards": [

                {
                    "components": [{
                        "type": "HEADER",
                        "format": "PRODUCT"
                    },

                        {
                            "type": "buttons",
                            "buttons": [

                                {
                                    "type": "spm",
                                    "text": "View"
                                }

                            ]
                        }
                    ]
                },
                {
                    "components": [{
                        "type": "HEADER",
                        "format": "PRODUCT"
                    },

                        {
                            "type": "buttons",
                            "buttons": [

                                {
                                    "type": "spm",
                                    "text": "View"
                                }

                            ]
                        }
                    ]
                },
                {
                    "components": [{
                        "type": "HEADER",
                        "format": "PRODUCT"
                    },

                        {
                            "type": "buttons",
                            "buttons": [

                                {
                                    "type": "spm",
                                    "text": "View"
                                }

                            ]
                        }
                    ]
                }

            ]
        }
    ]
  }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")


def send_flow_message(to, message, phone_number_id):
    print("in send_flow_message")
    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": to,
    "type": "interactive",
        "interactive": {
            "type": "flow",
            "header": {
                "type": "text",
                "text": "Flow message header"
            },
            "body": {
                "text": "Flow message body"
            },
            "footer": {
                "text": "Flow message footer"
            },
            "action": {
                "name": "main",
                "parameters": {
                                  "flow_message_version": "3",
                                  "flow_name": "main",
                "flow_cta": "Book!"
            }
        }
    }
         # end interactive
  }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message to {to}. Response: {response.status_code} {response.text}")
    else:
        print(f"Message sent to {to}.")
