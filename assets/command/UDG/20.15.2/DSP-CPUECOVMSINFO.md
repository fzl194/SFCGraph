---
id: UDG@20.15.2@MMLCommand@DSP CPUECOVMSINFO
type: MMLCommand
name: DSP CPUECOVMSINFO（显示VM的CPU节能策略）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CPUECOVMSINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- CPU节能策略
status: active
---

# DSP CPUECOVMSINFO（显示VM的CPU节能策略）

## 功能

该命令用于在开启节能策略后，查询当前VM的CPU节能策略。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

- 该命令执行后1分钟左右生效。
- 网元ID必须在系统中存在。
- 部分场景下，VM实际节能策略可能与网元期望策略不同。在已执行过[**SET CPUECOPOLICY**](设置全局的CPU调频和休眠策略（SET CPUECOPOLICY）_87832965.md)命令的场景，节能策略最长需要24小时可自动刷新为期望策略；如需快速生效，可通过重新执行[**SET CPUECOPOLICY**](设置全局的CPU调频和休眠策略（SET CPUECOPOLICY）_87832965.md)命令设置节能策略，使VM实际节能策略在2分钟内刷新为期望策略。如果未执行过[**SET CPUECOPOLICY**](设置全局的CPU调频和休眠策略（SET CPUECOPOLICY）_87832965.md)命令，则24小时定时更新策略不会启动。
- VNFD更新操作会将网元所有VM的实际节能策略恢复为VNFD模板定义的初始节能策略。
- 对VM进行强制重建、重建系统盘，会将该VM的实际节能策略恢复为VNFD模板定义的初始节能策略。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CPUECOVMSINFO]] · VM的CPU节能策略（CPUECOVMSINFO）

## 使用实例

查询网元ID为12的网元的VM节能策略。

```
%%DSP CPUECOVMSINFO: MEID=12;%%
RETCODE = 0  查询VM的CPU节能策略

进度报告
--------
已完成 = 0%
(结果个数 = 1)

---    END

%%DSP CPUECOVMSINFO: MEID=12;%%
RETCODE = 0  操作成功

操作结果如下
------------
虚拟机名称                     策略同步是否一致  CPU休眠策略期望值  CPU休眠策略实际值  CPU调频策略期望值  CPU调频策略实际值  

cscf_cpumml0709_SERVICE_VDU_0  是                深休眠             深休眠             开启               开启               
cscf_cpumml0709_SERVICE_VDU_1  是                深休眠             深休眠             开启               开启               
(结果个数 = 2)

共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示VM的CPU节能策略（DSP-CPUECOVMSINFO）_88024441.md`
