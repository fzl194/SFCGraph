---
id: UNC@20.15.2@MMLCommand@SET CHRSTORECFG
type: MMLCommand
name: SET CHRSTORECFG（设置CHR存盘配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CHRSTORECFG
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- CHR管理
- CHR存盘管理
status: active
---

# SET CHRSTORECFG（设置CHR存盘配置）

## 功能

**适用网元：SGSN、MME**

该命令用于控制系统在上报CHR单据时，配置CHR单据在 ucf 上的存储策略。 ucf 存储CHR单据功能主要应用于没有部署CloudUDN同时又想做本地单据分析的局点，或传输链路中断时将CHR单据本地保存的情况。存储功能打开时 UNC 采集订阅流程的CHR单据发送给 ucf ，并且通知 ucf 存储到本地硬盘中。

## 注意事项

- 该命令执行后立即生效。
- 系统初次运行时，会执行系统初始设置值。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STOREALLFLAG | CHR存储开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制CHR单据在<br>ucf<br>上本地存储功能是否打开。存储开关打开时，<br>ucf<br>上会存储<br>UNC<br>发送的全部单据。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关)”<br>- “ON(开)”<br>系统初始设置值：<br>“OFF(关)”<br>配置原则：<br>- 全量CHR单据不需要在ucf上进行本地存储的时候选择“OFF(关)”。<br>- 全量CHR单据需要在ucf上进行本地存储的时候选择“ON(开)”。 |
| STOREALLTYPE | 存储类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于配置CHR在<br>ucf<br>上进行存储策略的选择。<br>前提条件：该参数在<br>“CHR存储开关”<br>参数配置为<br>“ON(开)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “STORE_ONLY(仅存储)”<br>- “STORE_AND_SEND(存储和转发)”<br>系统初始设置值：<br>“STORE_ONLY(仅存储)”<br>配置原则：<br>- 全量CHR单据只需要在ucf上进行存储，不需要ucf发送给CloudUDN的时候，选择“STORE_ONLY(仅存储)”。<br>- 全量CHR单据需要在ucf上进行存储，同时需要ucf发送给CloudUDN的时候，选择“STORE_AND_SEND(存储和转发)”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHRSTORECFG]] · CHR存盘配置（CHRSTORECFG）

## 使用实例

配置CHR单据在 ucf 上的存储策略： “CHR存储开关” 设置为 “ON(开)” ， “存储类型” 设置为 “STORE_ONLY(仅存储)” 。

SET CHRSTORECFG: STOREALLFLAG=ON, STOREALLTYPE=STORE_ONLY;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CHRSTORECFG.md`
