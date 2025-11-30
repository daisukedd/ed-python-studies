def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

class Browser:
    def __init__(self):
        self.current_page = None
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url):
        if self.current_page:
            push(self.back_stack, self.current_page)

        self.current_page = url
        self.forward_stack.clear()
        print(f"Visitando: {url}")

    def back(self):
        if not self.back_stack:
            print("Não há página anterior.")
            return

        push(self.forward_stack, self.current_page)
        self.current_page = pop(self.back_stack)
        print(f"Voltando para: {self.current_page}")

    def forward(self):
        if not self.forward_stack:
            print("Não há página para avançar.")
            return

        push(self.back_stack, self.current_page)
        self.current_page = pop(self.forward_stack)
        print(f"Avançando para: {self.current_page}")

    def status(self):
        print("\n--- STATUS BROWSER ---")
        print("Página atual:", self.current_page)
        print("Voltar:", self.back_stack)
        print("Avançar:", self.forward_stack)
        print("--------------\n")


def main():
    browser = Browser()

    browser.visit("reddit.com")
    browser.visit("youtube.com")
    browser.visit("github.com")

    browser.back()      # volta para youtube
    browser.back()      # volta para reddit.com
    browser.forward()   # avança para youtube
    browser.visit("stackoverflow.com")  # limpa forward

    browser.status()

if __name__ == "__main__":
    main()
