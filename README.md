# ansible-role-consul [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-consul.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-consul)

CentOS 7 に consul を導入する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

| 項目名                  | デフォルト値| 説明                              |
| ----------------------- | ----------- | --------------------------------- |
| consul_server_hostnames | None        | serverとして起動する inventory 名 |
| consul_bootstrap_expect | 3           | leaderを決定する数                |
| consul_use_template     | no          | consul-templateを使用             |
| enable_dnsmasq          | yes         | dnsmasq利用有無                   |
