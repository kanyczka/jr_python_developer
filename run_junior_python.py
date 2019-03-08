from junior_python import JuniorDeveloper

def main():
    name = "Katarzyna Nyczka"
    level = "Junior"
    programming_language = "Python"
    new_developer = JuniorDeveloper(name, level, programming_language)
    new_developer.seeking_job()
    print("Help if you can, thanks :)")


if __name__ == "__main__":
    main()
