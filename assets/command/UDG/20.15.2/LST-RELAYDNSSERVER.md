---
id: UDG@20.15.2@MMLCommand@LST RELAYDNSSERVER
type: MMLCommand
name: LST RELAYDNSSERVER（查询媒体中继的DNS属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYDNSSERVER
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继DNS服务器配置
status: active
---

# LST RELAYDNSSERVER（查询媒体中继的DNS属性）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询媒体中继的DNS属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNSSERVERNAME | DNS服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYDNSSERVER]] · 媒体中继的DNS属性（RELAYDNSSERVER）

## 使用实例

假设需要查询媒体中继DNS属性，则命令如下：

```
LST RELAYDNSSERVER:;
```

```

RETCODE = 0  操作成功

结果如下
--------
     DNS服务器名称  =  dns01
       VPN实例名称  =  NULL
 IPv4主DNS服务器IP  =  10.0.0.1
 IPv4备DNS服务器IP  =  10.0.0.2
 IPv6主DNS服务器IP  =  NULL
 IPv6备DNS服务器IP  =  NULL
  超时时间间隔（秒）  =  1
    重发次数（次数）  =  1
     WAL-Value流控  =  1000
         配置域名称  =  NULL
    DNS探测功能开关  =  不使能
	      探测域名  =  NULL
探测功能定时器（秒）  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RELAYDNSSERVER.md`
