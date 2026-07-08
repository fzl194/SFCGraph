---
id: UDG@20.15.2@ConfigObject@SBILNKCTRLSW
type: ConfigObject
name: SBILNKCTRLSW（服务化接口链路自动控制功能开关）
nf: UDG
version: 20.15.2
object_name: SBILNKCTRLSW
object_kind: global_setting
status: active
---

# SBILNKCTRLSW（服务化接口链路自动控制功能开关）

## 说明

![](设置服务化接口链路自动控制功能开关（SET SBILNKCTRLSW）_28971851.assets/notice_3.0-zh-cn.png)

如果设置服务化接口链路自动控制功能，可能导致链路数量变化，触发拆链或者新建链路。链路数变多可能会超过对端链路规格限制，导致建链失败；链路数变少可能会导致单链路负载增高，存在单链路过载风险，而且可能会导致对端负载不均衡。

该命令用于设置服务化接口链路自动控制功能。当用户配置功能打开时，按系统默认的复杂链路控制原则建立HTTP链路；当用户配置功能关闭时，按系统默认的简单链路控制原则建立HTTP链路。

> **说明**
> - 该命令执行后立即生效。
>
> - 该功能从打开到关闭，会导致现网整体链路数量发送变化，可能影响对端服务端的负载均衡情况，不建议频繁打开关闭操作。
> - 该功能打开以后，比对的比特位需要基于各个运营商对UUID中NODE部分的不同定义确定，目前基于大部分运营商的自定义规则设置默认值。
> - 该功能仅建议部分局点开启使用，默认关闭局点需要打开需要联系华为技术支持。
> - 该功能打开后系统中默认的复杂链路控制功能打开，如果对具体的NF或某一类的NF存在特殊的链路控制策略，则可通过命令[**ADD SBILINKCFG**](../服务化接口链路属性管理/增加SBI接口链路属性配置（ADD SBILINKCFG）_83813628.md)进行配置，且该命令配置的链路控制策略优先级高于系统默认的链路控制策略。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | LNKCTRLSW | CMPSTARTBIT | CMPENDBIT |
> | --- | --- | --- |
> | OFF | 9 | 24 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SBILNKCTRLSW]] · LST SBILNKCTRLSW
- [[command/UDG/20.15.2/SET-SBILNKCTRLSW]] · SET SBILNKCTRLSW

## 证据

- 原始手册：`evidence/UDG/20.15.2/SBILNKCTRLSW.md`
- 原始手册：`evidence/UDG/20.15.2/SBILNKCTRLSW.md`
