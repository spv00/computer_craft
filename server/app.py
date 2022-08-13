import flask

app = flask.Flask("app")

i = 0
turtlei = 0
inspected = "none"

queue: list = [

]

cmd = "none"

@app.route("/increase")
def increase():
    global cmd
    global queue
    global i
    if len(queue) - 1 >= i:
        cmd = queue[i]
        i += 1
    return str(i)

@app.route("/inspect", methods=["POST"])
def inspect():
    global inspected
    inspected = flask.request.get_data().strip().split(b",")[1]
    return inspected

@app.route("/resp", methods=["POST"])
def resp():
    global i
    global turtlei
    data = flask.request.get_data().strip().split(b",")
    turtlei = int(data[0])
    print(data, turtlei, i)
    if turtlei >= i:
        increase()
    return str(data)

@app.route("/setcmd/<newcmd>")
def setcmd(newcmd):
    queue.append(newcmd.split("+"))
    print(queue)
    return f"ok - {cmd}"

@app.route("/controls")
def controls():
    global i
    global cmd
    global queue
    global inspected
    return flask.render_template("controls.html", index=i, command=cmd, queue=[f"{i}" for i in queue], inspected=inspected)

@app.route("/index")
def index():
    global i
    global turtlei
    if turtlei >= i:
        increase()
    return str(i)

@app.route("/cmd")
def setcmd():
    global cmd
    return ' '.join(cmd)

if __name__ == "__main__":
    app.run()