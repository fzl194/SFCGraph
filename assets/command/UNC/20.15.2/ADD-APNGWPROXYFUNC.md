---
id: UNC@20.15.2@MMLCommand@ADD APNGWPROXYFUNC
type: MMLCommand
name: ADD APNGWPROXYFUNC（增加APN网关Proxy功能配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNGWPROXYFUNC
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- APN网关Proxy功能
status: active
---

# ADD APNGWPROXYFUNC（增加APN网关Proxy功能配置）

## 功能

**适用NF：PGW-C、GGSN**

此命令用于增加指定APN的网关Proxy功能配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| PROXYSW | Proxy功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于基于APN控制是否打开网关Proxy功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |
| ALIASAPN | 别名APN | 可选必选说明：可选参数<br>参数含义：该参数用于控制Proxy GGSN/PGW在转发用户激活请求消息时将消息中的APN信元替换成本参数设置的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符。<br>默认值：无<br>配置原则：无 |
| MULTIDNNPROXYSW | 2B2C漫游双DNN特性Proxy功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于UNC是否支持2B2C漫游双DNN特性Proxy功能 。当UNC不支持2B2C双域DNN功能，使能该参数，UNC将信令消息转发至支持2B2C双域DNN功能的PGW，仅PGW-C形态生效。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNGWPROXYFUNC]] · APN网关Proxy功能配置（APNGWPROXYFUNC）

## 使用实例

增加“APN”为“huawei.com”，“别名APN”为“huawei1.com”，2B2C双域DNN特性Proxy功能开关为DISABLE的APN网关Proxy功能配置：

```
ADD APNGWPROXYFUNC: APN="huawei.com", PROXYSW=ENABLE, ALIASAPN="huawei1.com", MULTIDNNPROXYSW=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNGWPROXYFUNC.md`
