---
id: UDG@20.15.2@MMLCommand@ADD SERVICEPROP
type: MMLCommand
name: ADD SERVICEPROP（增加业务属性）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SERVICEPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 业务属性
status: active
---

# ADD SERVICEPROP（增加业务属性）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加业务属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 系统配置的所有业务中业务属性名称之间不能重复，业务标识之间不能重复，优先级之间不能重复。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVPROPNAME | 业务属性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务属性名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SERVICEID | 业务标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务标识。全局唯一。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务属性优先级。全局唯一。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：取值越小，优先级越高。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [业务属性（SERVICEPROP）](configobject/UDG/20.15.2/SERVICEPROP.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00029]]

## 使用实例

增加一条业务属性：SRVPROPNAME为test，SERVICEID为1，PRIORITY为10：

```
ADD SERVICEPROP:SRVPROPNAME="test",SERVICEID=1,PRIORITY=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加业务属性（ADD-SERVICEPROP）_82837590.md`
