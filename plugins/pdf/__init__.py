# This is in `plugins/pdf/__init__.py`
import os
import tempfile

from pelican import signals

# The pandoc command. The CV is saved in a static `pdfs/` subdirectory.
CMD = ('pandoc {fn} -o content/pdfs/PrashantTiwariResume.pdf '
       '-V geometry:margin=1in '
       '--template=plugins/pdf/cv.tex')


def generate_pdf(p):
    with tempfile.TemporaryDirectory() as tmpdir:
        print("Generating PrashantTiwariResume.pdf")
        with open('content/category/CV.md', 'r') as f:
            contents = f.read()
        fn = os.path.join(tmpdir, 'CV.md')
        contents = contents[contents.index('\n---') + 4:]
        # Add title and author in Markdown front matter.
        contents = ('---\n'
                    'Title: Curriculum Vitae\n'
                    'Category: CV\n'
                    '---\n\n' +
                    contents)
        with open(fn, 'w') as f:
            f.write(contents)
        print(CMD.format(fn=fn))
        os.system(CMD.format(fn=fn))
        print("Generating PrashantTiwariResume.pdf ... Done.")


def register():
    # Create the PDF before generating the site.
    signals.initialized.connect(generate_pdf)
