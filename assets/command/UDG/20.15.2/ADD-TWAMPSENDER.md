---
id: UDG@20.15.2@MMLCommand@ADD TWAMPSENDER
type: MMLCommand
name: ADD TWAMPSENDER（增加TWAMP发送端）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TWAMPSENDER
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TWAMP发送端配置
status: active
---

# ADD TWAMPSENDER（增加TWAMP发送端）

## 功能

该命令用于增加TWAMP发送端。

> **说明**
> - 该命令执行后立即生效。
>
> - 最多可输入12000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTID | 客户端ID | 可选必选说明：必选参数<br>参数含义：该参数用于配置客户端ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~12000。<br>默认值：无<br>配置原则：<br>CLIENTID必须在<br>[**ADD TWAMPCLIENT**](../TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>已经配置，可以用<br>[**LST TWAMPCLIENT**](../TWAMP客户端配置/查询TWAMP客户端（LST TWAMPCLIENT）_27262286.md)<br>查询。 |
| MODE | 会话发送类型 | 可选必选说明：可选参数<br>参数含义：该参数用于会话发送类型。<br>数据来源：全网规划<br>取值范围：<br>- CONTINUAL（连续统计）<br>默认值：CONTINUAL<br>配置原则：无 |
| DSCP | 差分服务码 | 可选必选说明：可选参数<br>参数含义：该参数用于配置差分服务码。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：0<br>配置原则：无 |
| PKTSIZETYPE | 报文类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置报文类型。<br>数据来源：全网规划<br>取值范围：<br>- FIXED（固定报文长度）<br>- RANDOM（报文随机填充）<br>默认值：FIXED<br>配置原则：无 |
| PKTSIZE | 报文长度 | 可选必选说明：该参数在"PKTSIZETYPE"配置为"FIXED"时为条件可选参数。<br>参数含义：该参数用于配置报文长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是69~1500，单位是字节。该参数取值范围上限不能超过外联口配置的MTU值。<br>默认值：128<br>配置原则：无 |
| PADDINGTYPE | 报文填充类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置报文填充类型。<br>数据来源：全网规划<br>取值范围：<br>- PADDING_ZERO（报文全零填充）<br>- PADDING_RANDOM（报文随机填充）<br>默认值：PADDING_RANDOM<br>配置原则：无 |
| PERIOD | 报文发送周期 | 可选必选说明：可选参数<br>参数含义：该参数用于配置报文发送周期。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~100。单位：10毫秒。<br>默认值：100<br>配置原则：无 |
| TIMEOUT | 超时时间 | 可选必选说明：可选参数<br>参数含义：该参数用于配置超时时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~10，单位是秒。<br>默认值：5<br>配置原则：无 |

## 操作的配置对象

- [TWAMP发送端（TWAMPSENDER）](configobject/UDG/20.15.2/TWAMPSENDER.md)

## 关联任务

- [0-00228](task/UDG/20.15.2/0-00228.md)

## 使用实例

增加客户端ID为1的发送端实例：

```
ADD TWAMPSENDER: CLIENTID=1, MODE=CONTINUAL, DSCP=0, PKTSIZETYPE=FIXED, PKTSIZE=128, PADDINGTYPE=PADDING_RANDOM, PERIOD=100, TIMEOUT=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加TWAMP发送端（ADD-TWAMPSENDER）_73302045.md`
