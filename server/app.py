import flask

app = flask.Flask("app")

i = 1

queue: list = []

cmd = "forward"

@app.route("/increase")
def increase():
    global i
    i += 1
    return str(i)

@app.route("/setcmd/<newcmd>")
def setcmd(newcmd):
    global cmd
    cmd = newcmd
    increase()
    return f"ok - {cmd}"

@app.route("/controls")
def controls():
    return flask.render_template("controls.html")

@app.route("/index")
def index():
    global i
    return str(i)

@app.route("/cmd")
def test():
    return cmd

if __name__ == "__main__":
    app.run()