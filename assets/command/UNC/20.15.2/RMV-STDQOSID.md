---
id: UNC@20.15.2@MMLCommand@RMV STDQOSID
type: MMLCommand
name: RMV STDQOSID（删除标准QoS ID配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: STDQOSID
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 扩展QCI功能
- 标准QoS ID配置
status: active
---

# RMV STDQOSID（删除标准QoS ID配置）

## 功能

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于删除标准QoS ID配置。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 配置中的标准QoS ID被EXTENQCIATTR中的EXTQCIMAPDEFQCI或EXTENDQCIMAP中的STANDARDQCI使用时，该配置无法删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSIDTYPE | QoS ID类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS ID类型。<br>数据来源：本端规划<br>取值范围：<br>- “QCI（QCI）”：QCI<br>- “FIVEQI（5QI）”：5QI<br>默认值：无<br>配置原则：无 |
| QOSIDSV | QoS ID起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS ID起始值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~255。<br>默认值：无<br>配置原则：<br>该参数的值必须小于等于QoS ID的结束值。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@STDQOSID]] · 标准QoS ID配置（STDQOSID）

## 使用实例

删除“QCI=90”的“标准QoS ID”配置：

```
RMV STDQOSID:QOSIDTYPE=QCI,QOSIDSV=90;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-STDQOSID.md`
