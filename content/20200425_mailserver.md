Title: 自前メールサーバの構築手順メモ
Date: 2020-04-25 
Category: Tech
Tags: Postfix, Linux, AWS, AmazonLinux
Slug: mailserver
Authors: s.hosoya

EC2で運用してる自前メールサーバ(受信＆転送専用)の構築手順のメモ  
https://github.com/mollinaca/til/blob/master/mail_server/メールサーバ構築メモ.md  

---

# メールサーバ構築

## 用途、前提

* 自前ドメインのメール受信用SMTPサーバの構築
    * 自前ドメインで受けたメールを、専用のgmailへ転送する
* 上記以外に、GIPを持ってるサーバとしてちょこちょこ利用する
* なるべく AWS FreeTrial の範囲で
    * 1年ごとの使い捨て

## EC2インスタンスを作成

* AWSアカウントを作成
    * アカウント作成
    * 2FA設定
    * ログイン・作業用IAM、API実行用IAM作成
        * 作業用IAM: EC2, S3, へのフルアクセス権限
        * 作業用IAMでログイン
* EC2インスタンス作成
    * AmazonLinux2
    * SecurityGroup作成、アタッチ
        * inbound: sshログイン用ポート, smtp/25 を解法
        * outbound: ICMP(IPv4), カスタムTCP/587 を解放
    * EIPアタッチ
* EC2へsshログイン

## EC2での作業

### インスタンス初期設定

~~~bash
## bash commands

# Login & passwd change
$ sudo su -
$ passwd root
 → rootのパスワード変更

# Package update
$ yum update
$ yum upgrade

# Disable SELinux
$ getenforce
 → Disabled ならOK

# modify sshd config
$ cd /etc/ssh
$ cp -pi sshd_config sshd_config.org
$ vi sshd_config
  ※内容 → https://github.com/mollinaca/dotfiles/blob/master/sshd/sshd_config_ec2

# create login user
$ groupadd hstn
$ passwd hstn
 → passwd 設定
$ visudo
 → hstn に sudo 権限を付与
---
hstn            ALL=(ALL)       NOPASSWD: ALL
---
 → hstn で sudo できることを確認

# login user setting

$ su - hstn
$ mkdir .ssh
$ chmod 755 .ssh
$ cd .ssh
  ※ログイン用公開鍵を設定
  ※ログイン確認
$ exit

# login as operation user
$ ssh hstn@[host]
$ sudo su -

# delete eu2-user
$ userdel -r ec2-user

## other settings
# change hostname
$ hostnamectl set-hostname mailserver

# modify TZ
$ timedatectl set-timezone Asia/Tokyo

# reboot
$ reboot
 → ログインして反映を確認

# modify prompt for operation user and root
$ su - hstn
  ※よしなに変更 

# install tools
$ yum install git ※ほかに必要なものがあればインストール
~~~

### メールサーバ設定

~~~bash
## bash commands

# modify /etc/hosts
$ vi /etc/hosts
 → 127.0.0.1 の行に mail.watarinohibi.tokyo を追加

# install sasl
$ yum -y install cyrus-sasl-plain cyrus-sasl-md5

# modify postfix and sasl conf
$ cd /etc/postfix
$ mv main.cf main.cf.org
$ vi main.cf
  ※内容は → https://github.com/mollinaca/dotfiles/blob/master/postfix/main.cf

$ vi /etc/postfix/smtp-auth-passwd
  ※内容は → https://github.com/mollinaca/dotfiles/blob/master/postfix/smtp-auth-passwd

$ postmap /etc/postfix/smtp-auth-passwd
$ rm -f /etc/postfix/smtp-auth-passwd

# postfix alias settings
$ vi aliases
  ※内容は → https://github.com/mollinaca/dotfiles/blob/master/postfix/aliases
$ newaliases

# restart postfix
$ systemctl restart postfix
~~~

## DNS設定

* zoneに以下のレコードを登録
~~~html
# add below records to my DNS ZONE
mail.watarinohibi.tokyo IN A [EIP]
mail.watarinohibi.tokyo IN MX 10 mail.watarinohibi.tokyo
~~~

# メール送受信テスト

~~~bash
## bash commands

# ローカルから送信  
$ sendmail test@mail.watarinohibi.tokyo
From:root@mailserver
To:test@mail.watarinohibi.tokyo
Subject:test mail sending
test
.
  → メールが届くこと、メールログを確認

# 外部から送信  
  → メールが届くこと、メールログを確認

~~~

## 監視設定

### CloudWatch

TBD

### maillog

TBD

### securelog

TBD

## その他

* NACLの上限緩和申請
