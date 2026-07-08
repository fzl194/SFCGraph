---
id: UNC@20.15.2@ConfigObject@REGNF
type: ConfigObject
name: REGNF（禁止NF实例）
nf: UNC
version: 20.15.2
object_name: REGNF
object_kind: action
applicable_nf:
- NRF
status: active
---

# REGNF（禁止NF实例）

## 说明

![](禁止NF实例（INH REGNF）_09651532.assets/notice_3.0-zh-cn_2.png)

执行此命令后该NF实例会被设置为SUSPENDED状态，在服务发现响应中以SUSPENDED状态返回，该NF实例可能不会被NF选择。

**适用NF：NRF**

该命令用于在NRF上禁止NF实例，将其设置为SUSPENDED状态。当运营商需要对单个NF实例进行隔离时则使用该命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/INH-REGNF]] · INH REGNF
- [[command/UNC/20.15.2/UIN-REGNF]] · UIN REGNF

## 证据

- 原始手册：`evidence/UNC/20.15.2/禁止NF实例（INH-REGNF）_09651532.md`
- 原始手册：`evidence/UNC/20.15.2/解禁NF实例（UIN-REGNF）_09652663.md`
