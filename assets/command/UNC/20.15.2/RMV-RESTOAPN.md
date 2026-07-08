---
id: UNC@20.15.2@MMLCommand@RMV RESTOAPN
type: MMLCommand
name: RMV RESTOAPN（删除容灾APN特征参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RESTOAPN
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
- 容灾APN特征管理
status: active
---

# RMV RESTOAPN（删除容灾APN特征参数）

## 功能

**适用网元：MME**

本命令用于删除支持容灾备份的APN。

## 注意事项

- “IMS”为系统缺省的APNNI记录，无需增加，也不能删除。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：本参数用于删除应用容灾备份功能的APNNI特征。<br>数据来源：全网规划<br>取值范围：1~62位字符串<br>默认值：无<br>配置原则：“IMS”为系统缺省记录，不允许删除。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTOAPN]] · 容灾APN特征参数（RESTOAPN）

## 使用实例

该命令用于删除支持容灾备份的APN特征，执行如下命令：

RMV RESTOAPN: APNNI="HUAWEI.COM";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RESTOAPN.md`
