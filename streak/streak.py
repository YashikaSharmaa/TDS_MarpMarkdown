from typing import Iterable, List

def detect_streaks(numbers: Iterable[int]) -> List[List[int]]:
    """
    Detects streaks of positive numbers in an iterable of integers.

    Args:
        numbers: An iterable of integers.

    Returns:
        A list of lists, where each inner list represents a streak of positive numbers.
    """
    streaks = []
    current_streak = []
    for number in numbers:
        if number > 0:
            current_streak.append(number)
        else:
            if current_streak:
                streaks.append(current_streak)
                current_streak = []
    if current_streak:
        streaks.append(current_streak)
    return streaks
