---
id: UNC@20.15.2@ConfigObject@GTPCWHITELIST
type: ConfigObject
name: GTPCWHITELIST（GTP-C路径白名单）
nf: UNC
version: 20.15.2
object_name: GTPCWHITELIST
object_kind: entity
applicable_nf:
- MME
status: active
---

# GTPCWHITELIST（GTP-C路径白名单）

## 说明

**适用网元：MME**

本命令用于增加GTP-C路径白名单，用于控制GTP-C路径的本端IP地址选择。

应用场景：Sv接口与SGs接口共用信令网络，但信令网络只提供平行路径的互通，不支持交叉路径的互通。比如，MSC提供IP地址MSC_IP_1、MSC_IP_2， UNC 提供IP地址USN_IP_A、USN_IP_B，平行路径指{MSC_IP_1，USN_IP_A}，{MSC_IP_2，USN_IP_B}，交叉路径指{MSC_IP_1，USN_IP_B}，{MSC_IP_2，USN_IP_A}。

Sv接口为GTP协议的接口，要求组网上DNS解析的IP地址全互联。为了解决这种矛盾，本命令提供Sv接口互通路径的配置。如果对端IP地址落入本命令的配置记录中， UNC 只能选择GTP-C路径白名单中指定的本端IP地址；如果对端IP地址不在本命令的配置记录中， UNC 在Sv接口的本端IP地址中进行轮选。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GTPCWHITELIST]] · ADD GTPCWHITELIST
- [[command/UNC/20.15.2/LST-GTPCWHITELIST]] · LST GTPCWHITELIST
- [[command/UNC/20.15.2/MOD-GTPCWHITELIST]] · MOD GTPCWHITELIST
- [[command/UNC/20.15.2/RMV-GTPCWHITELIST]] · RMV GTPCWHITELIST

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GTP-C路径白名单(MOD-GTPCWHITELIST)_72225597.md`
- 原始手册：`evidence/UNC/20.15.2/删除GTP-C路径白名单(RMV-GTPCWHITELIST)_26145918.md`
- 原始手册：`evidence/UNC/20.15.2/增加GTP-C路径白名单(ADD-GTPCWHITELIST)_72345517.md`
- 原始手册：`evidence/UNC/20.15.2/查询GTP-C路径白名单(LST-GTPCWHITELIST)_26305728.md`
