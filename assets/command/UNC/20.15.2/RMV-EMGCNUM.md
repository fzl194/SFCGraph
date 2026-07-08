---
id: UNC@20.15.2@MMLCommand@RMV EMGCNUM
type: MMLCommand
name: RMV EMGCNUM（删除紧急号码信息表记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EMGCNUM
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 紧急呼叫配置
- 紧急呼叫号码配置
status: active
---

# RMV EMGCNUM（删除紧急号码信息表记录）

## 功能

**适用网元：SGSN、MME**

此命令用于删除配置的紧急呼叫号码信息。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数表示所要删除的紧急呼叫号码所属国家码。<br>取值范围：3位的十进制数字<br>默认值：无 |
| NUM | 紧急呼叫号码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示要删除的紧急呼叫号码。<br>取值范围：长度不超过80的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EMGCNUM]] · 紧急号码信息表记录（EMGCNUM）

## 使用实例

删除给MCC为“123”配置的紧急号码“119”：

RMV EMGCNUM: MCC="123", NUM="119";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-EMGCNUM.md`
