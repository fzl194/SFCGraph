---
id: UNC@20.15.2@MMLCommand@MOD DMHOSTRT
type: MMLCommand
name: MOD DMHOSTRT（修改Diameter主机路由）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DMHOSTRT
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
- 信令传输管理
- Diameter管理
- Diameter主机路由
status: active
---

# MOD DMHOSTRT（修改Diameter主机路由）

## 功能

**适用网元：SGSN、MME**

该命令用于修改一条Diameter主机路由的路由名称，优先级和权重。

## 注意事项

- 该命令执行后立即生效。
- 不能修改选路模式。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter主机路由索引。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无<br>说明：可以通过<br>[**LST DMHOSTRT**](查询Diameter主机路由(LST DMHOSTRT)_72345873.md)<br>命令查看已有配置，确认所要修改的Diameter主机路由的索引。 |
| RSELMODE | 选路模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定主机路由选择对端的模式。<br>数据来源：整网规划<br>取值范围：<br>- “SELMODE_ROUND_ROBIN(轮选)”：当同一Diameter路由组存在多条Diameter主机路由时，采用顺序选择的方式选择主机路由。这种选路模式在负荷分担场景时使用。<br>- “SELMODE_MASTER_SLAVE(主从)”：当同一Diameter路由组存在多条Diameter主机路由时，采用主从选择的方式选择主机路由。主从关系根据配置的优先级来确定，参见PRIORITY参数。这种选路模式在主备场景时使用。<br>- “SELMODE_PRIORITY_WEIGHT(优先级权重)”：表示同一Diameter路由组存在多条Diameter主机路由时，先根据优先级选择主机路由，优先级相同时，再根据权重选择主机路由。 这种选路模式用于对端设备支持不同的接入能力时，通过指定不同的权重来使得能力较强的设备可以处理更多的消息。通过指定优先级可将设备根据优先级分组，支持复杂的负载分担方式。<br>默认值：无<br>配置原则：该参数不能修改。<br>说明：- 同一路由组索引下主机路由的选路模式必须相同。在“MML命令行-UNC”窗口上执行命令[**LST DMRTGRP**](../Diameter路由组/查询Diameter路由组(LST DMRTGRP)_26306104.md)查询路由组配置。<br>- 当参数设置为“SELMODE_PRIORITY_WEIGHT(优先级权重)”时，“基于权重/优先级的Diameter负荷分担”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-104404，License部件编码：LKV2DMLS01）。 |
| ROUTENAM | 路由名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定修改路由的名称。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于修改主机路由中对端的优先级。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>说明：- 该参数在“选路模式”设置为“SELMODE_MASTER_SLAVE(主从)”时和“SELMODE_PRIORITY_WEIGHT(优先级权重)”有效。<br>- 当“选路模式”设置为“SELMODE_MASTER_SLAVE(主从)”时，同一路由组索引中主机路由的优先级不能相同。在“MML命令行-UNC”窗口上执行命令[**LST DMRTGRP**](../Diameter路由组/查询Diameter路由组(LST DMRTGRP)_26306104.md)查询路由组配置。<br>- 数值越小，优先级越高。 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于修改主机路由中对端的权重。<br>数据来源：整网规划<br>取值范围：1～255<br>默认值：无<br>说明：- 该参数只在“选路模式”设置为“SELMODE_PRIORITY_WEIGHT(优先级权重)”有效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMHOSTRT]] · Diameter主机路由（DMHOSTRT）

## 使用实例

将主机路由表中索引号为2的路由名称改为dra，选路模式为主从的优先级改为1：

MOD DMHOSTRT: ROUTEIDX=2, RSELMODE=SELMODE_MASTER_SLAVE, ROUTENAM="dra", PRIORITY=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DMHOSTRT.md`
