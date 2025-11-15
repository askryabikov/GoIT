import re        # re stands for Regular Expression
from typing import Callable, Iterable


def generator_numbers(text: str) -> Iterable[float]:   # digits as text are returned as float numbers
    """
    In this function generator pattern:
    yields one number at a time using `yield`

    Yields:
        float: Each number in the text to be converted to float.

    Regular expression:
        - RE with word boundaries (\b) to avoid catching pieces of words.
        - Pattern r"\b\d+(?:\.\d+)?\b" stands for:
            * one or more digits:          \d+
            * optional decimal part:       (?:\.\d+)?
            * boundaries on both ends:     \b ... \b
    """
    pattern = r"\b\d+(?:\.\d+)?\b"     # integer or decimal with dot as separator

    # finditer returns an iterator over all non-overlapping matches in the text
    for match in re.finditer(pattern, text):
        number_str = match.group(0)    # exact substring that matched the pattern
        number = float(number_str)     # convert to float for further calculations
        yield number                   # yield one number at a time


def sum_profit(text: str, func: Callable[[str], Iterable[float]]) -> float:
    """
    Calculates total income using generator function.

    Args:
        text (str): Input text that may contain income
        func (Callable[[str], Iterable[float]]): 
            text being returned as an iterable/generator of floats to summarize

    Returns:
        float: Sum of all numbers produced by the generator function.
    """
    numbers = func(text)     # get generator (or iterable) with all numbers
    total = sum(numbers)     # sum of numbers
    return total


# TEST

if __name__ == "__main__":
    demo_text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )

    total_income = sum_profit(demo_text, generator_numbers)
    print(f"Загальний дохід: {total_income}")      # Answer expected: 1351.46
