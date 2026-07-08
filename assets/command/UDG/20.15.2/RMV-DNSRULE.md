---
id: UDG@20.15.2@MMLCommand@RMV DNSRULE
type: MMLCommand
name: RMV DNSRULE（删除DNS规则）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: DNSRULE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- DNS规则
status: active
---

# RMV DNSRULE（删除DNS规则）

## 功能

**适用NF：PGW-U、UPF**

![](删除DNS规则（RMV DNSRULE）_35373558.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令会删除满足条件的DNS规则，并且会导致正在使用这些规则的用户出现规则匹配错误、计费错误等现象。

该命令用于删除DNS规则，可以根据不同的参数组合删除一条或者多条DNS规则，当没有输入参数时，删除所有DNS规则。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATIONID | 应用标识 | 可选必选说明：可选参数<br>参数含义：该参数用于配置DNS列表所属的应用标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：该参数用于和SMF下发的PDR中携带的Application ID进行匹配。 |
| DNSRULENAME | DNS规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置DNS规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| DOMAIN | 域名 | 可选必选说明：可选参数<br>参数含义：该参数用于设置DNS规则的服务器域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DNSRULE]] · DNS规则（DNSRULE）

## 使用实例

- 删除一条DNS规则，其中APPLICATIONID是‘app1’，DNSRULENAME是'rule1'：
  ```
  RMV DNSRULE: APPLICATIONID="app1", DNSRULENAME="rule1";
  ```
- 删除APPLICATIONID关联的所有DNS规格，其中APPLICATIONID是‘app1’：
  ```
  RMV DNSRULE: APPLICATIONID="app1";
  ```
- 删除所有DNS规则，不输入参数：
  ```
  RMV DNSRULE:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-DNSRULE.md`
