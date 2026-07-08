---
id: UDG@20.15.2@ConfigObject@SESSLBCAPABILITY
type: ConfigObject
name: SESSLBCAPABILITY（会话均衡基线能力值）
nf: UDG
version: 20.15.2
object_name: SESSLBCAPABILITY
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# SESSLBCAPABILITY（会话均衡基线能力值）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](添加会话均衡基线能力值（ADD SESSLBCAPABILITY）_15006393.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果参数设置不合理，会导致业务板负荷不均、转发不通、用户激活失败等。

在异构硬件场景下，使用该命令用于配置CPU的基线能力。

## 操作本对象的命令

- [ADD SESSLBCAPABILITY](command/UDG/20.15.2/ADD-SESSLBCAPABILITY.md)
- [LST SESSLBCAPABILITY](command/UDG/20.15.2/LST-SESSLBCAPABILITY.md)
- [MOD SESSLBCAPABILITY](command/UDG/20.15.2/MOD-SESSLBCAPABILITY.md)
- [RMV SESSLBCAPABILITY](command/UDG/20.15.2/RMV-SESSLBCAPABILITY.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改会话均衡基线能力值（MOD-SESSLBCAPABILITY）_14794635.md`
- 原始手册：`evidence/UDG/20.15.2/删除会话均衡基线能力值（RMV-SESSLBCAPABILITY）_27399646.md`
- 原始手册：`evidence/UDG/20.15.2/查询会话均衡基线能力值（LST-SESSLBCAPABILITY）_27633936.md`
- 原始手册：`evidence/UDG/20.15.2/添加会话均衡基线能力值（ADD-SESSLBCAPABILITY）_15006393.md`
