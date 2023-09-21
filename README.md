# max-torch's Resume Generator

## Why this got made

I initially decided to write my resume using Markdown instead of using an office app like Microsoft 365 or LibreOffice. After I wrote my Markdown I used a VSCode extension called [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) to convert it into HTML. I added additional CSS and tweaked the HTML to make it have it's final cosmetic appearance. Lastly, I opened the HTML file in a browser and printed the resume to a PDF file.

 The problem was that I kept on editing, tweaking, and adding stuff to my resume. This meant I had to also keep going through the whole process again and again. To make my life easier, I wrote a python script that uses [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/index.html) and [pdfkit](https://pypi.org/project/pdfkit/) to automate the tweaking of the HTML output of [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) and generate a PDF file. I also transferred the CSS to an external style sheet so that I would only have to insert the style sheet link in the HTML rather than writing all the CSS inside the `<head>` tag each time.

 If you're here, and if you decide to make use of this for your own purposes, the most generous thing you can do is to contribute to this repository by making your own resume style template and adding it here.

 Currently, the contents of `resume.md` are the actual contents of my resume.

## Setup

 1. In the repository folder, run `pip install -r requirements.txt`
 2. Install wkhtmltopdf on your system and add it to PATH.

## Usage

 1. Write your resume in Markdown. Use h3 headings (`###`) for each resume section title.
 2. Use [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) to convert the `.md` file to `.html`.
 3. Run `stylize.py`.
 4. Your resume is ready as `My Resume.pdf`.
 5. Tailor your resume for each job application and keep track of all the different versions by using Git to create a new branch for each version of your resume you present to employers.
