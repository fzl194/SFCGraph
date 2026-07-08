---
id: UNC@20.15.2@MMLCommand@ADD RULEBINDDNAI
type: MMLCommand
name: ADD RULEBINDDNAI（增加预定义规则关联的DNAI）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD RULEBINDDNAI（增加预定义规则关联的DNAI）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加预定义规则关联的DNAI。

当需要指定预定义规则下发某边缘UPF时，可通过本命令绑定Rule和边缘UPF的DNAI的对应关系来实现。

当一个预定义规则绑定到某边缘UPF所对应的DNAI时，该预定义相关规则就只下发给该边缘UPF。

## 注意事项

- 该命令执行后立即生效。

- 仅当指定预定义规则的Rule Range为LOCAL时，才可以绑定到边缘UPF对应的DNAI上。Rule Range为ALL的预定义规则绑定DNAI无实际意义， SMF会将Rule同时下发给中心和所有边缘UPF。Rule Range为CENTRAL时，该预定义规则不能绑定到任何边缘UPF的DNAI上。

- 最多可输入10000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 预定义规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定预定义规则名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数通过ADD RULE命令配置生成。 |
| DNAI | 数据网络访问标识符 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识符。该参数的数据规划上需要和PNFDNAI命令中的“数据网络访问标识”参数保持一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RULEBINDDNAI]] · 预定义规则关联的DNAI（RULEBINDDNAI）

## 使用实例

如果要增加预定义规则关联的DNAI，则使用此命令。

```
ADD RULEBINDDNAI: RULENAME="rule1", DNAI="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加预定义规则关联的DNAI（ADD-RULEBINDDNAI）_27170471.md`
