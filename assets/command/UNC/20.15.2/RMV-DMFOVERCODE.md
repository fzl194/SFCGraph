---
id: UNC@20.15.2@MMLCommand@RMV DMFOVERCODE
type: MMLCommand
name: RMV DMFOVERCODE（删除触发重选路由的错误码）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMFOVERCODE
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
- 信令传输管理
- Diameter管理
- Diameter协议接口重选路配置
status: active
---

# RMV DMFOVERCODE（删除触发重选路由的错误码）

## 功能

**适用网元：SGSN、MME**

该命令用于删除Diameter链路上配置的触发重选路由的错误码。使用 [**SET DMFUNC**](../Diameter参数/设置Diameter配置(SET DMFUNC)_72225949.md) 命令打开 “重选路由功能开关” （ **SET DMFUNC:FAILOVER=YES;** ），当系统收到对端响应的错误码为触发重新选路的错误码（详见 [**ADD DMFOVERCODE**](增加触发重选路由的错误码(ADD DMFOVERCODE)_26146294.md) ），则会重新选择其他Diameter路由。若使用该命令删除已配置的错误码，则不会重选路由。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ERRCODE | 触发重选路由的错误码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要触发重选路由的错误码。<br>数据来源：整网规划<br>取值范围：0-4294967295<br>- “3002(DIAMETER_UNABLE_TO_DELIVER)”：对端不能把消息发送到目的地<br>- “3004(DIAMETER_TOO_BUSY)”：对端不能提供请求的服务<br>- “3005(DIAMETER_LOOP_DETECTED)”：系统向对端发消息时检测到有环路<br>默认值：无<br>说明：不输入参数时，删除所有配置的错误码记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMFOVERCODE]] · 触发重选路由的错误码（DMFOVERCODE）

## 使用实例

当不需要在对端不能提供请求的服务时触发重选路由，删除触发重选路由的错误码:

RMV DMFOVERCODE: ERRCODE=3004;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DMFOVERCODE.md`
