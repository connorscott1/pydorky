
# PyDorky: The Google Dork Generator

This script helps you generate Google dorks to search for keywords with various search parameters. It allows you to copy the generated dork to the clipboard or launch it in your default web browser.

## Features

- **Keyword Search**: Input single or multiple keywords to include in the search.
- **File Type Filter**: Restrict search to specific file types (e.g., PDF, DOCX, TXT).
- **Site Restriction**: Restrict search to a specific site.
- **Title Keyword Search**: Search for keywords in the title of the page.
- **URL Keyword Search**: Search for keywords in the URL of the page.
- **Date Range**: Restrict search results to a specific date range.
- **AND/OR Logic**: Combine multiple keywords using AND or OR logic.
- **Copy to Clipboard**: Copy the generated dork to the clipboard.
- **Launch in Browser**: Launch the generated dork in the default web browser.

## Prerequisites

- Python 3.x
- `pyperclip` library

## Installation

1. Clone the repository or download the script.
2. Install the `pyperclip` library:
   ```sh
   pip install pyperclip
   ```

## Usage

1. Run the script:
   ```sh
   python google_dork_generator.py
   ```

2. Follow the prompts to input keywords and select filters.

3. Choose to either copy the generated dork to the clipboard or launch it in your default browser.

## Example

### Input

- Keywords: `cybersecurity,threat;incident,breach`
- File types: `pdf;docx`
- Site: `example.com`
- Title keywords: `report,analysis;summary`
- URL keywords: `2023,confidential`
- Date range: `2023-01-01 to 2023-12-31`

### Output

```
(intext:"cybersecurity" AND intext:"threat") OR (intext:"incident" AND intext:"breach") filetype:pdf OR filetype:docx site:example.com (intitle:"report" AND intitle:"analysis") OR (intitle:"summary") (inurl:"2023" AND inurl:"confidential") after:2023-01-01 before:2023-12-31
```

This example demonstrates how to generate a comprehensive Google dork query using PyDorky with various filters and logical combinations.
