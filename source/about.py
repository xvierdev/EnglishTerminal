# about team
import time
import util

string = """\tEnglish Terminal is a simple terminal that can be used to play games, do translations, and more.
\tIt is a project developed by the students: @xvierdev, @Cubo3d and @bruna-hm.
\tThe project is open source and can be found at https://github.com/xvierdev/EnglishTerminal. Enjoy!
"""


def about():
    util.clear_console()
    print("\n" * 2)
    for i in range(string.count("\n")):
        print(string.split("\n")[i])
        time.sleep(0.1)
    print("\n" * 2)


if __name__ == "__main__":
    about()
