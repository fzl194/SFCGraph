---
id: UNC@20.15.2@MMLCommand@RMV NONRAI
type: MMLCommand
name: RMV NONRAI（删除非广播RAI配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NONRAI
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL区非广播RAI配置
status: active
---

# RMV NONRAI（删除非广播RAI配置信息）

## 功能

**适用网元：SGSN**

此命令用于删除非广播RAI配置记录。

## 注意事项

此命令执行立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NONRAI | 路由区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定非广播路由区标识。用于在迁移的时候，目的SGSN来识别MS是从哪个SGSN迁移过来的。一个非广播路由区标识可以唯一地标志一个SGSN。<br>取值范围：长度必须为11或者12位，前5或6位为十进制数，后6位为十六进制数的字符串<br>默认值：无<br>说明：NONRAI = LAI + RAC LAI = MCC + MNC + LAC。MCC由3个阿拉伯数字组成，MNC由2到3个阿拉伯数字组成，LAC是十六进制数，占2个字节。RAC是十六进制数，占1个字节。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NONRAI]] · 非广播RAI配置信息（NONRAI）

## 使用实例

删除NONRAI记录信息， “NONRAI” 为 “123000000000” ：

RMV NONRAI: NONRAI="123000000000";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除非广播RAI配置信息(RMV-NONRAI)_72345709.md`
