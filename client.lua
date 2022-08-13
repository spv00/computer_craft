url = "http://please.lickthe.tips:6069/"

function get(dir)
    return http.get(url .. dir).readAll()
end

function resp(dir, data)
    http.post(url .. dir, data)
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
            resp("resp", "ok")
        end
        
        if cmd == "back" then
            turtle.back()
            resp()
        end
        
        if cmd == "left" then
            turtle.turnLeft()
            resp()
        end
        
        if cmd == "right" then
            turtle.turnRight()
            resp()
        end

        if cmd == "attack" then
            turtle.attack()
            resp()
        end
    end
end