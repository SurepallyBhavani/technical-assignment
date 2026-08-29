#!/bin/bash

URL="$1"

# Check whether a URL was provided
if [ -z "$URL" ]; then
    echo "Error: Please provide a CSV URL."
    exit 1
fi

# Download the CSV dataset and raise error if the data doesnot exist
if ! curl -sSf "$URL" -o companies.csv; then
    echo "Error: Failed to retrieve the dataset."
    exit 1
fi

# Extract required columns, sort by founding year,
# and display the result in a readable table
mlr --icsv --opprint \
    sort -nr Founded then \
    cut -f "Security,Headquarters Location,Founded" \
    companies.csv
