---
id: UNC@20.15.2@MMLCommand@SET VLRSGSSELFFC
type: MMLCommand
name: SET VLRSGSSELFFC（设置VLR的SGs接口自保流控参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: VLRSGSSELFFC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 自保流控
status: active
---

# SET VLRSGSSELFFC（设置VLR的SGs接口自保流控参数）

## 功能

**适用NF：SMSF**

该命令用于设置VLR的SGs接口自保流控参数。

## 注意事项

- 该命令执行后立即生效。

- 双活组网的场景下，如果需要配置此命令，则两个VLR上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FCSWITCH | LOCUPFCRSP | MOFCRSP |
| --- | --- | --- |
| ON | CongestionReject | UeTemporarilyUnreachable |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VLR SGs接口消息流控开关状态。<br>数据来源：本端规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无。<br>配置原则：无 |
| LOCUPFCRSP | 位置更新流控响应 | 可选必选说明：该参数在"FCSWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于表示系统过载时在位置更新流程中，VLR收到SGs接口的SGsAP-LOCATION-UPDATE-REQUEST消息的响应原因值。<br>数据来源：本端规划<br>取值范围：<br>- “NoRsp（丢弃）”：VLR收到SGs接口的位置更新请求后直接将消息丢弃。<br>- “CongestionReject（拥塞拒绝）”：VLR收到SGS接口的位置更新请求后直接向对端回复SGsAP SGsAP-LOCATION-UPDATE-REJECT消息，拒绝原因值为22。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRSGSSELFFC查询当前参数配置值。<br>配置原则：无 |
| MOFCRSP | MO流控响应 | 可选必选说明：该参数在"FCSWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于表示系统过载时在MO短消息流程中，VLR收到SGs接口的SGsAP-UPLINK-UNITDATA消息的响应原因值。<br>数据来源：本端规划<br>取值范围：<br>- “NoRsp（丢弃）”：VLR收到SGs接口的MO请求后直接将消息丢弃。<br>- “UeTemporarilyUnreachable（临时不可达）”：VLR收到SGS接口SGsAP-UPLINK-UNITDATA消息后直接向对端回复SGsAP-RELEASE-REQUEST，SGs cause为14。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRSGSSELFFC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRSGSSELFFC]] · VLR的SGs接口自保流控参数（VLRSGSSELFFC）

## 使用实例

运营商希望设置“VLR SGs接口消息流控开关”为“开启”，“位置更新流控响应”为“拒绝拥塞”，“MO流控响应”为“临时不可达”，执行如下命令：

```
SET VLRSGSSELFFC: FCSWITCH=ON, LOCUPFCRSP=CongestionReject, MOFCRSP=UeTemporarilyUnreachable;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-VLRSGSSELFFC.md`
