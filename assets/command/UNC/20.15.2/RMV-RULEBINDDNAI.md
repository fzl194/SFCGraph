---
id: UNC@20.15.2@MMLCommand@RMV RULEBINDDNAI
type: MMLCommand
name: RMV RULEBINDDNAI（删除预定义规则关联的DNAI）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RULEBINDDNAI
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 预定义规则DNAI绑定
status: active
---

# RMV RULEBINDDNAI（删除预定义规则关联的DNAI）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于删除预定义规则关联的DNAI。

## 注意事项

- 该命令执行后立即生效。

- 如果DNAI为空， 删除预定义规则关联的所有DNAI。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 预定义规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定预定义规则名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数通过ADD RULE命令配置生成。 |
| DNAI | 数据网络访问标识符 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络访问标识符。该参数的数据规划上需要和PNFDNAI命令中的“数据网络访问标识”参数保持一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RULEBINDDNAI]] · 预定义规则关联的DNAI（RULEBINDDNAI）

## 使用实例

删除预定义规则关联的特定DNAI。 2. DNAI置为空时，删除预定义规则关联的所有DNAI。

```
RMV RULEBINDDNAI: RULENAME="rule1", DNAI="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RULEBINDDNAI.md`
