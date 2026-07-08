---
id: UNC@20.15.2@ConfigObject@UPFRDSSVR
type: ConfigObject
name: UPFRDSSVR（中转UPF与Radius服务器的绑定关系）
nf: UNC
version: 20.15.2
object_name: UPFRDSSVR
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# UPFRDSSVR（中转UPF与Radius服务器的绑定关系）

## 说明

![](增加中转UPF与Radius服务器的绑定关系（ADD UPFRDSSVR）_35636449.assets/notice_3.0-zh-cn_2.png)

新增中转UPF与RADIUS服务器的绑定关系，若中转UPF绑定的RADIUS Server IP与直连的RADIUS Server IP相同会造成直连RADIUS场景业务受损等问题。

**适用NF：PGW-C、SMF**

该命令用来新增中转UPF与Radius服务器的绑定关系。当SMF与Radius服务器不能直连时，采用通过UPF与Radius服务器连接的方式进行鉴权或者计费。

## 操作本对象的命令

- [ADD UPFRDSSVR](command/UNC/20.15.2/ADD-UPFRDSSVR.md)
- [LST UPFRDSSVR](command/UNC/20.15.2/LST-UPFRDSSVR.md)
- [RMV UPFRDSSVR](command/UNC/20.15.2/RMV-UPFRDSSVR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除中转UPF与Radius服务器的绑定关系（RMV-UPFRDSSVR）_35273631.md`
- 原始手册：`evidence/UNC/20.15.2/增加中转UPF与Radius服务器的绑定关系（ADD-UPFRDSSVR）_35636449.md`
- 原始手册：`evidence/UNC/20.15.2/查询中转UPF与Radius服务器的绑定关系（LST-UPFRDSSVR）_88248952.md`
