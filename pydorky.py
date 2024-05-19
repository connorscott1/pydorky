import webbrowser
import pyperclip

def get_keyword_groups(prompt):
    print(prompt)
    print("Example: 'keyword1,keyword2;keyword3,keyword4' will generate a search query for (keyword1 AND keyword2) OR (keyword3 AND keyword4).")
    group = input("Enter keywords: ").strip()
    keyword_groups = []
    if group:
        or_keywords = group.split(';')
        and_groups = [kw.strip().split(',') for kw in or_keywords]
        keyword_groups.extend(and_groups)
    return keyword_groups

def get_filetypes():
    print("Enter the file types you want to search for, separated by semicolons.")
    print("Example: 'pdf;docx;txt' will search for pdf, docx, and txt files.")
    filetypes = input("Enter file types: ").strip().split(';')
    return [filetype.strip() for filetype in filetypes if filetype.strip()]

def get_site():
    return input("Enter a site to restrict the search to (e.g., example.com) or press Enter to search all sites: ").strip()

def get_intitle():
    print("Enter title keywords using ';' for OR and ',' for AND.")
    print("Example: 'title1,title2;title3,title4' will generate a search query for (title1 AND title2) OR (title3 AND title4).")
    return get_keyword_groups("")

def get_inurl():
    print("Enter URL keywords using ';' for OR and ',' for AND.")
    print("Example: 'url1,url2;url3,url4' will generate a search query for (url1 AND url2) OR (url3 AND url4).")
    return get_keyword_groups("")

def get_date_range():
    start_date = input("Enter the start date in the format YYYY-MM-DD or press Enter to skip: ").strip()
    end_date = input("Enter the end date in the format YYYY-MM-DD or press Enter to skip: ").strip()
    if start_date and end_date:
        return f'after:{start_date} before:{end_date}'
    return ""

def construct_dork(keyword_groups, intitle_groups, inurl_groups, filters):
    if not keyword_groups:
        return ""

    filetype_dorks = [f"filetype:{filetype}" for filetype in filters.get('filetypes', [])]
    site_dork = f"site:{filters.get('site', '')}" if filters.get('site', '') else ""
    date_dork = filters.get('date_range', '')

    keyword_dork_groups = []
    for group in keyword_groups:
        keyword_dork = ' AND '.join([f'intext:"{keyword}"' for keyword in group])
        keyword_dork_groups.append(f'({keyword_dork})')

    intitle_dork_groups = []
    for group in intitle_groups:
        intitle_dork = ' AND '.join([f'intitle:"{keyword}"' for keyword in group])
        intitle_dork_groups.append(f'({intitle_dork})')

    inurl_dork_groups = []
    for group in inurl_groups:
        inurl_dork = ' AND '.join([f'inurl:"{keyword}"' for keyword in group])
        inurl_dork_groups.append(f'({inurl_dork})')

    intitle_dork = ' OR '.join(intitle_dork_groups) if intitle_dork_groups else ""
    inurl_dork = ' OR '.join(inurl_dork_groups) if inurl_dork_groups else ""

    dorks = [' OR '.join(keyword_dork_groups)] + filetype_dorks + [site_dork, intitle_dork, inurl_dork, date_dork]
    return ' '.join(filter(None, dorks)).strip()

def main():
    print("Welcome to PyDorky: The Google Dork Generator")
    print("This tool helps you generate Google dorks to search for keywords with various search parameters.")
    
    keyword_groups = get_keyword_groups("Enter keyword groups using ';' for OR and ',' for AND.")
    
    if not keyword_groups:
        print("No keyword groups provided. Exiting.")
        return
    
    print("\nAvailable filters:")
    print("1. File type")
    print("2. Site")
    print("3. Keyword in title")
    print("4. Keyword in URL")
    print("5. Date range")
    
    filter_indices = input("Enter the numbers of the filters you want to add, separated by commas (e.g., 1,3,5): ").strip().split(',')

    filters = {}
    intitle_groups = []
    inurl_groups = []
    if '1' in filter_indices:
        filters['filetypes'] = get_filetypes()
    if '2' in filter_indices:
        filters['site'] = get_site()
    if '3' in filter_indices:
        intitle_groups = get_intitle()
    if '4' in filter_indices:
        inurl_groups = get_inurl()
    if '5' in filter_indices:
        filters['date_range'] = get_date_range()
    
    dork = construct_dork(keyword_groups, intitle_groups, inurl_groups, filters)
    
    print("\nGenerated Google Dork:")
    print(dork)
    
    if not dork:
        print("No dork generated. Exiting.")
        return

    action = input("\nDo you want to (1) copy the dork to clipboard or (2) launch it in your default browser? Enter 1 or 2: ").strip()
    
    if action == "1":
        pyperclip.copy(dork)
        print("Google dork copied to clipboard.")
    elif action == "2":
        query = dork.replace(" ", "+")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        print("Google dork launched in default browser.")
    else:
        print("Invalid input. Exiting.")

if __name__ == "__main__":
    main()
