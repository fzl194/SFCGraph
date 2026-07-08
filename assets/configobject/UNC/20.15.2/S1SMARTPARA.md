---
id: UNC@20.15.2@ConfigObject@S1SMARTPARA
type: ConfigObject
name: S1SMARTPARA（S1模式信令抑制参数）
nf: UNC
version: 20.15.2
object_name: S1SMARTPARA
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# S1SMARTPARA（S1模式信令抑制参数）

## 说明

**适用网元：MME**

该命令用于设置S1模式附着、服务请求、PDN连接建立流程异常抑制参数，包括异常识别门限、异常抑制的时长、Parking APN。当用户的附着请求，服务请求或PDN连接请求达到设定的阈值后，系统根据 [**ADD S1SMARTRULE**](../S1模式信令抑制规则管理/增加S1模式信令抑制规则(ADD S1SMARTRULE)_26145746.md) 配置的抑制措施进行抑制。当抑制的时间达到抑制时长后，系统会解除抑制，允许用户重新接入业务。

## 操作本对象的命令

- [LST S1SMARTPARA](command/UNC/20.15.2/LST-S1SMARTPARA.md)
- [SET S1SMARTPARA](command/UNC/20.15.2/SET-S1SMARTPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1模式信令抑制参数(LST-S1SMARTPARA)_26305558.md`
- 原始手册：`evidence/UNC/20.15.2/设置S1模式信令抑制参数(SET-S1SMARTPARA)_72225427.md`
