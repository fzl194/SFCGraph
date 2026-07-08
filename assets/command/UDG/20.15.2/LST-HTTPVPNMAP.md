---
id: UDG@20.15.2@MMLCommand@LST HTTPVPNMAP
type: MMLCommand
name: LST HTTPVPNMAP（查询HTTP VPN映射关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPVPNMAP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP VPN映射管理
status: active
---

# LST HTTPVPNMAP（查询HTTP VPN映射关系）

## 功能

该命令用于查询HTTP对端地址与本端VPN的映射关系。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP VPN映射的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~512。<br>默认值：无<br>配置原则：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPVPNMAP]] · HTTP VPN映射关系（HTTPVPNMAP）

## 使用实例

若运营商想查询所有的HTTP VPN映射关系，可以用如下命令

```
%%LST HTTPVPNMAP:;%%
RETCODE = 0  操作成功

结果如下
------------------------
索引   VPN名称    对端地址类型     IPv4地址     IPv4掩码      IPv6地址  IPv6地址前缀长度  配置描述  

1      VPN1      IPv4地址       10.1.1.1      255.255.0.0   ::       0               NULL         
2      VPN2      IPv4地址       10.2.1.1      255.255.0.0   ::       0               NULL         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP-VPN映射关系（LST-HTTPVPNMAP）_46031597.md`
