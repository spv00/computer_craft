import flask

app = flask.Flask("app")

i = 1

queue: list = []

@app.route("/increase")
def increase():
    global i
    i += 1
    return str(i)

@app.route("/controls")
def controls():
    return flask.render_template("controls.html")

@app.route("/index")
def index():
    global i
    return str(i)

@app.route("/cmd")
def test():
    x = open("action.txt")
    return str(x.read())

if __name__ == "__main__":
    app.run()