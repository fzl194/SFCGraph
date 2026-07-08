---
id: UDG@20.15.2@MMLCommand@ADD ABNTRAFFICDT
type: MMLCommand
name: ADD ABNTRAFFICDT（新增异常流量检测开关）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ABNTRAFFICDT
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- APN下终端异常下行流量检测开关
status: active
---

# ADD ABNTRAFFICDT（新增异常流量检测开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来使能APN下终端异常下行流量检测功能。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 系统最多支持配置10000条ABNTRAFFICDT。
- Normal用户不支持异常流检测。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD APN命令配置生成。<br>- 该APN必须是系统已经配置的APN，此功能不支持别名APN的配置使能。 |
| SWITCH | 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定终端异常下行流量检测是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- ENABLE：开启指定APN下终端异常下行流量检测功能。<br>- DISABLE：关闭开启指定APN下终端异常下行流量检测功能。 |
| TRAFFICBEHAVIORSWITCH | 基于流行为的检测开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定基于流行为的终端异常下行流量检测是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：<br>- 如果运营商需要开启基于流行为检测开关时，需要配置该参数。<br>- ENABLE：开启指定APN下基于流行为的终端异常下行流量检测功能。<br>- DISABLE：关闭开启指定APN下基于流行为的终端异常下行流量检测功能。 |

## 操作的配置对象

- [异常流量检测开关（ABNTRAFFICDT）](configobject/UDG/20.15.2/ABNTRAFFICDT.md)

## 关联任务

- [0-00021](task/UDG/20.15.2/0-00021.md)

## 使用实例

假如运营商需使能名称为“apn1.com”的APN的终端异常下行流量检测功能：

```
ADD ABNTRAFFICDT: APN="apn1.com", SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/新增异常流量检测开关（ADD-ABNTRAFFICDT）_82837035.md`
