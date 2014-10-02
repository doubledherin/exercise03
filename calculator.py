"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():
    question = raw_input("> ")
    question_list = question.split()
    question_list.append(0)
    print question_list
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

    if question_list[0] == "**2" or question_list[0] == "square":
        print arithmetic.square(first)    

# revise for cube input
    #if question_list[0] == "":
    #    print arithmetic.cube(first)

    if question_list[0] == "pow":
        print arithmetic.power(first, second)

    if question_list[0] == "%" or question_list[0] == "mod":
        print arithmetic.mod(first, second)

if __name__ == '__main__':
    main()