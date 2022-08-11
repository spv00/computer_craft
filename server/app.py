import flask

app = flask.Flask("app")

@app.route("/test")
def test():
    return "test"

if __name__ == "__main__":
    app.run()