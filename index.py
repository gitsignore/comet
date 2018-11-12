import requests
import json
import os
from flask import Flask, render_template, make_response
from dotenv import load_dotenv
from flask_weasyprint import HTML, CSS, render_pdf
from io import StringIO, BytesIO
load_dotenv()


app = Flask('comet')


@app.route('/')
def pdf():
    # request = requests.get(os.getenv('API_HOST') + ':' +
    #                        os.getenv('API_PORT') + os.getenv('API_ENTRYPOINT'))
    # content = json.loads(request.text)

    # html = render_template(
    #     'pdf.html',
    #     header=content["headers"][0],
    #     profile=content["profiles"][0],
    #     experiences=content["experiences"],
    #     educations=content["educations"],
    #     skillCategories=content["skillCategories"],
    #     portfolios=content["portfolios"]
    # )

    html = render_template(
        'pdf.html',
        header={'title': 'title'}
    )

    # return html
    return render_pdf(HTML(string=html))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
