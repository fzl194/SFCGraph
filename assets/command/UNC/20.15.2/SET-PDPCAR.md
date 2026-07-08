---
id: UNC@20.15.2@MMLCommand@SET PDPCAR
type: MMLCommand
name: SET PDPCAR（设置PDP流控参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PDPCAR
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- 转发资源管理
- PDP资源管理
- PDP流控参数管理
status: active
---

# SET PDPCAR（设置PDP流控参数）

## 功能

**适用网元：SGSN**

该命令用于设置PDP上下文的流控参数。PDP流控包括上行数据流控和下行数据流控。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 动态修改该命令的“PDP流控倍数”、“PDP突发系数”只对以后创建的PDP上下文有效，对原来已存在的PDP上下文无效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PDPSWITCH | PDP流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用来表示PDP流控控制开关。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关)”<br>- “ON(开)”<br>系统初始设置值：<br>“ON(开)”<br>。<br>配置原则：<br>- 如果开关关闭，不进行PDP流控，即单用户不会限制上下行带宽。<br>- 如果开关打开，单用户会按照协商带宽进行流控。<br>- 动态修改该命令的“PDP流控开关”参数，对所有PDP上下文立即生效。 |
| PDPMULTI | PDP流控倍数 | 可选必选说明：条件可选参数<br>参数含义：该参数用来表示PDP流控实际使用的带宽相对协商带宽的倍数。将QoS协商后的最大带宽乘以<br>“PDP流控倍数”<br>即可得到PDP流控实际使用的最大带宽。<br>“PDP流控倍数”<br>越大，则PDP流控实际使用的最大带宽越大。<br>前提条件：该参数在<br>“PDP流控开关”<br>参数设置为<br>“ON(开)”<br>时，需要配置。<br>数据来源：本端规划<br>取值范围：1~127<br>系统初始设置值：<br>“1”<br>。<br>配置原则：PDP流控一般按照用户QoS协商后的最大带宽来进行，不建议放大其最大带宽，所以系统初始值为<br>“1”<br>。 |
| BURSTTIMES | PDP突发系数 | 可选必选说明：可选参数<br>参数含义：该参数用来表示PDP流控时对突发速率的容忍度。<br>“PDP突发系数”<br>越大，对于突发速率的容忍度越高。<br>数据来源：本端规划<br>取值范围：1~64<br>系统初始设置值：<br>“9”<br>。<br>配置原则：该参数为系统参数，如果设置过大，当大量用户同一时间段内均有较大突发流量时，会造成系统带宽拥塞。根据当前系统转发能力，设置初始值为<br>“9”<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDPCAR]] · PDP流控参数（PDPCAR）

## 使用实例

设置PDP流量控制参数，打开PDP流控控制开关，其他参数选默认值:

SET PDPCAR: PDPSWITCH=ON, PDPMULTI=1, BURSTTIMES=9;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置PDP流控参数(SET-PDPCAR)_72345451.md`
