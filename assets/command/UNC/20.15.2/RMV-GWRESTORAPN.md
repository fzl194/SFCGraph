---
id: UNC@20.15.2@MMLCommand@RMV GWRESTORAPN
type: MMLCommand
name: RMV GWRESTORAPN（删除网关容灾APN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GWRESTORAPN
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
- 网关故障管理
status: active
---

# RMV GWRESTORAPN（删除网关容灾APN）

## 功能

**适用网元：MME**

本命令用于删除支持S-GW/P-GW容灾功能的APNNI。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：本参数用于删除在S-GW/P-GW故障场景下，待恢复业务的APNNI。<br>数据来源：整网规划<br>取值范围：0～62位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWRESTORAPN]] · 网关容灾APN（GWRESTORAPN）

## 使用实例

该命令用于删除支持S-GW/P-GW容灾功能的APNNI，执行如下命令：

RMV GWRESTORAPN: APNNI="HUAWEI.COM";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除网关容灾APN(RMV-GWRESTORAPN)_26305892.md`
