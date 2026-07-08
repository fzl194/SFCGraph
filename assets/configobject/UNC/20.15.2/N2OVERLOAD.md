---
id: UNC@20.15.2@ConfigObject@N2OVERLOAD
type: ConfigObject
name: N2OVERLOAD（N2过载控制信息）
nf: UNC
version: 20.15.2
object_name: N2OVERLOAD
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# N2OVERLOAD（N2过载控制信息）

## 说明

![](设置N2过载控制信息（SET N2OVERLOAD）_09654395.assets/notice_3.0-zh-cn_2.png)

如果(R)AN仅与一个AMF互联，那么当该(R)AN从AMF收到OVERLOAD START消息后，将会拒绝UE的RRC连接建立请求，从而影响UE的正常业务。

**适用NF：AMF**

此命令用于设置N2接口过载控制信息。当AMF过载时向gNodeB发送OVERLOAD START（3GPP TS 38.413），指示gNodeB是否允许接受UE的RRC连接，以减轻对网络的信令冲击；当AMF从过载状态恢复到正常状态后向gNodeB发送OVERLOAD STOP消息，指示gNodeB允许UE接入。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-N2OVERLOAD]] · LST N2OVERLOAD
- [[command/UNC/20.15.2/SET-N2OVERLOAD]] · SET N2OVERLOAD

## 证据

- 原始手册：`evidence/UNC/20.15.2/N2OVERLOAD.md`
- 原始手册：`evidence/UNC/20.15.2/N2OVERLOAD.md`
