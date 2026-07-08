---
id: UNC@20.15.2@MMLCommand@LST FMTPKGCFG
type: MMLCommand
name: LST FMTPKGCFG（查询格式引擎软参配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FMTPKGCFG
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

# LST FMTPKGCFG（查询格式引擎软参配置信息）

## 功能

**适用NF：NCG**

该命令用于查询格式引擎包中的软参配置信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRFNAME | 格式引擎包名 | 可选必选说明：可选参数<br>参数含义：用于返回查询到的格式引擎配置包名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FMTPKGCFG]] · 格式引擎包软参（FMTPKGCFG）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询格式引擎软参配置信息（LST-FMTPKGCFG）_51174303.md`
