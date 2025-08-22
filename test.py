def walk(top):
    if top ==0:
        return 0
    return top+walk(top-1)

print(walk(2))