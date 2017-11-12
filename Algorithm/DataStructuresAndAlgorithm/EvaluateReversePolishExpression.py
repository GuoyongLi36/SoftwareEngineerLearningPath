class Solution:
    def evalRPN(self, tokens):
        stack=[];
        for i in tokens:
            if i =='+':
                stack[-2]=stack[-1]+stack[-2];
                stack.pop();
            elif i =='-':
                stack[-2]=stack[-2]-stack[-1];
                stack.pop();
            elif i =='*':
                stack[-2]=stack[-1]*stack[-2];
                stack.pop();
            elif i =='/':
                stack[-2]=int(stack[-2]/stack[-1]);
                stack.pop(); 
            else:
                stack.append(int(i));
        return stack[0];
