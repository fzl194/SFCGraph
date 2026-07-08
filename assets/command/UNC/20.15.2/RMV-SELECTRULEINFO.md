---
id: UNC@20.15.2@MMLCommand@RMV SELECTRULEINFO
type: MMLCommand
name: RMV SELECTRULEINFO（删除UPF选择规则信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SELECTRULEINFO
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF选择规则信息
status: active
---

# RMV SELECTRULEINFO（删除UPF选择规则信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于删除UPF选择规则信息。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCF下发的规则名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD UPFBINDSELRULE命令中的“规则名称”参数取值保持一致时，该规则的参数功能生效。 |

## 操作的配置对象

- [UPF选择规则信息（SELECTRULEINFO）](configobject/UNC/20.15.2/SELECTRULEINFO.md)

## 使用实例

删除UPF选择规则信息，规则名称为"rulename1"：

```
RMV SELECTRULEINFO: RULENAME="rulename1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UPF选择规则信息（RMV-SELECTRULEINFO）_44232741.md`
