---
id: UNC@20.15.2@MMLCommand@RMV NWNAMEBYHSS
type: MMLCommand
name: RMV NWNAMEBYHSS（删除不发送运营商名称的HSS）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NWNAMEBYHSS
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- 不发送运营商名称的HSS
status: active
---

# RMV NWNAMEBYHSS（删除不发送运营商名称的HSS）

## 功能

**适用网元：MME**

本命令用于删除不发送运营商名称的HSS。该命令对应的业务功能暂未实现。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置记录的索引。<br>数据来源：本端规划<br>取值范围：整数范围1~1000<br>默认值： 无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NWNAMEBYHSS]] · 不发送运营商名称的HSS（NWNAMEBYHSS）

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NWNAMEBYHSS.md`
