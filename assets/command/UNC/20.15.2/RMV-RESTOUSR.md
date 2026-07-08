---
id: UNC@20.15.2@MMLCommand@RMV RESTOUSR
type: MMLCommand
name: RMV RESTOUSR（删除容灾用户特征参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RESTOUSR
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
- MME容灾管理
- 容灾用户特征管理
status: active
---

# RMV RESTOUSR（删除容灾用户特征参数）

## 功能

**适用网元：MME**

本命令用于删除支持容灾备份的用户特征。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：本参数用于删除应用容灾备份功能的IMSI特征。<br>数据来源：本端规划<br>取值范围：5~15位数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTOUSR]] · 容灾用户特征参数（RESTOUSR）

## 使用实例

当现网停止调试功能时，用于删除支持容灾备份的用户特征，执行如下命令：

RMV RESTOUSR: IMSIPRE="12301";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RESTOUSR.md`
