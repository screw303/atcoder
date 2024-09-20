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
    
    # # パターン1: 整数1つ
    # n = int(data[0])
    
    # # パターン2: 整数のリスト
    # a = list(map(int, data[1:n+1]))
    
    # # パターン3: 文字列1つ
    # s = data[n+1]
    
    # # パターン4: 文字列のリスト
    # t = data[n+2:n+2+n]
    
    # # パターン5: 複数行の入力
    # m = int(data[n+2+n])
    # matrix = []
    # index = n+3+n
    # for i in range(m):
    #     matrix.append(list(map(int, data[index:index+n])))
    #     index += n
    
    # ここに問題解決のためのコードを書く
    # 例:
    # result = solve(n, a, s, t, matrix)

    
    # 結果を出力する
    # print(result)

if __name__ == "__main__":
    main()
