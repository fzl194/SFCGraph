---
id: UDG@20.15.2@MMLCommand@ADD FWPOLICY
type: MMLCommand
name: ADD FWPOLICY（增加防火墙策略）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: FWPOLICY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 200
category_path:
- 用户面服务管理
- 业务控制策略
- 防火墙策略控制
- 防火墙策略配置
status: active
---

# ADD FWPOLICY（增加防火墙策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置防火墙策略。防火墙策略用于控制上下行发起业务流的上下行报文处理策略，处理方式包括通过和丢弃两种。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为200。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FWPOLICYNAME | 防火墙策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定防火墙策略的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPINITUPACTION | 上行发起业务流上行门控动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定上行发起业务流上行门控动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：表示业务报文直接通过。<br>- DISCARD：表示业务报文直接丢弃。<br>默认值：PASS<br>配置原则：无 |
| UPINITDNACTION | 上行发起业务流下行门控动作 | 可选必选说明：可选参数<br>参数含义：该参数用户指定上行发起业务流下行门控动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：表示业务报文直接通过。<br>- DISCARD：表示业务报文直接丢弃。<br>默认值：PASS<br>配置原则：无 |
| DNINITUPACTION | 下行发起业务流上行门控动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下行发起业务流上行门控动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：表示业务报文直接通过。<br>- DISCARD：表示业务报文直接丢弃。<br>默认值：PASS<br>配置原则：无 |
| DNINITDNACTION | 下行发起业务流下行门控动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下行发起业务流下行门控动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：表示业务报文直接通过。<br>- DISCARD：表示业务报文直接丢弃。<br>默认值：PASS<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FWPOLICY]] · 防火墙策略（FWPOLICY）

## 使用实例

当运营商需要增加一条防火墙策略，策略要求是：上行发起业务流的上行报文通过，上行发起业务流的下行报文通过，下行发起业务流的上行报文丢弃，下行发起业务流的下行报文丢弃：

```
ADD FWPOLICY: FWPOLICYNAME="testfwpolicy", UPINITUPACTION=PASS, UPINITDNACTION=PASS, DNINITUPACTION=DISCARD, DNINITDNACTION=DISCARD;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-FWPOLICY.md`
