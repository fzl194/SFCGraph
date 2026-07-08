---
id: UNC@20.15.2@MMLCommand@MOD S1PAGINGRULE
type: MMLCommand
name: MOD S1PAGINGRULE（修改S1寻呼规则）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: S1PAGINGRULE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1寻呼规则管理
status: active
---

# MOD S1PAGINGRULE（修改S1寻呼规则）

## 功能

**适用网元：MME**

此命令用于修改S1寻呼规则。通过此命令可以修改指定S1寻呼规则的 “匹配优先级” 、 “寻呼动作组合” 和 “规则描述” 。

## 注意事项

- 此命令执行后立即生效。
- 此配置涉及LTE精准寻呼特性（特性编号：WSFD-206001，License部件编码：LKV2PRPG02），执行命令请使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RECID | 规则索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待修改的S1寻呼规则的索引。<br>取值范围：1～1001<br>默认值：无<br>说明：当执行<br>[**ADD S1PAGINGRULE**](增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md)<br>命令增加S1寻呼规则时，系统会自动为该规则分配一个1～1001之间未使用的最小的索引，以唯一的标识该S1寻呼规则。可以通过<br>[**LST S1PAGINGRULE**](查询S1寻呼规则(LST S1PAGINGRULE)_72225927.md)<br>命令查询系统分配的索引值。 |
| PRIORITY | 匹配优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼规则的匹配优先级。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>配置原则：优先级数值越小，代表优先级越高。0～255优先级逐渐降低<br>说明：在业务匹配多条寻呼规则的场景下，优先级高的寻呼规则优先匹配。 |
| ACTGRP | 寻呼动作组合 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼规则使用的寻呼动作组合。<br>数据来源：整网规划<br>取值范围：<br>- LAST_ENODEB(最近访问eNodeB)<br>- NEIGH_ENODEB(邻接eNodeB)<br>- LAST_TAI(最近访问TA)<br>默认值：无<br>说明：- 若都不选择，缺省使用TA List的寻呼。寻呼范围有最近访问eNodeB，邻接eNodeB，最近访问TA和TA List。TA List是缺省的寻呼范围，不允许通过本命令修改。<br>- 当通过本命令选择了多种不同的寻呼范围时，优先级按如下的顺序依次降低：最近访问eNodeB，邻接eNodeB，最近访问TA，TA List。 |
| DESC | 规则描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼规则的描述信息。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1PAGINGRULE]] · S1寻呼规则（S1PAGINGRULE）

## 使用实例

修改 “规则索引” 为 “1” 的S1寻呼规则，将该S1寻呼规则的 “匹配优先级” 修改为 “100” ， “寻呼动作组合” 修改为 “LAST_ENODEB(最近访问eNodeB)” ：

```
MOD S1PAGINGRULE: RECID=1, PRIORITY=100, ACTGRP=LAST_ENODEB-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-S1PAGINGRULE.md`
