
---

# Birthday Wisher Telegram Bot

## Overview
The Birthday Wisher Telegram Bot is designed to automatically send birthday wishes to users specified in a JSON file. This bot checks for birthdays daily and sends a personalized message to each user on their birthday.

## Components

- `main.py`: Contains the core logic of the bot, including functions to retrieve user data from Google Cloud Storage (GCS), check for birthdays based on the current date in Kazakhstan time zone, and send birthday wishes through Telegram.

- `requirements.txt`: Specifies the Python packages that need to be installed for the bot to function. This includes `python-telegram-bot` for interacting with the Telegram API, `google-cloud-storage` for accessing data stored in GCS, and `pytz` for timezone conversions.

## Deployment and Execution

This bot is hosted on the Google Cloud Platform and is designed to be run as a Cloud Function. It is triggered daily by Cloud Scheduler at 0:00 AM Kazakhstan time. This scheduling ensures that the bot checks for and sends out birthday wishes at the start of each day, according to the Kazakhstan time zone.

## Configuration

Before deploying, ensure that the `requirements.txt` file is updated with the correct versions of the necessary packages. Additionally, the `main.py` file should be configured with your Telegram bot token, GCS bucket name, file name containing user data, and the chat ID where birthday messages will be sent.

## Deployment Steps

1. Create a Google Cloud Function with the trigger set to HTTP.
2. Upload `main.py` and `requirements.txt` to the Cloud Function.
3. Change in `main.py`: `YOUR_API_TOKEN` to your Telegram bot id, `bucket_name` to the bucket in your cloud storage, `chat_id` to your Telegram chat id.
4. Set the Cloud Function's entry point to `birthday_bot`.
5. Configure Cloud Scheduler to trigger the Cloud Function at 0:00 AM Kazakhstan time daily.

With this setup, the Birthday Wisher Telegram Bot will automatically send out birthday wishes to users, making it a thoughtful and automated way to keep up with important dates.

---
