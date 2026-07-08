---
id: UNC@20.15.2@MMLCommand@RMV IUPAGING
type: MMLCommand
name: RMV IUPAGING（删除Iu接口寻呼数据）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IUPAGING
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Iu接口管理
- Iu接口寻呼数据
status: active
---

# RMV IUPAGING（删除Iu接口寻呼数据）

## 功能

![](删除Iu接口寻呼数据(RMV IUPAGING)_72345635.assets/notice_3.0-zh-cn_2.png)

删除RAI和RNCID的关联，可能导致寻呼失败。

**适用网元：SGSN**

该命令用于删除3G寻呼信息。删除了某个RAI记录后，3G用户在该路由区将无法被寻呼到。

## 注意事项

删除RAI和RNCID的关联，可能导致寻呼失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | 位置区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本SGSN管辖位置区的标识。<br>取值范围：长度为9~10个字符串<br>默认值：无<br>说明：LAI = MCC + MNC + LAC。MCC由3个阿拉伯数字组成，MNC由2到3个阿拉伯数字组成，LAC是十六进制数，占2个字节。 |
| RAC | 路由区编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本SGSN管辖路由区的编码。<br>取值范围：0x00~0xFF<br>默认值：无<br>说明：RAC是十六进制数，占1个字节。 |
| RNCINDEX | RNC索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RNC索引，可查询RNC信息表获得。<br>取值范围：0~511<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IUPAGING]] · Iu接口寻呼数据（IUPAGING）

## 使用实例

删除一个LAI为123000001，RAC为1，RNC INDEX为2的3G寻呼信息：

RMV IUPAGING:LAI="123000001",RAC="01",RNCINDEX=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IUPAGING.md`
