---
id: UDG@20.15.2@MMLCommand@LST DRCOMM
type: MMLCommand
name: LST DRCOMM（查询容灾实例地址）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DRCOMM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# LST DRCOMM（查询容灾实例地址）

## 功能

该命令用于查询本端或对端容灾实例地址信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| DRINSTID | 容灾实例ID | 可选必选说明：可选参数。<br>参数含义：该参数用于配置容灾实例标识。<br>数据来源：全网规划。<br>取值范围：整型，0~63。<br>默认值：无。 |
| IPVERSION | ip版本号 | 可选必选说明：必选参数。<br>参数含义：IP版本。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>COMM_IPV4：IP版本为IPv4。<br>COMM_IPV6：IP版本为IPv6。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DRCOMM]] · 容灾实例地址（DRCOMM）

## 使用实例

查询 “ip版本号” 为 “COMM_IPV4” 的容灾实例地址：

```
LST DRCOMM: IPVERSION=COMM_IPV4;
%%LST DRCOMM: IPVERSION=COMM_IPV4;%%
RETCODE = 0  操作成功
操作结果如下
------------
容灾实例ID  ip版本号  ipv4通信地址  VPN名称   通信名称
0           IPV4类型  10.1.1.1       _public_  NULL
1           IPV4类型  10.2.2.2       _public_  NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DRCOMM.md`
