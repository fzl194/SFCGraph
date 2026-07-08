---
id: UNC@20.15.2@MMLCommand@SET ACCESSLISTFUNC
type: MMLCommand
name: SET ACCESSLISTFUNC（设置接入控制名单功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ACCESSLISTFUNC
command_category: 配置类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 黑白名单控制
status: active
---

# SET ACCESSLISTFUNC（设置接入控制名单功能）

## 功能

**适用NF：GGSN、SGW-C、PGW-C**

该命令用来配置当前系统是否支持接入控制名单的功能以及系统支持的接入控制名单类型。假设运营商希望允许或者禁止某个名单接入，使用该命令。

当配置SGSN/S-GW/MME IP地址黑白名单控制类型为白名单时，如果SGSN/S-GW/MME信令面IP没有落在该命令配置的SGSN/S-GW/MME IP和掩码所表示的地址段里，用户激活或更新失败，失败原因码：service not supported。

当配置SGSN/S-GW/MME IP地址黑白名单控制类型为黑名单时，如果SGSN/S-GW/MME信令面IP落在该命令配置的SGSN/S-GW/MME IP和掩码所表示的地址段里，用户激活或更新失败，失败原因码：service not supported。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LISTSWITCH | LISTTYPE |
| --- | --- |
| DISABLE | BLACK |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LISTSWITCH | 设置系统是否支持接入控制名单的功能 | 可选必选说明：可选参数<br>参数含义：本参数用于控制打开或关闭接入控制名单的功能。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：关闭接入控制名单的功能<br>- “ENABLE（使能）”：打开接入控制名单的功能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ACCESSLISTFUNC查询当前参数配置值。<br>配置原则：无 |
| LISTTYPE | 黑白名单类型 | 可选必选说明：可选参数<br>参数含义：本参数用于控制接入控制名单类型。<br>数据来源：本端规划<br>取值范围：<br>- “WHITE（白名单使能）”：设置系统支持的接入控制类型为白名单类型<br>- “BLACK（黑名单使能）”：设置系统支持的接入控制类型为黑名单类型<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ACCESSLISTFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [接入控制名单功能（ACCESSLISTFUNC）](configobject/UNC/20.15.2/ACCESSLISTFUNC.md)

## 使用实例

当用户需要支持接入控制名单的功能并设置系统支持的接入控制名单类型为白名单时，进行如下设置，LISTSWITCH为ENABLE，LISTTYPE为WHITE：

```
SET ACCESSLISTFUNC:LISTSWITCH=ENABLE,LISTTYPE=WHITE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置接入控制名单功能（SET-ACCESSLISTFUNC）_72373079.md`
