---
id: UNC@20.15.2@MMLCommand@MOD DMRT
type: MMLCommand
name: MOD DMRT（修改Diameter域路由配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DMRT
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
- Diameter路由
status: active
---

# MOD DMRT（修改Diameter域路由配置）

## 功能

**适用网元：SGSN、MME**

该命令用于修改一条Diameter域路由配置数据。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令可修改Diameter域路由的“选路模式”、“路由名称”和“描述”的全部或部分信息，不能修改Diameter的“路由索引”。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter域路由索引。<br>数据来源：本端规划<br>取值范围：0~2047<br>默认值：无<br>说明：可以通过<br>[**LST DMRT**](查询Diameter域路由配置(LST DMRT)_72225969.md)<br>命令查看已有配置，确认所要修改的Diameter域路由的索引。 |
| RSELMODE | 选路模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域路由采用何种方式选择对端。<br>数据来源：本端规划<br>取值范围：<br>- “SELMODE_ROUND_ROBIN(轮选)”：表示存在多条链路集时，采用顺序选择的方式选取各条链路集。<br>- “SELMODE_MASTER_SLAVE(主从)”：表示1＋N备份模式。在这种模式中，域中仅有一个链路集处于激活状态，其余链路集则均处于备份状态。<br>- “SELMODE_ACTIVE(激活)”：表示使用上次使用的链路集。<br>- “SELMODE_PRIORITY_WEIGHT(优先级权重)”：表示存在多条链路集时，根据优先级和权重选取各条链路集。<br>- “SELMODE_IMSI_PRIORITY(IMSI指定优选)”：表示存在多条链路集时，根据路由组([**ADD DMRTGRP**](../Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md))指定的链路集和优先级选取各条链路集。<br>配置原则：<br>- 建议值为“SELMODE_ROUND_ROBIN(轮选)”。<br>- 当选路模式为SELMODE_IMSI_PRIORITY(IMSI指定优选)时，需要将域路由索引和需要使用的对端索引配置到路由组中。<br>说明：- 当参数设置为“SELMODE_PRIORITY_WEIGHT(优先级权重)”时，“基于权重/优先级的Diameter负荷分担”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-104404，License部件编码：LKV2DMLS01）。 |
| ROUTENAM | 路由名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定域路由的名称。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无<br>说明：- 一个域路由索引只有一个路由名称。<br>- 如果修改某一域路由索引下的路由名称时，该域路由索引下其他路由的路由名称都会被修改。 |
| PEERIDX | 对端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于标识目的对等端。<br>数据来源：整网规划<br>取值范围：0~639<br>默认值：无<br>说明：- 该参数无法修改DMRT中的对端实体索引。<br>- 该参数需要和“描述”参数联合使用，用于指定被修改的“描述”参数所在的记录。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Diameter域路由中对等端的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMRT]] · Diameter域路由配置（DMRT）

## 使用实例

将域路由表中索引号为0的域路由名称改为DIAM_ROUTNAM_NAME_TEST，选路模式改为主从，并且将该路由内，对端实体索引为0的记录的描述修改为ABC：

MOD DMRT: ROUTEIDX=0, RSELMODE=SELMODE_MASTER_SLAVE, ROUTENAM="DIAM_ROUTNAM_NAME_TEST", PEERIDX=0, DESC="ABC";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DMRT.md`
