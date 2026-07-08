---
id: UNC@20.15.2@MMLCommand@RMV SCCPNGT
type: MMLCommand
name: RMV SCCPNGT（删除SCCP新全局翻译码）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCCPNGT
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP新全局翻译码
status: active
---

# RMV SCCPNGT（删除SCCP新全局翻译码）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于删除SCCP新全局码表指定记录的信息。

## 注意事项

- 此命令执行后立即生效。
- 如果SCCP全局码翻译表中存在与该新全局码相关的记录，则删除失败。不会上报告警。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTX | 新GT码索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定新GT码对应的索引值。<br>取值范围：0~4095<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPNGT]] · SCCP新全局翻译码（SCCPNGT）

## 使用实例

以下命令删除SCCP新全局码表索引1记录的信息

RMV SCCPNGT: NGTX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SCCPNGT.md`
