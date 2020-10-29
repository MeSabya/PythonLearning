quotes = (
'A man is not complete until he is married. Then he is finished.',
'As I said before, I never repeat myself.',
'Behind a successful man is an exhausted woman.',
'Black holes really suck...',
'Facts are stubborn things.'
)
'''
Model view controller 
'''

class QuoteTerminalModel:
    def get_quote(self, n):
        try:
            val = quotes[n]
        except IndexError as err:
            value = 'not found'
        return val

class QuoteTerminalView:
    def show(self, quote):
        print(f'And the quote is: "{quote}"')

    def error(self, msg):
        print(f'Error : {msg}')

    def select_quote(self):
        return input('Which quote number would you like to select')


class QuoteTerminalController:
    def __init__(self):
        self._model = QuoteTerminalModel()
        self._view = QuoteTerminalView()
    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self._view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self._view.error(f'Incorrect index')
        quote = self._model.get_quote(n)
        self._view.show(quote)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()