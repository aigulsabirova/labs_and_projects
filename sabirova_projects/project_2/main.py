import argparse
import sys
from typing import List, Optional
from num_series import (
    v3_series, summarize, max_min_info,
    simple_moving_average, simple_moving_average_naive, exponential_moving_average,
    save_series_json
)

def build_series(n: int, seed: int) -> List[float]:
    return v3_series(n, seed)

def print_header(source: str) -> None:
    print("=" * 60)
    print(f"Источник данных: {source}")
    print("-" * 60)

def print_stats(stats: dict) -> None:
    print(f"Среднее арифметическое : {stats['mean']:>10.4f}")
    print(f"Медиана                : {stats['median']:>10.4f}")
    print(f"Размах (max - min)     : {stats['spread']:>10.4f}")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Вариант 3")
    parser.add_argument("--n", type=int, default=1000, help="количество точек")
    parser.add_argument("--window", type=int, default=5, help="размер окна k")
    parser.add_argument("--alpha", type=float, default=0.3, help="коэффициент EMA")
    parser.add_argument("--seed", type=int, default=42, help="зерно")
    parser.add_argument("--save", metavar="PATH", help="сохранить в JSON")
    return parser

def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        data = build_series(args.n, args.seed)
        source = f"Сгенерирован (n={args.n}, seed={args.seed})"
    except ValueError as err:
        print(f"Ошибка получения ряда: {err}", file=sys.stderr)
        return 1

    if args.save:
        try:
            save_series_json(data, args.save)
            print(f"[сохранено] {args.save} ({len(data)} точек)")
        except ValueError as err:
            print(f"Ошибка сохранения: {err}", file=sys.stderr)
            return 1

    try:
        stats = summarize(data)
        extra = max_min_info(data)
        sma_run = simple_moving_average(data, args.window)
        sma_naive = simple_moving_average_naive(data, args.window)
        ema = exponential_moving_average(data, args.alpha)
    except ValueError as err:
        print(f"Ошибка анализа: {err}", file=sys.stderr)
        return 1

    print_header(source)
    print_stats(stats)

    print(f"Разность max-min (по модулю): {extra['diff_abs']:>10.4f}")
    print(f"Индекс максимума: {extra['max_index']}")
    print(f"Индекс минимума : {extra['min_index']}")
    print("-" * 60)

    print(f"Первые 10 исходного ряда: {[round(x, 3) for x in data[:10]]}")
    print(f"Первые 10 SMA (бегущая) : {[round(x, 3) for x in sma_run[:10]]}")
    print(f"Первые 10 SMA (наивная) : {[round(x, 3) for x in sma_naive[:10]]}")
    print(f"Первые 10 EMA           : {[round(x, 3) for x in ema[:10]]}")
    print("-" * 60)

    if sma_run == sma_naive:
        print("ПРОВЕРКА: Обе реализации SMA работают корректно (совпадают).")
    else:
        print("ОШИБКА: Реализации SMA дают разные результаты!")

    print("=" * 60)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())