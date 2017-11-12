class Solution:
    def conversion(self, tokens):
        output=[];
        operators=[];
        prioritys={'(':3, '*':2, '/':2, '+':1, '-':1};
        for i in tokens:
            print(output);
            print(operators);
            if i ==')':
                while (operators[-1]!='('):
                    output.append(operators[-1]);
                    operators.pop();
                operators.pop();
            elif i in prioritys:
                priority=prioritys[i];
                while len(operators)>0 and (prioritys[ operators[-1]] >= priority) and (operators[-1] !='('):
                    output.append(operators[-1]);
                    operators.pop();
                operators.append(i);
            else:
                output.append(i);
        while len(operators)>0:
            output.append(operators[-1]);
            operators.pop();
        return output
