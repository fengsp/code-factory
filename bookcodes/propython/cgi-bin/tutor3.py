#!/usr/bin/python3
"""
runs on the server, reads form input, prints HTML;
url=http://localhost:8000/cgi-bin/tutor3.py
"""

import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<title>tutor3.py</title>
<h1>Greetings</h1>
<hr>
<P>%s</P>
<hr>"""

if not 'user' in form:
	print(html % 'Who are you?')
else:
	print(html % ('Hello, %s.' % form['user'].value))
