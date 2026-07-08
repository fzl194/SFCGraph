---
id: UNC@20.15.2@MMLCommand@LST QOS5QI2QCIMAP
type: MMLCommand
name: LST QOS5QI2QCIMAP（查询5QI到标准QCI的映射）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOS5QI2QCIMAP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- QoS映射
- 5QI到QCI映射
status: active
---

# LST QOS5QI2QCIMAP（查询5QI到标准QCI的映射）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询5QI到标准QCI的映射。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLTYPE | 控制类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- APN_LEVEL（APN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| APN | APN | 可选必选说明：该参数在"CTRLTYPE"配置为"APN_LEVEL"时为条件可选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| QOS5QISTART | 5QI范围起始点 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5QI范围的起始值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| QOS5QIEND | 5QI范围结束值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5QI范围的结束值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| QCI | QCI | 可选必选说明：可选参数<br>参数含义：该参数用于指定标准QCI。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：<br>该参数值为1~9或命令ADD STDQOSID中配置的QoS ID值，除此以外都属于扩展QCI/5QI。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOS5QI2QCIMAP]] · 5QI到QCI的映射（QOS5QI2QCIMAP）

## 使用实例

查询所有QOS5QI2QCIMAP配置：

```
LST QOS5QI2QCIMAP:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5QI到标准QCI的映射（LST-QOS5QI2QCIMAP）_39919393.md`
