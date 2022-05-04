def importable_function():
    if __name__ == "__main__":
        print("Running 'function' directly.")
    else:
        print("Running 'function' indirectly.")

    global_dict = globals()
    print("Module name:", global_dict['__name__'])
    print("Parent package:", global_dict['__package__'])
    print("Spec:", global_dict['__spec__'])


if __name__ == "__main__":
    # shell command (1): python -m src.app
    # shell command (2): python src/app.py
    importable_function()
