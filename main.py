from image_constructor import *


def main(num: int = 1) -> None:
    constructor = ImageConstructor()
    for i in range(num):
        constructor.main(i)


if __name__ == '__main__':
    main()