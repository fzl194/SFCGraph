---
id: UNC@20.15.2@MMLCommand@LST PCCCHGMODEBYPCFID
type: MMLCommand
name: LST PCCCHGMODEBYPCFID（查询基于PCF的计费策略接口类型）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCCCHGMODEBYPCFID
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 计费策略接口选择
status: active
---

# LST PCCCHGMODEBYPCFID（查询基于PCF的计费策略接口类型）

## 功能

**适用NF：SMF**

查询基于PCF的计费策略接口类型。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCFINSID | PCF实例标识 | 可选必选说明：可选参数<br>参数含义：字符串唯一标识PCF实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>PCF实例标识在TOPO本地配置，或者由NRF返回。需要整网协商配置。 |

## 操作的配置对象

- [基于PCF的计费策略接口类型（PCCCHGMODEBYPCFID）](configobject/UNC/20.15.2/PCCCHGMODEBYPCFID.md)

## 使用实例

查询PCF实例标识为pcf1的计费策略接口类型。

```
LST PCCCHGMODEBYPCFID: PCFINSID="pcf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于PCF的计费策略接口类型（LST-PCCCHGMODEBYPCFID）_96242347.md`
