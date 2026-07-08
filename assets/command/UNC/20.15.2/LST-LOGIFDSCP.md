---
id: UNC@20.15.2@MMLCommand@LST LOGIFDSCP
type: MMLCommand
name: LST LOGIFDSCP（查询逻辑接口DSCP配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOGIFDSCP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- GGSN
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- QOS管理
- 逻辑接口DSCP管理
status: active
---

# LST LOGIFDSCP（查询逻辑接口DSCP配置）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用来查看UNC网元逻辑接口对外发送IP包时携带的DSCP值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定逻辑接口DSCP的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “AMF（AMF）”：AMF<br>- “SMF（SMF/PGW-C/SGW-C/GGSN-C）”：融合2345G功能，包含SMF/PGW-C/SGW-C/GGSN-C独立或融合的NF形态<br>- “NRF（NRF）”：NRF<br>- “NSSF（NSSF）”：NSSF<br>- “SMSF（SMSF）”：SMSF<br>- “NCG（NCG）”：NCG<br>默认值：无<br>配置原则：<br>UNC产品包含多个NF，如AMF、SMF、NRF、NCG、NSSF、SMSF，这些NF中有些可以融合部署，也可以独立部署，有些必须独立部署，该配置中对部署不敏感。即只需要按NF类型配置，如果需要指定AMF的逻辑接口DSCP，则该参数需要选择为AMF。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOGIFDSCP]] · 逻辑接口DSCP配置（LOGIFDSCP）

## 使用实例

- 若运营商需要查询各逻辑接口的DSCP配置，则可以使用如下命令：
  ```
  LST LOGIFDSCP:;
  ```
- 若运营商需要查询AMF的逻辑接口的DSCP配置，则可以使用如下命令：
  ```
  LST LOGIFDSCP:NFTYPE=AMF;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询逻辑接口DSCP配置（LST-LOGIFDSCP）_50558742.md`
