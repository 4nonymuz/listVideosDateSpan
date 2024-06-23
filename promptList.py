import os
import subprocess
from datetime import datetime, timedelta

def fetch_videos():
    # Prompt for YouTube channel URL
    channel_url = input("Enter YouTube channel URL: ")

    # Prompt for date range
    before_year = input("Enter the year for before date (press Enter for current year): ")
    before_month = input("Enter the month for before date (press Enter for current month): ")
    before_day = input("Enter the day for before date (press Enter for current day): ")

    after_year = input("Enter the year for after date (press Enter for current year): ")
    after_month = input("Enter the month for after date (press Enter for current month): ")
    after_day = input("Enter the day for after date (press Enter for current day): ")

    # Get current date
    current_date = datetime.now()

    # Process before date
    if before_year == '':
        before_year = current_date.year
    if before_month == '':
        before_month = current_date.month
    if before_day == '':
        before_day = current_date.day
    
    before_year = int(before_year)
    before_month = int(before_month) if before_month else current_date.month
    before_day = int(before_day) if before_day else current_date.day
    before_date = f"{before_year}{before_month:02d}{before_day:02d}"

    # Process after date
    if after_year == '':
        after_year = current_date.year
    if after_month == '':
        after_month = current_date.month
    if after_day == '':
        after_day = current_date.day
    
    after_year = int(after_year)
    after_month = int(after_month) if after_month else current_date.month
    after_day = int(after_day) if after_day else current_date.day
    after_date = f"{after_year}{after_month:02d}{after_day:02d}"

    #format for --print-to-file output
    format_list = "%(upload_date)s %(id)s %(title)s %(webpage_url)s %(live_status)s %(duration_string)s"
   
    # Construct the yt-dlp command
    command = [
        "yt-dlp",
        f"--dateafter {after_date}",
        f"--datebefore {before_date}",
        "--verbose",
        "--get-title",
        "--get-id",
	f"-s --print-to-file '{format_list}' tmpList.txt", 
        channel_url
    ]

    # Join the command into a single string
    command_str = ' '.join(command)

    # Print the command for verification
    print(f"Running command: {command_str}")

    # Execute the command
    try:
        subprocess.run(command_str, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

if __name__ == "__main__":
    fetch_videos()
