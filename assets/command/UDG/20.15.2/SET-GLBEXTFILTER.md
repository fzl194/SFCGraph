---
id: UDG@20.15.2@MMLCommand@SET GLBEXTFILTER
type: MMLCommand
name: SET GLBEXTFILTER（配置全局扩展过滤器绑定关系）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBEXTFILTER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 流过滤器管理
- 全局扩展过滤器绑定
status: active
---

# SET GLBEXTFILTER（配置全局扩展过滤器绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置全局扩展过滤器绑定关系，即绑定重定向动作过滤条件，只有符合扩展过滤器的条件，才能执行重定向动作。重定向动作包括URL重定向（使用ADD REDIRECT或MOD REDIRECT配置）和CaptivePortal智能重定向动作（在ADD RULE或MOD RULE配置时指定Policy Type为SMARTREDIRECT，Policy Name为CaptivePortal业务对应的IPFarm的名称）。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 执行该命令前，必须通过ADD EXTENDEDFILTER命令配置扩展过滤器。
- 最多支持3个AND类型的扩展过滤器。
- 过滤条件分为AND组、OR组和NOT组。如果要对业务流执行对应的动作，需满足下述条件：匹配AND组中所有条件成功或者匹配OR组中任意一个，并且匹配NOT组都失败。如果没有配置，默认为所有业务资源访问按照重定向规则执行重定向动作。
- 扩展过滤器类型初始值取值为NULL表示对应的过滤器所属的分组无效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | EXTFLTTYPE1 | EXTFLTTYPE2 | EXTFLTTYPE3 | EXTFLTTYPE4 | EXTFLTTYPE5 |
| --- | --- | --- | --- | --- | --- |
| 初始值 | NULL | NULL | NULL | NULL | NULL |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTFLTNAME1 | 扩展过滤器名字1 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器名字1。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD EXTENDEDFILTER命令配置生成。 |
| EXTFLTTYPE1 | 扩展过滤器类型1 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器类型1。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AND：对应的过滤器所属的分组为AND组。<br>- OR：对应的过滤器所属的分组为OR组。<br>- NOT：对应的过滤器所属的分组为NOT组。<br>默认值：无<br>配置原则：<br>- 需要全部匹配的过滤器分为AND组。<br>- 需要部分匹配的过滤器分为OR组。<br>- 不能匹配的过滤器分为NOT组。 |
| EXTFLTNAME2 | 扩展过滤器名字2 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器名字2。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD EXTENDEDFILTER命令配置生成。 |
| EXTFLTTYPE2 | 扩展过滤器类型2 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器类型2。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AND：对应的过滤器所属的分组为AND组。<br>- OR：对应的过滤器所属的分组为OR组。<br>- NOT：对应的过滤器所属的分组为NOT组。<br>默认值：无<br>配置原则：<br>- 需要全部匹配的过滤器分为AND组。<br>- 需要部分匹配的过滤器分为OR组。<br>- 不能匹配的过滤器分为NOT组。 |
| EXTFLTNAME3 | 扩展过滤器名字3 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器名字3。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD EXTENDEDFILTER命令配置生成。 |
| EXTFLTTYPE3 | 扩展过滤器类型3 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器类型3。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AND：对应的过滤器所属的分组为AND组。<br>- OR：对应的过滤器所属的分组为OR组。<br>- NOT：对应的过滤器所属的分组为NOT组。<br>默认值：无<br>配置原则：<br>- 需要全部匹配的过滤器分为AND组。<br>- 需要部分匹配的过滤器分为OR组。<br>- 不能匹配的过滤器分为NOT组。 |
| EXTFLTNAME4 | 扩展过滤器名字4 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器名字4。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD EXTENDEDFILTER命令配置生成。 |
| EXTFLTTYPE4 | 扩展过滤器类型4 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器类型4。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AND：对应的过滤器所属的分组为AND组。<br>- OR：对应的过滤器所属的分组为OR组。<br>- NOT：对应的过滤器所属的分组为NOT组。<br>默认值：无<br>配置原则：<br>- 需要全部匹配的过滤器分为AND组。<br>- 需要部分匹配的过滤器分为OR组。<br>- 不能匹配的过滤器分为NOT组。 |
| EXTFLTNAME5 | 扩展过滤器名字5 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器名字5。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD EXTENDEDFILTER命令配置生成。 |
| EXTFLTTYPE5 | 扩展过滤器类型5 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器类型5。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AND：对应的过滤器所属的分组为AND组。<br>- OR：对应的过滤器所属的分组为OR组。<br>- NOT：对应的过滤器所属的分组为NOT组。<br>默认值：无<br>配置原则：<br>- 需要全部匹配的过滤器分为AND组。<br>- 需要部分匹配的过滤器分为OR组。<br>- 不能匹配的过滤器分为NOT组。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBEXTFILTER]] · 全局扩展过滤器绑定配置（GLBEXTFILTER）

## 使用实例

配置全局扩展过滤器绑定关系，设置AND类型的扩展过滤器ExtFilter1、NOT类型的扩展过滤器ExtFilter2，使用此命令：

```
SET GLBEXTFILTER:EXTFLTNAME1="ExtFilter1",EXTFLTTYPE1=AND,EXTFLTNAME2="ExtFilter2",EXTFLTTYPE2=NOT;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-GLBEXTFILTER.md`
