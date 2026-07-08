---
id: UNC@20.15.2@MMLCommand@SET SGWPLMNORIGIN
type: MMLCommand
name: SET SGWPLMNORIGIN（设置S-GW PLMN ID来源）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SGWPLMNORIGIN
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取PLMN管理
- S_P合一的SGW PLMN获取策略
status: active
---

# SET SGWPLMNORIGIN（设置S-GW PLMN ID来源）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于控制SGW-C和PGW-C合一形态时SGW-C PLMN的获取方式。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SGWPLMNORIGIN |
| --- |
| PGW_PLMN |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGWPLMNORIGIN | S-GW PLMN ID来源 | 可选必选说明：可选参数<br>参数含义：用于控制SGW-C和PGW-C合一形态时SGW-C PLMN ID的获取方式。<br>数据来源：本端规划<br>取值范围：<br>- “PGW_PLMN（P-GW PLMN）”：取PGW-C PLMN作为SGW-C PLMN。<br>- “NO_PGW_PLMN_FIRST（No P-GW PLMN first）”：优先从Serving Network信元中获取SGW-C PLMN，其次从ULI信元中获取SGW-C PLMN，两种方式都获取不到时取PGW-C PLMN作为SGW-C PLMN。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SGWPLMNORIGIN查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWPLMNORIGIN]] · S-GW PLMN ID来源（SGWPLMNORIGIN）

## 使用实例

设置P-GW PLMN作为S-GW PLMN：

```
SET SGWPLMNORIGIN: SGWPLMNORIGIN=PGW_PLMN;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置S-GW-PLMN-ID来源（SET-SGWPLMNORIGIN）_09651723.md`
