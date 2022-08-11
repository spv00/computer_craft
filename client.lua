url = "http://please.lickthe.tips:6069/"

function get(dir)
    return http.get(url + dir).readAll()
end

print(get("test"))