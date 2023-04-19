from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def get_base():
    """
    display madlibs prompt at start of website
    with required parts to generate Madlib
    """

    return render_template("questions.html", prompts = silly_story.prompts)


@app.get('/results')
def get_results():
    """
    Generate Madlib from inputted prompts
    """

    print(request.args)
    generated_madlib = silly_story.get_result_text(request.args)


    return render_template("results.html", generated_story=generated_madlib)