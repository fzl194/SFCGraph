---
id: UNC@20.15.2@MMLCommand@SET NSSFFCPARA
type: MMLCommand
name: SET NSSFFCPARA（设置流控等级对应的流控参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NSSFFCPARA
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF流控管理
status: active
---

# SET NSSFFCPARA（设置流控等级对应的流控参数）

## 功能

**适用NF：NSSF**

该命令用于设置流控等级对应的流控参数。

当NSSF需要设置不同流控级别对应的流控响应时，可配置此命令。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FCLEVEL | FCRSP |
| --- | --- |
| LOW | TooManyRequest_429 |
| MEDIUM | ServiceUnavailable_503 |
| HIGH | ServiceUnavailable_503 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCLEVEL | 流控等级 | 可选必选说明：必选参数<br>参数含义：该参数用于表示CPU过载程度的分级。<br>数据来源：本端规划<br>取值范围：<br>- “LOW（轻度过载）”：轻度过载对应的CPU阈值范围为大于等于75%、小于80%。<br>- “MEDIUM（中度过载）”：中度过载对应的CPU阈值范围为大于等于80%、小于85%。<br>- “HIGH（重度过载）”：重度过载对应的CPU阈值范围为大于等于85%、小于100%。<br>默认值：无。<br>配置原则：无 |
| FCRSP | 流控响应 | 可选必选说明：必选参数<br>参数含义：该参数表示NSSF对流控等级的响应。<br>数据来源：本端规划<br>取值范围：<br>- “TooManyRequest_429（请求过多）”：NSSF收到NF的服务发现请求后直接回复响应，错误码为429。<br>- “ServiceUnavailable_503（服务不可用）”：NSSF收到NF的服务发现请求后直接回复响应，错误码为503。<br>- “NoResponse（无响应）”：NSSF收到NF的服务发现请求后直接将消息丢弃。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFFCPARA]] · 流控等级对应的流控参数（NSSFFCPARA）

## 使用实例

当运营商希望NSSF的流控等级为轻度过载，流控响应为请求次数过多时，执行此命令：

```
SET NSSFFCPARA: FCLEVEL=LOW, FCRSP=TooManyRequest_429;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置流控等级对应的流控参数（SET-NSSFFCPARA）_44007993.md`
