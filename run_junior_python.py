from junior_python import Developer


def main():
    name = "Katarzyna Nyczka"
    level = "junior"
    programming_language = "python"
    developer = Developer(name, level, programming_language)
    developer.seeking_job()
    print("Help if you can, thanks :)")


if __name__ == "__main__":
    main()
