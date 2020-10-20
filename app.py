from book_openers.gutenberg import main
from gutenbergpy.gutenbergcache import GutenbergCache
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        main()
    elif argv[1] == "catalogue":
        GutenbergCache.create()
    else:
        try:
            id = int(argv[1])
        except:
            print("invalid options")
        else:
            main(id)
