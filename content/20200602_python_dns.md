Title: python でネームサーバを指定して dig/nslookup をしたい(memo)
Date: 2020-06-03
Category: Tech
Tags: Python, DNS
Slug: python_dns
Authors: s.hosoya

そこそこの数のレコードをそこそこの数のネームサーバに対して dig を行い、各レコードがそれぞれのNSで一致することを確認する、というタスクに対応するためにスクリプトを書こうと思い。  
いままでの自分だったらシェルで書いちゃうんだけど、Pythonがやりたいんだという強い意志の元pythonで実装していく。  

実装にあたり、pythonで NSを指定した dig/nslookup みたいなことをできるライブラリないしやり方を探したが、あまりいい検索結果がでなかったので、まとめた内容はまたQiitaに書こうかなというところ。

---

## 参考

検索すると上位に出てくるサイトなど。

[Pythonでnslookup(ドメインの正引きと逆引き)する](http://sonickun.hatenablog.com/entry/2014/10/30/183541)  
個人ブログ。  
`socket.gethostbyname`, `socket.gethostbyaddr` による実装。これらは名前解決の正引き、逆引きはできるけどNSの指定は（たぶん）できない。  
そもそも `socket` は通信レイヤ用のモジュールであり、DNSを扱うためのモジュールではない。名前解決はできる。  

[Pythonで名前解決する方法を現役エンジニアが解説【初心者向け】](https://techacademy.jp/magazine/20868)  
テックアカデミーの記事。  
これも名前解決のやり方で、NSの指定まではフォローしていない。  

`socket.gethostbyaddr` と `dnspython` について触れている。名前解決だけならこれでもまぁ十分。  
`dnspython` のサンプルコードが、MXレコードなのがちょっと気になるけど。。普通Aレコードがよいのでは？  
たぶんこれをそのままコピペしたっぽい。まぁ公式から正しいコードを引用してるだけマシか。  

~~~
https://github.com/rthalley/dnspython/blob/master/examples/mx.py
#!/usr/bin/env python3

import dns.resolver

answers = dns.resolver.query('nominum.com', 'MX')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)
~~~

## 調べたこと

ライブラリとしては、 `socket`, `dnspython`, `nslookup`, `pydig` あたりが使えそう。  
それぞれの開発状況と使い方をあわせてまとめよう。  

### dnspython

https://pypi.org/project/dnspython/  
http://www.dnspython.org/  
https://github.com/rthalley/dnspython  

## nslookup

https://pypi.org/project/nslookup/  
https://github.com/wesinator/pynslookup  

### PyDig

https://pypi.org/project/pydig/  
https://github.com/leonsmith/pydig  

pydigが一番開発されてそう。nslookupは新しめ。  
dnspythonはわりとオワコン臭がしている、開発続いてるみたいだけど。  

まとまったら記事かこ。  



