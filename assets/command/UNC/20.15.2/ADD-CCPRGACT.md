---
id: UNC@20.15.2@MMLCommand@ADD CCPRGACT
type: MMLCommand
name: ADD CCPRGACT（增加融合计费Proxy基于RG处理动作）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CCPRGACT
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy基于RG处理动作
status: active
---

# ADD CCPRGACT（增加融合计费Proxy基于RG处理动作）

## 功能

**适用NF：NCG**

该命令用于增加融合计费Proxy基于RG的处理动作。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1010条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RGTYPE | RG类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RG的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的费率组设置处理动作）<br>- VALUE（针对费率组设置处理动作）<br>默认值：无<br>配置原则：无 |
| RATINGGROUP | 费率组标识 | 可选必选说明：该参数在"RGTYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于指定费率组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~9223372036854775807。<br>默认值：无<br>配置原则：无 |
| FWDOCSENABLE | 是否转发OCS | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否转发OCS。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCPRGACT]] · 融合计费Proxy基于RG处理动作（CCPRGACT）

## 使用实例

增加费率组标识为2000000009的融合计费Proxy基于RG处理动作，设置是否转发OCS为TRUE：

```
ADD CCPRGACT: RGTYPE=VALUE, RATINGGROUP=2000000009, FWDOCSENABLE=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CCPRGACT.md`
