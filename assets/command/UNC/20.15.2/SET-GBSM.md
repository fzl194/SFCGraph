---
id: UNC@20.15.2@MMLCommand@SET GBSM
type: MMLCommand
name: SET GBSM（设置Gb模式SM协议参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GBSM
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- SM协议参数管理
- Gb模式SM协议参数
status: active
---

# SET GBSM（设置Gb模式SM协议参数）

## 功能

![](设置Gb模式SM协议参数(SET GBSM)_72345297.assets/notice_3.0-zh-cn_2.png)

修改GBSM协议配置信息，可能导致某些类型的会话无法激活成功。

**适用网元：SGSN**

该命令用于设置GBSM协议配置信息，包括定时器参数、流程执行控制标志等。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 修改GBSM协议配置信息，可能导致某些类型的会话无法激活成功。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| T3385 | T3385（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络侧激活定时器时长。在网络侧向MS发送一条ACTIVATE PDP CONTEXT REQUEST消息时启动，在当网络侧收到ACTIVATE PDP CONTEXT ACCEPT/REJECT消息时终止，超时后，将会重发ACTIVATE PDP CONTEXT REQUEST消息，重发次数由N3385来控制。当达到最大重发次数，则流程失败。<br>数据来源：整网规划<br>取值范围：1s~86400s<br>系统初始设置值：8s |
| N3385 | N3385（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定重发ACTIVATE PDP CONTEXT REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0times~5times<br>系统初始设置值：4times |
| T3386 | T3386（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络侧设置定时器时长。在网络侧向MS发送一条MODIFY PDP CONTEXT REQUEST消息时启动，当网络侧收到MODIFY PDP CONTEXT ACCEPT/REJECT消息时终止，终止后，将会根据接收到的消息不同来决定流程是成功还是失败。<br>数据来源：整网规划<br>取值范围：1s~86400s<br>系统初始设置值：8s |
| N3386 | N3386（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定重发MODIFY PDP CONTEXT REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0times~5times<br>系统初始设置值：4times |
| T3395 | T3395（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络侧去激活定时器时长。在网络侧向MS发送一条DEACTIVATE PDP CONTEXT REQUEST消息时启动，当网络侧收到DEACTIVATE PDP CONTEXT ACCEPT/REJECT消息时终止，终止后，将会根据接收到的消息不同来决定流程是成功还是失败。<br>数据来源：整网规划<br>取值范围：1s~86400s<br>系统初始设置值：8s |
| N3395 | N3395（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定重发DEACTIVATE PDP CONTEXT REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0times~5times<br>系统初始设置值：4times |
| PFT_USED | 是否启用PFT | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否启用PFT（Packet Flow Timer），PFT指示了BSS保存BSS分组流控上下文的最大时长。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>系统初始设置值：YES(是) |
| SM_BSS_PFT_T9 | BSS保留PFC的时长定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定BSS存储BSS分组流上下文的最大时间。BSS分组流上下文开始存储在BSS中时和从MS收到LLC帧时启动，等到定时器超时结束后，BSS上面删除BBS分组流上下文。<br>前提条件：该参数在<br>“是否启用PFT”<br>参数设置为<br>“YES(是)”<br>时有效。<br>数据来源：整网规划<br>取值范围：6s~11160s<br>系统初始设置值：40s<br>配置原则：<br>- 此定时器规定了BSS存储BSS分组流上下文的最大时间。当该定时器超时，BSS将删除BSS分组流上下文。 BSS保留PFC时长定时器的最小值为“6s”。<br>- 协议规定：当准备定时器的值大于等于“6s”时，BSS保留PFC时长定时器应该小于准备定时器的值；当准备定时器的值小于“6s”时，BSS保留PFC时长定时器的大小不与准备定时器关联。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBSM]] · Gb模式SM协议参数（GBSM）

## 使用实例

设置GBSM T3385 为8秒：

SET GBSM:T3385=8;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-GBSM.md`
