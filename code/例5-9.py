def rate(origin, userInput):
    if not (isinstance(origin, str) and isinstance(userInput, str)):
        print('The two parameters must be strings.')
        return
    right = sum((1 for o, u in zip(origin, userInput) if o==u))
    return round(right/len(origin), 2)

print(rate('Python xiaowu', 'python xiaowu'))
