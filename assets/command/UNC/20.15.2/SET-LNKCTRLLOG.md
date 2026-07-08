---
id: UNC@20.15.2@MMLCommand@SET LNKCTRLLOG
type: MMLCommand
name: SET LNKCTRLLOG（设置链路控制消息日志开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LNKCTRLLOG
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# SET LNKCTRLLOG（设置链路控制消息日志开关）

## 功能

**适用NF：AMF**

该命令用于设置链路控制消息日志开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTP | SCTP | 可选必选说明：可选参数<br>参数含义：该参数用于控制链路控制消息日志开关是否开启。<br>数据来源：全网规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>系统初始设置值：ON（开启）<br>配置原则： 无 |

## 操作的配置对象

- [链路控制消息日志开关（LNKCTRLLOG）](configobject/UNC/20.15.2/LNKCTRLLOG.md)

## 使用实例

若要关闭链路控制消息日志开关，可以用如下命令：

```
SET LNKCTRLLOG: SCTP=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置链路控制消息日志开关(SET-LNKCTRLLOG)_58047743.md`
