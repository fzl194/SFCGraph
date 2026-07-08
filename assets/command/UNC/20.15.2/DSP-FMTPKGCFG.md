---
id: UNC@20.15.2@MMLCommand@DSP FMTPKGCFG
type: MMLCommand
name: DSP FMTPKGCFG（显示格式引擎软参配置信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FMTPKGCFG
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 格式引擎包
status: active
---

# DSP FMTPKGCFG（显示格式引擎软参配置信息）

## 功能

**适用NF：NCG**

该命令用于显示当前生效的格式引擎软参配置信息。该命令执行后，系统会显示当前生效的格式引擎软参信息，返回相应的格式引擎包文件名和软参信息。

在系统新安装、系统调测或者故障时，可以使用该命令进行检查。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST CDRPROC**](../话单处理/查询话单处理（LST CDRPROC）_51174275.md)命令查询“接入网元分组标识”。如果没有符合要求的“接入网元分组标识”，还需执行[**ADD CDRPROC**](../话单处理/增加话单处理（ADD CDRPROC）_51174272.md)命令增加。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FMTPKGCFG]] · 格式引擎包软参（FMTPKGCFG）

## 使用实例

查询所有模块组的格式引擎软参配置：

```
DSP FMTPKGCFG:;
```

```
RETCODE = 0  操作成功。

结果如下:
--------
接入网元分组标识    RU的ID    格式引擎包名              格式引擎包软参名称    格式引擎包软参值 

PS4                 64        PS_R9_V940_M_RT.tar.gz    MaxDuration           0             
PS4                 64        PS_R9_V940_M_RT.tar.gz    MaxVolume             0             
PS4                 64        PS_R9_V940_M_RT.tar.gz    MergeCDRNum           0             
PS4                 65        PS_R9_V940_M_RT.tar.gz    MaxDuration           0             
PS4                 65        PS_R9_V940_M_RT.tar.gz    MaxVolume             0             
PS4                 65        PS_R9_V940_M_RT.tar.gz    MergeCDRNum           0       
(结果个数 = 6)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-FMTPKGCFG.md`
