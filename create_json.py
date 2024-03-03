# Let's try creating the file again after the reset.
import json

# Sample data
test_birthdays = {
    "user123": "02-14",
    "user321": "02-15",
    "user456": "08-25",
    "user789": "12-01"
}

birthday_data = '''

14 марта - Альберт Эйнштейн
8 июля - Ян ЛеКун
6 декабря - Джеффри Хинтон
'''

# Mapping of Russian month names to numerical representation
months = {
    "января": "01",
    "февраля": "02",
    "марта": "03",
    "апреля": "04",
    "мая": "05",
    "июня": "06",
    "июля": "07",
    "августа": "08",
    "сентября": "09",
    "октября": "10",
    "ноября": "11",
    "декабря": "12"
}

data = {}
user_id = 1
for line in birthday_data.strip().split("\n"):
    try:
        date_part, name = line.split(" - ")
        day, month_name = date_part.split()[:2]  # Only take the first two split parts
        month = months.get(month_name)
        if not month:
            raise ValueError(f"Unknown month: {month_name}")
        day = day.zfill(2)
        birthday = f"{month}-{day}"
        data_key = f"user{user_id}"
        data[data_key] = {"birthday": birthday, "name": name}
        user_id += 1
    except ValueError as e:
        print(f"Error processing line '{line}': {e}")

    
# Convert the dictionary to a JSON string
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Print or save the JSON data
print(json_data)

# Define the path for the new file
file_path = '/home/az/Projects/06_Telegram_bot/birthdays.json'

# Write the sample data to a JSON file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(json_data)

#file_path
