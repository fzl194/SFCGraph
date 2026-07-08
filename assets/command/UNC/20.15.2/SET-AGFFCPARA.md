---
id: UNC@20.15.2@MMLCommand@SET AGFFCPARA
type: MMLCommand
name: SET AGFFCPARA（设置流控等级对应的流控参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AGFFCPARA
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- AGF流控参数信息
status: active
---

# SET AGFFCPARA（设置流控等级对应的流控参数）

## 功能

**适用NF：NCG**

该命令用于设置流控等级对应的流控参数。

## 注意事项

- 该命令执行后立即生效。

- 当NCG需要设置不同流控级别对应的流控响应时，可配置此命令。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FCLEVEL | FCRSP |
| --- | --- |
| LOW | NoResponse |
| MEDIUM | NoResponse |
| HIGH | NoResponse |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCLEVEL | 流控等级 | 可选必选说明：必选参数<br>参数含义：该参数用于表示CPU过载程度的分级。<br>数据来源：本端规划<br>取值范围：<br>- “LOW（轻度过载）”：根据LOW选择FCL<br>- “MEDIUM（中度过载）”：根据MEDIUM选择FCL<br>- “HIGH（重度过载）”：根据HIGH选择FCL<br>默认值：无。<br>配置原则：<br>LOW（轻度过载）：轻度过载对应的CPU阈值范围为大于等于75%、小于80%。<br>MEDIUM（中度过载）：中度过载对应的CPU阈值范围为大于等于80%、小于85%。<br>HIGH（重度过载）：重度过载对应的CPU阈值范围为大于等于85%、小于100%。 |
| FCRSP | 流控响应 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NCG对CTF的计费请求如何响应。<br>数据来源：本端规划<br>取值范围：<br>- “TooManyRequest_429（请求过多）”：根据TooManyRequest_429选择FCRSP<br>- “ServiceUnavailable_503（服务不可用）”：根据ServiceUnavailable_503选择FCRSP<br>- “NoResponse（无响应）”：根据NoResponse选择FCRSP<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AGFFCPARA查询当前参数配置值。<br>配置原则：<br>TooManyRequest_429（请求过多）：NCG收到CTF的服务发现请求后直接回复响应，错误码为429。<br>ServiceUnavailable_503（服务不可用）：NCG收到CTF的服务发现请求后直接回复响应，错误码为503。<br>NoResponse（无响应）：NCG收到CTF的服务发现请求后直接将消息丢弃。 |

## 操作的配置对象

- [流控等级对应的流控参数（AGFFCPARA）](configobject/UNC/20.15.2/AGFFCPARA.md)

## 使用实例

设置流控等级为LOW的流控响应参数为NoResponse：

```
SET AGFFCPARA: FCLEVEL=LOW, FCRSP=NoResponse;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置流控等级对应的流控参数（SET-AGFFCPARA）_45110934.md`
