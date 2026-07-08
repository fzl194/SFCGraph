---
id: UNC@20.15.2@MMLCommand@STR CSCFGREBUILD
type: MMLCommand
name: STR CSCFGREBUILD（启动对特定配置的缓存重建）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: CSCFGREBUILD
command_category: 动作类
applicable_nf:
- PGW-C
- SGW-C
- AMF
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# STR CSCFGREBUILD（启动对特定配置的缓存重建）

## 功能

**适用NF：PGW-C、SGW-C、AMF、SMF、GGSN**

该命令用于启动业务进程对特定配置的缓存重建。

当发现本地配置缓存和OM的配置数据不一致时，可以使用该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMLNAME | 配置命令名称 | 可选必选说明：必选参数<br>参数含义：该参数表示配置命令的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：<br>该参数表示配置命令的名称，比如PLMNNS，不要输入ADD/RMV/MOD/LST等操作字符，优先LST命令名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CSCFGREBUILD]] · 对特定配置的缓存重建（CSCFGREBUILD）

## 使用实例

启动业务进程对PLMNNS配置的缓存重建，执行如下命令：

```
STR CSCFGREBUILD: MMLNAME="PLMNNS";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-CSCFGREBUILD.md`
