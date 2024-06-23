import sys
import subprocess
import datetime
import logging

from yt_dlp import YoutubeDL
from yt_dlp.utils import DateRange

# Configure logging
logging.basicConfig(filename='yt_dlp.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

def fetch_videos(channel_url, before_date, after_date):
    # Construct the yt-dlp options
    ydl_opts = {
        'skip_download': True,
        'get_title': True,
        'get_id': True,
        'get_upload_date': True,
        'get_duration': True,
        'get_url': True,
        'daterange': DateRange(after_date, before_date),
	'lazy_playlist': True,
    }

    # Create a YoutubeDL object with options
    ydl = YoutubeDL(ydl_opts)

    # Print the options for verification
    logging.info(f"Executing yt-dlp command with options: {ydl.params}")

    # Execute yt-dlp
    try:
        result = ydl.extract_info(channel_url, download=False)
        parse_and_display(result)
    except Exception as e:
        print(f"Error running yt-dlp: {e}")
        logging.error(f"Error running yt-dlp: {e}")

def parse_and_display(data):
    for entry in data['entries']:
        title = entry.get('title', 'N/A')
        video_id = entry.get('id', 'N/A')
        upload_date = entry.get('upload_date', 'N/A')
        upload_time = entry.get('upload_time', 'N/A')
        duration = entry.get('duration', 'N/A')
        video_url = entry.get('webpage_url', 'N/A')

        print(f"Video Title: {title}")
        print(f"Upload Date: {upload_date}")
        print(f"Upload Time: {upload_time}")
        print(f"Video ID: {video_id}")
        print(f"Video URL: {video_url}")
        print(f"Video Duration: {duration}")
        print("------")

if __name__ == "__main__":
    # Check if the channel URL is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <channel_url>")
        sys.exit(1)

    channel_url = sys.argv[1]

# Prompt for before date
before_year = input("Enter the year for before date (press Enter for current year): ")
before_month = input("Enter the month for before date (press Enter for current month): ")
before_day = input("Enter the day for before date (press Enter for current day): ")

if before_year == "":
    before_year = datetime.datetime.now().year
if before_month == "":
    before_month = datetime.datetime.now().month
else:
    before_month = int(before_month)  # Convert to integer

if before_day == "":
    before_day = datetime.datetime.now().day
else:
    before_day = int(before_day)  # Convert to integer

before_date = f"{before_year}{before_month:02d}{before_day:02d}"

# Prompt for after date
after_year = input("Enter the year for after date (press Enter for current year): ")
after_month = input("Enter the month for after date (press Enter for current month): ")
after_day = input("Enter the day for after date (press Enter for current day): ")

if after_year == "":
    after_year = datetime.datetime.now().year
if after_month == "":
    after_month = datetime.datetime.now().month
else:
    after_month = int(after_month)  # Convert to integer

if after_day == "":
    after_day = datetime.datetime.now().day
else:
    after_day = int(after_day)  # Convert to integer

after_date = f"{after_year}{after_month:02d}{after_day:02d}"

fetch_videos(channel_url, before_date, after_date)
