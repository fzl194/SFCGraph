---
id: UNC@20.15.2@MMLCommand@RMV SMCAUSEGRP
type: MMLCommand
name: RMV SMCAUSEGRP（删除SM原因值映射组配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV SMCAUSEGRP（删除SM原因值映射组配置）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

此命令用于删除一个原因值映射组配置记录。

## 注意事项

- 该命令执行后立即生效。

- 当删除一个原因值映射组时，一定确保在SMFCAUSECTRL、GGSNCAUSECTRL、SPGWCAUSECTRL和SMCAUSEMAP命令中无引用该ID记录，否则执行删除时系统提示CAUSEGRPID已被某个协议参数值使用，然后中断删除操作。建议通过查询命令确认在哪里使用CAUSEGRPID并删除那一条记录，再执行此删除命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定表示一个原因值映射规则集合的唯一数字ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMCAUSEGRP]] · SM原因值映射组配置（SMCAUSEGRP）

## 使用实例

当CAUSEGRPID值为126的原因值组标识未被任何协议使用时，删除CAUSEGRPID（原因值组标识）为126的原因值映射组记录：

```
RMV SMCAUSEGRP: CAUSEGRPID=126;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SMCAUSEGRP.md`
