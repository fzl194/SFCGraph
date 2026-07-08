---
id: UNC@20.15.2@MMLCommand@DSP NCCPEERLIST
type: MMLCommand
name: DSP NCCPEERLIST（显示NETCONFC管理的远端设备的信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCCPEERLIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议客户端
status: active
---

# DSP NCCPEERLIST（显示NETCONFC管理的远端设备的信息）

## 功能

该命令用于显示NETCONFC管理的远端设备的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERID | 远端ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示远端设备ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PID | 组件PID | 可选必选说明：可选参数<br>参数含义：该参数用于表示NETCONFC的组件PID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0～0xFFFFFFFF。<br>默认值：无 |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示远端设备信息的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PEER：远端设备信息。<br>默认值：PEER |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCCPEERLIST]] · NETCONFC管理的远端设备的信息（NCCPEERLIST）

## 使用实例

显示NETCONFC管理的远端设备的信息：

```
DSP NCCPEERLIST:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
输出字符串
    
----------------------------------------------------------------------------------------------------
Peer ID             : 10000
InstanceId          : cslbip-x86-pod-0__103__1
ServiceName         : 110
Peer Status         : READY
Driver Name         : schema
User Name           : 
Dest IP             : 192.168.0.1
HostDnsName         : 
ProtocolPort        : 21051
VrfIndex            : 0
AuthType            : PUBKEY/PASSWORD
ProtocolSessNum     : 1
PeerDir             : home:/
IsAutoConnect       : TRUE
SessionCapability   : NTF
PeerProtocolPid     : 0x2d70014
FtpProtocolPid      : 0x920015
PID                 : 0x1970016/0x81970033
ProxyPolicy         : 0x0
ProtocolType        : RESTCONF
PeerTypeId          : 1
TransProtocol       : HTTPS
ToBeAged            : 0
-----------------------------------------------------------------------------------------------------

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NETCONFC管理的远端设备的信息（DSP-NCCPEERLIST）_59103577.md`
