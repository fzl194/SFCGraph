---
id: UNC@20.15.2@MMLCommand@RMV POOLNRI
type: MMLCommand
name: RMV POOLNRI（删除POOL区NRI配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: POOLNRI
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL区NRI配置
status: active
---

# RMV POOLNRI（删除POOL区NRI配置信息）

## 功能

**适用网元：SGSN**

此命令用于删除本POOL区内非本SGSN的NRI属性配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POOL区标识。<br>取值范围：0～4095<br>默认值：无 |
| NRIV | NRI值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRI的值，NRI（Net Resource Identify），网络资源标识，用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>取值范围：0～1023<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/POOLNRI]] · POOL区NRI配置信息（POOLNRI）

## 使用实例

删除POOLID为1，NRI值为10的NRI记录：

RMV POOLNRI: POOLID=1, NRIV=10;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-POOLNRI.md`
