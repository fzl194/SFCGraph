---
id: UNC@20.15.2@MMLCommand@MOD APNSMCOMFUNC
type: MMLCommand
name: MOD APNSMCOMFUNC（修改APN粒度的通用会话拓展功能控制）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNSMCOMFUNC
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话管理拓展功能
- APN级通用会话拓展功能
status: active
---

# MOD APNSMCOMFUNC（修改APN粒度的通用会话拓展功能控制）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改APN粒度的通用会话拓展功能控制。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| GETPOLICYFIRST | 在EPS是否先获取策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当PGW-C对接PCF时，是否先跟PCF交互获取会话策略，再动态分配UE IP地址。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：表示PGW-C先跟PCF交互获取会话策略，再动态分配UE IP地址。<br>- “DISABLE（不使能）”：表示保持原有实现，即PGW-C先动态分配UE IP地址，再跟PCF交互获取会话策略。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNSMCOMFUNC]] · APN粒度的通用会话拓展功能控制（APNSMCOMFUNC）

## 使用实例

修改“APN名称”为“HUAWEI.COM”的APN粒度通用会话拓展功能控制，在EPS中不先获取策略。

```
MOD APNSMCOMFUNC: APN="HUAWEI.COM",GETPOLICYFIRST=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-APNSMCOMFUNC.md`
