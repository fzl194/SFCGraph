---
id: UNC@20.15.2@MMLCommand@RMV MVNORES
type: MMLCommand
name: RMV MVNORES（删除MVNO资源配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MVNORES
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
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO资源配置表
status: active
---

# RMV MVNORES（删除MVNO资源配置信息）

## 功能

![](删除MVNO资源配置信息(RMV MVNORES)_26146066.assets/notice_3.0-zh-cn_2.png)

如果不输入参数，将删除所有的MVNO的资源信息。

**适用网元：SGSN、MME**

此命令用于删除MVNO的资源信息。

## 注意事项

- 如果不输入参数，将删除所有的MVNO的资源信息。如果输入参数，则删除指定的MVNO的资源信息。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOID | MVNO标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要删除的MVNO的标识。<br>取值范围：1～64<br>默认值：无 |

## 操作的配置对象

- [MVNO资源配置信息（MVNORES）](configobject/UNC/20.15.2/MVNORES.md)

## 使用实例

删除标识为1的MVNO的用户资源：

RMV MVNORES: MVNOID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MVNO资源配置信息(RMV-MVNORES)_26146066.md`
