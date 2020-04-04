Title: python-pelican に theme を導入する
Date: 2020-04-04
Category: Tech
Tags: python, pelican
Slug: pelican-theme
Authors: s.hosoya

ものは試しに。

# やり方

pelican の theme は、以下の repo で管理されている。  
ここはただのファイル置き場なので、別にこの repo に拘る必要はなさそうだけど。  
[pelican-themes](https://github.com/getpelican/pelican-themes)  

いくつかの theme は、それぞれの作者の repo にあり、リンクになってる。  
上記 repo を、pelican の project directory から辿れる場所へ clone する

```
# git clone https://github.com/getpelican/pelican-themes
```

clone した theme を、 pelicanconf.py 、 および publichconf.py に適用する  
THEME変数に、ディレクトリへのパスを指定してあげればよいみたい  

```
THEME = "../pelican-themes/bootstrap2-dark"
```

上記で、 `make html` すると、 bootstrap2-dark が適用された。


# 参考

[Pelican Themes](http://www.pelicanthemes.com/)  
[pelican-themes](https://docs.getpelican.com/en/stable/settings.html#themes)  
[Pelicanにテーマを導入してみる](https://qiita.com/ryo-ma/items/20db8cd20f1086838249)  


## メモ

* 過去エントリのアーカイブリンク
* タグクラウド
* 静的ページへのリンクを目立つ場所に貼る

上記を解決できそうなテーマを探しつつ、他のプラグインも試す

