# 删除SMF信息（RMV SMFINFO）

- [命令功能](#ZH-CN_MMLREF_0209653154__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653154__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653154__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653154__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653154)

**适用NF：SMF**

该命令用以删除SMF实例信息。

## [注意事项](#ZH-CN_MMLREF_0209653154)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209653154)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653154)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMFINSTANCENAME | SMF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于在服务组（Service Group，简称SG）中唯一指定某个SMF实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，SMF_Instance_0。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653154)

删除当前配置的某SMF，其实例名称是SMF_Instance_0：

```
RMV SMFINFO: SMFINSTANCENAME="SMF_Instance_0";
```
