---
id: UNC@20.15.2@MMLCommand@RBK ACSPACKAGE
type: MMLCommand
name: RBK ACSPACKAGE（回退升级操作）
nf: UNC
version: 20.15.2
verb: RBK
object_keyword: ACSPACKAGE
command_category: 调测类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# RBK ACSPACKAGE（回退升级操作）

## 功能

![](回退升级操作（RBK ACSPACKAGE）_05338965.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会影响系统的正常启动和升级，请谨慎使用并联系华为支持协助操作。

该命令用于回退升级操作，当升级后的版本没有达到预期结果时，可使用该命令回退系统。

本命令只适用于ACS服务，其他微服务请使用RBK PACKAGE命令。

## 注意事项

- 该命令执行后立即生效。
- 系统只有升级过，才能执行该命令。
- 可以通过**DSP ACSRBKVER**，查询可回退版本。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RBKTYPE | 回退类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定回退类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LAST：上一个版本。<br>- BASESOFTWARE：基础版本。<br>- PATCH：补丁。<br>默认值：LAST |
| UPDOBJECT | 升级对象 | 可选必选说明：可选参数<br>参数含义：该参数用于指定升级对象。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BaseSoftware：只有基础版本。<br>- All：基础版本和补丁。<br>默认值：无 |
| BASICPKGVERSIONID | 基础软件包版本号 | 可选必选说明：条件必选参数，该参数在“UPDOBJECT”配置为“BaseSoftware” 或 “All”时为必选参数。<br>参数含义：该参数用于指定要加载的基础软件包版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| PATCHPKGVERSIONID | 补丁版本号 | 可选必选说明：条件必选参数，该参数在“UPDOBJECT”配置为“All”时为必选参数。<br>参数含义：该参数用于指定要加载的补丁版本。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| RBTMODE | 重启模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许的重启模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：不重启。<br>- SOFT：软重启，不需要重启虚拟机。<br>默认值：NO |

## 操作的配置对象

- [软件包（ACSPACKAGE）](configobject/UNC/20.15.2/ACSPACKAGE.md)

## 使用实例

回退升级操作：

```
RBK ACSPACKAGE:UPDOBJECT=All,BASICPKGVERSIONID="V100R005C00B020",PATCHPKGVERSIONID="SPH0001",RBKTYPE=BASESOFTWARE,RBTMODE=SOFT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/回退升级操作（RBK-ACSPACKAGE）_05338965.md`
