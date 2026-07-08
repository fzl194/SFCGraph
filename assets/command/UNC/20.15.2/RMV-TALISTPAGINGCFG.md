---
id: UNC@20.15.2@MMLCommand@RMV TALISTPAGINGCFG
type: MMLCommand
name: RMV TALISTPAGINGCFG（删除TALIST寻呼不重发TAC区间）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TALISTPAGINGCFG
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- S1寻呼TALIST寻呼管理
status: active
---

# RMV TALISTPAGINGCFG（删除TALIST寻呼不重发TAC区间）

## 功能

**适用网元：MME**

该命令用于删除TALIST寻呼不重发TAC区间。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAC | 跟踪区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0x0000~0xFFFF，输入时可以不输入0x前缀。<br>默认值： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TALISTPAGINGCFG]] · TALIST寻呼不重发TAC区间（TALISTPAGINGCFG）

## 使用实例

删除TAC起始为0x0000的跟踪区间：

RMV TALISTPAGINGCFG: TAC="0x0000";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-TALISTPAGINGCFG.md`
