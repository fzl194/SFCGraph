---
id: UNC@20.15.2@ConfigObject@NGSMARTPARA
type: ConfigObject
name: NGSMARTPARA（5G信令抑制参数）
nf: UNC
version: 20.15.2
object_name: NGSMARTPARA
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# NGSMARTPARA（5G信令抑制参数）

## 说明

![](设置5G信令抑制参数（SET NGSMARTPARA）_25121211.assets/notice_3.0-zh-cn_2.png)

执行该命令，如果阈值、下发原因值等配置设置不合理可能影响用户接入。

**适用NF：AMF**

当用户的初始注册请求，注册失败，服务请求，PDU会话建立请求，4G到5G重选请求或4G到5G切换请求次数达到设定的阈值后，为了保护网络资源，AMF支持根据配置的抑制措施对用户的请求信令进行抑制。当抑制的时间达到一定时长后，系统会解除抑制，即允许用户重新接入。该命令用于设置注册请求、注册失败、服务请求、PDU会话建立请求、4G到5G重选请求和4G到5G切换请求的异常抑制参数，包括异常识别门限、异常抑制的时长、抑制措施、Parking DNN等。

## 操作本对象的命令

- [LST NGSMARTPARA](command/UNC/20.15.2/LST-NGSMARTPARA.md)
- [SET NGSMARTPARA](command/UNC/20.15.2/SET-NGSMARTPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G信令抑制参数（LST-NGSMARTPARA）_25120889.md`
- 原始手册：`evidence/UNC/20.15.2/设置5G信令抑制参数（SET-NGSMARTPARA）_25121211.md`
