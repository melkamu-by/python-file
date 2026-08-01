def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(num1), len(num2)) + 2
        top = num1.rjust(length)
        bottom = operator + num2.rjust(length - 1)
        line = "-" * length
        
        first_line.append(top)
        second_line.append(bottom)
        dashes.append(line)

        if show_answers:
            if operator == '+':
                res = str(int(num1) + int(num2))
            else:
                res = str(int(num1) - int(num2))
            answers.append(res.rjust(length))
            
    arranged_problems = "    ".join(first_line) + "\n" + \
                        "    ".join(second_line) + "\n" + \
                        "    ".join(dashes)
    
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems
# 1. መደበኛ ድርድር ለማየት
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print("\n" + "="*30 + "\n") # ለመለያያ ያህል ነው

# 2. መልሱንም አብሮ እንዲያሳይ (show_answers=True ሲሆን)
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))