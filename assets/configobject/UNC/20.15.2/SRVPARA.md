---
id: UNC@20.15.2@ConfigObject@SRVPARA
type: ConfigObject
name: SRVPARA（业务参数配置）
nf: UNC
version: 20.15.2
object_name: SRVPARA
object_kind: entity
applicable_nf:
- NCG
status: active
---

# SRVPARA（业务参数配置）

## 说明

![](修改业务参数配置（MOD SRVPARA）_51174334.assets/notice_3.0-zh-cn_2.png)

如果业务参数类型选择PASSIVE模式参数，此操作会重启FTP服务，导致计费中心客户端会中断1~2秒。

**适用NF：NCG**

用于修改NCG相关参数。

执行命令之前，可执行 [**LST SRVPARA**](查询业务参数配置（LST SRVPARA）_51174335.md) 命令查询当前配置的参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SRVPARA]] · LST SRVPARA
- [[command/UNC/20.15.2/MOD-SRVPARA]] · MOD SRVPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/SRVPARA.md`
- 原始手册：`evidence/UNC/20.15.2/SRVPARA.md`
