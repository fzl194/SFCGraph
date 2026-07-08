---
id: UDG@20.15.2@MMLCommand@LST IFIPV4ADDRESSIPSEC
type: MMLCommand
name: LST IFIPV4ADDRESSIPSEC（查询接口IPv4地址）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IFIPV4ADDRESSIPSEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- IPv4地址
status: active
---

# LST IFIPV4ADDRESSIPSEC（查询接口IPv4地址）

## 功能

该命令用于查询接口的配置地址，借用地址以及被借用地址。配置地址类型包括主地址和从地址。借用地址代表本接口借用了另一个接口的主地址，被借用地址代表本接口的主地址被另一个接口借用。请使用 [**ADD IFIPV4UNNUMIPSEC**](../IPv4借用地址/增加接口IPv4借用地址（ADD IFIPV4UNNUMIPSEC）_25830687.md) 命令配置地址借用关系。

不指定IFNAME参数时，查询设备上所有接口的信息；当指定IFNAME参数时，可以查询指定接口的配置信息。

> **说明**
> 该命令在VNFP和VNFC上都可以执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要配置IP地址的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：<br>请使用<br>[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)<br>命令查看可用接口。 |

## 操作的配置对象

- [接口IPv4地址（IFIPV4ADDRESSIPSEC）](configobject/UDG/20.15.2/IFIPV4ADDRESSIPSEC.md)

## 使用实例

查询LoopBack4的信息：

```
LST IFIPV4ADDRESSIPSEC: IFNAME=""LoopBack4"";
RETCODE = 0  操作成功

结果如下
-------------------------
            IPv4地址  =  192.168.1.1
        IPv4地址掩码  =  255.255.255.0
        IPv4地址类型  =  主地址
          接口名  =  LoopBack4
(结果个数 = 1)

---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询接口IPv4地址（LST-IFIPV4ADDRESSIPSEC）_80751064.md`
