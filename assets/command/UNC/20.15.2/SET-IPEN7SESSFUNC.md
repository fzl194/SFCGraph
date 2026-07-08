---
id: UNC@20.15.2@MMLCommand@SET IPEN7SESSFUNC
type: MMLCommand
name: SET IPEN7SESSFUNC（设置智能双N7会话特性是否开启）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IPEN7SESSFUNC
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 智能双N7会话
status: active
---

# SET IPEN7SESSFUNC（设置智能双N7会话特性是否开启）

## 功能

**适用NF：SMF、PGW-C**

该命令用于设置智能双N7会话特性是否开启。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| IPEN7SESSFUNCSW |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPEN7SESSFUNCSW | 智能双N7会话特性开关 | 可选必选说明：必选参数<br>参数含义：智能双N7会话特性开关。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：智能N7会话不使能<br>- “ENABLE（使能）”：智能N7会话使能<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPEN7SESSFUNC]] · 智能双N7会话特性是否使能（IPEN7SESSFUNC）

## 使用实例

如果要创建智能双N7会话，则打开智能双N7会话特性开关：

```
SET IPEN7SESSFUNC: IPEN7SESSFUNCSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IPEN7SESSFUNC.md`
