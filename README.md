# Affinity Answers - Technical Assignment

This repository contains my solutions for the Affinity Answers Full Stack Engineering technical assignment.

The assignment covers:

- Python web scraping and data extraction
- SQL querying using the Rfam public MySQL database
- Unix shell scripting and CSV processing


## Repository Structure

```text
technical-assignment/
├── README.md
├── requirements.txt
├── question1/
│   └── scraper.py
├── question2/
│   └── queries.sql
└── question3/
    └── companies.sh
```


## Prerequisites

### Python

Python 3.8 or later is recommended.

Install the Python dependencies using:

```bash
pip install -r requirements.txt
```

The Python dependencies are:

- `requests` - used to send HTTP requests
- `beautifulsoup4` - used to parse HTML
- `tabulate` - used to display the extracted products in a readable table


### MySQL

Question 2 requires access to the public Rfam MySQL database.

The database can be accessed using:

```bash
mysql --user rfamro \
      --host mysql-rfam-public.ebi.ac.uk \
      --port 4497 \
      --database Rfam
```

The database connection details are provided by the Rfam documentation.


### Unix/Linux Shell

Question 3 requires a Unix-like shell environment with:

- Bash
- curl
- Miller (`mlr`)

Miller is used for CSV parsing, column selection, sorting, and formatted output.

Miller can be installed separately depending on the operating system.


## Question 1 - Python Web Scraping

### Description

The Python program searches the MDComputers website using a search term entered by the user.

It extracts:

- Product name
- Selling price
- Original price, when available
- Discount, when available

The results are displayed in a formatted table.

### Run

From the repository root:

```bash
python question1/scraper.py
```

The program prompts for a search term:

```text
Enter search term: external hard drive
```

### Error Handling

The program handles:

- Empty search terms
- Failed HTTP requests
- Cases where no products are found


## Question 2 - SQL and Database

### Description

The SQL queries use the public Rfam MySQL database.

The queries answer the following:

### A. Acacia Types

Determines the number of distinct Acacia types present in the `taxonomy` table.

### B. Longest Wheat DNA Sequence

Determines which wheat type has the longest DNA sequence using the `taxonomy` and `rfamseq` tables.

### C. Rfam Families

Finds Rfam families whose maximum DNA sequence length is greater than 1,000,000.

The results are:

- Sorted by maximum sequence length in descending order
- Limited to 15 results per page
- Retrieved from page 9

### Run

Connect to the Rfam database using the MySQL client and execute the queries in:

```text
question2/queries.sql
```

## Question 3 - Unix Shell Scripting

### Description

The shell script accepts the S&P 500 companies CSV URL as a command-line argument.

It:

1. Validates that a URL was supplied.
2. Downloads the CSV dataset using `curl`.
3. Processes the CSV data using Miller.
4. Extracts:
   - Company name
   - Headquarters location
   - Founding year
5. Sorts the records by founding year in descending order.
6. Displays the results in a readable table.

### Run

Make the script executable:

```bash
chmod +x question3/companies.sh
```

Run it by supplying the dataset URL:

```bash
./question3/companies.sh "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/refs/heads/main/data/constituents.csv"
```

### Error Handling

The script handles:

- Missing URL arguments
- Failure to retrieve the dataset

## Author

Submitted as part of the Affinity Answers Full Stack Engineering Technical Assignment.
