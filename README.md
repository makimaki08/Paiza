# Paiza用のリポジトリ
Paizaが回答を公開している事もあり、PrivateからPublicに変更


Pythonテクニック
	辞書型
		キーだけ取得「.keys()」
		値だけ取得「.values()」
		keyとvalueを同時に取得「.items()」
		参考資料
			https://qiita.com/ysuzuki19/items/ec592d30566a436996aa

	累積和
		配列型の累積和を求める場合は、numpyを利用するのが良い
		参考資料
			https://qiita.com/bluepost59/items/b3d982097b48488ed070
	区間和
		素直に区間の始まりと終わりを全探索して実装すると、計算量が O(N^2) となってしまい実行時間制限に間に合いません。
		累積和 S[i] = A[1] + ... + A[i] を用います。
		A[l]+...+A[r] = (A[0]+...A[r]) - (A[0]+...A[l-1]) = S[r]-S[l-1]
		の関係より、累積和 S を前もって計算しておけば、以上の関係から区間 l,r の和を O(1) で求めることができるので
		全体の計算量を O(N) にできます。
