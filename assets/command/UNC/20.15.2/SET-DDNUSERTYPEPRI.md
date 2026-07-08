---
id: UNC@20.15.2@MMLCommand@SET DDNUSERTYPEPRI
type: MMLCommand
name: SET DDNUSERTYPEPRI（设置基于用户属性的DDN消息优先级）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DDNUSERTYPEPRI
command_category: 配置类
applicable_nf:
- SGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 基于用户属性的DDN优先级管理
status: active
---

# SET DDNUSERTYPEPRI（设置基于用户属性的DDN消息优先级）

## 功能

**适用NF：SGW-C、SMF**

该命令用于设置本地用户、漫游用户、拜访用户的DDN消息的优先级。

## 注意事项

- 该命令执行后立即生效。

- DDN Throttling功能使能时高优先级业务流触发的DDN消息不流控。
- DDN Throttling功能使能时，当低优先级业务流触发的DDN消息被全部或部分流控时，最低优先级业务流触发的DDN消息会被全部流控。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DDNUSERTYPESW | HOMEPRIORITY | ROAMPRIORITY | VISITPRIORITY |
| --- | --- | --- | --- |
| DISABLE | DDN_LOW | DDN_LOWEST | DDN_LOW |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DDNUSERTYPESW | DDN用户类型优先级开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否使能基于用户的本地漫游拜访属性识别DDN消息的优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：无 |
| HOMEPRIORITY | 本地用户优先级 | 可选必选说明：该参数在"DDNUSERTYPESW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置本地用户的DDN消息的优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DDN_LOW（低）<br>- DDN_HIGH（高）<br>- DDN_LOWEST（最低）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNUSERTYPEPRI查询当前参数配置值。<br>配置原则：无 |
| ROAMPRIORITY | 漫游用户优先级 | 可选必选说明：该参数在"DDNUSERTYPESW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置漫游用户的DDN消息的优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DDN_LOW（低）<br>- DDN_HIGH（高）<br>- DDN_LOWEST（最低）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNUSERTYPEPRI查询当前参数配置值。<br>配置原则：无 |
| VISITPRIORITY | 拜访用户优先级 | 可选必选说明：该参数在"DDNUSERTYPESW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置拜访用户的DDN消息的优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DDN_LOW（低）<br>- DDN_HIGH（高）<br>- DDN_LOWEST（最低）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNUSERTYPEPRI查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DDNUSERTYPEPRI]] · 基于用户属性的DDN消息优先级（DDNUSERTYPEPRI）

## 使用实例

设置使能基于用户的本地漫游拜访属性识别DDN消息的优先级，本地用户的DDN消息优先级为high，漫游用户的DDN消息优先级为low，拜访用户的DDN消息优先级为lowest：

```
SET DDNUSERTYPEPRI: DDNUSERTYPESW=ENABLE, HOMEPRIORITY=DDN_HIGH, ROAMPRIORITY=DDN_LOW, VISITPRIORITY=DDN_LOWEST;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-DDNUSERTYPEPRI.md`
