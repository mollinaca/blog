Title: AtCoder Judge System Update Test Contest 202004
Date: 2020-04-05
Category: Tech
Tags: AtCoder, ABC, 競技プログラミング
Slug: testcontest_20200405
Authors: s.hosoya

---

[Judge System Update Test Contest 202004](https://atcoder.jp/contests/judge-update-202004) に参加しました。

# A

[A - Walking Takahashi](https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_a)  
現在位置がLとRの間ならそのまま出力、Lより小さいならLを、Rより大きいならRを出力すれば良い

[提出](https://atcoder.jp/contests/judge-update-202004/submissions/11582231)  
ちょっと冗長だった。absは不要だな。  
以下でOK

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S,L,R = map(int,input().split())
if S < L:
    print (L)
elif R < S:
    print (R)
else:
    print (S)
```

こっちのほうがシンプル。

# B 

[B - Picking Balls](https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_b)  
RとBの配列を持って置き、入力を受けてR/Bどちらかの配列に append して、入力を受け終わったらソートして R → B の順番に出力すればよい。  

[提出](https://atcoder.jp/contests/judge-update-202004/submissions/11583370)  

# C

ちょっと挑んで、あ！これ深さ優先探索だ！ってとこまではわかったけど、家庭の事情によりここで終了。  
制約が小さいので、全部列挙して出力させたほうが早いのかも。ｗ

<a target=_blank href="https://blog.watarinohibi.tokyo/images/20200405_c.jpg"><img src="https://blog.watarinohibi.tokyo/images/20200405_c.jpg" width="500"></a>  

と思ったら、やってる人いた。  
unratedなので、いろいろ遊んでる人もいるみたいｗ

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr"><a href="https://twitter.com/hashtag/JSUTC202004%E8%A7%A3%E8%AA%AC?src=hash&amp;ref_src=twsrc%5Etfw">#JSUTC202004解説</a><br>C問題です。 しっかり手を動かして10通り列挙しましょう。<br>これ以外の回答は認めません。 <a href="https://t.co/sGwr4vEy5V">pic.twitter.com/sGwr4vEy5V</a></p>&mdash; Reider (@Reider_AC) <a href="https://twitter.com/Reider_AC/status/1246786355666903040?ref_src=twsrc%5Etfw">April 5, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

次回のABCで、茶になるぞー





改めてトライする。



