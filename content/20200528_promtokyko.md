Title: promethes久々に動かした
Date: 2020-05-28
Category: Tech
Tags: docker, prometheus
Slug: prom_20200528
Authors: s.hosoya

# Prometheus Meetup Tokyo #3 に参加した

[Prometheus Meetup Tokyo #4](https://prometheus.connpass.com/event/175547/)  
オンラインで開催していたので参加。  
オンラインは人数制限なくて参加しやすいのがほんといいね。会場いかなくていいし。  

1年ちょっと前ぐらいに、チームの監視ツールを munin & zabbix から一新したくて、Prometheus と AlertManager に置き換えられないかなぁといろいろやって、  
担当案件のリソース監視に勝手に突っ込んだりしてたけどうまく通せず、それっきりになってた。  
その後チームの異動があったりでしばらく遠ざかってたけど、久々に監視ツール系でいい話が色々聞けた。  

クラウドネイティブ、k8sの監視が前提なので、今更「オンプレなんですが。。。」とは言いにくいんだけど、  
とはいえこの手のモダンな監視ツールは追っかけておきたい分野でもあるので、定期的にアップデートしておこう。

ただ今日の話ははっきりいってほとんどついていけなかった。。(´；ω；｀)  


# 以前自分でつくったmonitoringツール用のrepo

[mollinaca/monitor](https://github.com/mollinaca/monitor)  
これも5ヶ月ぐらい前か。。あっという間。  

ホストに、PrometheusとcAdvisorとnode_exporterとgrafanaのdockerイメージをpullしてきて、連携したgrafanaをすぐに立てられる。  
久々にローカルVMに引っ張ってきて立ててみたら、なんかPrometheusのコンテナだけコケて、あれあれと思ってたけど、dockerコンテナにaddするvolumeの権限周りだったっぽい。  
ファイルとディレクトリをえーいで777にしたら動いた。いいのかこれで。

# やりたいことって何だったんだっけ

* インフラの運用
    * 監視、モニタリング → SRE
    * セキュリティ

上記の分野を強化していきたいって思ってたんだし、思ってるんだよな。  
いまの業務がまったく直結してこないのがつらみだけど、やりたいことは見失わずにんがんばってこう。
