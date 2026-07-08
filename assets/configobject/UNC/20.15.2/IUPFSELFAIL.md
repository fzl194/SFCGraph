---
id: UNC@20.15.2@ConfigObject@IUPFSELFAIL
type: ConfigObject
name: IUPFSELFAIL（I-UPF选择失败处理方式）
nf: UNC
version: 20.15.2
object_name: IUPFSELFAIL
object_kind: global_setting
applicable_nf:
- SMF
status: active
---

# IUPFSELFAIL（I-UPF选择失败处理方式）

## 说明

**适用NF：SMF**

该命令用于配置当SMF/I-SMF在Service Request流程中选择I-UPF失败时的处理方式。如果处理方式为保留会话，则SMF/I-SMF保持该会话，并通知AMF拒绝该PDU会话的用户面连接建立请求；如果处理方式为释放会话，则SMF/I-SMF，先通知AMF拒绝该PDU会话的用户面建立请求，然后发送Namf_Communication_N1N2MessageTransfer Req消息并内置NAS删除消息（即PDU Session Release Command消息）来释放UE会话。其中，NAS删除消息中携带的释放原因值，通过本配置命令中的RELCAUSE字段来指定。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-IUPFSELFAIL]] · LST IUPFSELFAIL
- [[command/UNC/20.15.2/SET-IUPFSELFAIL]] · SET IUPFSELFAIL

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询I-UPF选择失败处理方式（LST-IUPFSELFAIL）_13960446.md`
- 原始手册：`evidence/UNC/20.15.2/设置I-UPF选择失败处理方式（SET-IUPFSELFAIL）_59000295.md`
