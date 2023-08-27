def longestprefix(strings):
    prefix=strings[0]
    for i in strings:
        while not i.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix:
                return "no common prefix"
    return prefix


print("hello")
string = ["clap", "clear","clever"]
lol=longestprefix(string)
print(lol)