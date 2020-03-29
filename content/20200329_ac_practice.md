Title: 競プロ Practice 日記
Date: 2020-03-29
Category: Tech
Tags: AtCoder, 競プロ, プログラミング, AOJ
Slug: practice_20200329
Authors: s.hosoya

## AOJ に挑戦した

競プロの基礎練習編として、AOJがお勧めされていたのでトライしてみた。  

[AIZU ONLINE JUDGE](http://judge.u-aizu.ac.jp/onlinejudge/)  
[mystatus](http://judge.u-aizu.ac.jp/onlinejudge/user.jsp?id=hstn2#3)  

入門編である ITP1 について、ITP1_1からITP1_6 まで、24問を解いた。  
ABCでA/Bは概ねできてるのでほとんど躓かずにできたけど、一部やったことないタイプの問題とかもあって面白かった。  
ITP1は全部挑戦しようと思います。

## AtCoder 本日の練習

ABC133のA～Cに挑戦。  
A/Bはさくっとできて、Cにまたちょっと苦戦。  
最初見た時に、全探索すると計算量が間に合わないから計算量落とす工夫がいるなと思い、その過程で場合分け等々を考えて計算していたけど、そもそも答えがWAしてしまい導出ロジックがうまく組めず。。  

結果的に難しく考えすぎてて、条件に収まる範囲での全探索であれば十分for文で行けることがわかったので、それで実装しなおしてACできた。  

<a target=_blank href="https://blog.watarinohibi.tokyo/images/acp_20200329.png"><img src="https://blog.watarinohibi.tokyo/images/acp_20200329.png" width="500"></a>  
うーん、あとで考えればあーこれで良いやなんだけど、これをさくっと思いつきたい。  
