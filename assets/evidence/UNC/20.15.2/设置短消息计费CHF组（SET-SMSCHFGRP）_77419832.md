# 设置短消息计费CHF组（SET SMSCHFGRP）

- [命令功能](#ZH-CN_MMLREF_0000001977419832__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001977419832__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001977419832__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001977419832__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001977419832)

**适用NF：SMSF**

在SMSF/VLR短消息计费的场景下，通过本命令配置计费CHF组，SMSF/VLR从计费CHF组中选择可用的CHF进行计费处理。

## [注意事项](#ZH-CN_MMLREF_0000001977419832)

- 该命令执行后立即生效。

- 该命令参数输入空格或者null（不区分大小写）清空参数值。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PRIMARYCHFGRP | SECONDARYCHFGRP |
| --- | --- |
| null | null |

#### [操作用户权限](#ZH-CN_MMLREF_0000001977419832)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001977419832)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRIMARYCHFGRP | 主CHF组的名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置主CHF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSCHFGRP查询当前参数配置值。<br>配置原则：<br>该参数使用ADD TNFGRP命令配置生成。 |
| SECONDARYCHFGRP | 备CHF组的名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置备CHF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSCHFGRP查询当前参数配置值。<br>配置原则：<br>该参数使用ADD TNFGRP命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0000001977419832)

配置短消息计费的chf组主为“SMS CHF Group1”，备为“SMS CHF Group2”：

```
SET SMSCHFGRP: PRIMARYCHFGRP="SMS CHF Group1", SECONDARYCHFGRP="SMS CHF Group2";
```
