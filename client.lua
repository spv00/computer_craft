url = "http://please.lickthe.tips:6069/"

function get(dir)
    return http.get(url .. dir).readAll()
end

function resp(dir, index, data)
    http.post(url .. dir, index .. "," .. data)
end

oldi = -1
i = 0
cmd = "none"

while true do
    oldi = 0
    serveri = tonumber(get("index"))
    print("i: " .. serveri .. "  oldi: " .. oldi .. "  cmd: " .. cmd)
    if serveri > oldi then
        cmd = get("cmd")

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

        oldi = 5
    end
end