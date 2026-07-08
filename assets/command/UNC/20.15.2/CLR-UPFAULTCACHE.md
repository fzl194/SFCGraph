---
id: UNC@20.15.2@MMLCommand@CLR UPFAULTCACHE
type: MMLCommand
name: CLR UPFAULTCACHE（清除用户面故障缓存）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: UPFAULTCACHE
command_category: 动作类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- 用户面故障管理
status: active
---

# CLR UPFAULTCACHE（清除用户面故障缓存）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于清除用户面故障缓存。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPINSTANCEID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。不区分大小写。<br>默认值：无<br>配置原则：无 |
| FAULTTYPE | 故障类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定故障类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（所有）<br>- N3（N3链路故障信息）<br>- N6（N6链路故障信息）<br>默认值：ALL<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"FAULTTYPE"配置为"N6"时为条件可选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFAULTCACHE]] · 用户面故障缓存（UPFAULTCACHE）

## 使用实例

清除所有用户面故障缓存。CLR UPFAULTCACHE: FAULTTYPE=ALL;

```
CLR UPFAULTCACHE: FAULTTYPE=ALL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-UPFAULTCACHE.md`
