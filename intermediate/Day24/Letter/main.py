
class Letter:
    def __init__(self):
        self.get_names()
        for name in self.names:
            self.set_letter(name.strip())

    def get_letter(self):
        with open("./Input/Letters/starting_leter.txt") as letter_file:
            self.letter = letter_file.read()
    
    def get_names(self):
        with open("./Input/Names/invited_names.txt") as f:
            self.names = f.readlines()
    
    def set_letter(self, name):
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", 'w') as f:
            self.get_letter()
            self.letter = self.letter.replace("Name", name)
            f.write(self.letter)



Letter()