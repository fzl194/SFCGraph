---
id: UNC@20.15.2@MMLCommand@RMV APNGWPROXYFUNC
type: MMLCommand
name: RMV APNGWPROXYFUNC（删除APN网关Proxy功能配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV APNGWPROXYFUNC（删除APN网关Proxy功能配置）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于删除基于APN的网关Proxy功能配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [APN网关Proxy功能配置（APNGWPROXYFUNC）](configobject/UNC/20.15.2/APNGWPROXYFUNC.md)

## 使用实例

删除“APN”为“huawei2.com”的APN网关Proxy功能配置：

```
RMV APNGWPROXYFUNC: APN="huawei2.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN网关Proxy功能配置（RMV-APNGWPROXYFUNC）_88733225.md`
