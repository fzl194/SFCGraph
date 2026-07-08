---
id: UNC@20.15.2@MMLCommand@MOD FILTEROCSPARA
type: MMLCommand
name: MOD FILTEROCSPARA（修改需要过滤掉的OCS实例信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: FILTEROCSPARA
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 需要过滤掉的OCS实例信息
status: active
---

# MOD FILTEROCSPARA（修改需要过滤掉的OCS实例信息）

## 功能

**适用NF：NCG**

该命令用于修改需要过滤掉的OCS实例信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERID | OCS过滤标识 | 可选必选说明：必选参数<br>参数含义：该参数表示过滤的OCS标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）、下划线（_）组成。<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例ID | 可选必选说明：可选参数<br>参数含义：该参数表示NF实例ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）、下划线（_）组成。"NF实例ID"可以通过DSP NFCACHE命令查询。<br>默认值：无<br>配置原则：无 |
| SERINSTANCEID | 业务实例ID | 可选必选说明：可选参数<br>参数含义：该参数表示业务实例ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）、下划线（_）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [需要过滤掉的OCS实例信息（FILTEROCSPARA）](configobject/UNC/20.15.2/FILTEROCSPARA.md)

## 使用实例

修改OCS过滤标识为"ocsid001"的OCS实例信息，设置SERINSTANCEID为"service_instance_0"：

```
MOD FILTEROCSPARA: FILTERID="ocsid001", SERINSTANCEID="service_instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改需要过滤掉的OCS实例信息（MOD-FILTEROCSPARA）_96242569.md`
