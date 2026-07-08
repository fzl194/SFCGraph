---
id: UNC@20.15.2@MMLCommand@RMV HNOINFO
type: MMLCommand
name: RMV HNOINFO（删除归属网络信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HNOINFO
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
- 归属网络信息管理
status: active
---

# RMV HNOINFO（删除归属网络信息）

## 功能

**适用网元：SGSN、MME**

该命令用于删除归属网络信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后会造成该运营商的相应配置失效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>取值范围：0～64，128～254<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HNOINFO]] · 归属网络信息（HNOINFO）

## 使用实例

删除一个 “运营商标识” 为 “128” 的HNOINFO：

RMV HNOINFO: NOID=128;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HNOINFO.md`
