---
id: UNC@20.15.2@ConfigObject@NRFBSFDNNREL
type: ConfigObject
name: NRFBSFDNNREL（BSF索引和DNN的关联关系）
nf: UNC
version: 20.15.2
object_name: NRFBSFDNNREL
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFBSFDNNREL（BSF索引和DNN的关联关系）

## 说明

**适用NF：NRF**

该命令用于新增BSF索引和DNN的关联关系。

该命令的使用场景为跨NRF对BSF进行寻址，基于特定DNN选择BSF的路由信息，其中BSF的路由需要通过ADD NRFBSFINDEXRT提前配置。

如果针对同一个BSFDNN配置了多个不同的BSF索引，那么当前NRF会选取符合条件的所有BSF索引对应NRF组中优先级最高的NRF。

此命令受到SET NRFFUNCSW命令中DNNNIMATCHSW开关控制。发现消息中DNN携带网络标识（NI）和操作标识符(OI)进行路由转发，当开关打开时，NRF优先精确匹配DNN的路由，如果未匹配到，再精确匹配DNN只包含NI的路由。当开关关闭时，NRF只能精确匹配DNN的路由。

## 操作本对象的命令

- [ADD NRFBSFDNNREL](command/UNC/20.15.2/ADD-NRFBSFDNNREL.md)
- [LST NRFBSFDNNREL](command/UNC/20.15.2/LST-NRFBSFDNNREL.md)
- [RMV NRFBSFDNNREL](command/UNC/20.15.2/RMV-NRFBSFDNNREL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BSF索引和DNN的关联关系（RMV-NRFBSFDNNREL）_45612435.md`
- 原始手册：`evidence/UNC/20.15.2/增加BSF索引和DNN的关联关系（ADD-NRFBSFDNNREL）_45612407.md`
- 原始手册：`evidence/UNC/20.15.2/查询BSF索引和DNN的关联关系（LST-NRFBSFDNNREL）_45612431.md`
