import flask

app = flask.Flask("app")

i = 1

queue: list = [
    
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
        increase()

@app.route("/resp", methods=["POST"])
def resp():
    data = flask.request.get_data().strip().split(b",")
    print(data)
    index = int(data[0])
    if index >= i:
        print("BRUH")
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