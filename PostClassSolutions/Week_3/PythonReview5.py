# Code-Writing: too wide a net
def read_age(path):
    try:
        with open(path) as f:
            return int(f.read())
    except ValueError:
        return 0
    except FileNotFoundError:
            return 0
    finally:
        print("Done")

# Code-Tracing: frequency table
freq = {'the': 3, 'cat': 2, 'in': 1, 'mat': 2, 'is': 1, 'a': 1, 'hat': 1}
print(freq.get('dog', 0))   # 0
print(freq['dog'])          # KeyError
