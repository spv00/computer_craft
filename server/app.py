import flask

app = flask.Flask("app")

i = 1
turtlei = 0

queue: list = [

]

cmd = "left"

@app.route("/increase")
def increase():
    global cmd
    global queue
    global i
    if len(queue) - 1 >= i:
        cmd = queue[i]
        i += 1
    return str(i)

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
    global cmd
    queue.append(newcmd)
    print(queue)
    return f"ok - {cmd}"

@app.route("/controls")
def controls():
    global i
    global cmd
    global queue
    return flask.render_template("controls.html", index=i, command=cmd, queue=[f"{i}" for i in queue])

@app.route("/index")
def index():
    global i
    global turtlei
    if turtlei >= i:
        increase()
    return str(i)

@app.route("/cmd")
def test():
    return cmd

if __name__ == "__main__":
    app.run()