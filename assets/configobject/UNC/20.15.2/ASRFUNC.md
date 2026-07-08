---
id: UNC@20.15.2@ConfigObject@ASRFUNC
type: ConfigObject
name: ASRFUNC（容灾功能参数）
nf: UNC
version: 20.15.2
object_name: ASRFUNC
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# ASRFUNC（容灾功能参数）

## 说明

![](设置容灾功能参数(SET ASRFUNC)_72345725.assets/notice_3.0-zh-cn_2.png)

该命令修改将启用或者关闭主备容灾功能，必须按照部署指导书中的步骤执行。

**适用网元：SGSN、MME**

该命令用于启用或者关闭网元的主备容灾功能。

现网 UNC 无法组POOL时，运营商可以选择两套 UNC 进行容灾，开启主备容灾功能。

两套 UNC 网元通过主备协商，确定运行主和运行备。主网元和备网元都配置相同的业务IP地址，主网元发布高优先级路由，备网元发布低优先级路由，控制业务只接入到主网元。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-ASRFUNC]] · LST ASRFUNC
- [[command/UNC/20.15.2/SET-ASRFUNC]] · SET ASRFUNC

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询容灾功能参数(LST-ASRFUNC)_26146126.md`
- 原始手册：`evidence/UNC/20.15.2/设置容灾功能参数(SET-ASRFUNC)_72345725.md`
