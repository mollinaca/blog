Title: pyenv の Python にインストールされた pipenv の仮想環境にインストールされた Python を cron で動かす
Date: 2020-05-04
Category: Tech
Tags: Python, pyenv, pipenv, Linux, cron
Slug: cron_pyenv_pipenv
Authors: s.hosoya

### Python 実行環境

OSのPythonは触らずに、pyenv を使いユーザローカルに Python をインストールする。  
その Python の pip に pipenv をインストールし、その pipenv を使って Python の仮想環境を構築する。  
ここで実行された仮想環境上の Python を、OSの cron から実行する。　  


### cron サンプル

~~~html
# cat /etc/cron.d/p

# init pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# cron job
SCRIPT_DIR=/root/scriptdir
01 * * * *     root cd "${SCRIPT_DIR}"; source /root/.local/share/virtualenvs/script-XXXXXXX/bin/activate; ./script.py
~~~
cron ファイルは、直接環境変数の指定などができる。  

### 説明

cron ジョブにおいて、環境変数の指定と、pyenvを有効化する。  
続いて、Pipfile が置いてあるディレクトリに移動し、pipenv を activate する。  
すると、pipenv仮想環境にインストールされた Python を実行できるようになる。

