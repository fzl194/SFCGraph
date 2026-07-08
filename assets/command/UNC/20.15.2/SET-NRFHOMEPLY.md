---
id: UNC@20.15.2@MMLCommand@SET NRFHOMEPLY
type: MMLCommand
name: SET NRFHOMEPLY（设置NRF归属地默认策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFHOMEPLY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# SET NRFHOMEPLY（设置NRF归属地默认策略）

## 功能

**适用NF：NRF**

此命令用于设置NRF作为归属地NRF时跨PLMN交互的默认策略。

## 注意事项

- 该命令执行后立即生效。

- 当NRF作为归属地NRF时，如果跨PLMN交互时，对于不同的拜访地PLMN需要定义不同的细分策略，请使用ADD NRFPLMNHOMEPLY配置对应的细分策略。
- 如果拜访地PLMN配置了细分策略，访问该拜访地PLMN时就以细分策略为准；如果拜访地PLMN没有进行细分策略的配置，访问该拜访地PLMN时就以本命令配置的默认策略为准。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| INTERSUBSW |
| --- |
| FUNC_ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERSUBSW | 是否支持跨PLMN订阅 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF作为归属地NRF时，是否处理其他拜访地PLMN的NF发起的对本PLMN的NF订阅以及订阅更新请求。开关为FUNC_ON表示处理，开关为FUNC_OFF表示不处理，并返回403错误码。订阅更新请求仅最终处理的NRF会按照此开关进行控制，中间层NRF仅做透传处理。<br>数据来源：全网规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFHOMEPLY查询当前参数配置值。<br>配置原则：无 |
| INFOHIDEPLY | 信息精简策略 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF作为归属地NRF时，对于收到跨PLMN服务发现和通知时，服务发现结果和订阅通知中精简的NF Profile的字段信息。<br>选择某一项表示该项被精简，不在消息中携带，不选择表示不精简。<br>数据来源：本端规划<br>取值范围：<br>- IP（IP）<br>- SERVINGSCOPE（servingScope）<br>- LOCALITY（locality）<br>- NFINFO（nfinfo）<br>- PORT（port）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFHOMEPLY查询当前参数配置值。<br>配置原则：<br>如果选择IP和PORT，NF Profile不携带ipv4Addresses、ipv6Addresses 、NFService中ipEndPoints。<br>如果选择IP，未选择PORT，NF Profile将不携带ipv4Addresses、ipv6Addresses，NFService会携带ipEndPoints，但不携带ipEndPoints中ipv4Addresses、ipv6Addresses。<br>如果未选择IP，则不能选择PORT。<br>如果选择locality，NF Profile不携带locality。<br>如果选择servingScope，NF Profile中不携带servingScope。<br>如果选择nfInfo，针对supi号段、gpsi号段、dnn列表、tai列表等这些量比较大的信元，则采取以下策略：<br>对于服务发现，只携带匹配上的信元信息，对于通知，只保留这些信元数组的第一个值。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFHOMEPLY]] · NRF归属地默认策略（NRFHOMEPLY）

## 使用实例

设置NRF归属地默认策略，支持跨PLMN订阅，信息精简策略选择IP。

```
SET NRFHOMEPLY: INTERSUBSW=FUNC_ON, INFOHIDEPLY=IP-1&SERVINGSCOPE-0&LOCALITY-0&NFINFO-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NRFHOMEPLY.md`
