"""
Log analyzer script.

Usage examples (from terminal):

    python main.py log.txt
    python main.py log.txt error

The script:
- reads a log file
- counts number of error entries: INFO / DEBUG / ERROR / WARNING
- optionally prints all lines of a specific level (e.g. ERROR)
"""

import sys
from typing import List, Dict

LOG_LEVELS = ("INFO", "DEBUG", "ERROR", "WARNING")   # Log warning levels

def parse_log_line(line: str) -> Dict[str, str] | None:
    """
    Parse single log line.

    Expected format:
        "YYYY-MM-DD HH:MM:SS LEVEL message..."

    Returns:
        dict with keys: date, time, level, message
        or None if line is invalid/empty.
    """

    line = line.strip()  # Removes leading/trailing whitespaces and newlines
    # If line becomes empty after strip → treat as invalid / empty record:
    if not line:
        return None  # empty line -> skip

    # Line consists of 4 logical parts:
    # date, time, level, and the rest as message.
    # maxsplit=3 means:
    # "a b c d e f".split(maxsplit=3) → ["a", "b", "c", "d e f"]
    parts = line.split(" ", 3)
    # If less than 4 parts - format is broken
    if len(parts) < 4:
        return None

    date_str, time_str, level_str, message = parts
    # Normalize level to uppercase, so "error" and "ERROR" become the same:
    level_str = level_str.upper()

    return {
        "date": date_str,
        "time": time_str,
        "level": level_str,
        "message": message,
    }


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Load and parse all log lines from file.

    Functional style:
        - map(parse_log_line, file)   → apply parser to each line
        - filter(None, ...)           → drop lines where parser returned None
        - list(...)                   → collect into list

    Returns:
        list of dictionaries with parsed logs
        or None if file read error occurred
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # map → apply parse_log_line to each line in file
            # filter(None, ...) → keep only those results which are not None
            logs = list(filter(None, map(parse_log_line, file)))
        return logs   # if no errors detected - return as a list

    except FileNotFoundError:       # in case file not found         
        print(f"Помилка: файл '{file_path}' не знайдено.")
        return None   # Error warning
    except OSError as e:
        # OSError stands for numerous issues: permissions, hardware, etc.
        print(f"Помилка читання файлу '{file_path}': {e}")
        return None   # Error warning


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Filter logs by given level (case-insensitive).

    Uses list comprehension (functional style):
        [log for log in logs if ...]
    """

    level = level.upper()    # Normalize input to uppercase
    return [log for log in logs if log.get("level") == level]
# Explanation:
# 1. for log in logs
#    cycle each line (dictionary) in the list
#
# 2. log.get("level")
#    get "level" value and returns None if key is missing
#
# 3. == level
#    keep only those logs where stored level equals desired level
#
# 4. result is a new filtered list


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Count log records for each known level.

    Uses dict comprehension + generator expressions:
        {level: sum(1 for log in logs if ...) for level in LOG_LEVELS}
    """
    return {
        level: sum(1 for log in logs if log.get("level") == level)
        for level in LOG_LEVELS
    }


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Good looking format for warnings

    Uses:
        - sorted(..., key=lambda x: x)  → explicit lambda as in FP examples
    """

    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level in sorted(LOG_LEVELS, key=lambda x: x):   # sorted with lambda
        print(f"{level:<17}| {counts.get(level, 0)}")   # {level:<17} → align string to width 17


def display_logs_for_level(logs: List[Dict[str, str]], level: str) -> None:
    """
    Print all log entries for given level in good lokking format

    Example output line:
        2024-01-22 09:00:45 - Database connection failed
    """
    level_upper = level.upper()
    filtered = filter_logs_by_level(logs, level_upper)

    print(f"\nДеталі логів для рівня '{level_upper}':")
    if not filtered:
        print("(Записів не знайдено.)")
        return

    for log in filtered:   # start cycle for checking each filtered line
        print(f"{log['date']} {log['time']} - {log['message']}")
        # example of an outcome: 2024-01-22 09:00:45 - Database connection failed


def main() -> None:
    """
    Entry point for CLI application.

    Usage:
        python main.py path/to/logfile.log
        python main.py path/to/logfile.log error

    First argument:
        - path to log file

    Optional second argument:
        - log level to show details (info, error, debug, warning)
    """
    if len(sys.argv) < 2:
        print("Використання: python main.py path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    # 0 - script name. example = main.py
    # 1 - path to the log file = log.txt
    level_arg = sys.argv[2] if len(sys.argv) >= 3 else None 
    # 2 - 2 or more - too much arguments, system overload oh my god

    logs = load_logs(file_path)
    if logs is None:
        sys.exit(1)   # error already printed in load_logs

    counts = count_logs_by_level(logs) # counts each type of warning
    display_log_counts(counts)

    if level_arg:
        display_logs_for_level(logs, level_arg)

if __name__ == "__main__":
    main()