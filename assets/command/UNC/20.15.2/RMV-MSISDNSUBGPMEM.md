---
id: UNC@20.15.2@MMLCommand@RMV MSISDNSUBGPMEM
type: MMLCommand
name: RMV MSISDNSUBGPMEM（删除MSISDN用户群成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MSISDNSUBGPMEM
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- MSISDN用户群成员管理
status: active
---

# RMV MSISDNSUBGPMEM（删除MSISDN用户群成员）

## 功能

**适用网元：SGSN、MME**

此命令用于删除MSISDN用户群成员。

## 注意事项

- 此命令执行后立即生效。
- 此命令如果只输入 “用户群标识” ，将提示：请输入"MSISDN Prefix"参数。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 用户群标识 | 可选必选说明：必选参数<br>参数含义：待删除的用户群标识。<br>取值范围：1～100。<br>默认值：无<br>说明：如果只输入用户群标识，将删除该用户群内所有记录。 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：可选参数<br>参数含义：待删除的MSISDN前缀。<br>取值范围：1～15位十进制数字。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MSISDNSUBGPMEM]] · MSISDN用户群成员（MSISDNSUBGPMEM）

## 使用实例

删除一条SUBID为1，MSISDN前缀为12345的用户群成员记录：

RMV MSISDNSUBGPMEM: SUBID=1, MSISDNPRE="12345";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MSISDNSUBGPMEM.md`
