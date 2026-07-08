---
id: UDG@20.15.2@MMLCommand@LST DDOS
type: MMLCommand
name: LST DDOS（查询DDoS防攻击流控阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DDOS
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- DDoS防护
- DDoS防护阈值
status: active
---

# LST DDOS（查询DDoS防攻击流控阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询DDoS攻击防护使用的流控阈值。DDoS攻击防护是通过对用户上行TCP SYN报文进行流控来实施的。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/DDOS]] · DDoS防攻击流控阈值（DDOS）

## 使用实例

使用LST DDOS命令查询当前配置的DDoS攻击防护使用的流控阈值：

```
LST DDOS:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
DDos防护阈值  =  5000
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DDoS防攻击流控阈值（LST-DDOS）_82837755.md`
