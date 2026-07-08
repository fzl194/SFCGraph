---
id: UNC@20.15.2@ConfigObject@TOKENALLOCWT
type: ConfigObject
name: TOKENALLOCWT（服务类型分配权重的管理策略）
nf: UNC
version: 20.15.2
object_name: TOKENALLOCWT
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
status: active
---

# TOKENALLOCWT（服务类型分配权重的管理策略）

## 说明

![](设置服务类型分配权重的管理策略（SET TOKENALLOCWT）_23736568.assets/notice_3.0-zh-cn_2.png)

该命令会调整不同Pod间的会话资源，调整过程中会导致容器短暂的内存升高和少量呼损。忙时操作会造成内存持续过载甚至流控，务必谨慎使用。配置该命令时，请联系华为技术支持。

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于设置服务类型的负载均衡方式。

## 操作本对象的命令

- [LST TOKENALLOCWT](command/UNC/20.15.2/LST-TOKENALLOCWT.md)
- [SET TOKENALLOCWT](command/UNC/20.15.2/SET-TOKENALLOCWT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务类型分配权重的管理策略（LST-TOKENALLOCWT）_24015940.md`
- 原始手册：`evidence/UNC/20.15.2/设置服务类型分配权重的管理策略（SET-TOKENALLOCWT）_23736568.md`
