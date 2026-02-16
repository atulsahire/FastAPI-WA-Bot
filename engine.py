from send_message import send_message, send_text_message, send_menu_message, send_ypcpl_menu_message, \
    send_ypcpl_lp_submenu_message, send_ypcpl_ep_submenu_message, send_ypcpl_cppd_submenu_message, \
    send_backdated_message, send_carousel_message, send_flow_message
from datetime import datetime

def string_to_date_safe(date_string):
    """
    Converts a string in YYYY-MM-DD format to a date object,
    handling ValueError for incorrect formats.
    """
    try:
        # Attempt to parse the string using the specified format
        date_object = datetime.strptime(date_string, "%d/%m/%Y")
        formatted_date_string = date_object.strftime("%d/%m/%Y")
        return formatted_date_string
    except ValueError as e:
        # Catch ValueError if the string does not match the format
        print(f"Error converting '{date_string}': {e}")
        return None

def handle_message(message, phone_number_id):
    sender_id = message["from"]
    message_type = message["type"]
    print(f"Message type: {message_type}")
    if (message_type == "text"):
        message_text = message["text"]
        print("Message text: ", message_text["body"])
        outMessage = "Hey this is bot"
        # Send a simple automated reply
        if message_text["body"].lower() == "start":
            outMessage = "Welcome " + sender_id + " to the conversation. Please type menu to start."
            send_text_message(sender_id, outMessage, phone_number_id)
            # send_flow_message(sender_id, outMessage, phone_number_id)
            print("Message start")
        elif message_text["body"].lower() == "help":
            outMessage = "Sure, Please type menu to start. "
            send_text_message(sender_id, outMessage, phone_number_id)
            print("Message help")
        elif message_text["body"].lower() == "exit":
            outMessage = "Thank You for having conversation. GoodBye!"
            print("Message exit")
            send_text_message(sender_id, outMessage, phone_number_id)
        elif message_text["body"].lower() == "menu":
            # send_text_message(sender_id, "Please wait for menu", phone_number_id)
            outMessage = "Welcome " + sender_id + ". Please select appropriate option."
            send_ypcpl_menu_message(sender_id, outMessage, phone_number_id)
            print("Message menu")
        elif message_text["body"].lower() == "report":
            outMessage = "Sure, Please type menu to start."
            send_message(sender_id, outMessage, phone_number_id)
            print("Message report")
        else:
            dt = message["text"]
            print("date :",dt["body"])
            date1 = string_to_date_safe(str(dt["body"]))
            if date1 is None:
                outMessage = "Sure, Please type menu to start."
                send_text_message(sender_id, outMessage, phone_number_id)
            else:
                print("Message date ::",date1)
                # print("Message report")
                # outMessage = "Please find retype menu to start."
                # send_text_message(sender_id, outMessage, phone_number_id)
                send_backdated_message(sender_id, "Please find News Letter of " + date1 + " attached.",date1, phone_number_id)

    elif (message_type == "voice"):
        message_voice = message["voice"]
        print(f"Message voice: {message_voice}")
        outMessage = "Currently voice message not configured. Please type menu to start"
        send_text_message(sender_id, outMessage, phone_number_id)
    elif (message_type == "sticker"):
        message_sticker = message["sticker"]
        print(f"Message sticker: {message_sticker}")
        outMessage = "Currently Sticker message not configured. Please type menu to start"
        send_text_message(sender_id, outMessage, phone_number_id)
    elif (message_type == "photo"):
        message_sticker = message["photo"]
        print(f"Message sticker: {message_sticker}")
        outMessage = "Currently photo message not configured. Please type menu to start"
        send_text_message(sender_id, outMessage, phone_number_id)
    elif (message_type == "video"):
        message_sticker = message["video"]
        print(f"Message sticker: {message_sticker}")
        outMessage = "Currently video message not configured. Please type menu to start"
        send_text_message(sender_id, outMessage, phone_number_id)
    elif (message_type == "location"):
        message_location = message["location"]
        print(f"Message location: {message_location}")
        outMessage = "Currently location message not configured. Please type menu to start"
        send_text_message(sender_id, outMessage, phone_number_id)
    elif (message_type == "contact"):
        message_contact = message["contact"]
        print(f"Message contact: {message_contact}")
        outMessage = "Currently contact message not configured. Please type menu to start"
        send_text_message(sender_id, outMessage, phone_number_id)
    elif (message_type == "interactive"):
        print("Message interactive")
        print(message)
        interactive_msg = message["interactive"]
        list_reply = interactive_msg["list_reply"]
        print("interactive",interactive_msg)
        print("Message interactive type",interactive_msg["type"])
        print("Message interactive list_reply", list_reply)
        print("Message interactive list_reply id", list_reply["id"])
        print("Message interactive list_reply title", list_reply["title"])
        print("Message interactive list_reply description", list_reply["description"])
        optionid = list_reply["id"]
        outMessage = "Thank You for Selecting : "+list_reply["title"] +" : " +list_reply["description"]
        if (optionid == "news_letter"):
            outMessage = "Thank You for Selecting : " + list_reply["title"] + " : " + list_reply["description"] + " : Please enter date in dd/mm/yyyy format"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "lp_main_renew"):
            outMessage = "Thank You for Selecting : " + list_reply["title"] + " : *Please Select Line.*"
            send_ypcpl_lp_submenu_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "ep_main_menu"):
            outMessage = "Thank You for Selecting : " + list_reply["title"] + " : *Please Select Line.*"
            send_ypcpl_ep_submenu_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "cppd_main_menu"):
            outMessage = "Thank You for Selecting : " + list_reply["title"] + " : *Please Select Line.*"
            send_ypcpl_cppd_submenu_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "cpp_summary"):
            outMessage = "*Please find Line Wise Cost Per Part summary :* \n* Re New Styling : Rs. 418.70 \n* Maxima HD Wider : Rs. 893.27 \n* Maxima ZUG : Rs. 544.86"
            send_text_message(sender_id, outMessage, phone_number_id)
            # send_carousel_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "cppd_renew"):
            outMessage = "*Please find Re New Styling Cost Per Part Details :* \n* Total : Rs. 418.70 \n* Labour : Rs. 204.05 \n* Electricity : Rs. 78.45"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "cppd_maxima"):
            outMessage = "*Please find Maxima HD Wider Cost Per Part Details :* \n* Total : Rs. 893.27 \n* Labour : Rs. 393.73 \n* Electricity : Rs. 289.75"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "cppd_zug"):
            outMessage = "*Please find Maxima ZUG Cost Per Part Details :* \n* Total : Rs. 544.86 \n* Labour : Rs. 304.97 \n* Electricity : Rs. 82.34"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "shift_ratings"):
            outMessage = "*As of Date: 26/10/2025*\n*Shift 1 Details :* \n* Re New Styling : N/A \n* Maxima HD Wider : N/A \n* Maxima ZUG : N/A \n\n*Shift 2 Details :* \n* Re New Styling : N/A \n* Maxima HD Wider : N/A \n* Maxima ZUG : N/A"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "lp_renew"):
            outMessage = "*As Of Date: 26/09/2025*\n*Re New Styling Labour Performance Details*\n*Shift 1 Details :* \n* No. of Labour : 37 \n* Production Qty : 624 \n* Dispatch Qty : 625 \n* Parts Per Man : 16.86 \n*  Labour Cost Per Part : Rs. 33.63 \n* YPCPL Norm Per Part : Rs. 147.6 \n* BAL Norm Per Part : Rs. 430.6 \n* Total Wages Cost : Rs. 21,021 \n\n*Shift 2 Details :* \n* No. of Labour : 41 \n* Production Qty : 400 \n* Dispatch Qty : 401 \n* Parts Per Man : 9.75 \n* Labour Cost Per Part : Rs. 57.53 \n* YPCPL Norm Per Part : Rs. 147.6 \n* BAL Norm Per Part : Rs. 430.6 \n* Total Wages Cost : Rs. 23,070"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "lp_maxima"):
            outMessage = "*As Of Date: 26/09/2025*\n*Maxima HD Wider Labour Performance Details.*\n*Shift 1 Details :* \n* No. of Labour : 22 \n* Production Qty : 244 \n* Dispatch Qty : 244 \n* Parts Per Man : 11.09 \n*  Labour Cost Per Part : Rs. 57.7 \n* YPCPL Norm Per Part : Rs. 356 \n* BAL Norm Per Part : Rs. 1,181.71 \n* Total Wages Cost : 14,078\n\n*Shift 2 Details :* \n* No. of Labour : 0 \n* Production Qty : 0 \n* Dispatch Qty : 0 \n* Parts Per Man : 0 \n*  Labour Cost Per Part : Rs. 0 \n* YPCPL Norm Per Part : Rs. 356 \n* BAL Norm Per Part : Rs. 1,181.71 \n* Total Wages Cost : Rs. 0"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "lp_zug"):
            outMessage = "*As Of Date: 26/09/2025*\n*Maxima ZUG Labour Performance Details.*\n*Shift 1 Details :* \n* No. of Labour : 25 \n* Production Qty : 258 \n* Dispatch Qty : 273 \n* Parts Per Man : 10.32 \n*  Labour Cost Per Part : Rs. 50.59 \n* YPCPL Norm Per Part : Rs. 608.91 \n* BAL Norm Per Part : Rs. 222.5 \n* Total Wages Cost : Rs. 13,810\n\n*Shift 2 Details :* \n* No. of Labour : 27 \n* Production Qty : 234 \n* Dispatch Qty : 248 \n* Parts Per Man : 8.66 \n*  Labour Cost Per Part : Rs. 59.55 \n* YPCPL Norm Per Part : Rs. 608.91 \n* BAL Norm Per Part : Rs. 222.5 \n* Total Wages Cost : Rs. 14,768"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "ep_renew"):
            outMessage = "*As Of Date: 26/09/2025*\n*Re New Styling Electricity Performance Details :*\n*Shift 1 Details :* \n* Units Consumption : 2,523.44 \n* Production Qty : 624 \n* Cost Per Unit : Rs. 43.22 \n* YPC Norm : Rs. 86.60 \n* Bal Norm : Rs. 116.12\n\n*Shift 2 Details :*\n* Units Consumption : 1,724.12 \n* Production Qty : 400 \n* Cost Per Unit : Rs. 46.06 \n* YPC Norm : Rs. 86.60 \n* Bal Norm : Rs. 116.12"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "ep_maxima"):
            outMessage = "*As Of Date: 26/09/2025*\n*Maxima HD Wider Electricity Performance Details :*\n*Shift 1 Details :* \n* Units Consumption : 3,215.33 \n* Production Qty : 244 \n* Cost Per Unit : Rs. 140.82 \n* YPC Norm : Rs. 173.67 \n* Bal Norm : Rs. 230.16\n\n*Shift 2 Details :*\n* Units Consumption : 911.13 \n* Production Qty : 0 \n* Cost Per Unit : Rs. 0 \n* YPC Norm : Rs. 173.67 \n* Bal Norm : Rs. 230.16"
            send_text_message(sender_id, outMessage, phone_number_id)
        elif (optionid == "ep_zug"):
            outMessage = "*As Of Date: 26/09/2025*\n*Maxima ZUG Electricity Performance Details :*\n*Shift 1 Details :* \n* Units Consumption : 802.25 \n* Production Qty : 258 \n* Cost Per Unit : Rs. 33.23 \n* YPC Norm : Rs. 239.04 \n* Bal Norm : Rs. 185.27\n\n*Shift 2 Details :*\n* Units Consumption : 791.50 \n* Production Qty : 234 \n* Cost Per Unit : Rs. 36.15 \n* YPC Norm : Rs. 239.04 \n* Bal Norm : Rs. 185.27"
            send_text_message(sender_id, outMessage, phone_number_id)
        else :
            send_text_message(sender_id, outMessage, phone_number_id)
            send_message(sender_id, "Please find "+ list_reply["title"].replace(".", "")+" report attached.", phone_number_id)
    else:
        outMessage = "Thank You for Contacting me : Please type menu to start"
        send_text_message(sender_id, outMessage, phone_number_id)
        print("Message unknown type")
