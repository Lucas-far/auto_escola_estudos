

def mtd_paint_random(label: str):

    from random import choice

    inks: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[1:37m',
        '\033[1:38m')

    return f"{choice(inks)}{label}{inks[-1]}"


if __name__ == '__main__':
    print(var := mtd_paint_random(label='Teste'))
