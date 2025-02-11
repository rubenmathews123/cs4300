def count_words(filename):
    with open(filename, "r") as file:
        return len(file.read().split())

# Implementing Metaprogramming for Dynamic Test Cases
def generate_test_function(filename):
    def test_function():
        assert count_words(filename) > 0
    test_function.__name__ = f"test_count_words_{filename.replace('.', '_')}"
    return test_function