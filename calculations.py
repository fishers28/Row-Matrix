def split_per_500(distance_m: float, time_seconds: float) -> float:
    """Return the average time (in seconds) to row 500m."""
    if distance_m <= 0:
        raise ValueError("Distance must be greater than 0")
    if time_seconds <= 0:
        raise ValueError("Time must be greater than 0")
    return time_seconds * 500 / distance_m


def format_split(seconds: float) -> str:
    """Turn a number of seconds into a split string, e.g. 107.5 -> '1:47.5'."""
    total_tenths = round(seconds * 10)
    minutes, tenths = divmod(total_tenths, 600)
    return f"{minutes}:{tenths / 10:04.1f}"


def watts_from_split(split_seconds: float) -> float:
    """Concept2 formula: watts = 2.80 / (seconds per meter) ** 3."""
    if split_seconds <= 0:
        raise ValueError("Split must be greater than 0")
    pace_per_meter = split_seconds / 500
    return 2.80 / pace_per_meter ** 3


def parse_split(text: str) -> float:
    """Turn '1:47.5' or '107.5' into seconds."""
    text = text.strip()
    if ":" in text:
        minutes, seconds = text.split(":")
        return int(minutes) * 60 + float(seconds)
    return float(text)