# Show document name and pages to be printed in a print queue

class PrintQueue:
    def __init__(self):
        self.queue = []

    def add_document(self, document_name, num_pages):
        self.queue.append({"document_name": document_name, "num_pages": num_pages})
        print(f"Document '{document_name}' with {num_pages} pages added to the print queue.")

    def print_next_document(self):
        if self.queue:
            document = self.queue.pop(0)
            print(f"Printing document: {document['document_name']} ({document['num_pages']} pages)")
        else:
            print("No documents in the print queue.")

def simulate_print_queue():
    print_queue = PrintQueue()

    print_queue.add_document("The Hitchhiker's Guide to the Galaxy.pdf", 500)
    print_queue.add_document("Guidorizzi.docx", 460)
    print_queue.add_document("Presentation.pptx", 20)

    while print_queue.queue:
        print_queue.print_next_document()

    print("All documents have been printed!")

if __name__ == "__main__":
    simulate_print_queue()