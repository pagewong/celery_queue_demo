from tasks import prod


def exe_qq():
    for i in range(10):
        prod.delay(f"A{i}")
    # prod.delay("cccccccccc")


if __name__ == '__main__':
    exe_qq()

