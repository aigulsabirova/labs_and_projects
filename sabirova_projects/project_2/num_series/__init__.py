from .generator import random_series, sine_series, trend_series, v3_series
from .stats import mean, median, spread, summarize, max_min_info
from .moving_average import (
    simple_moving_average,
    simple_moving_average_naive,
    exponential_moving_average
)
from .io_json import save_series_json, load_series_json
from .io_file import load_series_txt, load_series_csv, load_series_auto

__all__ = [
    "random_series", "sine_series", "trend_series", "v3_series",
    "mean", "median", "spread", "summarize", "max_min_info",
    "simple_moving_average", "simple_moving_average_naive", "exponential_moving_average",
    "save_series_json", "load_series_json",
    "load_series_txt", "load_series_csv", "load_series_auto",
]

version = "2.0.0"