---
id: UNC@20.15.2@MMLCommand@RMV IPAREAGP
type: MMLCommand
name: RMV IPAREAGP（删除IP区域群）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPAREAGP
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
- 基于位置分配IP地址管理
- IP区域群管理
status: active
---

# RMV IPAREAGP（删除IP区域群）

## 功能

**适用网元：SGSN、MME**

该命令用于删除IP区域群记录。

## 注意事项

- 此命令执行后立即生效。
- 删除IP区域群时必须首先执行[**RMV IPAREAGPMEM**](../IP区域群成员管理/删除IP区域群成员(RMV IPAREAGPMEM)_72345197.md)删除该区域群下的所有成员。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识待删除的区域群。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPAREAGP]] · IP区域群（IPAREAGP）

## 使用实例

删除一条标识为1的IP区域群记录：

RMV IPAREAGP: AREAID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IPAREAGP.md`
