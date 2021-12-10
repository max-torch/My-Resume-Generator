from bs4 import BeautifulSoup
import pdfkit

soup = BeautifulSoup(open("Resume.html", encoding = 'utf8'), "html.parser")
headings = soup.find_all('h3')

for heading in headings:
    new_span = soup.new_tag("span")
    for content in reversed(heading.contents):
        new_span.insert(0, content.string)
    heading.append(new_span)

new_link = soup.new_tag("link", rel="stylesheet", href="styles.css")
soup.head.append(new_link)

with open("StylizedResume.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))

config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
pdfkit.from_file('StylizedResume.html', 'My Resume.pdf', configuration=config)