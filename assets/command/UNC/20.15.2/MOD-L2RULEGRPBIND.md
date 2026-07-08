---
id: UNC@20.15.2@MMLCommand@MOD L2RULEGRPBIND
type: MMLCommand
name: MOD L2RULEGRPBIND（修改层二规则组与用户的绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: L2RULEGRPBIND
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 层二规则组绑定
status: active
---

# MOD L2RULEGRPBIND（修改层二规则组与用户的绑定关系）

## 功能

**适用NF：SMF**

该命令用于修改层二规则组与用户的绑定关系。

## 注意事项

- 该命令执行后只对新接入的会话生效。

- 在IMSI号段名称、APN名称、切片业务类型和切片细分标识都相同的情况仅允许绑定一个层二规则组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPBINDNAME | 层二规则组绑定名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定层二规则组绑定名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEGMENTNAME | IMSI号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的IMSI号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>该参数通过ADD IMSIMSISDNSEG命令配置，仅支持配置SEGMENTTYPE为IMSI和IMSIWILDCARD的SEGMENTNAME。 |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户接入的APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| SST | 切片业务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户接入的切片业务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定切片细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>该参数若不配置，默认值为ffffff。 |
| L2RULEGRPNAME | 层二规则组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定层二组规则名称。该参数已经通过ADD L2RULEGROUP命令中的L2RULEGRPNAME参数配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD L2RULEGROUP命令配置生成。 |

## 操作的配置对象

- [层二规则组与用户的绑定关系（L2RULEGRPBIND）](configobject/UNC/20.15.2/L2RULEGRPBIND.md)

## 使用实例

如果需要修改“bind1”的用户与层二规则组的绑定关系，其中APN名称修改为“apn2”，层二规则组名称修改为“rulegrp2”：

```
MOD L2RULEGRPBIND: GRPBINDNAME="bind1", APN="apn1", L2RULEGRPNAME="rulegrp2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改层二规则组与用户的绑定关系（MOD-L2RULEGRPBIND）_70382353.md`
