---
id: UDG@20.15.2@MMLCommand@RTR FABRICOAMSTAT
type: MMLCommand
name: RTR FABRICOAMSTAT（清除OAM统计信息）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: FABRICOAMSTAT
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- Fabric
status: active
---

# RTR FABRICOAMSTAT（清除OAM统计信息）

## 功能

该命令用来清除Fabric OAM历史报文统计结果。

为了便于观察计数信息，通过清零Fabric OAM收发报文的数目以及收发速率，从而方便故障诊断。

## 注意事项

1. 该命令执行后立即生效。
2. 执行本命令后，清除的信息不可恢复。在执行本命令前请务必仔细确认是否要执行本命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| REMOTERETB | 远端TB | 可选必选说明：可选参数<br>参数含义：该参数用于指定远端节点的资源ID。<br>数据来源：本端规划<br>取值范围：整数类型，0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FABRICOAMSTAT]] · OAM统计信息（FABRICOAMSTAT）

## 使用实例

- 清除微服务类型为“aa”微服务实例为“bb”到所有远端资源的Fabric OAM历史报文统计结果：
  ```
  RTR FABRICOAMSTAT:CELLTYPE="aa", CELLINSTANCE="bb";
  ```
- 清除微服务类型为“aa”微服务实例为“bb”到远端资源1034的Fabric OAM历史报文统计结果：
  ```
  RTR FABRICOAMSTAT:CELLTYPE="aa", CELLINSTANCE="bb",REMOTERETB=1034;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除OAM统计信息（RTR-FABRICOAMSTAT）_92520029.md`
