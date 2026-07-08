---
id: UDG@20.15.2@MMLCommand@LST CFIPWHITELIST
type: MMLCommand
name: LST CFIPWHITELIST（查询IP地址白名单列表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CFIPWHITELIST
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤IP白名单配置
status: active
---

# LST CFIPWHITELIST（查询IP地址白名单列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示配置IP地址。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Ip地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CFIPWHITELIST]] · IP地址白名单列表（CFIPWHITELIST）

## 使用实例

查询IP地址白名单列表：

```
LST CFIPWHITELIST: IPTYPE=IPV4;
```

```

RETCODE = 0  操作成功。

IPV4地址白名单
----------------
IP地址    IP地址掩码长度  配置域名称

0.0.0.0         32        NULL
127.0.0.0       24        NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CFIPWHITELIST.md`
