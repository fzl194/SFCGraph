# 设置NSSF流控开关（SET NSSFFCSWITCH）

- [命令功能](#ZH-CN_MMLREF_0244007994__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0244007994__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0244007994__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0244007994__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0244007994)

**适用NF：NSSF**

该命令用于设置NSSF流控开关状态。

## [注意事项](#ZH-CN_MMLREF_0244007994)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NSSFFCSWITCH |
| --- |
| FUNC_ON |

#### [操作用户权限](#ZH-CN_MMLREF_0244007994)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0244007994)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSSFFCSWITCH | NSSF流控开关 | 可选必选说明：必选参数<br>参数含义：该参数表示NSSF流控开关状态。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0244007994)

当运营商希望使用NSSF的自保流控功能时，需要通过该命令打开NSSF的流控开关：

```
SET NSSFFCSWITCH: NSSFFCSWITCH=FUNC_ON;
```
