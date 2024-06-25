 #format for --print-to-file output
 #format_list = "%(upload_date)s %(id)s %(title)s %(webpage_url)s %(live_status)s %(duration_string)s"
import os
import subprocess
import json
from datetime import datetime

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

    # Construct the yt-dlp command
    command = [
        "yt-dlp",
        "--dateafter", f"{after_date}",
        "--datebefore", f"{before_date}",
        "--verbose",
        "--get-title",
        "--get-id",
        "-j",
        "--skip-download",
        "--print-to-file", "%(upload_date)s %(id)s %(title)s %(webpage_url)s %(live_status)s %(duration_string)s", "tmpList.txt",
        channel_url
    ]

    # Print the command for verification
    command_str = ' '.join(command)
    print(f"Running command: {command_str}")

    # Execute the command and capture the output
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout + result.stderr
        print(f"Command output:\n{output}")  # Print the command output for debugging
        videos = output.splitlines()

        # Print each video's information
        for line in videos:
            if "[download]" in line and "upload date is not in range" in line:
                print("Stopping script: upload date is not in range.")
                break

            try:
                video = json.loads(line)
                title = video.get('title', 'N/A')
                video_id = video.get('id', 'N/A')
                upload_date = video.get('upload_date', 'N/A')
                duration = video.get('duration_string', 'N/A')
                url = video.get('webpage_url', 'N/A')

                print(f"Title: {title}")
                print(f"ID: {video_id}")
                print(f"Upload Date: {upload_date}")
                print(f"Duration: {duration}")
                print(f"URL: {url}")
                print("--------------------")
            except json.JSONDecodeError:
                print(f"Error decoding JSON: {line}")  # Print the line that caused the error
                continue

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"Command stdout:\n{e.stdout}")
        print(f"Command stderr:\n{e.stderr}")
    except KeyboardInterrupt:
        print("Process interrupted by user. Exiting...")
    finally:
        print("Process completed. Exiting...")

if __name__ == "__main__":
    fetch_videos()

