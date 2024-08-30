def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems.";
    
    line1 = [];
    line2 = [];
    line3 = [];
    line4 = [];

    for problem in problems:
        num1, sign, num2 = problem.split();
        
        if sign not in ['+', '-']:
            return "Error: Operator must be '+' or '-'.";
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits.";
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits.";
        
        width = max(len(num1), len(num2)) + 2;  
        
        if sign == '+':
            result = str(int(num1) + int(num2));
        elif sign == '-':
            result = str(int(num1) - int(num2));
        else:
            result = ""
        
        line1.append(num1.rjust(width));
        line2.append(sign + num2.rjust(width - 1));
        line3.append('-' * width);
        if show_answers:
            line4.append(result.rjust(width));
        else:
            pass

    if not show_answers:
        arranged_problems = '\n'.join(['    '.join(line1), 
                                   '    '.join(line2), 
                                   '    '.join(line3)])
    else:
        arranged_problems = '\n'.join(['    '.join(line1), 
                                   '    '.join(line2), 
                                   '    '.join(line3),
                                   '    '.join(line4)])
    
    return arranged_problems
