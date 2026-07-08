---
id: UNC@20.15.2@MMLCommand@RST PTPBVC
type: MMLCommand
name: RST PTPBVC（复位小区）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: PTPBVC
command_category: 动作类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- 小区管理
status: active
---

# RST PTPBVC（复位小区）

## 功能

![](复位小区(RST PTPBVC)_72345591.assets/notice_3.0-zh-cn_2.png)

复位小区会中断相关小区的服务。

**适用网元：SGSN**

该命令对GBP进程BSSGP层的PTPBVC实体进行复位。PTPBVC用来在对等点对点功能实体间传输BSSGP PDU，可参考 3GPP TS 08.18。

当系统发生影响PTP实体功能的故障恢复时，可执行此命令，使BSS和SGSN两端同步初始化PTP实体的相关上下文。

## 注意事项

操作该命令，该小区上的所有的业务全部中断，相关信息全部丢失，请谨慎操作。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLID | 小区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定小区的标识，CELLID = MCC + MNC + LAC + RAC + CI。<br>取值范围：长度不超过23的十六进制数<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PTPBVC]] · 复位小区（PTPBVC）

## 使用实例

复位标识为123000001020003的小区：

RST PTPBVC: CELLID="123000001020003";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RST-PTPBVC.md`
