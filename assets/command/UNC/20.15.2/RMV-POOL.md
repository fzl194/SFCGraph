---
id: UNC@20.15.2@MMLCommand@RMV POOL
type: MMLCommand
name: RMV POOL（删除POOL配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: POOL
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL区配置
status: active
---

# RMV POOL（删除POOL配置信息）

## 功能

![](删除POOL配置信息(RMV POOL)_26305912.assets/notice_3.0-zh-cn_2.png)

[**RMV POOL**](删除POOL配置信息(RMV POOL)_26305912.md) 命令执行后需要复位整系统才能生效。

**适用网元：SGSN**

该命令用于删除POOL配置信息。

## 注意事项

- 该命令执行后需要复位整系统才能生效，复位整系统请参考**RST VNFC**命令。
- POOLID必须是在POOL表中存在记录。
- 必须保证所删除的POOL区未配置LOCALNRI(RMV LOCALNRI)和POOLNRI(RMV POOLNRI)；否则，不允许删除。
- 删除POOL记录会同时清除OFFLOADINF中的POOLID和NULLNRI记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POOL标识。<br>取值范围：0~4095<br>默认值：无 |

## 操作的配置对象

- [POOL配置信息（POOL）](configobject/UNC/20.15.2/POOL.md)

## 使用实例

删除一个POOL配置信息，POOLID为1：

RMV POOL: POOLID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除POOL配置信息(RMV-POOL)_26305912.md`
