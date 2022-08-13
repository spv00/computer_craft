url = "http://please.lickthe.tips:6069/"

function get(dir)
    return http.get(url .. dir).readAll()
end

function resp(dir, index, data)
    http.post(url .. dir, index .. "," .. data)
end

function split(line)
    out = {}
    for token in string.gmatch(line, "[^%s]+") do
        table.insert(out, token)
    end
    return out
end


oldi = 0
i = 0
cmd = "none"

while true do
    serveri = tonumber(get("index"))
    if serveri > oldi then
        cmd = split(get("cmd"))
        action = cmd[1]
        table.remove(cmd, 1)
        args = cmd
        oldi = oldi + 1
        print("i: " .. serveri .. "  oldi: " .. oldi .. "  cmd: " .. action)
        if action == "forward" then
            turtle.forward()
            resp("resp", oldi, "ok")
        end

        if action == "back" then
            turtle.back()
            resp("resp", oldi, "ok")
        end

        if action == "left" then
            turtle.turnLeft()
            resp("resp", oldi, "ok")
        end

        if action == "right" then
            turtle.turnRight()
            resp("resp", oldi, "ok")
        end

        if action == "attack" then
            turtle.attack()
            resp("resp", oldi, "ok")
        end

        if action == "inspect" then
            local sucess, data = turtle.inspect()
            if sucess then
                resp("inspect", oldi, data.name)
            else
                resp("inspect", oldi, "air")
            end
            resp("resp", oldi, "inspected")
        end

        if action == "setname" then
            os.setComputerLabel(table.concat(args, " "))
            resp("resp", oldi, "ok")
        end
    end
end