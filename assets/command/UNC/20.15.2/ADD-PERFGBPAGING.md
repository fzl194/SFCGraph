---
id: UNC@20.15.2@MMLCommand@ADD PERFGBPAGING
type: MMLCommand
name: ADD PERFGBPAGING（增加Gb接口寻呼数据）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PERFGBPAGING
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能对象管理
status: active
---

# ADD PERFGBPAGING（增加Gb接口寻呼数据）

## 功能

**适用网元：SGSN**

该命令用于增加2G寻呼配置参数，用于Gb模式路由区号话统上报的对象。指定路由区Gb模式附着流程，指定路由区Gb模式分离流程测量，指定路由区Gb模式SGSN内路由跟新，指定路由区Gb模式SGSN间路由更新，指定路由区Gb模式分组寻呼，指定路由区Gb模式无线资源，指定路由区Gb模式会话资源，路由区2G会话业务测量和Gb MOCN模式下基本流程测量话统测量单元下的指标上报时必需知道所要上报的LAI和RAC，否则无法上报。因此，需要通过该命令手动增加动态上报的LAI和RAC。

## 注意事项

- 此命令执行后立即生效。
- 此命令的最大记录数是10000。

- 用户在执行[**ADD PERFGBPAGING**](增加Gb接口寻呼数据(ADD PERFGBPAGING)_26306002.md)的时候必需先使用[**LST GBPAGING**](../../../Gb接口管理/Gb接口寻呼数据/查询Gb接口寻呼数据(LST GBPAGING)_26146008.md)查询所有需要处理的LAI和RAC。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | 寻呼范围位置区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由区所在的位置区标识，与RAC共同构成路由区标识。LAI = MNC + MCC + LAC。<br>数据来源：整网规划<br>取值范围：9~10位十六进制数<br>默认值：无 |
| RAC | 寻呼范围路由区编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由区在位置区内的标识，与LAI共同构成路由区标识。<br>数据来源：整网规划<br>取值范围：0x00~0xFF<br>默认值：无<br>说明：RAC是十六进制数，占1个字节。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFGBPAGING]] · Gb接口寻呼数据（PERFGBPAGING）

## 使用实例

增加待处理的2G寻呼配置参数：

ADD PERFGBPAGING: LAI="123031111",RAC="08";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PERFGBPAGING.md`
