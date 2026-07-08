---
id: UNC@20.15.2@License@LKV2M2MS02
type: License
name: eMTC终端省电PSM模式
nf: UNC
version: 20.15.2
license_code: LKV2M2MS02
control_item_id: '82207718'
applicable_nf:
- MME
status: active
---

# eMTC终端省电PSM模式

`LKV2M2MS02` · 控制项 82207718 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

随着物联网的发展，eMTC（enhanced Machine-Type Communications）广泛应用于智能抄表等领域。这些领域的eMTC终端被置于某些固定位置，采用各种电池供电，这种情况对电池寿命要求较高。本特性可以在这类eMTC终端无上行数传时，指示终端进入PSM（Power Saving Mode）。终端进入PSM后MME将拒绝周边网元对终端的寻呼请求，达到省电的目的，从而提高电池的使用寿命。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在智能抄表等eMTC领域普遍对终端电池寿命有较高的要求且对业务时延要求不高，运营商可通过部署本特性满足用户此需求，帮助行业用户节约运维成本，提升行业竞争力，从而提升自身的业务竞争力。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-216001 eMTC终端省电PSM模式

## 控制的能力

- [WSFD-216001](feature/UNC/20.15.2/WSFD-216001.md)  — 控制项 82207718

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
