from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

"""from stories import silly_story"""

import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def get_home():

    return render_template("base.html", stories=stories.story_list)


@app.get('/questions')
def get_base():
    """
    display madlibs prompt at start of website
    with required parts to generate Madlib
    """

    id = request.args.get('story_code')
    print(id)

    return render_template("questions.html",
                           prompts = stories.story_access[id].prompts,
                           stories=stories.story_list,
                           story_code=stories.story_access[id].id)


@app.get('/<story_code>/results')
def get_results(story_code):
    """
    Generate Madlib from inputted prompts
    """

    story = stories.story_access[story_code]
    generated_madlib = story.get_result_text(request.args)


    return render_template("results.html",
                           generated_story=generated_madlib,
                           story_code = story_code)


"""Each button on the page will instantiate that class"""