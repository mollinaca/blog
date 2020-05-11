Title: bit全探索
Date: 2020-05-11
Category: Tech
Tags: 競技プログラミング, アルゴリズム
Slug: bit-fullsearch
Authors: s.hosoya

昨日の ABC167 - C は、bit全探索というアルゴリズムを使った問題だったらしい。知らなかったので学んだ。  

[bit全探索について簡単にまとめる](https://qiita.com/hareku/items/3d08511eab56a481c7db)   
[Python de アルゴリズム（bit全探索）](https://qiita.com/gogotealove/items/11f9e83218926211083a)   
[ビット演算 (bit 演算) の使い方を総特集！](https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361)   

## どういう手法か

二つの状態を持つ特定の要素群に対して全組み合わせを列挙するのに使う。  
状態を "0" or "1" の二進数で定義し、例えば要素が三つなら

> 000  
> 001  
> 010  
> 011  
> 100  
> 101  
> 110  
> 111  

の8パターンで全てを表現できる、ということ。なるほどと思った。  

### 例題

> みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。
> 財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。

三つの果物について、買うor買わないを全パターン列挙し、それぞれの値段が条件に収まるか、というもの。

[1.py](https://github.com/mollinaca/ac/blob/master/code/test/bit%E5%85%A8%E6%8E%A2%E7%B4%A2/1.py)
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)

#print (item)
for i in range(2 ** n):
    bag = []
    total = 0

    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            #print (j)
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
            total += item[j][1]
    if (total <= money):
        print (total, bag)
```

Qiitaの参考記事にもあるが、0or1のフラグチェックをシフト演算で行うのがミソ。これもなるほどと思った。


上記を一般化した例。

[2.py](https://github.com/mollinaca/ac/blob/master/code/test/bit%E5%85%A8%E6%8E%A2%E7%B4%A2/2.py)
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.py を一般化

# n = 入力される商品数
# m = 所持金
n,m = map(int,input().split())

# a1,p1 = 商品名、値段
# ...
# an,pn

item = []
for _ in range(n):
    l = list(map(int,input().split()))
    item.append(l)

#print (item)
for i in range(2**n):
    bag = []
    price = 0
    for j in range(n):
        if ((i>>j)&1):
            bag.append(item[j][0])
            price += item[j][1]

    if price <= m:
        print (price,bag)
```

これで、「二つの状態を持つ要素」に対して「組み合わせの全列挙」ができるようになった。  

## 例題

[abc079_c:TrainTicket](https://atcoder.jp/contests/abc079/tasks/abc079_c)   
[abc167_c:SkillUp](https://atcoder.jp/contests/abc167/tasks/abc167_c)   

解いてみる。
