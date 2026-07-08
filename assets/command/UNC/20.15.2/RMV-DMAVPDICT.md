---
id: UNC@20.15.2@MMLCommand@RMV DMAVPDICT
type: MMLCommand
name: RMV DMAVPDICT（删除Diameter AVP表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMAVPDICT
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
- 扩展调测
- 业务调测
- Diameter AVP表
status: active
---

# RMV DMAVPDICT（删除Diameter AVP表）

## 功能

**适用网元：SGSN、MME**

该命令用于删除Diameter AVP表信息。

## 注意事项

此命令执行后需要通过执行 [**RST PROCESS**](../../../../../../平台服务管理/单体服务维护功能管理/操作维护/系统调测/进程管理/复位进程(RST PROCESS)_29626893.md) 重启所有SPP进程、所有SGP进程才能生效。

如果不输入任何参数，则提示：请输入"Dictionary Name"参数或"Avp Name"参数或"AVP Code"参数。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DICTNAME | 字典名称 | 可选必选说明：可选参数<br>参数含义：待删除Diameter数据字典名称。<br>取值范围：0～65535<br>默认值：无 |
| AVPNAME | 信元名称 | 可选必选说明：可选参数<br>参数含义：待删除信元名称。<br>取值范围：0～65535<br>默认值：无 |
| AVPCODE | 信元编码 | 可选必选说明：可选参数<br>参数含义：待删除信元编码。<br>取值范围：0～4294967294<br>默认值：无<br>说明：AVP代码连同Vendor-ID字段一起来唯一地标识属性。代码1～255保留，用于保证和RADIUS向后兼容。255以上的代码为Diameter所用，由IANA分配。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMAVPDICT]] · Diameter数据字典中的AVP参数（DMAVPDICT）

## 使用实例

删除Diameter数据字典中字典名称为1的项：

RMV DMAVPDICT: DICTNAME=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter-AVP表(RMV-DMAVPDICT)_72345459.md`
