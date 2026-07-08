---
id: UDG@20.15.2@MMLCommand@RMV EXTERNALDB
type: MMLCommand
name: RMV EXTERNALDB（卸载外置规则数据库）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: EXTERNALDB
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 百万级业务规则库
- 外部规则数据库
status: active
---

# RMV EXTERNALDB（卸载外置规则数据库）

## 功能

**适用NF：PGW-U、UPF**

![](卸载外置规则数据库（RMV EXTERNALDB）_93973677.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，卸载外置规则数据库会改变使用外置规则数据库的用户业务的匹配结果，导致用户命中规则变化，请谨慎使用并联系华为支持协助操作。

该命令用来卸载已经加载的外置规则数据库。

## 注意事项

- 该命令执行后立即生效。
- 加载或者卸载命令两次执行间隔不能小于20s。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DBTYPE | 数据库类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置外置规则库类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OTT：OTT规则数据库。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXTERNALDB]] · 外置规则数据库（EXTERNALDB）

## 使用实例

卸载外置OTT规则数据库：

```
RMV EXTERNALDB: DBTYPE=OTT;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/卸载外置规则数据库（RMV-EXTERNALDB）_93973677.md`
