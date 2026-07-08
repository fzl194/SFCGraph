---
id: UNC@20.15.2@MMLCommand@CLR MSPROCESS
type: MMLCommand
name: CLR MSPROCESS（清除进程）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: MSPROCESS
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# CLR MSPROCESS（清除进程）

## 功能

![](清除进程（CLR MSPROCESS）_00520125.assets/notice_3.0-zh-cn_2.png)

注意：本命令属于高危命令，操作不当会误删除业务进程，请谨慎使用并联系华为技术支持协助操作。

该命令用于清除CMF管理的进程，当进程服务已经下线，但CMF无法感知进程已经不存在，则可使用该命令清除CMF中残留的数据。

## 注意事项

- 该命令执行后立即生效。

- 该命令仅供UDR/UDM/USC网元使用，其他网元请勿使用该命令。
- 在执行该命令前，管理员应明确该进程服务已下线，仍存在的进程，不应用此命令进行清除。
- 按进程ID清除时，若Pod中仅剩余该业务进程，为防止Pod空载，不允许清除。
- 按指定方式清除进程时，待清除的进程必须均为故障状态，否则不允许清除。
- 对于有多个CMF的系统，相同类型的进程被不同的CMF管理时，因状态同步到CMF中存在时间的先后，所以按进程名称清除进程时，存在只能清除部分进程的情况，可重新执行该命令进行清除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 清除方式 | 可选必选说明：必选参数<br>参数含义：该参数表示以何种方式清除进程。<br>数据来源：本端规划<br>取值范围：<br>- “BYNAME（进程名称）”：按进程名称清除。<br>- “BYID（进程ID）”：按进程ID清除。<br>- “BYLABEL（进程标签）”：按进程标签清除。<br>默认值：无<br>配置原则：无 |
| PROCESSID | 进程ID | 可选必选说明：该参数在"RANGE"配置为"BYID"时为条件必选参数。<br>参数含义：该参数表示进程的ID，可通过<br>[**DSP MSPROCESS**](显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| PROCESSNAME | 进程名称 | 可选必选说明：该参数在"RANGE"配置为"BYLABEL"、"BYNAME"时为条件必选参数。<br>参数含义：该参数表示进程名称，可通过<br>[**DSP MSPROCTYPE**](显示微服务进程类型（DSP MSPROCTYPE）_09587905.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| LABELKEY | 标签关键字 | 可选必选说明：该参数在"RANGE"配置为"BYLABEL"时为条件必选参数。<br>参数含义：该参数表示进程的标签关键字，可通过<br>[**DSP SERVICEINST**](显示注册的服务实例信息（DSP SERVICEINST）_01926552.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| LABELVALUE | 标签值 | 可选必选说明：该参数在"RANGE"配置为"BYLABEL"时为条件必选参数。<br>参数含义：该参数表示进程的标签值，可通过<br>[**DSP SERVICEINST**](显示注册的服务实例信息（DSP SERVICEINST）_01926552.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [复位微服务进程（MSPROCESS）](configobject/UNC/20.15.2/MSPROCESS.md)

## 使用实例

清除进程名称为CELL_UdrDsg的进程。

```
%%CLR MSPROCESS: RANGE=BYNAME, PROCESSNAME="CELL_UdrDsg";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除进程（CLR-MSPROCESS）_00520125.md`
