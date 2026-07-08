---
id: UNC@20.15.2@MMLCommand@OPR NRFNFSWTNRF
type: MMLCommand
name: OPR NRFNFSWTNRF（操作指示NF切换NRF）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: NRFNFSWTNRF
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

# OPR NRFNFSWTNRF（操作指示NF切换NRF）

## 功能

![](操作指示NF切换NRF（OPR NRFNFSWTNRF）_89132374.assets/notice_3.0-zh-cn_2.png)

执行该命令后会导致该NF实例注册或心跳请求短时间接收504响应，请谨慎操作。

**适用NF：NRF**

该命令用于NRF双活场景下指示NF切换到另外容灾的NRF上注册。

执行完该命令后，NRF会对NF限定次数的心跳和全量更新请求进行正常处理后返回504，或从下一次收到NF心跳或全量更新请求后的1分钟内对心跳和全量更新请求进行正常处理后返回504。

此命令执行结果通过DSP NRFNFSWTNRF命令查询。

## 注意事项

- 该命令执行后立即生效。

- 执行该命令后，该功能会在一定时间段内生效，在NF下一周期心跳请求还未到达NRF期间，如果进程复位该命令将不会生效。
- 需要在NF当前接入的NRF（通过DSP REGNFINSTANCE命令查询）上执行该命令，否则命令无法生效。
- 该命令仅用于指示NF的切换，最终是否切换依赖NF的行为。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示待指示切换的NF实例标识。不输入代表所有从本NRF接入的NF都收到切换指示。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。<br>默认值：无<br>配置原则：无 |
| RSPTYPE | 响应类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF对NF的心跳和全量更新请求的响应方式。<br>数据来源：本端规划<br>取值范围：<br>- “DIRECT_504（直接回复504）”：NRF收到NF的心跳请求和全量更新后直接回复504（Gateway Time-out）响应。<br>- “TIMEOUT_504（超时回复504）”：NRF收到NF的心跳请求和全量更新后，超时回复504（Gateway Time-out）响应，其中超时时间可通过LST HTTPCONF的“服务端回复HTTP响应消息超时时间(s)”参数查看。<br>默认值：DIRECT_504<br>配置原则：无 |
| RSPNUM | 响应次数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF对NF的心跳和全量更新请求进行正常处理后返回504的限定次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是3~10。<br>默认值：4<br>配置原则：无 |

## 操作的配置对象

- [操作指示NF切换NRF（NRFNFSWTNRF）](configobject/UNC/20.15.2/NRFNFSWTNRF.md)

## 使用实例

执行NF实例标识为"123e4567-e89b-12d3-a456-426655440000"的NF切换NRF。

```
OPR NRFNFSWTNRF: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/操作指示NF切换NRF（OPR-NRFNFSWTNRF）_89132374.md`
