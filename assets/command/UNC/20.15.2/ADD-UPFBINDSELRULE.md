---
id: UNC@20.15.2@MMLCommand@ADD UPFBINDSELRULE
type: MMLCommand
name: ADD UPFBINDSELRULE（增加UPF和规则的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPFBINDSELRULE
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF和规则的绑定关系
status: active
---

# ADD UPFBINDSELRULE（增加UPF和规则的绑定关系）

## 功能

**适用NF：SMF、PGW-C、SGW-C**

该命令用于增加UPF和规则的绑定关系。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入5000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF和规则的绑定关系的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4999。<br>默认值：无<br>配置原则：<br>该参数取值不能重复，建议从0开始顺序取值。 |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCF下发的规则名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD SELECTRULEINFO命令中的“规则名称”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFBINDSELRULE]] · UPF和规则的绑定关系（UPFBINDSELRULE）

## 使用实例

增加UPF和规则的绑定关系，UPF实例名称为"upf_instance_1"，规则名称为"rulename1"：

```
ADD UPFBINDSELRULE: INDEX=0, NFINSTANCENAME="upf_instance_1", RULENAME="rulename1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UPFBINDSELRULE.md`
