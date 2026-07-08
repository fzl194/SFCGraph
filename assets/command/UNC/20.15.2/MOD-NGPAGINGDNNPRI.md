---
id: UNC@20.15.2@MMLCommand@MOD NGPAGINGDNNPRI
type: MMLCommand
name: MOD NGPAGINGDNNPRI（修改基于DNN的Paging消息在流控期间放通的优先级）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGPAGINGDNNPRI
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
- 基于DNN的Paging消息流控优先级管理
status: active
---

# MOD NGPAGINGDNNPRI（修改基于DNN的Paging消息在流控期间放通的优先级）

## 功能

**适用NF：AMF**

该命令用于修改基于DNN识别Paging消息在N2口固定速率流控期间放通的优先级。配置高优先级对应的Paging消息优先被放通，配置低优先级对应的Paging消息优先被流控。

## 注意事项

- 该命令执行后立即生效。

- 该命令只能配置基于DNN识别Paging消息在流控期间放通的优先级，不保证一定不被流控。
- 配置的DNN需为系统中已配置的DNN。
- Paging消息流控优先顺序从高到低是NGPAGINGARPPRI，NGPAGINGDNNPRI。只有高优先级命令没有配置时，才会根据低优先级命令的配置识别DDN消息优先级。如果这两条命令都没有配置，所有的DDN消息都被识别为低优先级消息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Paging消息在流控期间放通的优先级。<br>数据来源：本端规划<br>取值范围：<br>- “PAGING_LOW（低）”：表示流控阶段放通概率低<br>- “PAGING_HIGH（高）”：表示流控阶段放通概率高<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPAGINGDNNPRI]] · 基于DNN的Paging消息在流控期间放通的优先级（NGPAGINGDNNPRI）

## 使用实例

修改DNN为"IMS"的Paging消息在流控期间放通的优先级为高优先级，执行如下命令：

```
MOD NGPAGINGDNNPRI: DNN="IMS", PRIORITY=PAGING_HIGH;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于DNN的Paging消息在流控期间放通的优先级（MOD-NGPAGINGDNNPRI）_98467637.md`
