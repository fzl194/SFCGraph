---
id: UNC@20.15.2@MMLCommand@DSP FMTSOFTPARA
type: MMLCommand
name: DSP FMTSOFTPARA（查询格式引擎包所有可配置软参）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FMTSOFTPARA
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
- 格式引擎包
status: active
---

# DSP FMTSOFTPARA（查询格式引擎包所有可配置软参）

## 功能

**适用NF：NCG**

该命令用于查询格式引擎包中所有可配置软参的描述信息。

## 注意事项

当前正在使用的格式引擎包可以使用 [**LST CDRPROC**](../话单处理/查询话单处理（LST CDRPROC）_51174275.md) 命令查询。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRFNAME | 格式引擎包名 | 可选必选说明：必选参数<br>参数含义：用于返回查询到的格式引擎配置包名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：<br>- 格式引擎包文件全名，包括后缀名。例如，“PS_R9_V940_M_RT.tar.gz”。<br>- 不同的局点话单处理规则不同，需要根据实际情况配置相应的格式引擎包。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |

## 操作的配置对象

- [格式引擎包所有可配置软参（FMTSOFTPARA）](configobject/UNC/20.15.2/FMTSOFTPARA.md)

## 使用实例

查询指定的格式引擎包中所有可配置软参情况：

```
DSP FMTSOFTPARA: PRFNAME="PS_R9_V940_M_RT.tar.gz";
```

```
RETCODE = 0  操作成功

结果如下:
---------
格式引擎包名              格式引擎包软参名称    格式引擎包软参类型    格式引擎包软参取值范围    格式引擎包软参描述    

PS_R9_V940_M_RT.tar.gz    MaxDuration           Integer               [0,10800]                 CG话单最大超时时长，默认值为10800
PS_R9_V940_M_RT.tar.gz    MaxVolume             Integer               [0,1048576]               CG话单最大流量，默认值为1048576
PS_R9_V940_M_RT.tar.gz    MergeCDRNum           Integer               [0,64]                    CG部分话单合并张数阈值，默认值为5
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询格式引擎包所有可配置软参（DSP-FMTSOFTPARA）_51174305.md`
