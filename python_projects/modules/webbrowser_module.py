import webbrowser

user_term = input("Enter a search term: ")
url = 'https://google.com'

webbrowser.open(f"{url}/search?q={user_term}")    # this format was obtained from the address bar after searching for something on google.com
