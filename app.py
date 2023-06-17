from flask import Flask, render_template

from code_blocks import grant_access_from_partial
import partials0 as core

app = Flask(__name__)

@app.route('/')
def grant_access():
    successful, unsuccessful = grant_access_from_partial(core)
    print(successful, unsuccessful)
    return render_template('access_template.html', successful=successful, unsuccessful=unsuccessful)
