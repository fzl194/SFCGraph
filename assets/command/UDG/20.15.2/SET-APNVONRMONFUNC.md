---
id: UDG@20.15.2@MMLCommand@SET APNVONRMONFUNC
type: MMLCommand
name: SET APNVONRMONFUNC（设置VoNR语音质量监控功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNVONRMONFUNC
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- APN VoNR语音质量检测功能
status: active
---

# SET APNVONRMONFUNC（设置VoNR语音质量监控功能开关）

## 功能

**适用NF：UPF**

该命令用于设置VoNR语音质量监控功能开关。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条。初始值均为DISABLE。
- 对应apn开启了VoNR语音质量监控功能，会导致性能下降，重新进行性能评估后再配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| SWITCH | VoNR语音质量监控功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VoNR语音质量监控功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNVONRMONFUNC]] · VoNR语音质量监控功能开关（APNVONRMONFUNC）

## 使用实例

为了监控APN ims的语音质量，设置APN ims的语音质量监控开关为ENABLE：

```
SET APNVONRMONFUNC: APN="ims", SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置VoNR语音质量监控功能开关（SET-APNVONRMONFUNC）_91056082.md`
