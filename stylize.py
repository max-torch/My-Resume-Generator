from bs4 import BeautifulSoup
import pdfkit


def main():
    soup = BeautifulSoup(open("Resume.html", encoding='utf8'), "html.parser")
    stylized_soup = stylize_soup(soup)
    soup_to_html("StylizedResume.html", stylized_soup)
    html_to_pdf("StylizedResume.html", "My Resume.pdf")

    
def stylize_soup(soup):
    headings = soup.find_all('h2')

    for heading in headings:
        new_span = soup.new_tag("span")
        for content in reversed(heading.contents):
            new_span.insert(0, content.string)
        heading.append(new_span)

    new_link = soup.new_tag("link", rel="stylesheet", href="styles.css")
    soup.head.append(new_link)
    return soup


def soup_to_html(file, soup):
    with open(file, "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))


def html_to_pdf(html_file, pdf_file):
    pdfkit.from_file(html_file, pdf_file, options={'enable-local-file-access': None})


if __name__ == "__main__":
    main()
