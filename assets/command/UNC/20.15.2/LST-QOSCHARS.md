---
id: UNC@20.15.2@MMLCommand@LST QOSCHARS
type: MMLCommand
name: LST QOSCHARS（查询Qos特征）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSCHARS
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 业务质量特征
status: active
---

# LST QOSCHARS（查询Qos特征）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询QoS特征，其中包括资源类型、5QI优先级、包时延预算、包错误率、平均窗口、最大数据突发。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FQI | 5QI或QCI | 可选必选说明：可选参数<br>参数含义：该参数用于配置5QI或QCI，不同的5QI或QCI的业务流需使用不同的承载。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [QoS特征（QOSCHARS）](configobject/UNC/20.15.2/QOSCHARS.md)

## 使用实例

查询5QI为“10”的QoS特征的信息。

```
LST QOSCHARS: FQI=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Qos特征（LST-QOSCHARS）_24796824.md`
