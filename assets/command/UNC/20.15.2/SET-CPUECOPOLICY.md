---
id: UNC@20.15.2@MMLCommand@SET CPUECOPOLICY
type: MMLCommand
name: SET CPUECOPOLICY（设置全局的CPU调频和休眠策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CPUECOPOLICY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- CPU节能策略
status: active
---

# SET CPUECOPOLICY（设置全局的CPU调频和休眠策略）

## 功能

使用虚拟机CPU节能功能时，通过此命令可以设置全局的虚拟机CPU调频和休眠策略：

- 虚拟机的CPU调频策略，是指允许虚拟机根据CPU核的负载状态自动地调节CPU核的运行频率，达到在低负载时节约能源的目的。
- 虚拟机的CPU休眠策略，是指当CPU核在较长时间（秒级）没有中断请求时，允许虚拟机进入休眠状态，以获得更多的节能效果。
  CPU休眠的深浅程度，表示CPU核参与休眠的部件范围大小，影响节能效果。是否支持休眠和参与休眠的部件范围与CPU类型和BIOS设置有关，休眠部件一般包括软件时钟、频率、缓存等。例如，ARM CPU不支持CPU休眠；X86 CPU支持浅休眠、深休眠；X86浅休眠主要包括软件时钟挂起/待机、降低倍频和电压，深休眠还包括清除L1/L2缓存等。一般来说，深休眠的节能效果比浅休眠好，不过CPU核从深休眠状态唤醒的所需时间要比浅休眠略长。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

- 虚拟机进入休眠降频后，CPU使用率可能会出现波动。
- 该命令执行后1分钟左右生效。
- 网元ID必须在系统中存在。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |
| IDLE_POLICY | CPU休眠策略 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定虚拟机的CPU休眠策略。<br>取值范围：<br>- “OFF(关闭)”：禁止CPU休眠。<br>- “SHALLOW(浅休眠)”：允许CPU浅休眠。<br>- “DEEP(深休眠)”：允许CPU深休眠。<br>默认值：无。<br>配置原则：若未配置<br>“CPU调频策略”<br>，则本参数必须配置。 |
| FREQ_POLICY | CPU调频策略 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定虚拟机的CPU调频策略。<br>取值范围：<br>- “OFF(关闭)”：禁止CPU调频。<br>- “ON(开启)”：允许CPU调频。<br>默认值：无。<br>配置原则：若未配置<br>“CPU休眠策略”<br>，则本参数必须配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CPUECOPOLICY]] · 全局的CPU调频和休眠策略（CPUECOPOLICY）

## 使用实例

设置 “网元ID” 为 “12” 的网元 “CPU休眠策略” 为 “深休眠” ， “CPU调频策略” 为 “开启” ：

```
%%SET CPUECOPOLICY: MEID=12, IDLE_POLICY=DEEP, FREQ_POLICY=ON;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CPUECOPOLICY.md`
