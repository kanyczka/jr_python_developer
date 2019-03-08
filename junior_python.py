class JuniorDeveloper():
    levels = ["junior", "mid", "senior"]

    def __init__(self, name, level, language):
        self.name = name
        self.level = level.lower()
        self.language = language
        if self.level not in JuniorDeveloper.levels:
            raise ValueError("Not a proper level name")
        else:
            print(f"{self.name} - a new {self.level} {self.language} developer was born")

    def __str__(self):
        return f"{self.name} {self.level} {self.language} developer"

    def seeking_job(self):
        print(f"{self.name} is looking for a job!")

