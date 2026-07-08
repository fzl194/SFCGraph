---
id: UNC@20.15.2@MMLCommand@SET SNDCP
type: MMLCommand
name: SET SNDCP（设置SNDCP参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SNDCP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- SNDCP参数
status: active
---

# SET SNDCP（设置SNDCP参数）

## 功能

**适用网元：SGSN**

该命令用来设置SNDCP层系统参数。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 参数修改后需要重启GBP进程才能生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAXNPDU | 最大缓冲N-PDU数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置单进程最大缓冲N-PDU数。<br>数据来源：整网规划<br>取值范围：0～1650000<br>系统初始设置值：20000 |
| NSAPIMAXNPDU | 每个NSAPI最大缓冲N-PDU数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置每个NSAPI最大缓冲N-PDU数。<br>数据来源：整网规划<br>取值范围：0～255<br>系统初始设置值：5 |
| UNSENTVL | 负流量阈值（KB） | 可选必选说明：可选参数<br>参数含义：该参数用于设置负流量阈值。<br>数据来源：整网规划<br>取值范围：1～10000<br>系统初始设置值：10 |

## 操作的配置对象

- [SNDCP参数状态（SNDCP）](configobject/UNC/20.15.2/SNDCP.md)

## 使用实例

设置SNDCP参数，设置最大缓冲N-PDU数为“20000”，每个NSAPI最大缓冲N-PDU数为“5”：

SET SNDCP: MAXNPDU=20000, NSAPIMAXNPDU=5;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SNDCP参数(SET-SNDCP)_26146026.md`
