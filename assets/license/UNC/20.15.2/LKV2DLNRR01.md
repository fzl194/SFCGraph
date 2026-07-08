---
id: UNC@20.15.2@License@LKV2DLNRR01
type: License
name: NRF双活容灾
nf: UNC
version: 20.15.2
license_code: LKV2DLNRR01
control_item_id: 82200CAC
applicable_nf:
- NRF
status: active
---

# NRF双活容灾

`LKV2DLNRR01` · 控制项 82200CAC ·  · 域 

## 归属/适用NF（原文）

NRF

## 功能描述

NRF通过跨DC（Data Center）建立双活容灾组，两个NRF互相备份且都处于运行状态，实现容灾管理。当任意一个NRF故障时，对应NF将业务自动切换到另一个NRF上继续处理，保证业务的正常进行且数据不会丢失。NRF故障恢复后，可以继续提供业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

1～2000000 TPS

## 默认值

1

## 应用场景

当硬件故障/DC故障/局点遭遇地震海啸时导致高优先级NRF异常，或高优先级NRF与周边设备通信中断无法接入业务等情况下，低优先级NRF可以快速接替高优先级NRF，实现设备的异地容灾功能。<br>双活的NRF具有更高的可靠性（例如NRF间链路故障，某NF和其中一个NRF间链路也故障的情况下，此NF的后续业务请求仍然可以被正常处理）。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-114002 NRF双活容灾

## 控制的能力

- [WSFD-114002](feature/UNC/20.15.2/WSFD-114002.md)  — 控制项 82200CAC

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967909.md`
