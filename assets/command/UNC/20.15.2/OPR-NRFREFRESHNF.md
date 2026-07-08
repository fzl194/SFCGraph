---
id: UNC@20.15.2@MMLCommand@OPR NRFREFRESHNF
type: MMLCommand
name: OPR NRFREFRESHNF（操作执行网元信息刷新）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: NRFREFRESHNF
command_category: 动作类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息刷新
status: active
---

# OPR NRFREFRESHNF（操作执行网元信息刷新）

## 功能

**适用NF：NRF**

该命令用于对NF的心跳请求强制返回404响应，指示NF到NRF上进行全量更新，达到刷NF信息的目的。执行完该命令后NRF会对NF下一周期的心跳请求返回404，NF收到404响应后是否进行全量更新取决于NF的实现。此命令执行结果通过DSP NRFREFRESHNF查询。

## 注意事项

- 该命令执行后立即生效。

- 执行该命令后，该功能会在NF的下一个心跳请求到达后生效，在NF下一周期心跳请求还未到达NRF期间，如果进程复位该命令将不会生效。
- 主备NRF容灾场景，需要在主NRF上执行该命令，如果在备NRF上执行该命令无法生效。
- 双活NRF容灾场景，需要在NF当前接入的NRF上执行该命令，否则命令无法生效。NF当前接入的NRF可以通过DSP REGNFINSTANCE命令查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示待指示刷新的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFREFRESHNF]] · 操作执行网元信息刷新（NRFREFRESHNF）

## 使用实例

执行NF实例标识为"123e4567-e89b-12d3-a456-426655440000"的网元信息刷新。

```
OPR NRFREFRESHNF:NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/OPR-NRFREFRESHNF.md`
