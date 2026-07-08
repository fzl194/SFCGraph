---
id: UDG@20.15.2@MMLCommand@LST DNSOVERWRITING
type: MMLCommand
name: LST DNSOVERWRITING（查询DNS重写动作配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DNSOVERWRITING
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- DNS重写控制
- DNS重写
status: active
---

# LST DNSOVERWRITING（查询DNS重写动作配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询DNS重写动作配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNSOVERWRTNAME | DNS重写动作名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS重写动作名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DNSOVERWRITING]] · DNS重写动作配置（DNSOVERWRITING）

## 使用实例

查询名称为test的DNS重写的配置信息：

```
LST DNSOVERWRITING: DNSOVERWRTNAME="test";
```

```

RETCODE = 0 操作成功。

DNS重写动作信息
------------------
DNS重写动作名字 = test
扩展过滤器类型1 = 与
扩展过滤器名称1 = e1
扩展过滤器类型2 = NULL
开启过滤器名称2 = NULL
扩展过滤器类型3 = NULL
扩展过滤器名称3 = NULL
扩展过滤器类型4 = NULL
扩展过滤器名称4 = NULL
扩展过滤器类型5 = NULL
扩展过滤器名称5 = NULL
服务器IPv4地址1 = 10.0.0.1
服务器IPv4地址2 = 0.0.0.0
服务器IPv4地址3 = 0.0.0.0
服务器IPv4地址4 = 0.0.0.0
服务器IPv4地址5 = 0.0.0.0
服务器IPv6地址1 = fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
服务器IPv6地址2 = ::
服务器IPv6地址3 = ::
服务器IPv6地址4 = ::
服务器IPv6地址5 = ::
绑定错误码名称 = errcode
   配置域名称  =  NULL
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DNSOVERWRITING.md`
