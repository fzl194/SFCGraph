---
id: UDG@20.15.2@MMLCommand@LST IFIPV6ADDRESSIPSEC
type: MMLCommand
name: LST IFIPV6ADDRESSIPSEC（查询接口IPv6地址）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IFIPV6ADDRESSIPSEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- IPv6地址
status: active
---

# LST IFIPV6ADDRESSIPSEC（查询接口IPv6地址）

## 功能

该命令用于查询接口的IPv6地址配置信息。

> **说明**
> 该命令在VNFP和VNFC上都可以执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要配置IP地址的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：<br>请使用<br>[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)<br>命令查看可用接口。 |

## 操作的配置对象

- [接口IPv6地址（IFIPV6ADDRESSIPSEC）](configobject/UDG/20.15.2/IFIPV6ADDRESSIPSEC.md)

## 使用实例

查询LoopBack4的信息：

```
LST IFIPV6ADDRESSIPSEC: IFNAME=""LoopBack4"";
RETCODE = 0  操作成功

结果如下
-------------------------
              接口名  =  LoopBack4
            IPv6地址  =  fc00:0000:0000:0000:0000:0000:0000:0000
        IPv6地址前缀  =  128
        IPv6地址类型  =  NULL
(结果个数 = 1)

---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询接口IPv6地址（LST-IFIPV6ADDRESSIPSEC）_21521228.md`
