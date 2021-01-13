# This is here to allow testing
# a standalone flask web app
# in place of the full fledged one
#
# To run it change the run command in docker-compose.yml
#

from flask import Flask, render_template_string

app = Flask(import_name=__name__)

@app.route("/")
def index() :
    html = "HELLO, not much going on here."
    return render_template_string(html)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5001)

# That's everything!
