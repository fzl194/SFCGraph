---
id: UNC@20.15.2@MMLCommand@STP CDRRECEIVE
type: MMLCommand
name: STP CDRRECEIVE（停止接收话单）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: CDRRECEIVE
command_category: 动作类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 话单接收管理
status: active
---

# STP CDRRECEIVE（停止接收话单）

## 功能

![](停止接收话单（STP CDRRECEIVE）_51174326.assets/notice_3.0-zh-cn_2.png)

停止接收话单会导致NCG停止接收话单，把接收到的原始话单转换成最终话单。

**适用NF：NCG**

该命令用于停止NCG接收话单。

## 注意事项

- 当用户执行了[**STP CDRRECEIVE**](停止接收话单（STP CDRRECEIVE）_51174326.md)命令时，NCG中满足输入参数的AP进程，主动停止话单接收。产生“**ALM-82014停止接收话单**”告警。
- 执行[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)命令重启NCG网元后，此告警恢复，话单恢复正常接收。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST CDRPROC**](../../业务配置管理/话单处理/查询话单处理（LST CDRPROC）_51174275.md)命令查询“接入网元分组标识”。如果没有符合要求的“接入网元分组标识”，还需执行[**ADD CDRPROC**](../../业务配置管理/话单处理/增加话单处理（ADD CDRPROC）_51174272.md)命令增加。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../../业务配置管理/话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| MNAME | 模块名 | 可选必选说明：可选参数<br>参数含义：用于标识一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST MODULE**](../../业务配置管理/业务模块/查询业务模块（LST MODULE）_51174292.md)命令，查询出存在的MNAME进行填写。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../../业务配置管理/话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CDRRECEIVE]] · 接收话单（CDRRECEIVE）

## 使用实例

停止NCG接收话单：

```
STP CDRRECEIVE:
RETCODE = 0  操作成功。

结果如下:
---------
接入网元分组标识    RU的ID    模块名    执行结果

PS1                 64        AP64_1    成功    
PS2                 65        AP65_1    成功    
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STP-CDRRECEIVE.md`
