import flask

app = flask.Flask("app")

i = 1

queue: list = []

@app.route("/increase")
def increase():
    global i
    i += 1
    return str(i)

@app.route("/controls", methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        if flask.request.form.get('action1') == 'VALUE1':
            pass # do something
        elif  flask.request.form.get('action2') == 'VALUE2':
            pass # do something else
        else:
            pass # unknown
    elif flask.request.method == 'GET':
        return flask.render_template('controls.html', form=flask.form)
    
    return flask.render_template("index.html")

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