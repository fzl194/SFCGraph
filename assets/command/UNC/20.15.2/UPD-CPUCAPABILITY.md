---
id: UNC@20.15.2@MMLCommand@UPD CPUCAPABILITY
type: MMLCommand
name: UPD CPUCAPABILITY（更新CPU能力基线）
nf: UNC
version: 20.15.2
verb: UPD
object_keyword: CPUCAPABILITY
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务维护功能管理
- 操作维护
- 系统调测
- CPU能力基线信息
status: active
---

# UPD CPUCAPABILITY（更新CPU能力基线）

## 功能

该命令用于更新指定CPU信息所对应的能力基线值，指定CPU信息包含CPU类型、CPU代数以及CPU主频率。

## 注意事项

CPU类型、CPU代数以及CPU主频这三者的值会确定记录的唯一性，因此执行该命令前确保已存在指定的CPU信息记录，否则更新会失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPUTYPE | CPU类型 | 可选必选说明：必选参数。<br>参数含义：该参数表示CPU类型。当前只支持CPU的类型为x86_64和aarch64，其x86_64为X86机器使用的CPU类型，aarch64为ARM机器使用的CPU类型。<br>数据来源：本端规划。<br>取值范围：<br>- “x86_64(x86_64) ”<br>- “aarch64(aarch64) ”<br>默认值：无 |
| CPUVERSION | CPU代数 | 可选必选说明：必选参数<br>参数含义：该参数表示CPU代数。<br>数据来源：本端规划<br>取值范围：字符串形式，区分大小写，字符串长度为1～63。<br>默认值：无 |
| CPUFREQUENCY | CPU主频 | 可选必选说明：必选参数<br>参数含义：该参数表示CPU主频率。<br>数据来源：本端规划<br>取值范围：整形数值，范围0~65536。<br>默认值：无 |
| CAPABILITY | 能力基线 | 可选必选说明：必选参数<br>参数含义：该参数表示CPU对应的能力基线值，能力基线值越大，代表CPU运算能力越大，可承载的业务量越多，反之越小。<br>数据来源：本端规划<br>取值范围：整形数值，范围0~65536。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。该参数不能取值为VNFP、ACS、VNRS_VNFC的服务实例名称。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CPUCAPABILITY]] · CPU能力基线（CPUCAPABILITY）

## 使用实例

更新CPU类型、主频、代数分别为x86_64、2100MHz、E5-2690所对应的能力基线值为1100的记录，执行以下命令：

UPD CPUCAPABILITY: CPUTYPE=x86_64, CPUVERSION="E5-2690", CPUFREQUENCY=2100, CAPABILITY=1100 ,SERVICEINSTANCE=" vnfc " ;

## 证据

- 原始手册：`evidence/UNC/20.15.2/UPD-CPUCAPABILITY.md`
