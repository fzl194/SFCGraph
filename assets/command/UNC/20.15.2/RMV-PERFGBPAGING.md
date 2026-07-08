---
id: UNC@20.15.2@MMLCommand@RMV PERFGBPAGING
type: MMLCommand
name: RMV PERFGBPAGING（删除Gb接口寻呼数据）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFGBPAGING
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

# RMV PERFGBPAGING（删除Gb接口寻呼数据）

## 功能

**适用网元：SGSN**

该命令用于删除指定Gb接口寻呼数据。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | 寻呼范围位置区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由区所在的位置区标识，与RAC共同构成路由区标识。LAI = MNC + MCC + LAC。<br>数据来源：整网规划<br>取值范围：9~10位十六进制数<br>默认值：无 |
| RAC | 寻呼范围路由区编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由区在位置区内的标识，与LAI共同构成路由区标识。<br>数据来源：整网规划<br>取值范围：0x00~0xFF<br>默认值：无<br>说明：RAC是十六进制数，占1个字节。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFGBPAGING]] · Gb接口寻呼数据（PERFGBPAGING）

## 使用实例

删除Gb接口寻呼数据下记录：

RMV PERFGBPAGING: LAI="123031111",RAC="08";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFGBPAGING.md`
