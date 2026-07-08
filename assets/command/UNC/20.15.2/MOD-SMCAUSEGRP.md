---
id: UNC@20.15.2@MMLCommand@MOD SMCAUSEGRP
type: MMLCommand
name: MOD SMCAUSEGRP（修改SM原因值映射组配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SMCAUSEGRP
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM原因值管理
- 原因值映射组管理
status: active
---

# MOD SMCAUSEGRP（修改SM原因值映射组配置）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

此命令用于修改原因值映射组配置。每个原因值映射组表示一个原因值映射规则集合，通常将一个源接口和一个目标接口的原因值映射规则作为一个映射组，如N7 cause to GTPv2 cause。SMCAUSEGRP通常是一组SMCAUSEMAP的集合。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定表示一个原因值映射规则集合的唯一数字ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~127。<br>默认值：无<br>配置原则：无 |
| CAUSEGRPNM | 原因值组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当前CAUSEGRPID对应的字符名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMCAUSEGRP]] · SM原因值映射组配置（SMCAUSEGRP）

## 使用实例

当修改原因值组标识为126的原因值组名称时，把CAUSEGRPNM（原因值组名称）修改为aaa：

```
MOD SMCAUSEGRP: CAUSEGRPID=126, CAUSEGRPNM="aaa";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SMCAUSEGRP.md`
