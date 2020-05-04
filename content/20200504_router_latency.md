Title: ルータのレイテンシ測定記録
Date: 2020-05-04
Category: Tech
Tags: Network, Latency, 自宅PC環境
Slug: router_latency
Authors: s.hosoya

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">もともとつかってたルータが急に調子悪くなってしまい、急遽眠ってた控えのルータを稼働させているがなかなか調子よくて助かった。<br>しかし、稼働中の PC - ルータ 間の smokeping を見てるんだけど、この latency の差はなにで生まれてるのか悩ましい。。単純に使ってる時間のほうが短くなるのかしら <a href="https://t.co/Mw0qrH2sX0">pic.twitter.com/Mw0qrH2sX0</a></p>&mdash; mollinaca (@syoutin) <a href="https://twitter.com/syoutin/status/1257193137325240320?ref_src=twsrc%5Etfw">May 4, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


5年ぐらい使ってたASUSのルータが調子悪くなってきて、とつぜんインターネットとの接続が消れるようになった。。  
なんどか再起動したりしてもダメだったので、暫定で控えにいた使っていないルータ（妻が以前使っていたもの）にバトンタッチして様子見中。  

いわゆるNECの普通の家庭用ルータだけど、機能的にはまぁ問題ないやつだったのでよかった。  

<iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="https://rcm-fe.amazon-adsystem.com/e/cm?ref=qf_sp_asin_til&t=watarinohibi-22&m=amazon&o=9&p=8&l=as1&IS2=1&detail=1&asins=B0037TSAM6&linkId=1cc3b8650d89ad27b5bc0986b85975c9&bc1=ffffff&lt1=_top&fc1=333333&lc1=0066c0&bg1=ffffff&f=ifr">
    </iframe>

これの何年か前の機種。Atermってよく見るやつだね。  

こいつを使ってインターネット接続後、しばらく PC - ルータ 間の latency を見ていたんだけど、

![router_latency](https://blog.watarinohibi.tokyo/images/20200504_router_latency.png "router_latency")  

という感じで、latencyが低いときと高い時があることに気づいた。  

それぞれ何をしていたのかというと、

![router_latency2](https://blog.watarinohibi.tokyo/images/20200504_router_latency2.png "router_latency2")    

みたいな感じ。

* 使われていない idletime の時は一定をキープ
* ゲームで使われており、ステートフルなセッションが張られていると低い値で推移
* 使われている状態で、普通にインターネット（httpやssh程度）のみだと、上記の中間のような状態

になるように見える。   
使ってるときと使ってないときで、状態に違いがあるのはたぶんそういうことなんだろうな。  


面白いので、しばらく経過観察してみる。  
