---
id: UNC@20.15.2@ConfigObject@DYNAMICPOLICY
type: ConfigObject
name: DYNAMICPOLICY（服务类型分配动态权重的管理策略）
nf: UNC
version: 20.15.2
object_name: DYNAMICPOLICY
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# DYNAMICPOLICY（服务类型分配动态权重的管理策略）

## 说明

![](设置服务类型分配动态权重的管理策略（SET DYNAMICPOLICY）_24015952.assets/notice_3.0-zh-cn_2.png)

如果配置不合理会导致不同POD间负载不均衡。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置指定服务类型的动态权重调整的动态负载均衡参数。

## 操作本对象的命令

- [LST DYNAMICPOLICY](command/UNC/20.15.2/LST-DYNAMICPOLICY.md)
- [SET DYNAMICPOLICY](command/UNC/20.15.2/SET-DYNAMICPOLICY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务类型分配动态权重的管理策略（LST-DYNAMICPOLICY）_24015936.md`
- 原始手册：`evidence/UNC/20.15.2/设置服务类型分配动态权重的管理策略（SET-DYNAMICPOLICY）_24015952.md`
