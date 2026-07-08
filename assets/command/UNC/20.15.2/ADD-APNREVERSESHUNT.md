---
id: UNC@20.15.2@MMLCommand@ADD APNREVERSESHUNT
type: MMLCommand
name: ADD APNREVERSESHUNT（增加基于APN的反向分流配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNREVERSESHUNT
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 本地分流管理
- 反向分流控制
status: active
---

# ADD APNREVERSESHUNT（增加基于APN的反向分流配置）

## 功能

**适用NF：SMF**

该命令用于开启或关闭基于APN的反向分流功能。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |
| REVERSESHUNT | 反向分流开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭基于APN的反向分流功能。当开启反向分流功能时，在ULCL/BP场景下，当UE离开MEC园区时，MEC业务从主锚点UPF出到Local DN，Internet业务从辅锚点UPF出到DN。当UE在MEC园区时，MEC业务仍然从辅锚点UPF出到Local DN，Internet业务从主锚点UPF出到DN。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |

## 操作的配置对象

- [基于APN的反向分流功能配置（APNREVERSESHUNT）](configobject/UNC/20.15.2/APNREVERSESHUNT.md)

## 使用实例

增加“APN”为“HUAWEI.COM”的反向分流功能：

```
ADD APNREVERSESHUNT: APN="HUAWEI.COM", REVERSESHUNT=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加基于APN的反向分流配置（ADD-APNREVERSESHUNT）_51696222.md`
