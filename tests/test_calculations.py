import pytest
from calculations import split_per_500, format_split, watts_from_split


def test_split_for_2k():
    # 2000m in 7:00 (420s) -> 1:45 per 500m
    assert split_per_500(2000, 420) == 105


def test_split_rejects_zero_distance():
    with pytest.raises(ValueError):
        split_per_500(0, 420)


def test_format_split():
    assert format_split(107.5) == "1:47.5"
    assert format_split(105) == "1:45.0"
    assert format_split(119.96) == "2:00.0"


def test_watts_at_two_minute_split():
    # A 2:00 split is about 203 watts on a Concept2
    assert watts_from_split(120) == pytest.approx(202.6, abs=0.5)

def parse_split(text: str) -> float:
    """Turn '1:47.5' or '107.5' into seconds."""
    text = text.strip()
    if ":" in text:
        minutes, seconds = text.split(":")
        return int(minutes) * 60 + float(seconds)
    return float(text)