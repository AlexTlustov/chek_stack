class Stack:
    def __init__(self, string, stack: list, new_element):
        self.string = string
        self.stack = stack
        self.new_element = new_element

    def is_empty(self) -> bool:
        return bool(self.stack)

    def push(self) -> str:
        self.new_stack = self.stack + self.new_element

    def pop(self): 
        return self.stack.pop()
    
    def peek(self):
        self.first_element = list(self.stack)
        return self.first_element[-1]

    def size(self):
        return len(self.stack)
    
    def сhek_stack(self):
        ob_open: list = ['(', '[', '{']
        ob_close: list = [')', ']', '}']
        for element in self.string:
            if element in ob_open:
                self.stack.append(element)
            elif element in ob_close:
                ind = ob_close.index(element)
                if Stack.is_empty(self) and (ob_open[ind] == self.stack[len(self.stack)-1]):
                    Stack.pop(self)
                else:
                    return print("Не сбалансирован.")
        if Stack.size(self) == 0:
            return print("Сбалансирован.")
        else:
            return print("Не сбалансирован.")

        



if __name__ == '__main__':
    str_balans1: str = '(((([{}]))))'
    str_balans2: str = '[([])((([[[]]])))]{()}'
    str_balans3: str = '{{[()]}}'
    str_no_balans1: str = '}{}'
    str_no_balans2: str = '{{[(])]}}'
    str_no_balans3: str = '[[{())}]'
    new_element: str = '1'
    stack: list = []
    chek_stack = Stack(str_balans1, stack, new_element)
    chek_stack.сhek_stack()