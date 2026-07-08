---
id: UDG@20.15.2@MMLCommand@MOD FINGERIDENT
type: MMLCommand
name: MOD FINGERIDENT（修改SA指纹识别配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: FINGERIDENT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- SA指纹识别
- SA指纹识别
status: active
---

# MOD FINGERIDENT（修改SA指纹识别配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来修改SA指纹识别功能配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅用于修改参数FingerIdentCtrl或CfgDomainName。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGPROTMODE | 协议配置方式 | 可选必选说明：必选参数<br>参数含义：该参数用于设置SA指纹识别功能协议的配置方式。<br>数据来源：本端规划<br>取值范围：<br>- ALL：所有协议。<br>- SPECIFIC：指定协议。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CFGPROTMODE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于设置协议名称。<br>数据来源：本端规划<br>取值范围：不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| FINGERIDENTCTRL | 指纹识别结果控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置指纹识别结果控制开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：SA指纹识别结果既用于统计，又参与业务控制。<br>- STATIC_ONLY：SA指纹识别结果只用于统计，不参与业务控制。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CFGPROTMODE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FINGERIDENT]] · SA指纹识别配置（FINGERIDENT）

## 使用实例

修改Facebook协议SA指纹识别结果只用于统计不用于业务控制，配置如下：

```
MOD FINGERIDENT: CFGPROTMODE=SPECIFIC, PROTOCOLNAME="facebook", FINGERIDENTCTRL=STATIC_ONLY;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-FINGERIDENT.md`
