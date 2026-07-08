---
id: UNC@20.15.2@MMLCommand@SET PTTFUNC
type: MMLCommand
name: SET PTTFUNC（设置一键通配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PTTFUNC
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 一键通
- 全局一键通配置
status: active
---

# SET PTTFUNC（设置一键通配置）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于配置整机LTE一键通功能相关的信息。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LTEPTTSWITCH |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LTEPTTSWITCH | LTE一键通功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于全局控制开启和关闭LTE一键通功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PTTFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PTTFUNC]] · 一键通功能配置（PTTFUNC）

## 使用实例

全局使能LTE一键通功能，进行如下设置：

```
SET PTTFUNC: LTEPTTSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PTTFUNC.md`
