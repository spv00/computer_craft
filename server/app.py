import flask

app = flask.Flask("app")

@app.route("/test")
def test():
    return "Test complete"

if __name__ == "__main__":
    app.run()