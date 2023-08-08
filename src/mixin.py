class Mixinlang:
    def __init__(self, language="EN"):
        self.language = language

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return self


