---
id: UNC@20.15.2@MMLCommand@ADD NGPAGINGARPPRI
type: MMLCommand
name: ADD NGPAGINGARPPRI（增加基于ARP的Paging消息在流控期间放通的优先级）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGPAGINGARPPRI
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2接口消息流控优先级管理
- 基于ARP的Paging消息流控优先级管理
status: active
---

# ADD NGPAGINGARPPRI（增加基于ARP的Paging消息在流控期间放通的优先级）

## 功能

**适用NF：AMF**

该命令用于配置基于ARP识别Paging消息在N2口固定速率流控期间放通的优先级。配置高优先级对应的Paging消息优先被放通，配置低优先级对应的Paging消息优先被流控。

## 注意事项

- 该命令执行后立即生效。

- 当用户不配置NGPAGINGARPPRI时，则默认为低优先级。
- 该命令只能配置基于APR识别Paging消息在流控期间放通的优先级，不保证一定不被流控。
- Paging消息流控期间的放通优先顺序从高到低是NGPAGINGARPPRI，NGPAGINGDNNPRI。只有高优先级命令没有配置时，才会根据低优先级命令的配置识别DDN消息优先级。如果这两条命令都没有配置，所有的DDN消息都被识别为低优先级消息。

- 最多可输入15条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ARP | ARP数值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Paging消息在流控期间放通的优先级。<br>数据来源：本端规划<br>取值范围：<br>- “PAGING_LOW（低）”：表示流控阶段放通概率低<br>- “PAGING_HIGH（高）”：表示流控阶段放通概率高<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGPAGINGARPPRI]] · 基于ARP的Paging消息在流控期间放通的优先级（NGPAGINGARPPRI）

## 使用实例

设置ARP为1的Paging消息在流控期间放通的优先级为高，执行如下命令：

```
ADD NGPAGINGARPPRI: ARP=1, PRIORITY=PAGING_HIGH;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NGPAGINGARPPRI.md`
