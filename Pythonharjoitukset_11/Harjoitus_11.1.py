class Publication:
    def __init__(self, name):
        self.name = name


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
    def print_info(self):
        print(f"Lehden nimi:   {self.name} \nPäätoimittaja: {self.editor}\n")


class Book(Publication):
    def __init__(self, name, writer, pages):
        super().__init__(name)
        self.writer = writer
        self.pages = pages
    def print_info(self):
        print(f"Kirjan nimi:   {self.name} \nKirjailija:    {self.writer} \nKirjan pituus: {self.pages} sivua")


# Pääohjelma
ankka = Magazine("Aku Ankka", "Aki Hyyppä")
ankka.print_info()

hytti = Book("Hytti n:o 6", "Rosa Liksom", 200)
hytti.print_info()