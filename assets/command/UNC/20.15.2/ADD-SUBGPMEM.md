---
id: UNC@20.15.2@MMLCommand@ADD SUBGPMEM
type: MMLCommand
name: ADD SUBGPMEM（增加用户群成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SUBGPMEM
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 20000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- 用户群成员管理
status: active
---

# ADD SUBGPMEM（增加用户群成员）

## 功能

**适用网元：SGSN、MME**

此命令用于增加用户群成员记录。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为20000。
- 此命令配置的“SUBID（用户群标识）”参数值不能在[**ADD MSISDNSUBGPMEM**](../MSISDN用户群成员管理/增加MSISDN用户群成员(ADD MSISDNSUBGPMEM)_72345167.md)配置中使用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 用户群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户群标识。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD SUBGP**](../用户群管理/增加用户群(ADD SUBGP)_72225241.md)<br>设置此参数。<br>数据来源：整网规划<br>取值范围：1～100<br>默认值：无<br>配置原则：配置的参数值不能在<br>[**ADD MSISDNSUBGPMEM**](../MSISDN用户群成员管理/增加MSISDN用户群成员(ADD MSISDNSUBGPMEM)_72345167.md)<br>配置中使用。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>数据来源：整网规划<br>取值范围：5～15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [用户群成员（SUBGPMEM）](configobject/UNC/20.15.2/SUBGPMEM.md)

## 使用实例

增加一条用户群成员记录，用户群标识为30，IMSI前缀为12345：

ADD SUBGPMEM: SUBID=30, IMSIPRE="12345";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加用户群成员(ADD-SUBGPMEM)_26305374.md`
