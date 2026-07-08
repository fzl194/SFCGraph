# 删除5GC QoS控制动作配置（RMV 5GCQOSACTION）

- [命令功能](#ZH-CN_MMLREF_0209652131__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652131__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652131__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652131__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652131)

**适用NF：SMF**

该命令用于删除5G用户QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

## [注意事项](#ZH-CN_MMLREF_0209652131)

命令执行后只对新接入用户生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652131)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652131)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| FIVEQI | 5QI值 | 可选必选说明：必选参数<br>参数含义：该参数表示5G QoS identifier。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652131)

删除QoS Profile名称为“test”的5GC QoS Action配置，5QI值为2：

```
RMV 5GCQOSACTION:QOSPROFILENAME="test",FIVEQI=2;
```
