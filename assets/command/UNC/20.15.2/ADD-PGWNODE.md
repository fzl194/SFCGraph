---
id: UNC@20.15.2@MMLCommand@ADD PGWNODE
type: MMLCommand
name: ADD PGWNODE（增加P-GW局向）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PGWNODE
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- P-GW信息管理
- P-GW节点管理
status: active
---

# ADD PGWNODE（增加P-GW局向）

## 功能

**适用网元：SGSN、MME**

该命令用于增加P-GW局向。配置PGW Node Name后缀的列表，只有在列表中的才能开启MME支持基于P-GW Back-off timer的APN级流控功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | P-GW组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定P-GW组号。<br>数据来源：本端规划<br>取值范围：0～15<br>默认值：无<br>配置原则：该ID必须是<br>[**ADD PGWGROUP**](../P-GW组管理/增加P-GW组(ADD PGWGROUP)_72225385.md)<br>命令中已配置的ID记录。 |
| SUFFIX | P-GW Nodename后缀 | 可选必选说明：必选参数<br>参数含义：该参数用来设置P-GW的Nodename后缀，用于匹配P-GW的Nodename识别P-GW局向。<br>数据来源：本端规划<br>取值范围：1～255位字符串<br>默认值：无<br>配置原则：<br>- 该参数只能由字母（A～Z或者a～z）、数字（0～9）、连字符（-）和点（.）组成。<br>- 按照协议RFC1035规定，Hostname最大有效字符数为253，并且每个Label最大长度为63个字节。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述P-GW局向信息。<br>数据来源：本端规划<br>取值范围：0～256位字符串<br>默认值：noname |

## 操作的配置对象

- [P-GW局向（PGWNODE）](configobject/UNC/20.15.2/PGWNODE.md)

## 使用实例

运营商希望增加新的P-GW局向。增加组号为“2”的“P-GW组号”，“P-GW Nodename后缀”设置为“GW01.CITY-B.PROVINCE-A.NODE.EPC.MNC000.MCC460.3GPPNETWORK.ORG”。运行如下命令:

ADD PGWNODE: GRPID=2, SUFFIX="GW01.CITY-B.PROVINCE-A.NODE.EPC.MNC000.MCC460.3GPPNETWORK.ORG";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加P-GW局向(ADD-PGWNODE)_72225387.md`
