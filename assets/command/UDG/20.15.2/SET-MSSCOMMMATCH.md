---
id: UDG@20.15.2@MMLCommand@SET MSSCOMMMATCH
type: MMLCommand
name: SET MSSCOMMMATCH（设置通信模块规则匹配开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: MSSCOMMMATCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 通信管理统计查询
status: active
---

# SET MSSCOMMMATCH（设置通信模块规则匹配开关）

## 功能

![](设置通信模块规则匹配开关（SET MSSCOMMMATCH）_49961350.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置通信模块规则匹配开关，即诊断开关命令；通过开关打开规则匹配，协助问题定位。

当规则列表输入格式有误时，有错误信息“绑定的规则无效。”。

当输入的规则ID有不存在的，有错误信息“绑定的规则不存在。”。

当设置的服务类型和规则ID的类型不一致，有错误信息“绑定的规则类型有冲突。”。

## 注意事项

- 该命令执行后立即生效。
- 本命令用于使能通信过滤规则开关，使能后会降低性能且在用户指定的时间之后会自动去使能，关闭后会恢复性能。默认时间是300秒。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| ENABLE | 使能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：关闭。<br>- TRUE：打开。<br>默认值：无 |
| SERVICETYPE | 服务类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLE”配置为“FALSE”时为可选参数。<br>参数含义：该参数用于服务类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- packet：正常报文。<br>- packet-discard：丢弃报文。<br>- message：正常消息。<br>- message-discard：丢弃消息。<br>默认值：无 |
| SRCTHREADID | 源线程ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于源线程ID。如果不输入该参数，则表示匹配所有源线程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～127。<br>默认值：无 |
| DSTFBID | 目的功能块ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于目的功能块ID。如果不输入该参数，则表示匹配所有目的功能块。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| DSTINSTANCEID | 目的实例ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于目的实例ID。如果不输入该参数，则表示匹配所有目的实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| RULELIST | 规则列表 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于规则ID列表，支持绑定多个规则ID，输入格式为“1,2,3”，匹配时按照输入的顺序进行，如果当前规则匹配不成功，则会继续匹配下一个规则，如果当前规则匹配成功后，那么不会继续匹配下一个规则。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| TIME | 时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于表示开关持续的时间，超时后开关自动关闭，单位为秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～7200。<br>默认值：300 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MSSCOMMMATCH]] · 通信模块规则匹配开关（MSSCOMMMATCH）

## 使用实例

设置规则匹配开关：

```
SET MSSCOMMMATCH: ENABLE=TRUE,SERVICETYPE=packet-discard,SRCTHREADID=1,DSTFBID=0,DSTINSTANCEID=1,RULELIST="1",RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-MSSCOMMMATCH.md`
