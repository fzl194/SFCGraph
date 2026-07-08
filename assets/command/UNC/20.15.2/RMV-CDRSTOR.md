---
id: UNC@20.15.2@MMLCommand@RMV CDRSTOR
type: MMLCommand
name: RMV CDRSTOR（删除话单存储）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CDRSTOR
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单存储
status: active
---

# RMV CDRSTOR（删除话单存储）

## 功能

![](删除话单存储（RMV CDRSTOR）_51174278.assets/notice_3.0-zh-cn_2.png)

此命令不能动态生效，需要执行“RST SERVICE”重启服务，并且删除话单存储可能导致业务不可用。

**适用NF：NCG**

该命令用于删除原始话单、第一份最终话单和第二份最终话单的存储规则。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST SERVICE**](../../业务系统管理/业务管理/复位业务（RST SERVICE）_51174329.md)”命令重新启动系统才能生效。
- 此命令为高危险操作。在系统运行过程中，执行此命令很可能导致CG整个系统瘫痪。
- 系统运行过程中，不能删除话单存储规则；仅当配置了All与具体通道下的第二份最终话单的存储规则时，允许删除具体通道的存储规则。
- 通道名称为“All”的话单存储规则不能被删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRSTORID | 话单存储标识 | 可选必选说明：必选参数<br>参数含义：话单存储对象标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [话单存储（CDRSTOR）](configobject/UNC/20.15.2/CDRSTOR.md)

## 使用实例

删除第二份最终话单下default通道下，话单存储标识为“FinalCDR_2ndCopy”的话单存储规则：

```
RMV CDRSTOR: CDRSTORID="FinalCDR_2ndCopy";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话单存储（RMV-CDRSTOR）_51174278.md`
