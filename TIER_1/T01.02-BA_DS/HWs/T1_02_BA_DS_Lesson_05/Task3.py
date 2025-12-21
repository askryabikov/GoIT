import timeit
from pathlib import Path

"""
PURPOSE:
- Compare 3 search algorithms on 2 texts (articles) using timeit:
  1) Boyer-Moore
  2) Knuth-Morris-Pratt (KMP)
  3) Rabin-Karp
- For each text measure time for:
  - existing substring (present in text)
  - non-existing substring (absent in text)
- Print results and show a diagram

How it works:
1) Read both articles from files
2) Pick one “existing” substring per article
3) Build one “non-existing” substring
4) Benchmark each algorithm with timeit
5) Print table-like results + plot comparison

Structure:
A) Helpers:
   - read_file() - reads text with fallback encodings
   - measure_time() - wraps timeit
   - make_non_existing_pattern() - generates safe missing substring
B) Algorithms:
   - rabin_karp_search() + polynomial_hash()
   - boyer_moore_search()
   - kmp_search() + compute_lps()
C) Output:
   - print_results()
   - plot_results()
"""


BASE_DIR = Path(__file__).resolve().parent    # to read articles
    
def read_file(filename):
    file_path = BASE_DIR / filename
    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:                  # article 2
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="cp1251", errors="replace") as f:   # article 1
            return f.read()


def polynomial_hash(s, base=256, modulus=101):
    n = len(s)                # where n - number of symbols in string
    hash_value = 0            # starting point

    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1, modulus)  # calculate base power under modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus  # ord for Unicode
    return hash_value


def rabin_karp_search(main_string, substring):
    m = len(substring)        # lenght of searched string
    n = len(main_string)      # lenght of text

    if m == 0:                # for empty strings
        return 0
    if m > n:                 # do not start if search is longer than text
        return -1

    base = 256                # base for polynominal hash
    modulus = 101             # modulus to limit hash size

    # Hash of the substring (pattern)
    sub_hash = polynomial_hash(substring, base, modulus)

    # Hash of the first window of text with size m
    window_hash = polynomial_hash(main_string[:m], base, modulus)

    # base^(m-1) mod modulus
    h_multiplier = pow(base, m - 1, modulus) # removes leftmost char from the rolling hash

    # Slide over all possible windows
    for i in range(n - m + 1):
        if sub_hash == window_hash:                 # if they match:
            if main_string[i:i + m] == substring:   # direct comparing of substring
                return i

        if i < n - m:     # Update rolling hash for the next window (if any)
            # Remove leftmost char
            window_hash = (window_hash - ord(main_string[i]) * h_multiplier) % modulus
            # Shift window hash and add new rightmost char:
            window_hash = (window_hash * base + ord(main_string[i + m])) % modulus

    return -1


def build_shift_table(pattern):
    table = {}
    length = len(pattern)

    # For each char except the last one:
    # shift = length - index - 1
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    # If last char is not in table, default shift is length
    table.setdefault(pattern[-1], length)

    return table


def boyer_moore_search(text, pattern):
    if len(pattern) == 0:
        return 0
    if len(pattern) > len(text):
        return -1

    shift_table = build_shift_table(pattern)
    i = 0    # start position in text

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # start comparing from the end of pattern

        while j >= 0 and text[i + j] == pattern[j]:   
            j -= 1            # Move left while characters match

        if j < 0:             # If j < 0, we matched the whole pattern
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
        # where:
        # 1. text[i + len(pattern) - 1] - symbol in text matched with last symbol of pattern
        # 2. shift_table.get - holds number of symbols to shift

    return -1


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0  # length of the current longest prefix-suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    if len(pattern) == 0:
        return 0
    if len(pattern) > len(main_string):
        return -1

    m = len(pattern)
    n = len(main_string)

    lps = compute_lps(pattern)

    i = 0           # index for main_string
    j = 0           # index for pattern

    while i < n:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]     # jump in pattern using lps
        else:
            i += 1             # can't jump - move in text

        if j == m:             # if matches
            return i - j

    return -1


# Benchmark


# for a guaranteed non-existing string in article:
def make_non_existing_pattern(texts, base="no_such_substring"):
    s = base
    k = 0
    while any(s in t for t in texts):
        k += 1
        s = f"{base}_{k}"
    return s


def measure_time(func, text, pattern, number=5, repeat=5):
    """
    Benchmark function `func(text, pattern)`.

    - timeit.repeat runs the code multiple times.
    - `number` = how many calls per one run (AVG inside a run)
    - `repeat` = how many runs total

    For calculating we will use: min(times) / number
    """
    times = timeit.repeat(lambda: func(text, pattern), number=number, repeat=repeat)
    return min(times) / number


def print_results(results):
    print("\n--- Benchmark results (seconds per call) ---")
    for row in results:
        print(
            f"{row['text_name']} | {row['pattern_type']}: "
            f"BM={row['bm']:.6f}  KMP={row['kmp']:.6f}  RK={row['rk']:.6f}"
        )


def plot_results(results):
    """
    Build a graphic bar chart  with 3 algorithms per group for:
      - Article 1 existing / non-existing
      - Article 2 existing / non-existing

    *If matplotlib is missing, we will skip plotting
    """
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ModuleNotFoundError:
        print("\nmatplotlib not installed — skipping plot.")
        return

    labels = [f"{r['text_name']}\n{r['pattern_type']}" for r in results]
    bm = [r["bm"] for r in results]
    kmp = [r["kmp"] for r in results]
    rk = [r["rk"] for r in results]

    x = np.arange(len(labels))
    width = 0.25

    plt.figure(figsize=(10, 6))
    plt.bar(x - width, bm, width, label="Boyer-Moore")
    plt.bar(x, kmp, width, label="KMP")
    plt.bar(x + width, rk, width, label="Rabin-Karp")

    plt.xticks(x, labels)
    plt.ylabel("Seconds per call")
    plt.title("Substring search benchmark (Article1 vs Article2, existing vs non-existing)")
    plt.legend()
    plt.tight_layout()
    plt.show()



# Main

if __name__ == "__main__":
    text1 = read_file("article1.txt")
    text2 = read_file("article2.txt")

    # existing patterns (one per article)
    existing_1 = "Алгоритми"
    existing_2 = "Рекомендаційні системи"

    if existing_1 not in text1:
        raise ValueError("Existing substring for article1.txt was not found. Change existing_1.")
    if existing_2 not in text2:
        raise ValueError("Existing substring for article2.txt was not found. Change existing_2.")


    # Create a guaranteed "non-existing" substring (absent in both texts)
    non_existing = make_non_existing_pattern([text1, text2], base="хахахахахаха")

    # “List style” organization similar to your sorting benchmark example
    test_texts = [
        ("Article 1", text1, existing_1),
        ("Article 2", text2, existing_2),
    ]

    algorithms = {
        "bm": boyer_moore_search,
        "kmp": kmp_search,
        "rk": rabin_karp_search,
    }

    results = []

    # For each text: benchmark both existing and non-existing patterns
    for text_name, text, existing in test_texts:
        patterns = {
            "existing": existing,
            "non_existing": non_existing,
        }

        for pattern_type, pattern in patterns.items():
            row = {
                "text_name": text_name,
                "pattern_type": pattern_type,
                "bm": measure_time(algorithms["bm"], text, pattern),
                "kmp": measure_time(algorithms["kmp"], text, pattern),
                "rk": measure_time(algorithms["rk"], text, pattern),
            }
            results.append(row)

    print_results(results)
    plot_results(results)
