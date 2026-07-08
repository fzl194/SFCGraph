---
id: UNC@20.15.2@MMLCommand@RMV IPGP
type: MMLCommand
name: RMV IPGP（删除IP群组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPGP
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
- 业务安全管理
- 会话管理
- IP群组管理
- IP群组配置
status: active
---

# RMV IPGP（删除IP群组）

## 功能

**适用网元：SGSN、MME**

该命令用于删除IP群组配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPGPID | IP群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP群组标识。<br>数据来源：本端规划<br>取值范围：1-255<br>默认值：无 |

## 操作的配置对象

- [IP群组（IPGP）](configobject/UNC/20.15.2/IPGP.md)

## 使用实例

删除IPGPID为1的IP群组配置：

RMV IPGP: IPGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IP群组(RMV-IPGP)_72225395.md`
