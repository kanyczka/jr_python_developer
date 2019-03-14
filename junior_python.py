class Developer():
    levels = ["Junior", "Mid", "Senior"]

    def __init__(self, name, level, language):
        self.name = name
        self.level = level.capitalize()
        self.language = language.capitalize()
        if self.level not in Developer.levels:
            raise ValueError("Not a proper level")
        else:
            print(f"{self.name} - a new {self.level} {self.language} Developer showed up.")

    def __str__(self):
        return f"{self.name} {self.level} {self.language} developer"

    def seeking_job(self):
        print(f"{self.name} is looking for a job!")



