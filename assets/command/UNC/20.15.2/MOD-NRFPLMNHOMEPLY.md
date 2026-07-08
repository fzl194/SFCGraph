---
id: UNC@20.15.2@MMLCommand@MOD NRFPLMNHOMEPLY
type: MMLCommand
name: MOD NRFPLMNHOMEPLY（修改指定拜访地PLMN的归属地策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NRFPLMNHOMEPLY
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

# MOD NRFPLMNHOMEPLY（修改指定拜访地PLMN的归属地策略）

## 功能

**适用NF：NRF**

该命令用于修改NRF作为归属地NRF时对指定拜访地PLMN的跨PLMN请求处理策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示拜访地PLMN的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示拜访地PLMN的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| INTERSUBSW | 是否支持跨PLMN订阅 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF作为归属地NRF时，是否处理指定的拜访地PLMN的NF发起的对本PLMN内的NF订阅以及订阅更新请求。开关为FUNC_ON表示处理，开关为FUNC_OFF表示不处理，并返回403错误码。订阅更新请求仅最终处理的NRF会按照此开关进行控制，中间层NRF仅做透传处理。<br>数据来源：全网规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无<br>配置原则：无 |
| INFOHIDEPLY | 信息精简策略 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF作为归属地NRF时，对于收到指定的拜访地PLMN的跨PLMN服务发现和通知中精简的NF Profile字段信息。<br>选择某一项表示该项被精简，不在消息中携带，不选择表示不精简。<br>数据来源：本端规划<br>取值范围：<br>- IP（IP）<br>- SERVINGSCOPE（servingScope）<br>- LOCALITY（locality）<br>- NFINFO（nfinfo）<br>- PORT（port）<br>默认值：无<br>配置原则：<br>如果选择IP和PORT，NF Profile不携带ipv4Addresses、ipv6Addresses 、NFService中ipEndPoints。<br>如果选择IP，未选择PORT，NF Profile将不携带ipv4Addresses、ipv6Addresses，NFService会携带ipEndPoints，但不携带ipEndPoints中ipv4Addresses、ipv6Addresses。<br>如果未选择IP，则不能选择PORT。<br>如果选择locality，NF Profile不携带locality。<br>如果选择servingScope，NF Profile中不携带servingScope。<br>如果选择nfInfo，针对supi号段、gpsi号段、dnn列表、tai列表等这些量比较大的信元，则采取以下策略：<br>对于服务发现，只携带匹配上的信元信息，对于通知，只保留这些信元数组的第一个值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFPLMNHOMEPLY]] · 指定拜访地PLMN的归属地策略（NRFPLMNHOMEPLY）

## 使用实例

修改移动国家码为460，移动网号为03的指定拜访地PLMN的归属地策略，关闭信息精简策略。

```
MOD NRFPLMNHOMEPLY: MCC="460", MNC="03", INTERSUBSW=FUNC_OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改指定拜访地PLMN的归属地策略（MOD-NRFPLMNHOMEPLY）_24956642.md`
