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
end


oldi = 0
i = 0
cmd = "none"

while true do
    serveri = tonumber(get("index"))
    if serveri > oldi then
        cmd = split(get("cmd"))
        print(cmd[1])
        oldi = oldi + 1
        print("i: " .. serveri .. "  oldi: " .. oldi .. "  cmd: " .. cmd)
        if cmd == "forward" then
            turtle.forward()
            resp("resp", oldi, "ok")
        end

        if cmd == "back" then
            turtle.back()
            resp("resp", oldi, "ok")
        end

        if cmd == "left" then
            turtle.turnLeft()
            resp("resp", oldi, "ok")
        end

        if cmd == "right" then
            turtle.turnRight()
            resp("resp", oldi, "ok")
        end

        if cmd == "attack" then
            turtle.attack()
            resp("resp", oldi, "ok")
        end

        if cmd == "inspect" then
            local sucess, data = turtle.inspect()
            if sucess then
                resp("inspect", oldi, data.name)
            end
            resp("resp", oldi, "inspected")
        end
    end
end