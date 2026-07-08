---
id: UNC@20.15.2@MMLCommand@RMV CHRRPTLOCINFO
type: MMLCommand
name: RMV CHRRPTLOCINFO（删除CHR本地存盘位置配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHRRPTLOCINFO
command_category: 配置类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- CHR本地存盘位置
status: active
---

# RMV CHRRPTLOCINFO（删除CHR本地存盘位置配置）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于删除本地存储CHR的用户的位置过滤条件，包括N2TAC、S1TAC、LACRAC、eNodeB、gNodeB。

## 注意事项

该命令执行后只对之后发生承载更新的用户或者新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCTYPE | 位置类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置类型。<br>数据来源：本端规划<br>取值范围：<br>- N2TAC（N2跟踪区域码）<br>- S1TAC（S1跟踪区域码）<br>- LACRAC（位置区编码和路由区编码）<br>- ENODEBIP（eNodeB IP地址）<br>- GNODEBIP（gNodeB IP地址）<br>默认值：无<br>配置原则：无 |
| S1TAC | S1TAC | 可选必选说明：该参数在"LOCTYPE"配置为"S1TAC"时为条件必选参数。<br>参数含义：该参数用于指定S1TAC。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~6。不支持空格，不区分大小写，必须是4位16进制数，范围为0x0000~0xFFFF。前缀0x可以选择不输入。<br>默认值：无<br>配置原则：无 |
| N2TAC | N2TAC | 可选必选说明：该参数在"LOCTYPE"配置为"N2TAC"时为条件必选参数。<br>参数含义：该参数用于指定N2TAC。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~8。不支持空格，不区分大小写，必须是6位16进制数，范围为0x000000~0xFFFFFF。前缀0x可以选择不输入。<br>默认值：无<br>配置原则：无 |
| LACRAC | LAC和RAC | 可选必选说明：该参数在"LOCTYPE"配置为"LACRAC"时为条件必选参数。<br>参数含义：该参数用于设置位置区编码和路由区编码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~8。不支持空格，不区分大小写，必须是6位16进制数，范围为0x000000~0xFFFFFF。其中LAC为4位16进制数，RAC为2位16进制数，配置时将LAC和RAC拼接成一个6位的16进制数配置。前缀0x可以选择不输入。<br>默认值：无<br>配置原则：无 |
| ENODEBIPTYPE | eNodeB IP地址类型 | 可选必选说明：该参数在"LOCTYPE"配置为"ENODEBIP"时为条件必选参数。<br>参数含义：该参数用于设置eNodeB IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| ENODEBIPV4ADDR | eNodeB IPv4地址 | 可选必选说明：该参数在"ENODEBIPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于设置eNodeB IPv4地址。只有用户的eNodeB IPv4地址或通过S11-U接口传递业务层数据的MME IPv4地址，与配置匹配才进行CHR表单本地存储处理。包含eNodeB地址，和通过S11-U接口传递业务层数据的MME地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| ENODEBIPV6ADDR | eNodeB IPv6地址 | 可选必选说明：该参数在"ENODEBIPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于设置eNodeB IPv6地址。只有用户的eNodeB IPv6地址或通过S11-U接口传递业务层数据的MME IPv6地址，与配置匹配才进行CHR表单本地存储处理。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| GNODEBIPTYPE | gNodeB IP地址类型 | 可选必选说明：该参数在"LOCTYPE"配置为"GNODEBIP"时为条件必选参数。<br>参数含义：该参数用于设置gNodeB IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| GNODEBIPV4ADDR | gNodeB IPv4地址 | 可选必选说明：该参数在"GNODEBIPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于设置gNodeB IPv4地址。只有用户的gNodeB IPv4地址配置匹配才进行CHR表单本地存储处理。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| GNODEBIPV6ADDR | gNodeB IPv6地址 | 可选必选说明：该参数在"GNODEBIPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于设置gNodeB IPv6地址。只有用户的gNodeB IPv6地址配置匹配才进行CHR表单本地存储处理。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHRRPTLOCINFO]] · CHR本地存盘位置配置（CHRRPTLOCINFO）

## 使用实例

删除N2TAC为0x123123的用户的本地存储CHR表单的配置：

```
RMV CHRRPTLOCINFO: LOCTYPE=N2TAC, N2TAC="0x123123";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除CHR本地存盘位置配置（RMV-CHRRPTLOCINFO）_15343997.md`
