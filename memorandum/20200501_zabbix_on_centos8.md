Title: CentOS8 に zabbix4.4 をインストールする
Date: 2020-05-01
Category: Tech
Tags: Linux, CentOS8, zabbix, php, apache, mysql
Slug: zabbix
Authors: s.hosoya

## 環境

* ローカルVM
| IPアドレス | 192.168.56.101 |
| /etc/redhat-release | CentOS Linux release 8.1.1911 (Core) |
| uname -r | 4.18.0-147.8.1.el8_1.x86_64 |

## インストールするもの

| apache | 2.4 |
| php | 7.4 |
| MySQL | |
| zabbix-server | | 

### apache

* インストール
```
# dnf -y install httpd mod_ssl
```

* 起動
```
# systemctl enable httpd
# systemctl start httpd
```

http://192.168.56.101 へアクセスし、Apacheのテストページが表示されることを確認

### php

* remi Repository を追加
```
# dnf install http://rpms.famillecollet.com/enterprise/remi-release-8.rpm
# dnf install mod_php
# dnf info php74 --enablerepo=remi
```

* 確認
```
# php74 -r 'print "Hello, World!\n";'
```

