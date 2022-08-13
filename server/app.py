import flask

app = flask.Flask("app")

i = 0
turtlei = 0
inspected = "none"
terminated = False

queue: list = [

]

cmd = "none"

@app.after_request
def add_headers(response: flask.Response):
    # Take care of preflight post request
    if flask.request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Access-Control-Allow-Origin'
        response.headers['Access-Control-Max-Age'] = '300'
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/', defaults={'path': ''}, methods=['OPTIONS'])
@app.route('/<path:path>', methods=['OPTIONS'])
def catch_all(path):
  return ""

@app.route("/terminate")
def terminate():
    global cmd, terminated
    terminated = True
    return "Terminated"

@app.route("/unterminate")
def unterminate():
    global terminated
    terminated = False
    return "Back up!"

@app.route("/eval", methods=["POST"])
def eval_code():
    out = exec(flask.request.get_data())
    return str(out)

@app.route("/reset")
def reset():
    global queue, cmd, i, turtlei
    cmd = "none"
    queue = []
    i = 0
    turtlei = 0
    return "Reset"

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

def run_cmd(cmd: str, args: list):
    args.insert(0, cmd)
    setcmd('+'.join(args))

@app.route("/controls")
def controls():
    global i
    global cmd
    global queue
    global inspected
    return flask.render_template("controls.html", index=i, command=cmd, queue=[f"{i}" for i in queue], inspected=str(inspected.strip()))

@app.route("/index")
def index():
    global terminated
    if terminated:
        return str(0)
    global i
    global turtlei
    if turtlei >= i:
        increase()
    return str(i)

@app.route("/cmd")
def getcmd():
    global cmd
    return ' '.join(cmd)

if __name__ == "__main__":
    app.run()