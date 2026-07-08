---
id: UNC@20.15.2@ConfigObject@STCNFPROFILE
type: ConfigObject
name: STCNFPROFILE（手动注册的NFProfile）
nf: UNC
version: 20.15.2
object_name: STCNFPROFILE
object_kind: action
applicable_nf:
- NRF
status: active
---

# STCNFPROFILE（手动注册的NFProfile）

## 说明

**适用NF：NRF**

该命令用于去注册手动上线的NF。

该命令执行完成后，该NF将不能继续在网络中提供服务，但该NF的Profile文件还在NRF中，如果需要重新在网络中提供服务，直接执行手动注册命令即可。

## 操作本对象的命令

- [ACT STCNFPROFILE](command/UNC/20.15.2/ACT-STCNFPROFILE.md)
- [DEACT STCNFPROFILE](command/UNC/20.15.2/DEACT-STCNFPROFILE.md)
- [LST STCNFPROFILE](command/UNC/20.15.2/LST-STCNFPROFILE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/去激活手动注册的NFProfile（DEACT-STCNFPROFILE）_44006686.md`
- 原始手册：`evidence/UNC/20.15.2/查询手动注册的NFProfile（LST-STCNFPROFILE）_44007244.md`
- 原始手册：`evidence/UNC/20.15.2/激活手动注册NFProfile（ACT-STCNFPROFILE）_44006304.md`
