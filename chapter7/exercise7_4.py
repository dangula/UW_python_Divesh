
def eval_loop():
    while True:
        line = raw_input("eval_loop>")
        if line == 'done':
            break
        print eval(line)

eval_loop()