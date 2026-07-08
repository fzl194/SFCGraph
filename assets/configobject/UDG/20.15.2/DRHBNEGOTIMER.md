---
id: UDG@20.15.2@ConfigObject@DRHBNEGOTIMER
type: ConfigObject
name: DRHBNEGOTIMER（容灾定时器）
nf: UDG
version: 20.15.2
object_name: DRHBNEGOTIMER
object_kind: global_setting
status: active
---

# DRHBNEGOTIMER（容灾定时器）

## 说明

该命令用于配置容灾组中网元间发送心跳、协商消息的间隔时间及次数。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。
> - 在容灾运行期间执行命令，需要参考容灾配置指导书，避免主备容灾协商失败。
> - 在容灾组中的两个网元中配置容灾定时器时，参数应保持一致。
> - 在冷备容灾模式下，心跳超时时间的最小时间建议设置为6s。
> - 使用[**LST DRHBNEGOTIMER**](查询容灾定时器（LST DRHBNEGOTIMER）_23235162.md)查询容灾定时器时，只有当前容灾组的容灾定时器会被显示。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DRGROUPID | HELLOINTERVAL | NEGOINTERVAL | TIMES | OMHBTIMES | OMHBINTERVAL |
> | --- | --- | --- | --- | --- | --- |
> | 1 | 10 | 10 | 30 | 3 | 10 |
> | 2 | 10 | 10 | 30 | 3 | 10 |
> | 3 | 10 | 10 | 30 | 3 | 10 |
> | 4 | 10 | 10 | 30 | 3 | 10 |
> | 5 | 10 | 10 | 30 | 3 | 10 |
> | 6 | 10 | 10 | 30 | 3 | 10 |
> | 7 | 10 | 10 | 30 | 3 | 10 |
> | 8 | 10 | 10 | 30 | 3 | 10 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DRHBNEGOTIMER]] · LST DRHBNEGOTIMER
- [[command/UDG/20.15.2/SET-DRHBNEGOTIMER]] · SET DRHBNEGOTIMER

## 证据

- 原始手册：`evidence/UDG/20.15.2/DRHBNEGOTIMER.md`
- 原始手册：`evidence/UDG/20.15.2/DRHBNEGOTIMER.md`
