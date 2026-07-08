---
id: UNC@20.15.2@ConfigObject@LAIVLR
type: ConfigObject
name: LAIVLR（LAI与VLR号对应关系）
nf: UNC
version: 20.15.2
object_name: LAIVLR
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# LAIVLR（LAI与VLR号对应关系）

## 说明

**适用网元：SGSN、MME**

该命令用于增加LAI与MSC/VLR的对应关系。 UNC 将根据本命令配置的LAI和MSC/VLR对应关系，为UE选择提供服务的MSC/VLR。具体规则如下：

不组Pool场景下， UNC 直接根据LAI和MSC/VLR对应关系为UE选择提供服务的MSC/VLR，此种场景下不考虑链路状态。

组Pool场景下， UNC 首先根据 [**ADD LAIVLR**](增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md) 里LAI和MSC/VLR的映射关系，结合 [**ADD VLR**](../VLR管理/增加VLR配置信息(ADD VLR)_26305254.md) 命令配置的 “VLR号” 和 “MSC POOL名称” 映射关系选择到MSC POOL，然后再根据用户IMSI V值与MSC/VLR的对应关系在Pool内选择一个链路状态正常的MSC/VLR为UE提供服务（IMSI V值与MSC/VLR的对应关系通过 [**ADD VLR**](../VLR管理/增加VLR配置信息(ADD VLR)_26305254.md) 命令进行配置）。MSC POOL的作用是负荷分担和容灾的，因此MSC POOL内的各个MSC管辖的LAI范围是一样的，此步骤只需要配置MSC Pool中任意一个MSC/VLR与LAI的对应关系即可。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LAIVLR]] · ADD LAIVLR
- [[command/UNC/20.15.2/LST-LAIVLR]] · LST LAIVLR
- [[command/UNC/20.15.2/RMV-LAIVLR]] · RMV LAIVLR

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除LAI与VLR号对应关系(RMV-LAIVLR)_26145414.md`
- 原始手册：`evidence/UNC/20.15.2/增加LAI与VLR号对应关系(ADD-LAIVLR)_72345015.md`
- 原始手册：`evidence/UNC/20.15.2/查询LAI与VLR号对应关系(LST-LAIVLR)_72225095.md`
