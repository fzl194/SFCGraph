---
id: UDG@20.15.2@MMLCommand@LST IFALLOWEDVLAN
type: MMLCommand
name: LST IFALLOWEDVLAN（查询主接口允许通过的VLAN）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IFALLOWEDVLAN
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VLAN管理
- 主接口允许通过的VLAN
status: active
---

# LST IFALLOWEDVLAN（查询主接口允许通过的VLAN）

## 功能

该命令用于查询主接口允许通过的VLAN。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无。<br>配置原则：请使用<br>[LST INTERFACE](../../接口管理/接口配置/查询接口（LST INTERFACE）_49801850.md)<br>命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IFALLOWEDVLAN]] · 主接口允许通过的VLAN（IFALLOWEDVLAN）

## 使用实例

查询在接口Ethernet64/0/4上配置的允许通过的VLAN范围：

```
LST IFALLOWEDVLAN: IFNAME="Ethernet64/0/4";
```

```
RETCODE = 0  操作成功

结果如下:
---------
接口名          VLAN最小值  VLAN最大值  

Ethernet64/0/4  50          100         
Ethernet64/0/4  100         150         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询主接口允许通过的VLAN（LST-IFALLOWEDVLAN）_25183529.md`
