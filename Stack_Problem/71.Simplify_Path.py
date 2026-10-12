def simplifyPath(path):
    result = path.split("/")
    stack = []

    for pathh in result:
        if pathh == "" or pathh == ".":
            continue

        elif pathh == "..":
            if stack:
                stack.pop()

        else:
            stack.append(pathh)

    return "/" + "/".join(stack)

print(simplifyPath(path = "/home//foo/"))
print(simplifyPath(path = "/home/"))
print(simplifyPath(path = "/home/user/Documents/../Pictures"))
print(simplifyPath(path = "/../"))
print(simplifyPath(path = "/.../a/../b/c/../d/./"))