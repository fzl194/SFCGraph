---
id: UNC@20.15.2@MMLCommand@RMV CCT
type: MMLCommand
name: RMV CCT（删除融合计费模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CCT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费模板
status: active
---

# RMV CCT（删除融合计费模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除融合计费模板（Converged Charging Template），用于配置融合计费相关参数。

## 注意事项

- 该命令执行后立即生效。

- 当CCT配置在APNCHARGECTRL，USRPROFCHARGE，RGRCACT，RGTRIGGER，PDUTRIGGER，QBCQOSFTRIGGER，QBCPDUTRIGGER，PDUSCACT，SELECTCCTBYCC中时，不可以删除。
- 默认记录不可以删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置融合计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CCT]] · 融合计费模板（CCT）

## 使用实例

删除名为“test”的CCT融合计费模板：

```
RMV CCT: CCTMPLTNAME="test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CCT.md`
