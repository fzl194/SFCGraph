---
id: UNC@20.15.2@ConfigObject@NRFFCPKGMIX
type: ConfigObject
name: NRFFCPKGMIX（NRF大小包协同返回功能参数）
nf: UNC
version: 20.15.2
object_name: NRFFCPKGMIX
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFFCPKGMIX（NRF大小包协同返回功能参数）

## 说明

**适用NF：NRF**

该命令用于设置NRF大小包协同返回功能参数。当NRF启动流控时，会根据此命令配置的参数，将服务发现返回结果的大包数量比例逐渐减少，小包数量比例逐渐增多，提高服务发现请求突增时的业务成功率。流控解除后，根据此命令配置的参数，逐渐恢复大包数量比例直到全部返回大包。

大包表示返回NF Profile全量报文，小包表示返回NF Profile精确匹配的报文。

## 操作本对象的命令

- [LST NRFFCPKGMIX](command/UNC/20.15.2/LST-NRFFCPKGMIX.md)
- [SET NRFFCPKGMIX](command/UNC/20.15.2/SET-NRFFCPKGMIX.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF大小包协同返回功能参数（LST-NRFFCPKGMIX）_96805489.md`
- 原始手册：`evidence/UNC/20.15.2/设置NRF大小包协同返回功能参数（SET-NRFFCPKGMIX）_96805507.md`
