---
id: UNC@20.15.2@MMLCommand@SET CPGTPUPARA
type: MMLCommand
name: SET CPGTPUPARA（设置GTPU参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CPGTPUPARA
command_category: 配置类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N4 GTP-U管理
- N4 GTP-U路径参数管理
status: active
---

# SET CPGTPUPARA（设置GTPU参数）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于设置协议定义的GTPU相关功能参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ECHOSWITCH | ECHOINTERVAL | ECHOTIME | T3ECHO | N3ECHO |
| --- | --- | --- | --- | --- |
| ENABLE | 60 | 30 | 3 | 3 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ECHOSWITCH | 主动发送路径探测消息开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMF是否主动发送路径探测Echo消息。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（关）<br>- ENABLE（开）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPGTPUPARA查询当前参数配置值。<br>配置原则：<br>ENABLE：GTPU路径建立后，SMF主动发送路径探测Echo消息；<br>DISABLE：GTPU路径建立后，SMF不主动发送路径探测Echo消息。 |
| ECHOINTERVAL | 路径探测消息间隔(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置SMF发送GTPU路径探测消息时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是60~3600。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPGTPUPARA查询当前参数配置值。<br>配置原则：无 |
| ECHOTIME | 故障后重试探测次数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置GTPU路径故障后，SMF为等待路径恢复而发送路径探测消息的次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~60。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPGTPUPARA查询当前参数配置值。<br>配置原则：无 |
| T3ECHO | 路径探测消息重发时间间隔(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置SMF发送GTPU路径探测消息重发时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~20。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPGTPUPARA查询当前参数配置值。<br>配置原则：无 |
| N3ECHO | 路径探测消息最大重试次数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SMF发送GTPU路径探测消息最大重试次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~6。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPGTPUPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [GTPU参数（CPGTPUPARA）](configobject/UNC/20.15.2/CPGTPUPARA.md)

## 使用实例

打开GTPU Echo请求发送开关；

```
SET CPGTPUPARA: ECHOSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置GTPU参数（SET-CPGTPUPARA）_13800472.md`
