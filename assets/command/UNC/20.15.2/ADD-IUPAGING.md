---
id: UNC@20.15.2@MMLCommand@ADD IUPAGING
type: MMLCommand
name: ADD IUPAGING（增加Iu接口寻呼数据）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IUPAGING
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 20000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Iu接口管理
- Iu接口寻呼数据
status: active
---

# ADD IUPAGING（增加Iu接口寻呼数据）

## 功能

**适用网元：SGSN**

该命令用于在触发3G寻呼时，利用此信息根据RAI或者LAI定位RNC。用户进行附着或路由区更新时根据此表判断是否为SGSN间的流程。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为20000。
- 在设置3G寻呼表之前需先配置RNC信息表（[**ADD RNC**](../Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md)）。
- 设置的RNC INDEX必须在RNC信息表中存在。
- 在非POOL组网场景下，不同SGSN覆盖的RA不能重复。因此，在RNC调整时，在新侧增加IUPAGING信息的同时务必在Old SGSN上删除相应的IUPAGING信息。
- 和RNC对接时，需要根据实际对接次序逐步增加IUPAGING配置，不建议按照目标网络一次添加所有配置，否则会存在冗余配置，最终影响SGSN间流程的判断。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | 位置区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本SGSN管辖位置区的标识。<br>数据来源：整网规划<br>取值范围：9~10位字符串<br>默认值：无<br>说明：LAI=MCC+MNC+LAC。MCC由3个阿拉伯数字组成，MNC由2到3个阿拉伯数字组成，LAC是十六进制数，占2个字节。 |
| RAC | 路由区编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本SGSN管辖路由区的编码。<br>数据来源：整网规划<br>取值范围：0x00~0xFF<br>默认值：无<br>说明：RAC是十六进制数，占1个字节。 |
| RNCINDEX | RNC索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RNC索引，可查询RNC信息表获得。<br>数据来源：整网规划<br>取值范围：0~511<br>默认值：无 |

## 操作的配置对象

- [Iu接口寻呼数据（IUPAGING）](configobject/UNC/20.15.2/IUPAGING.md)

## 使用实例

增加一个LAI为123000001，RAC为01，RNC INDEX为0的3G寻呼信息：

ADD IUPAGING:LAI="123000001",RAC="01",RNCINDEX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Iu接口寻呼数据(ADD-IUPAGING)_26305844.md`
