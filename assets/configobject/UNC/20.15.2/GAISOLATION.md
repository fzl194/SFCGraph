---
id: UNC@20.15.2@ConfigObject@GAISOLATION
type: ConfigObject
name: GAISOLATION（Ga业务隔离配置）
nf: UNC
version: 20.15.2
object_name: GAISOLATION
object_kind: entity
applicable_nf:
- NCG
status: active
---

# GAISOLATION（Ga业务隔离配置）

## 说明

![](增加Ga业务隔离配置（ADD GAISOLATION）_63762720.assets/notice_3.0-zh-cn_2.png)

此命令不能动态生效，需要执行RST RU生效。隔离正常运行中的AP模块，需要先执行STP CDRRECEIVE命令停止话单接收。添加隔离配置会导致隔离AP停止接收话单并禁止链路迁入。

**适用NF：NCG**

该命令用于隔离AP模块上的234G话单业务，即禁止Ga接口的接收话单，使得被隔离的AP不生成234G话单文件，并且禁止隔离AP上Ga链路的新建或迁入。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GAISOLATION]] · ADD GAISOLATION
- [[command/UNC/20.15.2/LST-GAISOLATION]] · LST GAISOLATION
- [[command/UNC/20.15.2/RMV-GAISOLATION]] · RMV GAISOLATION

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Ga业务隔离配置（RMV-GAISOLATION）_99921349.md`
- 原始手册：`evidence/UNC/20.15.2/增加Ga业务隔离配置（ADD-GAISOLATION）_63762720.md`
- 原始手册：`evidence/UNC/20.15.2/查询Ga业务隔离配置（LST-GAISOLATION）_99762889.md`
