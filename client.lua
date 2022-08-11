url = "http://please.lickthe.tips:6069/"

function get(dir)
    return http.get(url + dir).readAll()
end

cmd = get("cmd")
i = 0

while true do
    oldi = i
    i = get("index")
    if i > oldi then
        i = i + 1
        if cmd == "forward" then
            turtle.forward()
        end
        
        if cmd == "back" then
            turtle.back()
        end
        
        if cmd == "left" then
            turtle.turnLeft()
        end
        
        if cmd == "right" then
            turtle.turnRight()
        end
    end
end