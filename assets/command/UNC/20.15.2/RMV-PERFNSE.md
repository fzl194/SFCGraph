---
id: UNC@20.15.2@MMLCommand@RMV PERFNSE
type: MMLCommand
name: RMV PERFNSE（删除NSE标识）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFNSE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能对象管理
status: active
---

# RMV PERFNSE（删除NSE标识）

## 功能

**适用网元：SGSN**

该命令用于删除指定的NSE标识。

## 注意事项

- 该命令执行后立即生效。
- 若未输入参数，表示删除所有记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>取值范围：0～65535<br>默认值：无<br>说明：输入的NSEI必须能够通过<br>[**LST PERFNSE**](查询NSE标识(LST PERFNSE)_72225869.md)<br>查询到。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFNSE]] · NSE标识（PERFNSE）

## 使用实例

1. 删除NSE列表下所有记录：
  RMV PERFNSE:;
2. 删除NSEI为10的NSE：
  RMV PERFNSE: NSEI=10;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFNSE.md`
