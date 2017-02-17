# coding:UTF-8
import copy

tuka = (200,100,50,20,10,5,2,1)
ans = []

def money(price,selected,tk):
	"""
	残価(price)を支払い可能な硬貨の組み合わせを求める
	price		:残価、あとどの金額を硬貨の組み合わせで作ればよいか
	selected	:今までに選択した硬貨枚数の組み合わせをリスト形式で保有している
	tk			:高額硬貨を0とし、何番目の硬貨で支払を計算するかを示す
	"""

	if tk == 7:									#再帰の復帰条件。最少額の硬貨まで探索した場合
		n_selected = list(selected)				#引数のリストをコピーして実体化する
		n_selected.append(price)				#1ポンド硬貨なので、残価イコール必要枚数となる
		ans.append(n_selected)					#グローバル変数に、硬貨枚数の組み合わせリストを保存する
	else:
		m = 0									#硬貨枚数。最初は０枚から考えてみる
		while price - m * tuka[tk] >= 0:		#候補硬貨枚数の金額が残価を超えない場合、処理を継続する
			n_selected = list(selected)
			n_selected.append(m)
			n_price = price - m * tuka[tk]
			money(n_price,n_selected,tk+1)
			
			m += 1

money(200,[],0)

for i,n in enumerate(ans):
	print(i,n)
print(len(ans))
