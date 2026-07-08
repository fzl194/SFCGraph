---
id: UNC@20.15.2@MMLCommand@SYN FMTPKG
type: MMLCommand
name: SYN FMTPKG（同步格式引擎包）
nf: UNC
version: 20.15.2
verb: SYN
object_keyword: FMTPKG
command_category: 动作类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 格式引擎包
status: active
---

# SYN FMTPKG（同步格式引擎包）

## 功能

![](同步格式引擎包（SYN FMTPKG）_51174304.assets/notice_3.0-zh-cn_2.png)

此命令会覆盖目的地的文件，使用此命令正向同步时（即选择参数“REVSYN”为“NO”时），需要执行“RST VNFC”重启服务才能使格式引擎包生效。

**适用NF：NCG**

该命令用于从工作区目录获取格式引擎包或者向工作区目录同步格式引擎包。

## 注意事项

- 该命令执行后立即生效。
- 使用此命令正向同步时（即选择参数“REVSYN”为“NO”时），需要执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”重启服务才能使格式引擎包生效。
- 使用此命令反向同步时（即选择参数“REVSYN”为“YES”时），被同步的格式引擎包在OM Portal文件传输服务下的NCG话单格式引擎库目录中文件名会有“export_”前缀。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRFNAME | 格式引擎包名 | 可选必选说明：必选参数<br>参数含义：用于返回查询到的格式引擎配置包名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：<br>- 格式引擎包文件全名，包括后缀名。例如，“PS_R9_V940_NM_RT.tar.gz”。<br>- 不同的局点话单处理规则不同，需要根据实际情况配置相应的格式引擎包。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| REVSYN | 是否反向同步 | 可选必选说明：必选参数<br>参数含义：该参数用于确定是否将格式引擎包同步到OM Portal文件传输服务下的NCG话单格式引擎库目录。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：YES<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@FMTPKG]] · 同步格式引擎包（FMTPKG）

## 使用实例

将格式引擎包同步到工作区目录，采用的格式引擎包为“PS_R9_V940_NM_RT.tar.gz”，示例如下：

```
SYN FMTPKG: PRFNAME="PS_R9_V940_NM_RT.tar.gz", REVSYN=NO;
```

将格式引擎包同步到OM Portal文件传输服务下的NCG话单格式引擎库目录，采用的格式引擎包为“PS_R9_V940_NM_RT.tar.gz”，示例如下：

```
SYN FMTPKG: PRFNAME="PS_R9_V940_NM_RT.tar.gz", REVSYN=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SYN-FMTPKG.md`
