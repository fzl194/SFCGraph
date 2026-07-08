---
id: UNC@20.15.2@MMLCommand@DSP NCCDIAGLOG
type: MMLCommand
name: DSP NCCDIAGLOG（显示NETCONFC与其他组件的消息交互信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCCDIAGLOG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议客户端
status: active
---

# DSP NCCDIAGLOG（显示NETCONFC与其他组件的消息交互信息）

## 功能

该命令用于显示NETCONFC与其他组件的消息交互信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATATYPE | 诊断数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示诊断信息数据的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FSM：状态机信息。<br>- NCCOPERATION：NETCONFC操作信息。<br>- MESSAGE：消息交互信息。<br>- FAILOPERATION：操作失败信息。<br>- CONNECT：建连信息。<br>- RPC：报文信息。<br>- DATA：静态数据信息。<br>- MODELRSHHIS：模型刷新历史。<br>默认值：无 |
| PEERID | 远端ID | 可选必选说明：条件必选参数或条件可选参数，该参数在<br>“DATATYPE”<br>配置为<br>“MODELRSHHIS”<br>时为必选参数。该参数在<br>“DATATYPE”<br>配置为<br>“MESSAGE”<br>、<br>“FAILOPERATION”<br>、<br>“CONNECT”<br>、<br>“RPC”<br>、<br>“FSM”<br>或<br>“ DATA”<br>时为可选参数。<br>参数含义：该参数用于表示远端设备ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PID | 组件PID | 可选必选说明：条件可选参数，该参数在<br>“DATATYPE”<br>配置为<br>“MESSAGE”<br>、<br>“FAILOPERATION”<br>、<br>“CONNECT”<br>、<br>“RPC”<br>、<br>“FSM ”<br>或<br>“DATA”<br>时为可选参数。<br>参数含义：该参数用于表示NETCONFC的组件PID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0～0xFFFFFFFF。<br>默认值：无 |
| RPCTYPE | 报文类型 | 可选必选说明：条件必选参数，该参数在<br>“DATATYPE”<br>配置为<br>“RPC”<br>时为必选参数。<br>参数含义：该参数用于表示报文信息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HISTORY：报文历史信息。<br>- ERROR：报文错误信息。<br>默认值：无 |
| STATCDATATYPE | 静态数据类型 | 可选必选说明：条件必选参数，该参数在<br>“DATATYPE”<br>配置为<br>“DATA”<br>时为必选参数。<br>参数含义：该参数用于表示静态数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCAL：本地数据。<br>- DRVLOAD：驱动加载记录。<br>默认值：无 |
| FAILTYPE | 失败信息类型 | 可选必选说明：条件可选参数，该参数在<br>“DATATYPE”<br>配置为<br>“FAILOPERATION”<br>时为可选参数。<br>参数含义：该参数用于表示失败信息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- XSS：Xss Lib失败信息。<br>默认值：无 |
| FSMTYPE | 状态机类型 | 可选必选说明：条件必选参数，该参数在<br>“DATATYPE”<br>配置为<br>“FSM”<br>时为必选参数。<br>参数含义：该参数用于表示状态机信息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SESSION：会话状态机信息。<br>- CHANNEL：通道状态机信息。<br>- SYNCGETPEER：对账获取远端状态机。<br>- SYNCGETLOCAL：对账获取本地状态机。<br>- SYNCEDIT：对账编辑远端状态机。<br>- SYNCCONFIG：对账状态机。<br>- RPC：报文状态机。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCCDIAGLOG]] · NETCONFC与其他组件的消息交互信息（NCCDIAGLOG）

## 使用实例

显示NETCONFC与其他组件的消息交互信息：

```
DSP NCCDIAGLOG:DATATYPE=NCCOPERATION
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
输出字符串                                                                                           
######################################################SESSION#######################################################
---------------------------------------------------------------------------------------------------------
Time            Event              FromAppName     ChannelID  OriChannelID SvrSessionID Terminal
---------------------------------------------------------------------------------------------------------
05/16:45:09:870 connect request    PID_2fb003c     0x00000000 0x00058000   0            172.17.0.1
05/16:45:14:460 connect success    PID_2fb003c     0x00000000 0x00058000   159          172.17.0.1
05/16:45:14:860 disconnect request PID_2fb003c     0x00000000 0x00058000   159          172.17.0.1
05/16:45:24:890 connect request    PID_2fb003c     0x00000002 0x00058000   0            172.17.0.1
05/16:45:25:590 connect success    PID_2fb003c     0x00000002 0x00058000   166          172.17.0.1
05/16:45:25:900 disconnect request PID_2fb003c     0x00000002 0x00058000   166          172.17.0.1
05/16:45:22:170 connect request    TempApi_        0x00000001 0x5f697041   0            172.17.0.1
05/16:45:22:880 connect success    TempApi_        0x00000001 0x5f697041   165          172.17.0.1
05/16:45:22:940 disconnect request TempApi_        0x00000001 0x5f697041   165          172.17.0.1
05/16:45:27:020 connect request    TempApi_        0x00000003 0x5f697041   0            172.17.0.1
05/16:45:27:740 connect success    TempApi_        0x00000003 0x5f697041   167          172.17.0.1
05/16:45:27:780 disconnect request TempApi_        0x00000003 0x5f697041   167          172.17.0.1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
########################################################RPC#########################################################
---------------------------------------------------------------------------------------------------------
Time            ChannelID  MsgID       Dir        Method  Operation
---------------------------------------------------------------------------------------------------------
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
05/16:45:22:900 0x00000001 1           NCC->NCS   POST    Uri=/SwmSirp/SwmVersionRegs/SwmVersionReg,BodyLen=139
05/16:45:22:940 0x00000001 1           NCS->NCC   POST    ok:
05/16:45:27:760 0x00000003 1           NCC->NCS   POST    Uri=/SwmSirp/SwmVersionRegs/SwmVersionReg,BodyLen=139
05/16:45:27:780 0x00000003 1           NCS->NCC   POST    ok:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
######################################################RPC QUERY#####################################################
---------------------------------------------------------------------------------------------------------
Time            ChannelID  MsgID       Dir        Method  Operation
---------------------------------------------------------------------------------------------------------
05/16:45:14:460 0x00000000 1           NCC->NCS   GET     Uri=/devm/SchNlsHeart,BodyLen=128
05/16:45:14:500 0x00000000 1           NCS->NCC   GET     data:devm:SchNlsHeart:Lsname:ugw:1525538715:0:
05/16:45:14:510 0x00000000 2           NCC->NCS   GET     Uri=/devm/SchCommMsg,BodyLen=352
05/16:45:14:520 0x00000000 2           NCS->NCC   GET     data:devm:SchCommMsg:lsName:ugw:9:96:0000000100000004ffffffff0000000300000004000000030000000400000004ffffffff0000000700
05/16:45:25:590 0x00000002 1           NCC->NCS   GET     Uri=/devm/SchNlsHeart,BodyLen=136
05/16:45:25:630 0x00000002 1           NCS->NCC   GET     data:devm:SchNlsHeart:Lsname:ugw:1525538715:1525538715:

(结果个数 = 3)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCCDIAGLOG.md`
