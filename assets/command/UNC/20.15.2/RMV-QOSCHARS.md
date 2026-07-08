---
id: UNC@20.15.2@MMLCommand@RMV QOSCHARS
type: MMLCommand
name: RMV QOSCHARS（删除QoS特征）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSCHARS
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 业务质量特征
status: active
---

# RMV QOSCHARS（删除QoS特征）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除QoS特征。

## 注意事项

- 该命令执行后立即生效。

- 如果本命令中的5QI的值与QOSPROP中5QI的值相同，并且QOSPROP正在被线上的用户使用，则删除此配置可能会导致该用户业务触发创建专载失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FQI | 5QI或QCI | 可选必选说明：必选参数<br>参数含义：该参数用于配置5QI或QCI，不同的5QI或QCI的业务流需使用不同的承载。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSCHARS]] · QoS特征（QOSCHARS）

## 使用实例

删除5QI为“10”的QoS特征。

```
RMV QOSCHARS: FQI=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除QoS特征（RMV-QOSCHARS）_24796836.md`
