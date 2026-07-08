---
id: UNC@20.15.2@MMLCommand@SET CHRFILESTGMODE
type: MMLCommand
name: SET CHRFILESTGMODE（设置上传至文件服务器的CHR文件转储方式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CHRFILESTGMODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Chr管理
- Chr文件管理
status: active
---

# SET CHRFILESTGMODE（设置上传至文件服务器的CHR文件转储方式）

## 功能

该命令用于设置上传至文件服务器的CHR文件转储方式。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| UPLOADSWITCH | ROTATETHRESHOLD | ROTATEPERIOD |
| --- | --- | --- |
| FALSE | 100 | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPLOADSWITCH | 是否开启上传CHR文件到文件服务器 | 可选必选说明：必选参数<br>参数含义：该参数用于描述是否开启上传CHR文件到文件服务器的功能。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。<br>配置原则：无 |
| ROTATETHRESHOLD | 文件转储大小（MB） | 可选必选说明：可选参数<br>参数含义：该参数用于描述开启上传CHR文件到文件服务器时，文件转储的大小，单位为MB。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是20~300。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHRFILESTGMODE查询当前参数配置值。<br>配置原则：无 |
| ROTATEPERIOD | 文件转储周期（分钟） | 可选必选说明：可选参数<br>参数含义：该参数用于描述开启上传CHR文件到文件服务器时，文件转储的周期，单位为分钟。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~60。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHRFILESTGMODE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [上传至文件服务器的CHR文件转储方式（CHRFILESTGMODE）](configobject/UNC/20.15.2/CHRFILESTGMODE.md)

## 使用实例

- 当用户需要开启上传CHR文件到文件服务器的功能时，将UPLOADSWITCH参数设置成TRUE，在ROTATETHRESHOLD的参数上填写文件转储的大小，在ROTATEPERIOD的参数上填写文件转储的周期，执行该命令。
  ```
  SET CHRFILESTGMODE: UPLOADSWITCH=TRUE, ROTATETHRESHOLD=20, ROTATEPERIOD=10;
  ```
- 当用户需要关闭上传CHR文件到文件服务器的功能时，将UPLOADSWITCH参数设置成FALSE，执行该命令。
  ```
  SET CHRFILESTGMODE: UPLOADSWITCH=FALSE;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置上传至文件服务器的CHR文件转储方式（SET-CHRFILESTGMODE）_28195465.md`
