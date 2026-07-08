---
id: UNC@20.15.2@MMLCommand@ADD NOCENTCNCHL
type: MMLCommand
name: ADD NOCENTCNCHL（增加RU通道过滤规则）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NOCENTCNCHL
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
max_records: 10000
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- RU通道过滤规则
status: active
---

# ADD NOCENTCNCHL（增加RU通道过滤规则）

## 功能

**适用NF：NCG**

该命令用于增加RU对应的通道过滤规则。配置支持指定RU中某些通道话单不推送到汇聚RU。

## 注意事项

- 该命令最大记录数为10000。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：必选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| CHLNAME | 通道名称 | 可选必选说明：必选参数<br>参数含义：通道名称的取值为具体的通道名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：通道名称需要通过执行<br>[**DSP FEMPACKET**](../../业务配置管理/格式引擎包/显示格式引擎配置信息（DSP FEMPACKET）_51174306.md)<br>来获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NOCENTCNCHL]] · RU通道过滤规则（NOCENTCNCHL）

## 使用实例

添加RUID为64，通道名称为00/ABNORMAL的过滤规则，示例如下：

```
ADD NOCENTCNCHL: RUID=64, CHLNAME="00/ABNORMAL";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NOCENTCNCHL.md`
