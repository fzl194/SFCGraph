---
id: UNC@20.15.2@MMLCommand@SET SOFTPARAEXP
type: MMLCommand
name: SET SOFTPARAEXP（设置软件参数配置导出模式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SOFTPARAEXP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 软件参数管理
- 软件参数配置导出
status: active
---

# SET SOFTPARAEXP（设置软件参数配置导出模式）

## 功能

**适用网元：SGSN、MME**

该命令用于控制软件参数导出。控制执行导出命令后，导出的MML配置文件中 [**SET SOFTPARA**](../软件参数/设置软件参数表(SET SOFTPARA)_26146182.md) 命令是包括全部软件参数值，还是只包括与系统初始默认值不一致的软件参数值。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXPORTTYPE | 软件参数导出模式 | 可选必选说明：可选参数<br>参数含义：控制导出的MML文件中，<br>[**SET SOFTPARA**](../软件参数/设置软件参数表(SET SOFTPARA)_26146182.md)<br>是包括全部软件参数值，还是只包括与系统初始值不一致的软件参数。<br>数据来源：整网规划<br>取值范围：枚举类型。<br>- “ALL_VALUE(全部软件参数值)”：执行导出命令，生成的mml文件中[**SET SOFTPARA**](../软件参数/设置软件参数表(SET SOFTPARA)_26146182.md)包括所有软参参数值。<br>- “NOT_INIT_VALUE(非缺省默认软件参数值)”：执行导出命令，生成的mml文件中[**SET SOFTPARA**](../软件参数/设置软件参数表(SET SOFTPARA)_26146182.md)只包括与系统初始值不同的软件参数值。<br>系统初始设置值：ALL_VALUE |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SOFTPARAEXP]] · 软件参数配置导出模式（SOFTPARAEXP）

## 使用实例

设置软件参数配置导出模式为 “非缺省默认软件参数值” ：

SET SOFTPARAEXP: EXPORTTYPE=NOT_INIT_VALUE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SOFTPARAEXP.md`
