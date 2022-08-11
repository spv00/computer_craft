url = "http://please.lickthe.tips:6069/"

function get(dir)
    return http.get(url .. dir).readAll()
end

i = 0

while true do
    oldi = i
    i = tonumber(get("index"))
    print("i: " .. i)
    print("oldi: " .. oldi)
    if i < oldi then
        cmd = get("cmd")
        print(cmd)
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