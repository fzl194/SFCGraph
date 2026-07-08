---
id: UNC@20.15.2@MMLCommand@LST IFIPV6ADDRESS
type: MMLCommand
name: LST IFIPV6ADDRESS（查询接口IPv6地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IFIPV6ADDRESS
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6地址
status: active
---

# LST IFIPV6ADDRESS（查询接口IPv6地址）

## 功能

该命令用于查询接口的IPv6地址配置信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令可以在VNRS_VNFC的Ethernet接口，Ethernet子接口，Eth-Trunk接口，Eth-Trunk子接口以及Loopback口，Tunnel口上配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [接口IPv6地址（IFIPV6ADDRESS）](configobject/UNC/20.15.2/IFIPV6ADDRESS.md)

## 使用实例

查询所有接口的IPv6地址：

```
LST IFIPV6ADDRESS:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
        接口名称  = Ethernet64/0/3
        IPv6地址  = 2001:db8::11
    IPv6地址前缀  = 64
    IPv6地址类型  = 全球单播地址
IPv6地址计算类型  = none
(结果个数 = 1)
---   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询接口IPv6地址（LST-IFIPV6ADDRESS）_00866605.md`
