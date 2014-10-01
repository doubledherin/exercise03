"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():
    question = raw_input("> ")
    question_list = question.split()
    first = int(question_list[1])
    second = int(question_list[2])

    if question_list[0] == "+":
        print arithmetic.add(first, second)

    if question_list[0] == "-":
        print arithmetic.subtract(first, second)

    if question_list[0] == "*":
        print arithmetic.multiply(first, second)

    if question_list[0] == "/":
        print arithmetic.divide(first, second)

# revise square input
    #if question_list[0] == "**2" or "square":
    #    return arithmetic.square(first, second)    

# revise for cube input
    #if question_list[0] == "":
    #    return arithmetic.cube(first, second)

    if question_list[0] == "**":
        print arithmetic.power(first, second)

    if question_list[0] == "%" or "mod":
        print arithmetic.mod(first, second)

if __name__ == '__main__':
    main()