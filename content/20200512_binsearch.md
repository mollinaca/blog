Title: 二分探索
Date: 2020-05-12
Category: Tech
Tags: 競技プログラミング, アルゴリズム
Slug: binsearch
Authors: s.hosoya

今日たまたまやった練習問題  

[C - Buy an Integer](https://atcoder.jp/contests/abc146/tasks/abc146_c)  
が、二分探索の問題だった。  

最初読んでどうやればいいかわからず（計算量的にNの全探索ではないことはすぐわかったが、どうやって減らす？）、  
数学的に、累乗の指数から答え付近を探して、そこから探していけばいいのかな～とか考えていたけどうまくいかず解説を読んだら二分探索だった。  

あー、二分探索はわかるぞということでがんばって実装した。  

[提出](https://atcoder.jp/contests/abc146/submissions/13154541)  

最終的に出力する `ans` をしたから、上限を `over` として一番上に設定し、二つの平均を求め、  
平均が制約の上限より上なら `over` を平均へ入れ替え、下なら `ans` を平均といれかえる、というのを繰り返し、  
`ans`と`over`の差が1以下になったら終了という感じ。  

これはちょっと考えたけど、にぶたんということがわかったらなんとなく実装できた！

~~~python
#!/usr/bin/env python3

a,b,x = map(int,input().split())

ans = 0
over = (10**9)+1

while over - ans > 1:
    avg = int((ans+over)/2)
    if a*avg+b*len(str(avg)) <= x:
        ans = avg
    else:
        over = avg

print (ans)
~~~
