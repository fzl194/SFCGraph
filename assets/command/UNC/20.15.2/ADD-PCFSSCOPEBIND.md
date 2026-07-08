---
id: UNC@20.15.2@MMLCommand@ADD PCFSSCOPEBIND
type: MMLCommand
name: ADD PCFSSCOPEBIND（增加PCF业务服务区的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PCFSSCOPEBIND
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF业务服务区绑定
status: active
---

# ADD PCFSSCOPEBIND（增加PCF业务服务区的绑定关系）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加PCF业务服务区与用户基本信息（如用户TAI区域）的绑定关系。其中，PCF业务服务区通过ADD PCFSSCOPE增加配置。当语音用户通过N7口发起会话建立请求时，可根据该绑定关系映射PCF业务服务区，从而选择可用PCF。

## 注意事项

- 该命令执行后立即生效。

- 需要预先配置ADD PCFSSCOPE。若BINDTYPE取值为USRTAIRANGE，需要预先配置ADD USRTAIRANGE。
- 若BINDTYPE取值为USRTAIRANGE，系统中不同PCF业务服务区对应的用户TAI区域不能重叠，配置命令时会有相应检测，若用户TAI区域有重叠则配置下发失败。
- 若PCFSSCOPE配置有记录，且激活请求未携带用户TAI、或根据用户TAI无法从PCFSSCOPEBIND中匹配到合适的SSCOPEID，则从PCFSSCOPE的记录内随机选择一个SSCOPENAME用于PCF服务发现。

- 最多可输入5000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BINDNAME | 绑定名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定绑定记录的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：无 |
| SSCOPEID | 服务区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务区标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：<br>配置的SSCOPEID必须是ADD PCFSSCOPE命令已配置的SSCOPEID。 |
| BINDTYPE | 绑定类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定和服务区标识绑定的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- “USRTAIRANGE（用户TAI范围）”：指定用户TAI范围与PCF服务区标识绑定。<br>默认值：无<br>配置原则：无 |
| USRTAIRANGENAME | 用户TAI区域名称 | 可选必选说明：该参数在"BINDTYPE"配置为"USRTAIRANGE"时为条件必选参数。<br>参数含义：该参数用于指定用户TAI区域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：<br>配置的USRTAIRANGENAME必须是ADD USRTAIRANGE命令已配置的RANGENAME。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCFSSCOPEBIND]] · PCF业务服务区的绑定关系（PCFSSCOPEBIND）

## 使用实例

增加PCFSSCOPEBIND配置，BINDNAME为towna，SSCOPEID为citya，BINDTYPE为USRTAIRANGE，USRTAIRANGENAME为tai1。

```
ADD PCFSSCOPEBIND: BINDNAME="towna", SSCOPEID="citya", BINDTYPE=USRTAIRANGE, USRTAIRANGENAME="tai1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PCFSSCOPEBIND.md`
