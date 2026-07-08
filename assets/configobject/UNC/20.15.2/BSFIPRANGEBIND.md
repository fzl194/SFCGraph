---
id: UNC@20.15.2@ConfigObject@BSFIPRANGEBIND
type: ConfigObject
name: BSFIPRANGEBIND（BSF实例与IPRANGE之间的绑定关系）
nf: UNC
version: 20.15.2
object_name: BSFIPRANGEBIND
object_kind: binding
applicable_nf:
- SMF
status: active
---

# BSFIPRANGEBIND（BSF实例与IPRANGE之间的绑定关系）

## 说明

**适用NF：SMF**

该命令用于配置BSF（Binding Support Function）所管辖的IP地址范围。BSF用于保存UE的PDU Session和PCF的绑定关系。在BSF向NRF注册时，会将自己管辖的IP地址范围注册到NRF中。后续其他NF需要查询UE的IP地址和PCF的对应关系时，可向NRF查询UE归属的BSF信息，进而获取UE的PDU会话对应的PCF信息。

## 操作本对象的命令

- [ADD BSFIPRANGEBIND](command/UNC/20.15.2/ADD-BSFIPRANGEBIND.md)
- [LST BSFIPRANGEBIND](command/UNC/20.15.2/LST-BSFIPRANGEBIND.md)
- [RMV BSFIPRANGEBIND](command/UNC/20.15.2/RMV-BSFIPRANGEBIND.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BSF实例与IPRANGE之间的绑定关系（RMV-BSFIPRANGEBIND）_09652154.md`
- 原始手册：`evidence/UNC/20.15.2/增加BSF实例与IPRANGE之间的绑定关系（ADD-BSFIPRANGEBIND）_09653749.md`
- 原始手册：`evidence/UNC/20.15.2/查询BSF实例与IPRANGE之间的绑定关系（LST-BSFIPRANGEBIND）_09651737.md`
