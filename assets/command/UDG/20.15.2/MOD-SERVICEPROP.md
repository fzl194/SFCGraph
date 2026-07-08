---
id: UDG@20.15.2@MMLCommand@MOD SERVICEPROP
type: MMLCommand
name: MOD SERVICEPROP（修改业务属性）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: SERVICEPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 业务属性
status: active
---

# MOD SERVICEPROP（修改业务属性）

## 功能

**适用NF：PGW-U、UPF**

![](修改业务属性（MOD SERVICEPROP）_86528681.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，ServiceProp可能已经被绑定。

该命令用于修改业务属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVPROPNAME | 业务属性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务属性名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SERVICEID | 业务标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务标识。全局唯一。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务属性优先级。全局唯一。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SERVICEPROP]] · 业务属性（SERVICEPROP）

## 使用实例

修改一组SERVICEID以及优先级：SRVPROPNAME为test，SERVICEID为1，PRIORITY为100：

```
MOD SERVICEPROP:SRVPROPNAME="test",SERVICEID=1,PRIORITY=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改业务属性（MOD-SERVICEPROP）_86528681.md`
