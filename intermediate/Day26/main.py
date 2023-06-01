import pandas as pd


class NatoPhonetic:
    def __init__(self):
        file_name = "nato_phonetic_alphabet.csv"
        data = pd.read_csv(file_name)
        self.data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

        self.ask_for_name()
        self.analize_letter()

    def analize_letter(self):
        output = [self.data_dict.get(ch) for ch in self.name]
        print(output)

    def ask_for_name(self):
        self.name = input("what is your name: ").upper()

NatoPhonetic()