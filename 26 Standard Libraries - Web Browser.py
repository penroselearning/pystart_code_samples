import webbrowser

url = 'https://www.penroselearning.com'

webbrowser.register('chrome', None)

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)