---
id: UNC@20.15.2@MMLCommand@SET ESM
type: MMLCommand
name: SET ESM（设置S1模式SM协议参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ESM
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- SM协议参数管理
- S1模式SM协议参数
status: active
---

# SET ESM（设置S1模式SM协议参数）

## 功能

**适用网元：MME**

该命令用于设置S1模式SM(Session Management)协议参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| T3485 | T3485（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器T3485的时长。此定时器在MME发送ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST或ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST时启动，在收到UE发回的ACTIVATE DEFAULT EPS BEARER ACCEPT、ACTIVATE DEFAULT EPS BEARER REJECT、ACTIVATE DEDICATED EPS BEARER ACCEPT或ACTIVATE DEDICATED EPS BEARER REJECT时停止。 如果超时会重发ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST或ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST消息，重启定时器，重发次数由参数“N3485”确定，如果重发次数达到配置的最大次数仍没有收到UE响应消息，MME就释放已经分配的资源，启动此定时器的流程结束。<br>数据来源：整网规划<br>取值范围：1s～86400s<br>系统初始设置值：8s |
| N3485 | N3485（times） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器T3485的超时时ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST或ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST消息的重发次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times<br>说明：“0times”<br>表示不进行重发。 |
| T3486 | T3486（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器T3486的时长。此定时器在MME发送MODIFY EPS BEARER CONTEXT REQUEST时启动，在收到UE发回的MODIFY EPS BEARER CONTEXT ACCEPT或MODIFY EPS BEARER CONTEXT REJECT时停止。如果超时会重发MODIFY EPS BEARER CONTEXT REQUEST消息，重启定时器，重发次数由参数“N3486”确定，如果重发次数达到配置的最大次数仍没有收到UE响应消息，MME中承载上下文保持为激活态，启动此定时器的流程结束。<br>数据来源：整网规划<br>取值范围：1s～86400s<br>系统初始设置值：8s |
| N3486 | N3486（times） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器T3486的超时时MODIFY EPS BEARER CONTEXT REQUEST消息的重发次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times<br>说明：“0times”<br>表示不进行重发。 |
| T3489 | T3489（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器T3489的时长。此定时器在MME给UE发ESM INFORMATION REQUEST消息时启动，收到UE响应消息ESM INFORMATION RESPONSE停止。如果超时会重发ESM INFORMATION REQUEST消息，重启定时器，重发次数由参数“N3489”确定，如果重发次数达到配置的最大次数仍没有收到UE响应消息，MME就释放相应资源，启动此定时器的流程结束。<br>数据来源：整网规划<br>取值范围：1s～86400s<br>系统初始设置值：4s |
| N3489 | N3489（times） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器T3489的超时时ESM INFORMATION REQUEST消息的重发次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：2times<br>说明：“0times”<br>表示不进行重发。 |
| T3495 | T3495（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器T3495的时长。此定时器在MME在发送DEACTIVATE EPS BEARER CONTEXT REQUEST消息时启动，收到UE响应DEACTIVATE EPS BEARER CONTEXT ACCEPT消息停止。如果超时会重发DEACTIVATE EPS BEARER CONTEXT REQUEST消息，重启定时器，重发次数由参数“N3495”确定，如果重发次数达到配置的最大次数仍没有收到UE响应消息，MME就去激活EPS承载上下文，启动此定时器的流程结束。<br>数据来源：整网规划<br>取值范围： 1s～86400s<br>系统初始设置值：8s |
| N3495 | N3495（times） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器T3495的超时时DEACTIVATE EPS BEARER CONTEXT REQUEST消息的重发次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times<br>说明：“0times”<br>表示不进行重发。 |
| TSAEBRSETUP | SAE承载建立定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器TSAEBRSETUP的时长。此定时器在MME给eNodeB发送E-RAB SETUP REQUEST消息后启动，收到eNodeB的响应消息E-RAB SETUP RESPONSE后停止。如果超时后还没有收到eNodeB的响应消息，启动此定时器的流程结束。<br>数据来源：整网规划<br>取值范围：0s～30s<br>系统初始设置值：12s |
| TSAEBRMOD | SAE承载修改定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器TSAEBRMOD的时长。此定时器在MME给eNodeB发送E-RAB MODITY REQUEST消息后启动，收到eNodeB的响应消息E-RAB MODITY RESPONSE后停止。如果超时后还没有收到eNodeB的响应消息，启动此定时器的流程结束。<br>数据来源：整网规划<br>取值范围：0s～30s<br>系统初始设置值：12s |
| TSAEBRREL | SAE承载释放定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定定时器TSAEBRREL的时长。此定时器在MME给eNodeB发送E-RAB RELEASE REQUEST消息后启动，收到eNodeB的响应消息E-RAB RELEASE RESPONSE后停止。如果超时后还没有收到eNodeB的响应消息，启动此定时器的流程结束。<br>数据来源：整网规划<br>取值范围：0s～30s<br>系统初始设置值：12s |
| TSAEBRHOLD | SAE承载保留时长（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定在无信号场景下对VoLTE语音或者视频承载的保留时长。MME收到eNodeB的S1连接释放请求消息，如果原因值为<br>“Radio Connection With UE Lost”<br>、或者为<br>[**ADD VOLTEHOLDON**](../../语音承载保活/增加语音承载保活(ADD VOLTEHOLDON)_72345319.md)<br>命令中配置的<br>“S1释放原因值”<br>、或者为<br>“Time critical handover”<br>且软参BYTE_EX_B136 BIT4设置为<br>“1”<br>，则暂时不删除VoLTE语音或者视频承载，对承载保留一段时间，用于协助用户恢复这些承载。<br>数据来源：整网规划<br>取值范围：1s～120s<br>系统初始设置值：60s |

## 操作的配置对象

- [S1模式SM协议参数（ESM）](configobject/UNC/20.15.2/ESM.md)

## 使用实例

设置S1模式SM协议参数，设置所有定时器的时长为10秒，设置N3485为3，设置N3486为2，设置N3489为1，设置N3495为3：

SET ESM: T3485=10, N3485=3, T3486=10, N3486=2, T3489=10, N3489=1, T3495=10, N3495=3;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置S1模式SM协议参数(SET-ESM)_72225383.md`
