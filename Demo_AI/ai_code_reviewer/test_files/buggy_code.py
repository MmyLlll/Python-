def bad_function(x, y):
    result = x / y
    return result

def inefficient_search(target, items):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

def unsafe_input_processing(user_input):
    eval(user_input)
    return "处理完成"