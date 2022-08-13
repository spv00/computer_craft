url = "http://please.lickthe.tips:6069/"

function get(dir)
    return http.get(url .. dir).readAll()
end

function resp(dir, index, data)
    http.post(url .. dir, index .. "," .. data)
end

i = 0

while true do
    oldi = i
    i = tonumber(get("index"))
    if i > oldi then
        cmd = get("cmd")
        i = i + 1

        if cmd == "forward" then
            turtle.forward()
            resp("resp", i, "ok")
        end
        
        if cmd == "back" then
            turtle.back()
            resp("resp", i, "ok")
        end
        
        if cmd == "left" then
            turtle.turnLeft()
            resp("resp", i, "ok")
        end
        
        if cmd == "right" then
            turtle.turnRight()
            resp("resp", i, "ok")
        end

        if cmd == "attack" then
            turtle.attack()
            resp("resp", i, "ok")
        end
    end
end