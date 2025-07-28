from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Sample HTML Document</title>
    </head>
    <body>
        <div id="first">
            <h3 data-example="yes">First Header</h3>
            <p class="text">This is the first paragraph.</p>
        </div>
        <ol>
            <li class="special">This list item is special.</li>
            <li class="special">This list item is also special.</li>
            <li>This list item is not special.</li>
        </ol>
    </body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')

# Print the prettified HTML
print(soup.prettify())

# Get the title tag
print(soup.title)


# Get the first div with id 'first'
first_div = soup.find('div', id='first')
print('first_div', first_div)

# Get the h3 tag inside the first div
h3_tag = first_div.find('h3')
print('h3_tag', h3_tag)

# Get the value of 'data-example' attribute from h3
print('data-example', h3_tag['data-example'])

# Get all li tags with class 'special'
special_lis = soup.find_all('li', class_='special')
for li in special_lis:
    print('li', li)

# Get the text of all li tags with class 'special'
for li in special_lis:
    print('li_text', li.get_text())

# Get the first p tag with class 'text'
p_text = soup.find('p', class_='text')
print('p_text', p_text)

# Get all text in the document
print('document_text', soup.get_text())
