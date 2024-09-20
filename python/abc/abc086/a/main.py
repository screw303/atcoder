import sys
input = sys.stdin.read
from collections import defaultdict, deque
import heapq
import itertools
import math
import bisect
import string

def main():
    # 標準入力からデータを読み取る
    data = input().strip().split()
    # input(): ユーザーからの入力
    # strip(): trim()
    # split(): 文字列を空白で分割、リストに変換します。「Hello World」は['Hello', 'World']
    seki = int(data[0])*int(data[1] )
    if (seki % 2 == 1 ):
        print("Odd")
    else :
        print("Even")
    # ここに問題解決のためのコードを書く
    # 例:
    # result = solve(n, a, s, t, matrix)

    
    # 結果を出力する
    # print(result)

if __name__ == "__main__":
    main()
