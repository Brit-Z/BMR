
def rev(userInput):

    param = userInput.rpartition('(')
    if param[0]:
        userInput = param[0]
        param = param[2]
        param = param.replace(')', '')
        param = param.replace(' ', '')
        param = list(map(int, param.split(',')))
    else:
        userInput = param[2]


    userInput = userInput.lower()
    arrOfWord = userInput.split()
    i = 0
    for word in arrOfWord:
        if not(i+1 in param):
            arrOfWord[i] = word[::-1] 
        i += 1

    arrOfWord = arrOfWord[::-1]

    return ' '.join(arrOfWord)