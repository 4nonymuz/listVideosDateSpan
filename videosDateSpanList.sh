#!/bin/zsh

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <URL> <DATE_BEFORE> <DATE_AFTER>"
    exit 1
fi

# Assign arguments to variables
URL="$1"
DATE_BEFORE="$2"
DATE_AFTER="$3"

# Define the format string
#nTITLE="Title: %(title)s"
#nURL="%(webpage_url)"
#OUTPUT="${nTITLE}${nURL}"
#OUTPUT="Title: %(title)s\nURL: %(webpage_url)s\nUpload Date: %(upload_date>%Y-%m-%d)s\nDuration: %(duration>%H:%M:%S)s\nVideo ID: %(id)s\n"

# Create a temporary file to store the output
#OUTPUT_FILE=$(mktemp)

# Print a start message
echo "Starting to process videos from $URL between $DATE_AFTER and $DATE_BEFORE"

# Use yt-dlp to get video details within the specified date range and save to the temporary file
yt-dlp --verbose "$URL" --dateafter "$DATE_AFTER" --datebefore "$DATE_BEFORE" --skip-download --get-title --get-id

# Print a progress message
echo "Finished retrieving video information. Processing output..."

# Read the output file and print each line
#while IFS= read -r line; do
#    echo "$line"
#done < "$OUTPUT_FILE"

# Remove the temporary file
# rm #####"$OUTPUT_FILE"

# Print completion message
echo "Processing completed for the date range $DATE_AFTER to $DATE_BEFORE."

exit 0
