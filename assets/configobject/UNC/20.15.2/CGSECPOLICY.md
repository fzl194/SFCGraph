---
id: UNC@20.15.2@ConfigObject@CGSECPOLICY
type: ConfigObject
name: CGSECPOLICY（安全策略）
nf: UNC
version: 20.15.2
object_name: CGSECPOLICY
object_kind: global_setting
applicable_nf:
- NCG
status: active
---

# CGSECPOLICY（安全策略）

## 说明

![](设置安全策略（SET CGSECPOLICY）_51174350.assets/notice_3.0-zh-cn_2.png)

当安全策略配置低于默认配置时，可能存在安全风险，请谨慎操作。配置RODD分发目录只读参数后，需要执行“RST VNFC”重启服务。

**适用NF：NCG**

该命令用于设置NCG对外开放的FTP/SFTP服务的安全策略。开放FTP/SFTP服务时，密码参数必须符合本命令设置的密码复杂度。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-CGSECPOLICY]] · LST CGSECPOLICY
- [[command/UNC/20.15.2/SET-CGSECPOLICY]] · SET CGSECPOLICY

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询安全策略（LST-CGSECPOLICY）_51174351.md`
- 原始手册：`evidence/UNC/20.15.2/设置安全策略（SET-CGSECPOLICY）_51174350.md`
