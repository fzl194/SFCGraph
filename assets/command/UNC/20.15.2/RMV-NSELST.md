---
id: UNC@20.15.2@MMLCommand@RMV NSELST
type: MMLCommand
name: RMV NSELST（删除NSE列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NSELST
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- MS上下文管理
- 基于NSE的MS上下文管理
status: active
---

# RMV NSELST（删除NSE列表）

## 功能

**适用网元：SGSN**

该命令用于从NSE列表中删除指定的NSEI。

## 注意事项

- 该命令执行后立即生效。
- 若未输入参数，表示删除所有记录。
- 如果执行该命令时[**RMV NSEUSR**](删除NSE列表下的用户(RMV NSEUSR)_26305832.md)任务正在运行，则删除的NSEI仍然会被[**RMV NSEUSR**](删除NSE列表下的用户(RMV NSEUSR)_26305832.md)处理，即属于这个NSE的用户仍然会被删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>取值范围：0～65535<br>默认值：无<br>说明：输入的NSEI必须能够通过<br>[**LST NSE**](../../信令实体管理/查询信令实体（LST NSE）_72345629.md)<br>查询到。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSELST]] · NSE列表（NSELST）

## 使用实例

1. 删除NSE列表下所有记录：
  RMV NSELST:;
2. 从NSE列表中删除NSEI为10的NSE：
  RMV NSELST: NSEI=10;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NSE列表(RMV-NSELST)_26146022.md`
