# 设置漫游参数协商开关（SET HVNEGRCPSW）

- [命令功能](#ZH-CN_MMLREF_0000001870462621__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001870462621__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001870462621__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001870462621__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001870462621)

**适用NF：SMF**

该命令用于设置V-SMF和H-SMF之间是否进行Roaming Charging Profile的协商。

## [注意事项](#ZH-CN_MMLREF_0000001870462621)

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| VSMFSW | HSMFSW |
| --- | --- |
| ENABLE | ENABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0000001870462621)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001870462621)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VSMFSW | V-SMF漫游参数协商开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置V-SMF是否和H-SMF进行Roaming Charging Profile协商。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HVNEGRCPSW查询当前参数配置值。<br>配置原则：无 |
| HSMFSW | H-SMF漫游参数协商开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置H-SMF是否和V-SMF进行Roaming Charging Profile协商。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HVNEGRCPSW查询当前参数配置值。<br>配置原则：<br>该参数配置为DISABLE时，SET HSMFCHGCTRL中LOCALRCPSELMODE功能不生效。 |

## [使用实例](#ZH-CN_MMLREF_0000001870462621)

设置漫游参数协商开关：

```
SET HVNEGRCPSW: VSMFSW=DISABLE, HSMFSW=DISABLE;
```
