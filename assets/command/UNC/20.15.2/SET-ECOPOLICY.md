---
id: UNC@20.15.2@MMLCommand@SET ECOPOLICY
type: MMLCommand
name: SET ECOPOLICY（设置全局的CPU调频和休眠策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ECOPOLICY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- CPU节能策略
status: active
---

# SET ECOPOLICY（设置全局的CPU调频和休眠策略）

## 功能

使用虚拟机CPU节能功能时，通过此命令可以设置全局的虚拟机CPU调频和休眠策略。

虚拟机的CPU调频策略，是指允许虚拟机根据CPU核的负载状态自动地调节CPU核的运行频率，达到在低负载时节约能源的目的。

虚拟机的CPU休眠策略，是指当CPU核在较长时间（秒级）没有中断请求时，允许虚拟机进入休眠状态，以获得更多的节能效果。

CPU休眠的深浅程度，表示CPU核参与休眠的部件范围大小，影响节能效果。是否支持休眠和参与休眠的部件范围与CPU类型和BIOS设置有关，休眠部件一般包括软件时钟、频率、缓存等。例如，ARM CPU不支持CPU休眠；X86 CPU支持浅休眠、深休眠；X86浅休眠主要包括软件时钟挂起/待机、降低倍频和电压，深休眠还包括清除L1/L2缓存等。一般来说，深休眠的节能效果比浅休眠好，不过CPU核从深休眠状态唤醒的所需时间要比浅休眠略长。

## 注意事项

- 此命令执行后1分钟左右生效。

- 此命令仅在虚机场景下支持。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| IDLEPOLICY | FREQPOLICY |
| --- | --- |
| OFF | OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDLEPOLICY | CPU休眠策略 | 可选必选说明：必选参数<br>参数含义：该参数用于指定虚拟机的CPU休眠策略。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：禁止CPU休眠<br>- “SHALLOW（浅休眠）”：允许CPU浅休眠<br>- “DEEP（深休眠）”：允许CPU深休眠<br>默认值：无。<br>配置原则：无 |
| FREQPOLICY | CPU调频策略 | 可选必选说明：必选参数<br>参数含义：该参数用于指定虚拟机的CPU调频策略。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：禁止CPU调频<br>- “ON（开启）”：允许CPU调频<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ECOPOLICY]] · 全局的CPU调频和休眠策略（ECOPOLICY）

## 使用实例

设置CPU休眠策略为深休眠，调频策略为开启：

```
%%SET ECOPOLICY: IDLEPOLICY=DEEP, FREQPOLICY=ON;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-ECOPOLICY.md`
