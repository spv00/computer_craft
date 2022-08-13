import flask

app = flask.Flask("app")

i = 0

queue: list = [
    "forward",
    "forward",
    "left",
    "right"
]

cmd = "forward"

@app.route("/increase")
def increase():
    global i
    i += 1
    return str(i)

def next_step():
    global cmd
    global queue
    global i
    if len(queue) >= i:
        cmd = queue[i]

@app.route("/resp", methods=["POST"])
def resp():
    data = flask.request.get_data().strip().split(b",")
    index = int(data[0])
    if index <= i:
        increase()
        next_step()
    return str(data)

@app.route("/setcmd/<newcmd>")
def setcmd(newcmd):
    global cmd
    queue.append(newcmd)
    print(queue)
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