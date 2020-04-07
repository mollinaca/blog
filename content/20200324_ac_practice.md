Title: AtCoder Practice 日記
Date: 2020-03-24
Category: Tech
Tags: atcoder, abc, programming
Slug: practice_0324
Authors: s.hosoya

先日の日記
[AtCoder Beginner Contest 159](https://blog.watarinohibi.tokyo/posts/2020/03/22/abc159/)に書いたように、AtCoderで競プロ、およびpythonの勉強を始めました。  
競技プログラミングもpythonもまったく初心者なので、いまはまだ灰レート、茶を目指している段階です。  

AtCoderには有志で作られている連携サービスのようなものがいくつかあり、そのうちの一つに [AtCoder Problems](https://kenkoooo.com/atcoder#/user/hstn) というのがあります。これは私のページ。  
AtCoderで記事を検索すると、この AtCoder Problems を見て、解いていない過去問題を埋めたり、streak を伸ばしたりしながらスコアを上げていったという事例があり、それをまねて頑張って streak を継続しています。  
streak を継続するためには、1日1問以上、まだ一度もACしていない問題をACする、という条件がつきます。  
私はまだ始めたばかりなので、解いていない過去問も大量にあるので、まだしばらく余裕をもって続けられそうですが、早晩A-B問題は尽きると思われるので、そのころには本格的にCは余裕、Dに挑戦できるようになってないとな、、といったところ。

現在 streak は20日で、AB問題はどちらも 1/4 ほど埋めたので、およそ2ヶ月ぐらいでここからどこまで成長できるか、がんばっていこうと思います。

2020/03/24 現在のステータス。

<a target=_blank href="https://blog.watarinohibi.tokyo/images/20200324_acp_stats.png"><img src="https://blog.watarinohibi.tokyo/images/20200324_acp_stats.png" width="500"></a>  
<a target=_blank href="https://blog.watarinohibi.tokyo/images/20200324_acp_de.png"><img src="https://blog.watarinohibi.tokyo/images/20200324_acp_de.png" width="500"></a>  
<a target=_blank href="https://blog.watarinohibi.tokyo/images/20200324_acp_hm.png"><img src="https://blog.watarinohibi.tokyo/images/20200324_acp_hm.png" width="500"></a>  

現在は、レコメンドで dif500 前後の問題が提案されているので、それに従い概ね500~600のC問題を含む未挑戦のABC過去問の、A-C問題を中心に解いています。

## 本日の挑戦

本日挑戦したのは、[ABC094](https://atcoder.jp/contests/abc094)。  
A問題B問題は無事さくっと解けたけど、C問題は問題文を見て愚直な解法はすぐに思いついたけど、また数学的にどう計算量を落とすか？で苦戦してギブアップ。

最初に実装した提出。当然TLE  
[https://atcoder.jp/contests/abc094/submissions/11185141](https://atcoder.jp/contests/abc094/submissions/11185141)  
毎回元のリストから対象の1要素を抜いたリストを生成し、そこから中央値を抽出するという手法。  
確実に解けるけど、N回リストのコピーとリストの操作が発生するため、O(N^2)かな？  

解説を見て作った答え、AC  
[https://atcoder.jp/contests/abc094/submissions/11185502](https://atcoder.jp/contests/abc094/submissions/11185502)  
言われてなるほどと思ったけど、中央値はソート済みの元リスト（Nが偶数）の中央のどちらかの値になるため、それよりも小さい数なら (2/N)-1 番目の要素、大きい数なら (2/N)+1 番目の要素でOK  
これなら、全部の要素に対してO(1)で答えがでるので、トータルはO(N)になる。  

うーん、解説みたらなるほどだけど、これをぱっと思いつけるようになりたい。。  
