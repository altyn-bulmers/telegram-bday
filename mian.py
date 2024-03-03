import json
import datetime
from google.cloud import storage
from telegram import Bot
from telegram.error import BadRequest
import pytz

# Initialize the bot with your API token
bot = Bot(token='YOUR_API_TOKEN')

def get_birthdays_from_gcs(bucket_name, file_name):
    """Retrieve the birthday JSON from GCS."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    
    data = json.loads(blob.download_as_string())
    return data

def check_and_send_birthday_wishes(users_data, chat_id):
    """Check for birthdays and send messages."""
    # Convert UTC now to Kazakhstan time zone
    #today = datetime.datetime.utcnow().strftime("%m-%d")  # Use UTC to match the Cloud Function's timezone
    kz_tz = pytz.timezone('Asia/Almaty')
    today = datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(kz_tz).strftime("%m-%d")
    
    
    for user_id, user_info in users_data.items():
        if user_info["birthday"] == today:
            message = f"Happy Birthday, {user_info['name']}! 🎉"
            try:
                bot.send_message(chat_id=chat_id, text=message)
            except BadRequest as e:
                print(f"Failed to send message to chat_id {chat_id}: {e.message}")

def birthday_bot(request):
    """HTTP Cloud Function entry point."""
    try:
        bucket_name = ''  # Replace with your bucket name
        file_name = 'telegram-bday/birthdays.json'      # Replace with your file name
        chat_id = ''          # Replace with your known chat_id

        users_data = get_birthdays_from_gcs(bucket_name, file_name)
        check_and_send_birthday_wishes(users_data, chat_id)
        return 'Birthday messages sent successfully', 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Error: {str(e)}", 500
