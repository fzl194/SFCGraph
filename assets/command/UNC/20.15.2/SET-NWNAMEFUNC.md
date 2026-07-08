---
id: UNC@20.15.2@MMLCommand@SET NWNAMEFUNC
type: MMLCommand
name: SET NWNAMEFUNC（设置运营商名称信息功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NWNAMEFUNC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- 运营商名称信息功能管理
status: active
---

# SET NWNAMEFUNC（设置运营商名称信息功能）

## 功能

**适用NF：MME**

本命令用于设置运营商名称信息下发功能。该命令对应的业务功能暂未实现。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UNSNDBYHSSID | 使用HSS网元标识不发送运营商名称开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定根据用户归属的HSS主机名中的HSS网元标识判断不给UE发送运营商名称消息的开关。<br>前提条件：SET MMFUNC中的参数“MMINFO（发送网络信息）”和“EMMINFOFIRST（PS网络信息优先）”均勾选“S1_MODE（S1模式）”时该参数配置才生效。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：OFF（关闭）<br>配置原则：通过HSS网元标识区分人网用户和物联网用户时，可以打开本开关。并且使用ADD NWNAMEBYHSS命令配置不发送运营商名称的HSS网元标识。 |
| UNSNDBYHSSNAME | 使用HSS主机名或域名不发送运营商名称开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定根据用户归属的HSS主机名或域名判断不给UE发送运营商名称消息的开关。<br>前提条件：SET MMFUNC中的参数“MMINFO（发送网络信息）”和“EMMINFOFIRST（PS网络信息优先）”均勾选“S1_MODE（S1模式）”时该参数配置才生效。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：OFF（关闭）<br>配置原则：通过HSS的主机名或域名区分人网用户和物联网用户时，可以打开本开关。并且使用ADD NWNAMEBYHSS命令配置不发送运营商名称的HSS的主机名或域名。 |
| UNSNDNB | NB-IoT用户不发送运营商名称开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NB-IoT用户不发送运营商名称的开关。<br>前提条件：SET MMFUNC中的参数“MMINFO（发送网络信息）”和“EMMINFOFIRST（PS网络信息优先）”均勾选“S1_MODE（S1模式）”时该参数配置才生效。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：OFF（关闭）<br>配置原则：针对NB-IoT用户，预期不发送运营商名称时，可以打开本开关。 |
| N26SNDNM | 5G到4G业务流程发送运营商名称开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G到4G的业务流程发送运营商名称的开关。<br>前提条件：SET MMFUNC中的参数“MMINFO（发送网络信息）”和“EMMINFOFIRST（PS网络信息优先）”均勾选“S1_MODE（S1模式）”时该参数配置才生效。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：OFF（关闭）<br>配置原则：针对AMF下发过运营商名称的用户，需要在MME下发默认的运营商名称的场景，可以打开本开关。<br>注意事项：该参数设置为“<br>ON（开启）<br>”后，<br>SET MMFUNC<br>的参数<br>EMMINFOSENDPLY<br>将不生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NWNAMEFUNC]] · 运营商名称信息功能（NWNAMEFUNC）

## 使用实例

现网需要根据用户归属的HSS主机名中的HSS网元标识，判断不给UE发送运营商名称消息，可执行此命令：

SET NWNAMEFUNC: UNSNDBYHSSID=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NWNAMEFUNC.md`
