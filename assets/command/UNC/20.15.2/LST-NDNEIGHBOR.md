---
id: UNC@20.15.2@MMLCommand@LST NDNEIGHBOR
type: MMLCommand
name: LST NDNEIGHBOR（查询静态ND邻居表项）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NDNEIGHBOR
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND表项
status: active
---

# LST NDNEIGHBOR（查询静态ND邻居表项）

## 功能

该命令用于IPv6 ND静态表项的查询。

若不指定IFNAME参数时，则显示所有接口的ND静态表项信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NDNEIGHBOR]] · 静态ND邻居表项（NDNEIGHBOR）

## 使用实例

查询IPv6 ND静态表项：

```
LST NDNEIGHBOR:IFNAME="Ethernet65/0/8";
```

```

        结果如下
        --------
        接口名            IPv6地址        MAC地址

        Ethernet65/0/8   2001:db8::11     00e0-fc03-0004
        Ethernet65/0/8   2001:db8::12     00e0-fc02-0003
        (结果个数 = 2)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NDNEIGHBOR.md`
