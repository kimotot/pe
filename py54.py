"""Problem 54 「ポーカーハンド」 †
カードゲームのポーカーでは, 手札は5枚のカードからなりランク付けされている. 役を低い方から高い方へ順に並べると以下である.

役無し(ハイカード): 一番値が大きいカード
ワン・ペア: 同じ値のカードが2枚
ツー・ペア: 2つの異なる値のペア
スリーカード: 同じ値のカードが3枚
ストレート: 5枚の連続する値のカード
フラッシュ: 全てのカードが同じスート (注: スートとはダイヤ・ハート・クラブ/スペードというカードの絵柄のこと)
フルハウス: スリーカードとペア
フォーカード: 同じ値のカードが4枚
ストレートフラッシュ: ストレートかつフラッシュ
ロイヤルフラッシュ: 同じスートの10, J, Q, K, A
ここでカードの値は小さい方から2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, Aである. (訳注：データ中で10は'T'と表される)

もし2人のプレイヤーが同じ役の場合には, 役を構成する中で値が最も大きいカードによってランクが決まる:
poker.txtには1000個のランダムな手札の組が含まれている. 各行は10枚のカードからなる (スペースで区切られている): 最初の5枚がプレイヤー1の手札であり, 残りの5枚がプレイヤー2の手札である. 以下のことを仮定してよい

全ての手札は正しい (使われない文字が出現しない. 同じカードは繰り返されない)
各プレイヤーの手札は特に決まった順に並んでいるわけではない
各勝負で勝敗は必ず決まる
1000回中プレイヤー1が勝つのは何回か? (訳注 : この問題に置いてA 2 3 4 5というストレートは考えなくてもよい)"""

import basic

NH = 0
OP = 1
TP = 2
TC = 3
ST = 4
FL = 5
FH = 6
FC = 7
SF = 8
RF = 9

def handcount(tc):
    """ 引数tcで５枚のトランプカードが与えられる
        個々のトランプは('2','H")というタプルが要素になったリスト形式である

        引数の５枚のカードの数字と、種類をカウントする関数
        {'2':3,...} のように辞書の形式で返す"""

    dicn = [0] * 15
    dics = {'D': 0, 'C': 0, 'H': 0, 'S': 0}

    for (tn_str, ts) in tc:
        if tn_str.isnumeric():
            tn = int(tn_str)
        elif tn_str == 'T':
            tn = 10
        elif tn_str == 'J':
            tn = 11
        elif tn_str == 'Q':
            tn = 12
        elif tn_str == 'K':
            tn = 13
        elif tn_str == 'A':
            tn = 14

        dicn[tn] += 1
        dics[ts] += 1

    return dicn, dics


def analyzehand(tc):
    """役の判定をする関数"""
    listn, dics = handcount(tc)
    print(listn, dics)
    bign = []

    # フラッシュであるかを判定し変数に保存しておく
    isflash = False
    for n in dics.values():
        if n == 5:
            isflash = True
            break

    # ロイヤルフラッシュの判定
    if listn[10] == listn[11] == listn[12] == listn[13] == listn[14] == 1 and isflash:
        return RF, [14]

    # ストレートの判定
    isstraight = False
    for n in range(2, 11):
        if listn[n] == listn[n+1] == listn[n+2] == listn[n+3] == listn[n+4] == 1:
            isstraight = True
            bign = [n+4]
            break

    # ストレートフラッシュの判定
    if isflash and isstraight:
        return SF, bign

    # ストレートの判定
    if isstraight:
        return ST, bign

    # フラッシュの反映

if __name__ == "__main__":
    def test():
        print(analyzehand([('T', 'C'), ('J', 'D'), ('Q', 'S'), ('K', 'S'), ('A', 'D')]))


    test()
