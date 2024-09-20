import sys
input = sys.stdin.read

def main():
    # 標準入力からデータを読み取る
    data = input().strip().split()

    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2 : len(data) + 1]))

    # 結果を出力する
    a[:] = a[n-k :] + a[: n-k]
    # 拡張スライス
    # [1, 2, 3, 4, 5]  n=2
    # arr[n:]: [3, 4, 5] 
    # arr[:n]: [1, 2] 

    # print(a)
    print(" ".join(map(str, a)))
    #


if __name__ == "__main__":
    main()
