---
id: UDG@20.15.2@MMLCommand@LST QOSIFTRUST
type: MMLCommand
name: LST QOSIFTRUST（查询QoS接口信任）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: QOSIFTRUST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 接口信任信息
status: active
---

# LST QOSIFTRUST（查询QoS接口信任）

## 功能

该命令用来查询绑定在以太主接口上的简单流分类策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| DSNAME | DS域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DS域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| FLAG8021P | 8021p标志 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射的优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- false：不支持以太子接口上根据802.1p的值进行简单流分类。<br>- true：支持以太子接口上根据802.1p的值进行简单流分类。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@QOSIFTRUST]] · QoS接口信任（QOSIFTRUST）

## 使用实例

查询当前所有的简单流分类策略：

```
LST QOSIFTRUST:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
    DS域名 = 1
  接口名称 = Ethernet66/0/3
8021p标志 = 否
  (结果个数 = 1)
----END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-QOSIFTRUST.md`
