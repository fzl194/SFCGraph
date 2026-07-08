---
id: UDG@20.15.2@MMLCommand@SET UPETHSRVPARA
type: MMLCommand
name: SET UPETHSRVPARA（设置用户面以太业务参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPETHSRVPARA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 5G LAN管理
- 用户面以太业务参数配置
status: active
---

# SET UPETHSRVPARA（设置用户面以太业务参数）

## 功能

**适用NF：UPF**

该命令用于设置用户面以太业务相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | UPETHSRVSW |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPETHSRVSW | 用户面以太业务开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否使能用户面以太业务。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| UPETHSRVMAC | 用户面以太业务MAC地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“UPETHSRVSW”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于配置用户面以太业务的MAC地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度为17位。字符串应符合MAC地址格式，如10-11-11-11-11-11。配置的MAC地址需为单播MAC地址。<br>默认值：无<br>配置原则：<br>- 建议使用N3逻辑接口对应的物理接口的MAC地址作为VXLAN隧道源端的MAC地址，避免MAC地址冲突。<br>- 配置的MAC地址需要确保在本DC内不冲突，如果找不到合适的单播MAC地址，可以使用本设备内联口MAC地址作为以太业务的MAC地址。如果配置的MAC地址出现冲突，请重新设置以太业务MAC地址。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPETHSRVPARA]] · 用户面以太业务参数配置（UPETHSRVPARA）

## 使用实例

设置用户面以太业务相关参数，将用户面以太业务开关开启并设置用户面以太业务MAC地址为10-11-11-11-11-11：

```
SET UPETHSRVPARA: UPETHSRVSW=ENABLE, UPETHSRVMAC="10-11-11-11-11-11";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置用户面以太业务参数（SET-UPETHSRVPARA）_25238686.md`
