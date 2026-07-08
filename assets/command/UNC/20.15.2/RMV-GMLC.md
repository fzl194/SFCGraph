---
id: UNC@20.15.2@MMLCommand@RMV GMLC
type: MMLCommand
name: RMV GMLC（删除GMLC配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GMLC
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
- LCS
- GMLC配置
status: active
---

# RMV GMLC（删除GMLC配置）

## 功能

**适用网元：SGSN、MME**

此命令用于删除GMLC配置。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCID | GMLC 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GMLC标识。<br>取值范围：0～639<br>默认值 ：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLC]] · GMLC配置（GMLC）

## 使用实例

删除一条 “GMLC 标识” 为 “1” 的GMLC配置记录：

RMV GMLC: GMLCID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GMLC.md`
