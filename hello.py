import argparse

def add(x, y):
    return int(x) + int(y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("parametro1")
    parser.add_argument("parametro2")
    args = parser.parse_args()
    print(args.parametro1) 
    print(args.parametro2) 
    print(add(args.parametro1, args.parametro2))

