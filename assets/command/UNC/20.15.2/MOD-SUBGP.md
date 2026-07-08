---
id: UNC@20.15.2@MMLCommand@MOD SUBGP
type: MMLCommand
name: MOD SUBGP（修改用户群）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SUBGP
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
- 用户群管理
status: active
---

# MOD SUBGP（修改用户群）

## 功能

**适用网元：SGSN、MME**

该命令用于修改用户群名称。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 用户群标识 | 可选必选说明：必选参数<br>参数含义：待修改的指定用户群标识 。<br>数据来源：整网规划<br>取值范围：1～100<br>默认值：无 |
| SUBN | 用户群名称 | 可选必选说明：可选参数<br>参数含义：待修改的指定用户群名称。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：无 |

## 操作的配置对象

- [用户群（SUBGP）](configobject/UNC/20.15.2/SUBGP.md)

## 使用实例

修改一条用户群标识为30的用户群管理记录，将用户群名称修改为group30：

MOD SUBGP: SUBID=30, SUBN="group30";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户群(MOD-SUBGP)_72345159.md`
