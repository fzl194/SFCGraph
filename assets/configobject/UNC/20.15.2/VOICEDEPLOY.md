---
id: UNC@20.15.2@ConfigObject@VOICEDEPLOY
type: ConfigObject
name: VOICEDEPLOY（语音部署配置）
nf: UNC
version: 20.15.2
object_name: VOICEDEPLOY
object_kind: entity
applicable_nf:
- MME
status: active
---

# VOICEDEPLOY（语音部署配置）

## 说明

**适用网元：MME**

该命令用于增加UE使用E-UTRAN网络接入时的IMS VoPS语音部署方案配置。UE使用E-UTRAN网络接入时可以选择两种语音部署方案：

- IMS VoPS（IMS Voice over PS session），即基于IMS网络提供语音业务。PS网络上部署专门的IMS APNNI，用于承载IMS业务相关的信令和数据。
- CSFB（Circuit Switched Fallback），利用现有的GSM /UMTS网络实现语音通话的一种语音解决方案。用户进行语音业务时，由EPS（Evolved Packet System）网络指示用户回落到目标GSM/UMTS电路域（CS）网络之后，再发起语音呼叫。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-VOICEDEPLOY]] · ADD VOICEDEPLOY
- [[command/UNC/20.15.2/LST-VOICEDEPLOY]] · LST VOICEDEPLOY
- [[command/UNC/20.15.2/MOD-VOICEDEPLOY]] · MOD VOICEDEPLOY
- [[command/UNC/20.15.2/RMV-VOICEDEPLOY]] · RMV VOICEDEPLOY

## 证据

- 原始手册：`evidence/UNC/20.15.2/VOICEDEPLOY.md`
- 原始手册：`evidence/UNC/20.15.2/VOICEDEPLOY.md`
- 原始手册：`evidence/UNC/20.15.2/VOICEDEPLOY.md`
- 原始手册：`evidence/UNC/20.15.2/VOICEDEPLOY.md`
