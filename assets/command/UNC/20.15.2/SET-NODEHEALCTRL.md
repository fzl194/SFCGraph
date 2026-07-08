---
id: UNC@20.15.2@MMLCommand@SET NODEHEALCTRL
type: MMLCommand
name: SET NODEHEALCTRL（设置Node自愈策略控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NODEHEALCTRL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET NODEHEALCTRL（设置Node自愈策略控制参数）

## 功能

该命令用于设置Node自愈策略控制参数。

## 注意事项

- 该命令执行后立即生效。

- 该命令中部分功能在第三方CaaS场景下不可使用。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| BONDINGHEALSW | STGFAULTSWPSW | PODPRTUGDHLSW | PODALLUGDHLSW | TOPOCHECKHLSW | FABRICFAULTSW | NPLINKFAULTSW | VFFAULTHEALSW | OVERLOADHLSW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENABLE | ENABLE | DISABLE | ENABLE | ENABLE | DISABLE | DISABLE | ENABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BONDINGHEALSW | Bonding自愈控制 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SRIOV Bonding组网场景下出现物理网卡正常而上面的虚拟网卡异常而导致通信亚健康时，是否对Node进行复位自愈处理。<br>参数只在虚机场景下生效。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：去使能Node自愈<br>- “ENABLE（使能）”：使能Node自愈<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NODEHEALCTRL查询当前参数配置值。<br>配置原则：<br>此参数配置仅在SRIOV Bonding组网的虚机容器场景下才生效。 |
| STGFAULTSWPSW | 存储故障倒换开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示Node存储故障时，是否将此Node上OM主控倒换到存储正常的Node上。<br>参数只在虚机场景下生效。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：去使能存储故障倒换功能。<br>- “ENABLE（使能）”：使能存储故障倒换功能。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NODEHEALCTRL查询当前参数配置值。<br>配置原则：<br>为提高系统可靠性，此参数推荐配置为“ENABLE(使能)”。 |
| PODPRTUGDHLSW | 部分Pod故障升级自愈控制 | 可选必选说明：可选参数<br>参数含义：该参数用于表示Node中单个Pod或部分Pod故障时，并进行Pod重建无法修复时，是否需要将自愈升级到Node进行复位、重建、迁移处理。<br>参数只在虚机场景下生效。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：Node中单个Pod或部分Pod故障时，并进行Pod重建无法修复时，不作处理。<br>- “ENABLE（使能）”：Node中单个Pod或部分Pod故障时，并进行Pod重建无法修复时，将自愈升级到Node进行自愈处理。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NODEHEALCTRL查询当前参数配置值。<br>配置原则：<br>此功能不依赖于CSP自愈开关开启，如果SET NODEREPSWITCH关闭Node自愈功能，那么建议此功能也协同关闭；如果SET NODEREPSWITCH并未关闭Node自愈功能，那么客户根据自己实际需求选择开启或者关闭。<br>去使能升级Node自愈： Node中单个Pod或部分Pod故障时，并进行Pod重建无法修复时，不作处理。<br>使能升级Node自愈：Node中单个Pod或部分Pod故障时，并进行Pod重建无法修复时，将自愈升级到Node进行自愈处理。<br>该功能初始值为关闭。 |
| PODALLUGDHLSW | 全部Pod故障升级自愈控制 | 可选必选说明：可选参数<br>参数含义：该参数用于表示Node中所有Pod故障时，并进行Pod重建无法修复时，是否需要将自愈升级到Node进行复位、重建、迁移处理。裸机容器场景缺省关闭。<br>参数只在虚机场景下生效。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：Node中所有Pod故障时，并进行Pod重建无法修复时，不作处理。<br>- “ENABLE（使能）”：Node中所有Pod故障时，并进行Pod重建无法修复时，将自愈升级到Node进行自愈处理。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NODEHEALCTRL查询当前参数配置值。<br>配置原则：<br>此功能不依赖于CSP自愈开关开启，如果SET NODEREPSWITCH关闭Node自愈功能，那么建议此功能也协同关闭；如果SET NODEREPSWITCH并未关闭Node自愈功能，那么客户根据自己实际需求选择开启或者关闭。<br>去使能升级Node自愈：Node中所有Pod故障时，并进行Pod重建无法修复时，不作处理。<br>使能升级Node自愈：Node中所有Pod故障时，并进行Pod重建无法修复时，将自愈升级到Node进行自愈处理。<br>该功能初始值为开启。 |
| TOPOCHECKHLSW | Pod拓扑核查自愈控制 | 可选必选说明：可选参数<br>参数含义：该参数用于表示系统与MANO进行Pod拓扑核查时，当系统检测到MANO上存在拓扑信息，而系统本身长时间未实时生成拓扑信息时，是否触发针对Pod所在的Node进行复位、重建、迁移处理。<br>参数适用于虚机和裸机（包括三方CaaS）场景。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：当系统检测到MANO上存在拓扑信息，而系统本身长时间未实时生成拓扑信息时，不作处理。<br>- “ENABLE（使能）”：当系统检测到MANO上存在拓扑信息，而系统本身长时间未实时生成拓扑信息时，触发针对Pod所在Node的自愈处理。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NODEHEALCTRL查询当前参数配置值。<br>配置原则：<br>此功能不依赖于CSP自愈开关开启，如果SET NODEREPSWITCH关闭Node自愈功能，那么建议此功能也协同关闭；如果SET NODEREPSWITCH并未关闭Node自愈功能，那么客户根据自己实际需求选择开启或者关闭。<br>去使能Pod拓扑核查自愈：当系统检测到MANO上存在拓扑信息，而系统本身长时间未实时生成拓扑信息时，不作处理。<br>使能Pod拓扑核查自愈：当系统检测到MANO上存在拓扑信息，而系统本身长时间未实时生成拓扑信息时，触发针对Pod所在Node的自愈处理。<br>此功能的初始值为开启。 |
| FABRICFAULTSW | Fabric平面断隔离控制 | 可选必选说明：可选参数<br>参数含义：该参数用于表示Host间vFabric通信全断而vBase通信正常时，是否进行隔离处理。虚机场景：如果Host内vFabric通信也全断，则对Host内带有vFabric通信的Pod进行隔离处理。FusionStage裸机场景：对Host内带有vFabric通信的Pod进行隔离处理。<br>参数适用于虚机和裸机（包括三方CaaS）场景。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：Host间vFabric通信全断而vBase通信正常时，不进行隔离处理。<br>- “ENABLE（使能）”：Host间vFabric通信全断而vBase通信正常时，进行隔离处理。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NODEHEALCTRL查询当前参数配置值。<br>配置原则：<br>此功能仅限于普通框式服务器或UPF使用高密度框式服务器场景下使用。此功能的初始值为关闭。 |
| NPLINKFAULTSW | NP链路故障隔离控制 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当由于NP与交换芯片间的多链路故障导致Fabric通信亚健康时，是否对其影响的Host进行隔离处理。<br>参数仅适用于NP场景。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：不进行隔离处理<br>- “ENABLE（使能）”：进行隔离处理<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NODEHEALCTRL查询当前参数配置值。<br>配置原则：无 |
| VFFAULTHEALSW | VF故障隔离控制 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在SRIOV-Bonding场景下，当由于PF状态正常而VF状态故障导致的Fabric通信亚健康时，是否对其影响的Pod进行隔离处理。该参数默认打开，但功能不生效。<br>参数适用于虚机和裸机（包括三方CaaS）场景。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：不进行隔离处理<br>- “ENABLE（使能）”：进行隔离处理<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NODEHEALCTRL查询当前参数配置值。<br>配置原则：无 |
| OVERLOADHLSW | 存储过载自愈控制 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在容器存储驱动使用OverlayFS2，Pod存储过载导致Node存储过载时，是否对存储过载的Pod进行复位自愈。<br>参数只在虚机场景下生效。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：存储过载不会触发自愈<br>- “ENABLE（使能）”：存储过载会触发自愈<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NODEHEALCTRL查询当前参数配置值。<br>配置原则：<br>容器存储驱动使用OverlayFS2时建议手动打开。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NODEHEALCTRL]] · Node自愈策略控制参数（NODEHEALCTRL）

## 使用实例

SRIOV Bonding组网场景下去使能Node自愈。

```
SET NODEHEALCTRL: BONDINGHEALSW=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NODEHEALCTRL.md`
