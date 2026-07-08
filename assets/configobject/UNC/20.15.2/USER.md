---
id: UNC@20.15.2@ConfigObject@USER
type: ConfigObject
name: USER（用户锁定状态）
nf: UNC
version: 20.15.2
object_name: USER
object_kind: entity
applicable_nf:
- NCG
status: active
---

# USER（用户锁定状态）

## 说明

本命令用于创建OM Portal的操作用户。该用户可以通过OM Portal页面登录系统。

- 账号策略：对于账号的一些特定要求，可以通过OM Portal的“ 安全 > 安全策略 ”查询。
- 密码策略：对于密码的一些特定要求，可以通过OM Portal的“ 安全 > 安全策略 ”查询。
- 默认用户：系统缺省已配置的用户，可以通过OM Portal的“ 安全 > 用户管理 ”查询。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-USER]] · ADD USER
- [[command/UNC/20.15.2/DSP-USER]] · DSP USER
- [[command/UNC/20.15.2/MOD-USER]] · MOD USER
- [[command/UNC/20.15.2/RMV-USER]] · RMV USER
- [[command/UNC/20.15.2/ULK-USER]] · ULK USER

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示用户锁定状态（DSP-USER）_51174353.md`
- 原始手册：`evidence/UNC/20.15.2/解锁用户（ULK-USER）_51174354.md`
- 原始手册：`evidence/UNC/20.15.2/修改用户操作权限(MOD-USER)_06404642.md`
- 原始手册：`evidence/UNC/20.15.2/删除用户(RMV-USER)_06404641.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户(ADD-USER)_06404640.md`
