---
id: UDG@20.15.2@MMLCommand@LST IFIPV4UNNUMIPSEC
type: MMLCommand
name: LST IFIPV4UNNUMIPSEC（查询接口IPv4借用地址）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IFIPV4UNNUMIPSEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- IPv4借用地址
status: active
---

# LST IFIPV4UNNUMIPSEC（查询接口IPv4借用地址）

## 功能

"该命令用于查询接口的借用IPv4地址。

不指定IFNAME参数时，查询所有接口的IPv4借用地址；当指定IFNAME参数时，可以查询指定接口的IPv4借用地址。"。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：<br>请使用<br>[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)<br>命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IFIPV4UNNUMIPSEC]] · 接口IPv4借用地址（IFIPV4UNNUMIPSEC）

## 使用实例

查询tunnel口借用的IPv4地址：

```
LST IFIPV4UNNUMIPSEC:IFNAME=""tunnel1"";
RETCODE = 0  操作成功

结果如下
--------
      接口名  =  tunnel1
被借用接口名  =  loopback1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询接口IPv4借用地址（LST-IFIPV4UNNUMIPSEC）_80910990.md`
