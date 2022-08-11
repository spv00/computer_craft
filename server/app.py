import flask

app = flask.Flask("app")

@app.route("/test")
def test():
    x = open("action.txt")
    return str(x.read())

if __name__ == "__main__":
    app.run()