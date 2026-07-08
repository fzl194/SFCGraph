---
id: UNC@20.15.2@MMLCommand@RMV MSCONTEXTS
type: MMLCommand
name: RMV MSCONTEXTS（删除所有MS上下文信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MSCONTEXTS
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- MS上下文管理
- 基本MS上下文管理
status: active
---

# RMV MSCONTEXTS（删除所有MS上下文信息）

## 功能

![](删除所有MS上下文信息(RMV MSCONTEXTS)_72225699.assets/notice_3.0-zh-cn_2.png)

删除所有MS上下文信息会中断所有相关用户的服务，并且导致非预期流程。

**适用网元：SGSN**

该命令用于删除一个GBP进程上的所有MS上下文。

## 注意事项

- 该命令执行立即生效。
- 该命令执行后，对应进程上的所有2G用户业务都受损，请谨慎使用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划。<br>取值范围：0~63 位字符串<br>默认值：无 |
| PRONO | 进程号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GBP进程所在的进程号。<br>取值范围：0～20<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSCONTEXTS]] · 所有MS上下文信息（MSCONTEXTS）

## 使用实例

删除USN_SP_RU_0064上的GBP进程上所有的MS上下文：

RMV MSCONTEXTS:RUNAME="USN_SP_RU_0064", PRONO=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除所有MS上下文信息(RMV-MSCONTEXTS)_72225699.md`
