---
id: UNC@20.15.2@License@LKV2NFACV01
type: License
name: 支持NF属性检查与校验
nf: UNC
version: 20.15.2
license_code: LKV2NFACV01
control_item_id: '81203513'
applicable_nf:
- NRF
status: active
---

# 支持NF属性检查与校验

`LKV2NFACV01` · 控制项 81203513 ·  · 域 

## 归属/适用NF（原文）

NRF

## 功能描述

为了避免NF的异常操作影响到NRF设备安全及5G Core业务，NRF支持对NF进行白名单和校验控制：符合NRF白名单的NF才允许注册/更新；NF进行上述服务化流程时，对应参数校验通过的NF才能完成对应的服务化流程。<br>为了避免号段类NF的号段配置错误影响到5G Core业务，NRF支持对NF Profile的属性冲突核验，对于存在号段冲突的情况可以查询或提示告警。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

NF进行基本的服务化流程包含NF注册/更新/订阅通知/发现流程时，可以使用本特性进行相应的参数检查或属性冲突核查，避免误操作或者误配置导致5G Core业务受损。

## 相关控制项（原文，未解释为边）

1

## 对应特性（原文）

WSFD-214101 支持NF属性检查与校验

## 控制的能力

- [WSFD-214101](feature/UNC/20.15.2/WSFD-214101.md)  — 控制项 81203513

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15408078.md`
