---
id: UNC@20.15.2@MMLCommand@SYN GENERATECDR
type: MMLCommand
name: SYN GENERATECDR（立即生成话单）
nf: UNC
version: 20.15.2
verb: SYN
object_keyword: GENERATECDR
command_category: 动作类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 维护管理
status: active
---

# SYN GENERATECDR（立即生成话单）

## 功能

**适用NF：NCG**

该命令用于立即生成话单。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST CDRPROC**](../../业务配置管理/话单处理/查询话单处理（LST CDRPROC）_51174275.md)命令查询“接入网元分组标识”。如果没有符合要求的“接入网元分组标识”，还需执行[**ADD CDRPROC**](../../业务配置管理/话单处理/增加话单处理（ADD CDRPROC）_51174272.md)命令增加。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../../业务配置管理/话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| MNAME | 模块名 | 可选必选说明：可选参数<br>参数含义：用于表示一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST MODULE**](../../业务配置管理/业务模块/查询业务模块（LST MODULE）_51174292.md)命令，查询出存在的MNAME进行填写。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../../业务配置管理/话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GENERATECDR]] · 立即生成话单（GENERATECDR）

## 使用实例

- 显示所有话单生成情况，示例如下：
  ```
  SYN GENERATECDR:;
  RETCODE = 0  操作成功。

  结果如下:
  --------
  模块名    任务状态 

  AP66_1    成功     
  AP67_1    成功     
  (结果个数 = 2)
  ---    END
  ```
- 显示同一个接入网元分组标识的话单生成情况，示例如下：
  ```
  SYN GENERATECDR: AGID="PS_GROUP_1";
  RETCODE = 0  操作成功。

  结果如下
  --------
  模块名     =   AP66_1 
  任务状态   =   成功
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SYN-GENERATECDR.md`
