---
id: UNC@20.15.2@MMLCommand@ADD APNWIFILTEHO
type: MMLCommand
name: ADD APNWIFILTEHO（增加基于APN的E-UTRAN和WLAN互操作控制属性）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNWIFILTEHO
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- E-UTRAN和WLAN互操作控制
- 基于APN的E-UTRAN和WLAN互操作控制
status: active
---

# ADD APNWIFILTEHO（增加基于APN的E-UTRAN和WLAN互操作控制属性）

## 功能

**适用NF：PGW-C**

该命令用于增加基于APN的E-UTRAN和WLAN互操作控制属性。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户请求的APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| S2BHANDOVER | S2b接口切换开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Create Session Request消息未携带HI标记位但PGW-C上有符合切换条件的上下文时，E-UTRAN和WLAN相关S2b接口的互操作是否按照切换处理。该参数为Enable时，WSFD-201302支持WLAN与GSM/UMTS/LTE双流并发失效。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：表示按照切换处理。<br>- “DISABLE（不使能）”：表示按照激活处理。<br>- “INHERIT（继承全局）”：表示继承全局配置SET GLOBALWIFILTEHO的S2BHANDOVER选项。<br>默认值：INHERIT<br>配置原则：无 |
| S2AHANDOVER | S2a接口切换开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Create Session Request消息未携带HI标记位但PGW-C上有符合切换条件的上下文时，E-UTRAN和WLAN相关S2a接口的互操作是否按照切换处理。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：表示按照切换处理。<br>- “DISABLE（不使能）”：表示按照激活处理。<br>- “INHERIT（继承全局）”：表示继承全局配置SET GLOBALWIFILTEHO的S2BHANDOVER选项。<br>默认值：INHERIT<br>配置原则：无 |

## 操作的配置对象

- [基于APN的E-UTRAN和WLAN互操作控制属性（APNWIFILTEHO）](configobject/UNC/20.15.2/APNWIFILTEHO.md)

## 使用实例

新增APN为"huawei.com"的E-UTRAN和WLAN互操作属性，使能S2b接口切换开关：

```
ADD APNWIFILTEHO: APN="huawei.com",S2BHANDOVER=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加基于APN的E-UTRAN和WLAN互操作控制属性（ADD-APNWIFILTEHO）_82122523.md`
