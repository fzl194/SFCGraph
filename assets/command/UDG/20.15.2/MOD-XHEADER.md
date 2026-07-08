---
id: UDG@20.15.2@MMLCommand@MOD XHEADER
type: MMLCommand
name: MOD XHEADER（修改扩展头域）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: XHEADER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 扩展头域
status: active
---

# MOD XHEADER（修改扩展头域）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置扩展头域相关参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| XHEADERNAME | 扩展头域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置扩展头域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| XHEADER | 扩展头域 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展头域。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| XHEADERVALUE | 扩展头域取值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展头域值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/XHEADER]] · 扩展头域（XHEADER）

## 使用实例

假如运营商需要修改一条扩展头域：

```
MOD XHEADER: XHEADERNAME="testxheader", XHEADER="x-mms", XHEADERVALUE="6";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改扩展头域（MOD-XHEADER）_82912621.md`
