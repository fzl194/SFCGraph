---
id: UDG@20.15.2@ConfigObject@FLOWLETPARA
type: ConfigObject
name: FLOWLETPARA（大流优化参数）
nf: UDG
version: 20.15.2
object_name: FLOWLETPARA
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
- SGW-U
status: active
---

# FLOWLETPARA（大流优化参数）

## 说明

![](设置大流优化参数(SET FLOWLETPARA)_83137140.assets/notice_3.0-zh-cn.png)

修改该参数配置会影响数据转发性能和大流优化效果，请谨慎修改。

**适用NF：PGW-U、UPF、SGW-U**

该命令为配置类命令，用于配置大流优化参数。

> **说明**
> - 该命令执行后立即生效。
> - 最多可输入1条记录。
> - 执行该命令修改参数配置会影响数据转发性能和大流优化效果，请谨慎修改。
> - 该命令存在系统初始记录，参数的初始设置值如下表：
>   | FLOWOPTSW | THREADUPDINT | FLOWCHKPPS | FLOWGUARDPKTNUM | FLOWGUARDTIME | CPUOVERLOADTHR | CPUBIASDIFF |
>   | --- | --- | --- | --- | --- | --- | --- |
>   | DISABLE | 256 | 78000 | 64 | 10 | 80 | 15 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-FLOWLETPARA]] · LST FLOWLETPARA
- [[command/UDG/20.15.2/SET-FLOWLETPARA]] · SET FLOWLETPARA

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询大流优化参数(LST-FLOWLETPARA)_82901202.md`
- 原始手册：`evidence/UDG/20.15.2/设置大流优化参数(SET-FLOWLETPARA)_83137140.md`
