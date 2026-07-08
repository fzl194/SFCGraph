---
id: UDG@20.15.2@ConfigObject@FCPARAM
type: ConfigObject
name: FCPARAM（流控参数）
nf: UDG
version: 20.15.2
object_name: FCPARAM
object_kind: entity
status: active
---

# FCPARAM（流控参数）

## 说明

该命令用于增加指定微服务实例的流控参数，本命令可以配置该微服务实例在流控过程中的最大令牌数、最小令牌数、权重生成方法、权重参数等。

> **说明**
> - 该命令执行后下次流控时生效。
>
> - 使用本命令会修改流控参数配置，配置错误可能导致流控效果达不到预期，需要联系华为技术支持来调整参数。
>
> - 最多可输入1000条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-FCPARAM]] · ADD FCPARAM
- [[command/UDG/20.15.2/LST-FCPARAM]] · LST FCPARAM
- [[command/UDG/20.15.2/MOD-FCPARAM]] · MOD FCPARAM
- [[command/UDG/20.15.2/RMV-FCPARAM]] · RMV FCPARAM

## 证据

- 原始手册：`evidence/UDG/20.15.2/FCPARAM.md`
- 原始手册：`evidence/UDG/20.15.2/FCPARAM.md`
- 原始手册：`evidence/UDG/20.15.2/FCPARAM.md`
- 原始手册：`evidence/UDG/20.15.2/FCPARAM.md`
