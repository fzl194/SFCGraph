---
id: UNC@20.15.2@MMLCommand@LST CDRAUDIT
type: MMLCommand
name: LST CDRAUDIT（查询话单稽核）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRAUDIT
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
- 话单稽核
status: active
---

# LST CDRAUDIT（查询话单稽核）

## 功能

**适用NF：NCG**

该命令用于查询当前系统已配置的话单稽核信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRAUDITID | 稽核任务标识 | 可选必选说明：可选参数<br>参数含义：稽核任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| MNAME | 模块名 | 可选必选说明：可选参数<br>参数含义：用于表示一个模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：无 |
| CHLNAME | 通道名称 | 可选必选说明：可选参数<br>参数含义：通道名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| AUDITSTORDAYS | 话单稽核文件保存天数（天） | 可选必选说明：可选参数<br>参数含义：话单稽核文件的保存天数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～180，单位是天。<br>默认值：无<br>配置原则：无 |
| AUDITNAME | 话单稽核文件命名规则 | 可选必选说明：可选参数<br>参数含义：话单稽核文件的命名规则。具体的配置规则及举例请参见<br>[**表1**](增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEC2)<br>。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。<br>默认值：无<br>配置原则：无 |
| AUDITFORMAT | 稽核内容格式 | 可选必选说明：可选参数<br>参数含义：话单稽核文件内容的格式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- txt：Txt格式。<br>- csv：Csv格式。<br>默认值：无<br>配置原则：无 |
| ISCOLLECTINFO | 是否汇总稽核信息 | 可选必选说明：可选参数<br>参数含义：是否汇总稽核信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：无<br>配置原则：无 |
| ISADDNOTES | 是否添加文件抬头 | 可选必选说明：可选参数<br>参数含义：是否在稽核文件的第一行显示每列的含义。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：无<br>配置原则：无 |
| AUDITPARA1 | 话单稽核参数1 | 可选必选说明：可选参数<br>参数含义：配置话单稽核文件统计的稽核指标。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CDRFileName：话单文件名。<br>- CDRNumber：话单文件话单张数。<br>- CDRFileSize：话单文件大小。<br>- CDRFileModifyTime：话单文件修改时间。<br>默认值：无<br>配置原则：无 |
| AUDITPARA2 | 话单稽核参数2 | 可选必选说明：可选参数<br>参数含义：配置话单稽核文件统计的稽核指标。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CDRFileName：话单文件名。<br>- CDRNumber：话单文件话单张数。<br>- CDRFileSize：话单文件大小。<br>- CDRFileModifyTime：话单文件修改时间。<br>默认值：无<br>配置原则：无 |
| AUDITPARA3 | 话单稽核参数3 | 可选必选说明：可选参数<br>参数含义：配置话单稽核文件统计的稽核指标。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ParaNotNeed：不需要参数。<br>- CDRFileName：话单文件名。<br>- CDRNumber：话单文件话单张数。<br>- CDRFileSize：话单文件大小。<br>- CDRFileModifyTime：话单文件修改时间。<br>默认值：无<br>配置原则：无 |
| AUDITPARA4 | 话单稽核参数4 | 可选必选说明：可选参数<br>参数含义：配置话单稽核文件统计的稽核指标。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ParaNotNeed：不需要参数。<br>- CDRFileName：话单文件名。<br>- CDRNumber：话单文件话单张数。<br>- CDRFileSize：话单文件大小。<br>- CDRFileModifyTime：话单文件修改时间。<br>默认值：无<br>配置原则：无 |
| PARASEPARATOR | 稽核参数分隔符 | 可选必选说明：可选参数<br>参数含义：配置话单稽核参数之间的分隔符。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Space：空格。<br>- Semicolon：分号。<br>- VerticalLine：竖线。<br>默认值：无<br>配置原则：无 |
| GENINTERVAL | 稽核文件生成时间间隔（分） | 可选必选说明：可选参数<br>参数含义：配置话单稽核文件生成的间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1440，单位是分钟。<br>默认值：0<br>配置原则：<br>- 当取值为0时，表示每天的零点生成话单稽核文件。<br>- 当取值非0时，表示按指定的时间间隔生成话单稽核文件，同时每天的零点也会生成话单稽核文件。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRAUDIT]] · 话单稽核（CDRAUDIT）

## 使用实例

查询话单稽核任务：

```
LST CDRAUDIT:;
```

```
RETCODE = 0  操作成功。

结果如下:
---------
              稽核任务标识  =  audit
          接入网元分组标识  =  PS_GROUP_1
                    模块名  =  NULL
                  通道名称  =  All
话单稽核文件保存天数（天）  =  30
      话单稽核文件命名规则  =  %Y%m%d.log
              稽核内容格式  =  Txt格式
          是否汇总稽核信息  =  是
          是否添加文件抬头  =  是
             话单稽核参数1  =  话单文件名
             话单稽核参数2  =  话单文件话单张数
             话单稽核参数3  =  话单文件大小
             话单稽核参数4  =  话单文件修改时间
            稽核参数分隔符  =  空格
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话单稽核（LST-CDRAUDIT）_51174242.md`
