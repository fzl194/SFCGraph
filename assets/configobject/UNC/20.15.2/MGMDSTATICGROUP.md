---
id: UNC@20.15.2@ConfigObject@MGMDSTATICGROUP
type: ConfigObject
name: MGMDSTATICGROUP（IGMP静态组配置）
nf: UNC
version: 20.15.2
object_name: MGMDSTATICGROUP
object_kind: entity
status: active
---

# MGMDSTATICGROUP（IGMP静态组配置）

## 说明

该命令用来创建IGMP静态组配置。

当用户需要长期稳定的接收某组播组数据，即用户网段上存在稳定的组播组成员时，可以通过配置接口静态加入组播组实现快速响应用户请求，减少用户的频道切换时间。

## 操作本对象的命令

- [ADD MGMDSTATICGROUP](command/UNC/20.15.2/ADD-MGMDSTATICGROUP.md)
- [DSP MGMDSTATICGROUP](command/UNC/20.15.2/DSP-MGMDSTATICGROUP.md)
- [LST MGMDSTATICGROUP](command/UNC/20.15.2/LST-MGMDSTATICGROUP.md)
- [MOD MGMDSTATICGROUP](command/UNC/20.15.2/MOD-MGMDSTATICGROUP.md)
- [RMV MGMDSTATICGROUP](command/UNC/20.15.2/RMV-MGMDSTATICGROUP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IGMP静态组配置（MOD-MGMDSTATICGROUP）_50121294.md`
- 原始手册：`evidence/UNC/20.15.2/删除IGMP静态组配置（RMV-MGMDSTATICGROUP）_50280782.md`
- 原始手册：`evidence/UNC/20.15.2/显示IGMP静态加入信息（DSP-MGMDSTATICGROUP）_00601369.md`
- 原始手册：`evidence/UNC/20.15.2/查询IGMP静态组配置（LST-MGMDSTATICGROUP）_49961718.md`
- 原始手册：`evidence/UNC/20.15.2/添加IGMP静态组配置（ADD-MGMDSTATICGROUP）_00601281.md`
