---
id: UNC@20.15.2@MMLCommand@RMV NCGALMSRV
type: MMLCommand
name: RMV NCGALMSRV（删除告警服务器相关配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NCGALMSRV
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 短消息告警服务功能
status: active
---

# RMV NCGALMSRV（删除告警服务器相关配置信息）

## 功能

![](删除告警服务器相关配置信息（RMV NCGALMSRV）_77419824.assets/notice_3.0-zh-cn_2.png)

该命令用于删除告警服务器相关配置信息。若删除可能导致NCG无法向目的网元上报相关告警信息。

**适用NF：NCG**

该命令用于删除告警服务器相关配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMSRVNAME | 告警服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定告警服务器名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCGALMSRV]] · 告警服务器相关配置信息（NCGALMSRV）

## 使用实例

删除告警服务器配置标识为AlarmServerCfg配置：

```
RMV NCGALMSRV:ALMSRVNAME="AlarmServerCfg";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NCGALMSRV.md`
