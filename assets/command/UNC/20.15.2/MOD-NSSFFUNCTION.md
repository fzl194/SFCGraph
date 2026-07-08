---
id: UNC@20.15.2@MMLCommand@MOD NSSFFUNCTION
type: MMLCommand
name: MOD NSSFFUNCTION（修改NSSF功能实例信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NSSFFUNCTION
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- NSSF性能对象管理
status: active
---

# MOD NSSFFUNCTION（修改NSSF功能实例信息）

## 功能

**适用NF：NSSF**

本命令用于修改NSSF功能实例信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NSSF功能实例号 | 可选必选说明：必选参数<br>参数含义：NSSF功能实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| NAME | NSSF功能实例描述 | 可选必选说明：可选参数<br>参数含义：NSSF功能实例描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |
| ADMINSTATE | 管理状态 | 可选必选说明：可选参数<br>参数含义：NSSF功能实例的管理状态。<br>数据来源：本端规划<br>取值范围：<br>- Locked（锁定）<br>- Unlocked（未锁定）<br>- ShuttingDown（关机）<br>默认值：无<br>配置原则：无 |
| OPERATIONSTATE | 运行状态 | 可选必选说明：可选参数<br>参数含义：NSSF功能实例的运行状态。<br>数据来源：本端规划<br>取值范围：<br>- Enabled（运行）<br>- Disabled（不运行）<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：可选参数<br>参数含义：NSSF功能实例的FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSSFFUNCTION]] · NSSF功能实例信息（NSSFFUNCTION）

## 使用实例

修改NSSF功能实体号为Instanceid01的NSSF功能实例信息，将NSSF功能实体描述改为nfdescription02，管理状态改为Locked，运行状态改为Enabled，FQDN改为fqdn02，最大切片选择次数修改为101。

```
MOD NSSFFUNCTION:INSTANCEID="Instanceid01",NAME="nfdescription02",ADMINSTATE=Locked,OPERATIONSTATE=Enabled,FQDN="fqdn02";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NSSFFUNCTION.md`
