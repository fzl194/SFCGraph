---
id: UDG@20.15.2@MMLCommand@ADD APPPERFSTAT
type: MMLCommand
name: ADD APPPERFSTAT（增加应用性能统计）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: APPPERFSTAT
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 20
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 应用性能统计
status: active
---

# ADD APPPERFSTAT（增加应用性能统计）

## 功能

**适用NF：UPF、PGW-U**

该命令用于增加应用性能统计。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为20。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPNAME | 应用名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定应用名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| FILTERMODE | 过滤器模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤器模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOLGROUP：协议组级别。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERMODE”配置为“PROTOCOLGROUP”时为必选参数。<br>参数含义：该参数用来指定协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 仅支持绑定自定义协议组，不支持绑定默认协议组。<br>- 该取值必须和ADD PROTOCOLGROUP中配置的“ProtGroupName”参数取值相同。<br>- 输入单空格将删除该参数已有配置项。 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于设置优先级。优先级1-65535，越小优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型。<br>默认值：无<br>配置原则：不允许重复，以免同时匹配中多个。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APPPERFSTAT]] · 应用性能统计（APPPERFSTAT）

## 使用实例

假如需要创建应用性能统计，则命令如下：

```
ADD APPPERFSTAT: APPNAME="test", FILTERMODE=PROTOCOLGROUP, PROTGROUPNAME="test", PRIORITY=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加应用性能统计（ADD-APPPERFSTAT）_94871975.md`
