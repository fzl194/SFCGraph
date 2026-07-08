---
id: UNC@20.15.2@ConfigObject@VSMFDFTQOSCTRL
type: ConfigObject
name: VSMFDFTQOSCTRL（VSMF的Default QoS Flow配置）
nf: UNC
version: 20.15.2
object_name: VSMFDFTQOSCTRL
object_kind: entity
applicable_nf:
- SMF
status: active
---

# VSMFDFTQOSCTRL（VSMF的Default QoS Flow配置）

## 说明

**适用NF：SMF**

该命令用来增加V-SMF的Default QoS Flow配置。在V-SMF插入或改变流程中，V-SMF会将本地配置的Default QoS Flow参数，通过信元VplmnQoS发送给H-SMF，H-SMF再将VplmnQoS透传给PCF。PCF收到VplmnQos携带的QoS参数之后，经过跟本地签约的QoS参数协商之后，正式下发Default QoS Flow的Qos参数给H-SMF，H-SMF再下发给V-SMF。V-SMF收到H-SMF返回的QoS参数之后，跟本地配置的Default Qos参数进行比较，如果H-SMF传递的QoS参数超出预置范围（如5QI不在允许列表、Session-AMBR超出最大值等），V-SMF按QoS协商失败处理，拒绝V-SMF插入或改变流程。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-VSMFDFTQOSCTRL]] · ADD VSMFDFTQOSCTRL
- [[command/UNC/20.15.2/LST-VSMFDFTQOSCTRL]] · LST VSMFDFTQOSCTRL
- [[command/UNC/20.15.2/MOD-VSMFDFTQOSCTRL]] · MOD VSMFDFTQOSCTRL
- [[command/UNC/20.15.2/RMV-VSMFDFTQOSCTRL]] · RMV VSMFDFTQOSCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/VSMFDFTQOSCTRL.md`
- 原始手册：`evidence/UNC/20.15.2/VSMFDFTQOSCTRL.md`
- 原始手册：`evidence/UNC/20.15.2/VSMFDFTQOSCTRL.md`
- 原始手册：`evidence/UNC/20.15.2/VSMFDFTQOSCTRL.md`
