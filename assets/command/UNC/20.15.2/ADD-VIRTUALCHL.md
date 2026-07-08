---
id: UNC@20.15.2@MMLCommand@ADD VIRTUALCHL
type: MMLCommand
name: ADD VIRTUALCHL（增加虚拟通道映射）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: VIRTUALCHL
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 虚拟通道映射
status: active
---

# ADD VIRTUALCHL（增加虚拟通道映射）

## 功能

**适用NF：NCG**

该命令用于增加虚拟通道映射。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为256。
- 最终话单文件的存储目录和话单查询浏览界面显示的目录均为源通道。
- 增加虚拟通道后，本地备份和本地分发的目的路径的源通道目录下如果存在话单文件，不会自动删除，会占用NCG的磁盘空间。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SOURCECHL | 源通道名称 | 可选必选说明：必选参数<br>参数含义：需要映射的通道名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 源通道名称需要通过执行[**DSP FEMPACKET**](../格式引擎包/显示格式引擎配置信息（DSP FEMPACKET）_51174306.md)命令来获取。<br>- 同一个接入分组的一个源通道只能配置一个虚拟通道映射。 |
| AGID | 接入网元分组标识 | 可选必选说明：必选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST CDRPROC**](../话单处理/查询话单处理（LST CDRPROC）_51174275.md)命令查询“接入网元分组标识”。如果没有符合要求的“接入网元分组标识”，还需执行[**ADD CDRPROC**](../话单处理/增加话单处理（ADD CDRPROC）_51174272.md)命令增加。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| VIRTUALCHL | 虚拟通道名称 | 可选必选说明：必选参数<br>参数含义：映射后的虚拟通道名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 长度不超过32的字符串，且只能为大小写英文字母、数字、字符“-”、字符“/”及字符“_”，且不能包含连续的“/”。<br>- 虚拟通道不能和该接入分组的格式引擎包通道重复。<br>- 虚拟通道不能和该接入分组的其他虚拟通道重复。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VIRTUALCHL]] · 虚拟通道映射（VIRTUALCHL）

## 使用实例

增加接入分组PS1的"98/OFFLINE"通道的虚拟通道映射，配置举例如下：

```
ADD VIRTUALCHL: SOURCECHL="98/OFFLINE", AGID="PS1", VIRTUALCHL="90/OFFLINE";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-VIRTUALCHL.md`
