def vraca(nesto):
    for i in nesto:
        if i % 2 == 0:
            return True
        else:
            continue
    return False

print(vraca([1, 2, 5]))

danas