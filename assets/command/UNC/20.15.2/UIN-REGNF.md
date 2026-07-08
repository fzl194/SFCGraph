---
id: UNC@20.15.2@MMLCommand@UIN REGNF
type: MMLCommand
name: UIN REGNF（解禁NF实例）
nf: UNC
version: 20.15.2
verb: UIN
object_keyword: REGNF
command_category: 调测类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF实例管理
status: active
---

# UIN REGNF（解禁NF实例）

## 功能

![](解禁NF实例（UIN REGNF）_09652663.assets/notice_3.0-zh-cn_2.png)

执行该命令后，可以解除NF实例的隔离状态，NRF将继续处理该NF实例的消息。

**适用NF：NRF**

该命令用于解禁止NF实例。当需要解除NF实例的隔离状态时使用。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示NRF上指定SUSPENDED状态的NF实例标识。可以通过DSP REGNFINSTANCE命令查询NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：<br>可以通过DSP REGNFINSTANCE命令查询NF实例标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/REGNF]] · 禁止NF实例（REGNF）

## 使用实例

被禁止的NF设备故障恢复正常，NF实例标识为123e4567-e89b-12d3-a456-426655440000，运营商希望继续使用此NF实例，对其进行解除隔离时配置如下：

```
UIN REGNF:NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/解禁NF实例（UIN-REGNF）_09652663.md`
