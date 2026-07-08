---
id: UNC@20.15.2@MMLCommand@MOD APNTOHCTRL
type: MMLCommand
name: MOD APNTOHCTRL（修改APN粒度的智家随行会话控制）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNTOHCTRL
command_category: 配置类
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 智家随行会话管理
status: active
---

# MOD APNTOHCTRL（修改APN粒度的智家随行会话控制）

## 功能

该命令用于修改APN粒度的智家随行会话控制。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定智家随行会话的APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| TOHSW | 智家随行会话开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMF是否支持建立智家随行会话。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>如果不配置该参数，默认为不使能。<br>优先级高于整机配置SET SMFFUNC中的NGLANSWITCH字段。 |
| FWASW | FWA开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMF是否支持建立智家随行场景下的FWA会话。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNTOHCTRL]] · APN粒度的智家随行会话控制（APNTOHCTRL）

## 使用实例

修改APN粒度的智家随行会话控制，APN名称为“toh.apn”，智家随行会话开关由“不使能”修改为“使能”，FWA开关由“不使能”修改为“使能”。

```
MOD APNTOHCTRL: APN="toh.apn",TOHSW=ENABLE,FWASW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-APNTOHCTRL.md`
