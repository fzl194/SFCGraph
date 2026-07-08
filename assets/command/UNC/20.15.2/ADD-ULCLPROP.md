---
id: UNC@20.15.2@MMLCommand@ADD ULCLPROP
type: MMLCommand
name: ADD ULCLPROP（增加ULCL属性）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ULCLPROP
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 16000
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- ULCL属性
status: active
---

# ADD ULCLPROP（增加ULCL属性）

## 功能

**适用NF：SMF**

该命令用于添加ULCL分流策略的属性，用于实现本地分流策略控制。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为16000。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- 同一“ULCL属性名称”下最多可添加16个DNAI。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ULCLPROPNAME | ULCL属性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置ULCL的属性名称。该参数可供RULE命令中的“策略名称”参数引用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNAI | 数据网络访问标识符 | 可选必选说明：必选参数<br>参数含义：该参数用于设置ULCL属性名称相关联的数据网络访问标识符。该参数的数据规划上需要和PNFDNAI命令中的“数据网络访问标识”参数保持一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ULCLPROP]] · ULCL属性（ULCLPROP）

## 使用实例

假如运营商需要定义一个ULCL属性名称与DNAI对应关系，ULCL属性名称为“testulclpropname”，DNAI为“testdnai”：

```
ADD ULCLPROP: ULCLPROPNAME="testulclpropname", DNAI="testdnai";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加ULCL属性（ADD-ULCLPROP）_16935565.md`
