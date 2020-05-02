Title: CentOS8 に WordPress をインストールする
Date: 2020-05-02
Category: Tech
Tags: Linux, CentOS8, WordPress , php, apache, mysql
Slug: wp
Authors: s.hosoya

## 環境

* ローカルVM  

| モノ | 情報 |
| - | - |
| IPアドレス | 192.168.56.101 |
| /etc/redhat-release | CentOS Linux release 8.1.1911 (Core) |
| uname -r | 4.18.0-147.8.1.el8_1.x86_64 |

## インストールするもの

| モノ | バージョン |
| - | - |
| apache | 2.4 |
| php | 7.4 |
| MySQL | 8.0.17-3 |
| WordPress | 5.4.1 |

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
# dnf install php74-php-cli php74-php-fpm php74-php-mysqlnd php74-php-opcache php74-php-mbstring --enablerepo=remi
# systemctl start php74-php-fpm
# systemctl enable php74-php-fpm
```

* 確認
```
# php74 -r 'print "Hello, World!\n";'
```

```
# cd /var/www/html
# vin phpinfo.php
=======
<?php
phpinfo();
=======
```
http://192.168.56.101/phpinfo.php へアクセスし、 phpinfo が表示されることを確認  

![phpinfo](https://blog.watarinohibi.tokyo/images/20200502_phpinfo.png "phpinfo")

### MySQL

* AppStreamからインストール
```
# dnf install mysql mysql-server
# systemctl enable mysqld.service
# systemctl start mysqld
# mysql_secure_installation
 → 初期セットアップを完了する
 * root のパスワードを設定
 * Remove anonymous user → Yes
 * Disallow root login remotely → Yes
 * Remove test database → Yes
 * Reload Privilages tables now → Yes
 → All done!
```

* 確認
```
# mysql -uroot -p
Password:
mysql> select * from mysql.user \G
 → アカウント情報を確認
```

### WordPress

* MySQL に Wordpress 設定
```
# mysql -uroot -p
mysql> CREATE DATABASE wpdb;
mysql> CREATE USER 'wp'@'localhost' identified by '{password}';
mysql> GRANT ALL on wpdb.* TO 'wp'@'localhost';
```

* インストール

Wordpress最新版のソースを入手  
https://ja.wordpress.org/download/  
20200502 本日時点では、 5.4.1 の模様  

```
# cd /usr/local/src
# wget https://ja.wordpress.org/latest-ja.tar.gz
# tar zxvf latest-ja.tar.gz
# mv wordpress /var/www/html/
# cd /var/www/html/
# chwon root:root -R /var/www/html/wordpress
# cd wordpress
# cp -pi wp-config-sample.php wp-config.php
# vi wp-config.php
=======================
define( 'DB_NAME', 'database_name_here' );
↓
define( 'DB_NAME', 'wpdb' );

define( 'DB_USER', 'username_here' );
↓
define( 'DB_USER', 'wp' );

define( 'DB_PASSWORD', 'password_here' );
↓
define( 'DB_PASSWORD', '{password}' );

define( 'DB_CHARSET', 'utf8' );
↓
define( 'DB_CHARSET', 'utf8mb4' );

define( 'DB_HOST', 'localhost' );
↓
define( 'DB_HOST', 'localhost:/var/lib/mysql/mysql.sock' );
=======================

```

以上まで完了したら、ブラウザで http://192.168.56.101/wordpress へアクセスして、WordPress の初期設定画面が表示されることを確認  

![wp_install](https://blog.watarinohibi.tokyo/images/20200502_wp_install.png "wp_install")


上記項目をいれて、無事インストールが完了されば構築完了。  

![wp_hello](https://blog.watarinohibi.tokyo/images/20200502_wp_hello.png "wp_hello")
