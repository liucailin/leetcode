def test(fn, *args):
    print("Input:", args)
    result = fn(*args)
    print("Output:", args, "return:", result)
    print()