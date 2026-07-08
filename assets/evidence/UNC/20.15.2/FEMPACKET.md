# 显示格式引擎配置信息（DSP FEMPACKET）

- [命令功能](#ZH-CN_CONCEPT_0251174306__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0251174306__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0251174306__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0251174306__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0251174306__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0251174306__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0251174306__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0251174306)

**适用NF：NCG**

该命令用于显示当前生效的格式引擎配置信息。该命令执行后，系统会查询当前生效的格式引擎信息，返回相应的格式引擎包文件名、通道信息和后存盘补丁名称。

在系统新安装、系统调测或者故障时，可以使用该命令进行检查。

#### [注意事项](#ZH-CN_CONCEPT_0251174306)

无。

#### [本地用户权限](#ZH-CN_CONCEPT_0251174306)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0251174306)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0251174306)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- “接入网元分组标识”可以通过[**LST CDRPROC**](../话单处理/查询话单处理（LST CDRPROC）_51174275.md)命令查询获取。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |

#### [使用实例](#ZH-CN_CONCEPT_0251174306)

显示格式引擎配置：

```
DSP FEMPACKET:;
```

```
RETCODE = 0  操作成功。

结果如下:
---------
接入网元分组标识    RU的ID    格式引擎包名               通道名称    源格式引擎配置包名称    格式引擎包版本     后存盘补丁名称    格式引擎包生成编译时间

PS1                 64        PS_R9_V940_NM_RT.tar.gz    egcdr       PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    gcdr        PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    ggsnmbms    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    gwmbms      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    lcsmocdr    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    lcsmtcdr    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    lcsnicdr    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    mcdr        PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    pgwcdr      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    scdr        PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    sgsnmbms    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    sgwcdr      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    smocdr      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS1                 64        PS_R9_V940_NM_RT.tar.gz    smtcdr      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    egcdr       PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    gcdr        PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    ggsnmbms    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    gwmbms      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    lcsmocdr    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    lcsmtcdr    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    lcsnicdr    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    mcdr        PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    pgwcdr      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    scdr        PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    sgsnmbms    PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    sgwcdr      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    smocdr      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
PS2                 65        PS_R9_V940_NM_RT.tar.gz    smtcdr      PS_R9_V940_NM_RT        V100R017C10B062    NULL              2017-01-14 11:13:34   
(结果个数 = 28)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0251174306)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 接入网元分组标识 | 用于区分不同域的接入网元。 |
| RU的ID | RU的ID。 |
| 通道名称 | 用于返回格式引擎配置包中所设置的通道名称。 |
| 源格式引擎配置包名称 | 用于返回查询到的格式引擎配置包名称的描述。 |
| 格式引擎包版本 | 用于返回查询到的格式引擎配置包的版本。 |
| 后存盘补丁名称 | 用于返回查询到的后存盘补丁的名称。 |
| 格式引擎包生成编译时间 | 用于返回查询到的格式引擎配置包的生成编译时间。 |

其余输出项请参见 [**ADD FMTPKGCFG**](增加格式引擎包软参（ADD FMTPKGCFG）_51174301.md) 的参数说明。
