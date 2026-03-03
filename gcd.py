# 最大公約数
from functools import reduce


def gcd(a: int, b: int) -> int:
    # 負の値は絶対値に変換（GCDは一般に非負）
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def gcd_list(numbers: list) -> int:
    # バリデーション: 空リストのチェック
    if not numbers:
        raise ValueError("リストが空です")

    # バリデーション: すべて整数かチェック
    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("すべての要素は整数である必要があります")

    # reduceを使ってリスト全体のGCDを算出
    return reduce(gcd, numbers)


# 実行例
print(gcd_list([12, -18, 24]))  # 6
