---
id: UNC@20.15.2@MMLCommand@SET IMSDDNFLOWCTRLCHR
type: MMLCommand
name: SET IMSDDNFLOWCTRLCHR（设置IMS DDN流量控制上报CHR配置开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IMSDDNFLOWCTRLCHR
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- IMS DDN流量控制上报CHR配置
status: active
---

# SET IMSDDNFLOWCTRLCHR（设置IMS DDN流量控制上报CHR配置开关）

## 功能

**适用NF：SGW-C**

该命令用来设置语音IMS的DDN消息流控时是否上报CHR单据功能的开关。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| IMSDDNFLOWCTRLCHR |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSDDNFLOWCTRLCHR | IMS DDN流量控制上报CHR配置开关 | 可选必选说明：可选参数<br>参数含义：该参数用来设置IMS DDN流量控制上报CHR配置开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSDDNFLOWCTRLCHR查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [IMS DDN流量控制上报CHR配置开关（IMSDDNFLOWCTRLCHR）](configobject/UNC/20.15.2/IMSDDNFLOWCTRLCHR.md)

## 使用实例

设置语音IMS的DDN消息流控时上报CHR单据开关使能，IMSDDNFLOWCTRLCHR为ENABLE：

```
SET IMSDDNFLOWCTRLCHR: IMSDDNFLOWCTRLCHR=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置IMS-DDN流量控制上报CHR配置开关（SET-IMSDDNFLOWCTRLCHR）_49776577.md`
