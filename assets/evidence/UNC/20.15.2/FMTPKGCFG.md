# 查询格式引擎软参配置信息（LST FMTPKGCFG）

- [命令功能](#ZH-CN_CONCEPT_0251174303__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0251174303__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0251174303__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0251174303__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0251174303__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0251174303__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0251174303__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0251174303)

**适用NF：NCG**

该命令用于查询格式引擎包中的软参配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0251174303)

无。

#### [本地用户权限](#ZH-CN_CONCEPT_0251174303)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0251174303)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0251174303)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRFNAME | 格式引擎包名 | 可选必选说明：可选参数<br>参数含义：用于返回查询到的格式引擎配置包名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0251174303)

查询指定的格式引擎软参配置情况：

```
LST FMTPKGCFG: PRFNAME="PS_R9_V940_M_RT.tar.gz";
```

```
RETCODE = 0  操作成功。

结果如下:
---------
格式引擎包名              格式引擎包软参名称    格式引擎软参类型 格式引擎软参值

PS_R9_V940_M_RT.tar.gz    MaxDuration           FEM_PARA_ENUM    0             
PS_R9_V940_M_RT.tar.gz    MaxVolume             FEM_PARA_UINT    0             
PS_R9_V940_M_RT.tar.gz    MergeCDRNum           FEM_PARA_UINT    0             
(结果个数 = 3)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0251174303)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 格式引擎软参值 | 格式引擎软参值。 |

其余输出项请参见 [**ADD FMTPKGCFG**](增加格式引擎包软参（ADD FMTPKGCFG）_51174301.md) 的参数说明。
