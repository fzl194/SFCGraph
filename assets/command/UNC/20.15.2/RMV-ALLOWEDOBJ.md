---
id: UNC@20.15.2@MMLCommand@RMV ALLOWEDOBJ
type: MMLCommand
name: RMV ALLOWEDOBJ（删除授权控制对象信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ALLOWEDOBJ
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 访问授权控制
- 访问授权对象管理
status: active
---

# RMV ALLOWEDOBJ（删除授权控制对象信息）

## 功能

**适用NF：NRF**

该命令用于删除授权控制对象信息。当运营商不希望在NRF上配置特定NF对象的访问授权控制时使用。

## 注意事项

- 该命令执行后立即生效。

- 执行此命令后，会导致此授权对象对应的相关授权控制命令配置失败。相关授权控制命令有ADD ALLOWEDPLMNS、ADD ALLOWEDNSSAIS、ADD ALLOWEDNFTYPES、ADD ALLOWEDDOMAINS。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：必选参数<br>参数含义：该参数表示设置访问授权控制策略的NF对象名称，该参数通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。该字段值需要全系统唯一，只能由字母（A-Z或者a-z）、数字（0-9）组成，不能以数字开始。<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：必选参数<br>参数含义：该参数表示设置访问授权控制策略的NF对象的FQDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALLOWEDOBJ]] · 授权控制对象信息（ALLOWEDOBJ）

## 使用实例

当运营商不希望在NRF上配置对象名称为objname001的NF对象的访问授权控制时配置下面命令。

```
RMV ALLOWEDOBJ: OBJNAME="objname001", FQDN="demo123com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除授权控制对象信息（RMV-ALLOWEDOBJ）_09652585.md`
