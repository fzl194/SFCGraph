---
id: UNC@20.15.2@MMLCommand@SET HTR
type: MMLCommand
name: SET HTR（设置HTR功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HTR
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- HTR流控局向管理
- Gr HTR流控局向管理
- 流控功能管理
status: active
---

# SET HTR（设置HTR功能）

## 功能

**适用网元：SGSN**

此命令用于设置HTR（Hard to Reach）流控功能的相关参数。当Gr或者Ge口出现拥塞时需要进行流控。

Gr口拥塞的表现和控制场景：

- 场景1：SGSN与HLR之间直连链路拥塞，此时进行自动启控。
- 场景2：HLR过载，此时进行手工启控。
- 场景3：STP到HLR链路拥塞，此时进行手工启控。
- 场景4：STP过载，此时进行手工启控。
- 场景5：SGSN与STP之间直连链路拥塞，此时进行自动启控。

HTR功能提供如下配置功能：

- 运营商可以通过调整HTR流控启动阈值决定低于什么样的成功率启动HTR流控，通过调整HTR流控恢复阈值决定流控目标成功率。
- 在非SGSN直连链路拥塞场景下如果要进行HTR流控可以打开HTR功能手工开关。
- HTR流控的对象可以使用配置的HTR局向（使用命令[**ADD HTROFC**](../配置局向/增加HTR局向(ADD HTROFC)_72345753.md)）也可以使用系统自动生成的HTR局向，HTR功能手工开关关闭时必须使用系统自动生成局向，HTR功能手工开关打开时可以使用配置局向或系统自动生成局向，但不能既使用配置局向又使用系统自动生成局向。自动生成的局向是指SGSN通过SCCP GT翻译后获取的局向，例如，如果SGSN通过STP和多个HLR连接，而STP采用GT寻址转发消息则自动局向只能生成到STP的局向，通过配置局向可以精确到每个HLR，流控对象更准确，流控效果会更好。
- HTR流控功能同时适用于Gr和Ge接口，Ge接口不支持运营商配置HTR局向，即不支持命令[**ADD HTROFC**](../配置局向/增加HTR局向(ADD HTROFC)_72345753.md)配置Ge接口的HTR局向。
- 只有在直连场景下，HTR流控功能才适用于Ge接口。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HTRSWITCH | HTR功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置HTR功能开关。开启本开关是进行流控的必要条件。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”：HTR流控功能打开。<br>- “NO(否)”：HTR流控功能关闭。<br>系统初始设置值：<br>“YES(是)” |
| HTRMANUALSWITCH | HTR功能手工开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置HTR功能手工开关。默认的流控（即自动流控）针对直连链路拥塞场景，其他场景需要手工打开本参数开关强制进行流控，此时HTR流控起控条件不需要判断“直连链路拥塞”条件。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”：打开该开关，HTR启控不再需要“直连链路拥塞”条件。<br>- “NO(否)”：关闭该开关，HTR启控需要“直连链路拥塞”条件。<br>系统初始设置值：<br>“YES(是)” |
| HTRTARGETDELAY | 流控目标时延 | 可选必选说明：可选参数<br>参数含义：保留参数，不建议自行配置。<br>取值范围：500~4500<br>系统初始设置值：<br>“1500” |
| HTRCONFIGOFCSWITCH | HTR配置局向是否生效 | 可选必选说明：可选参数<br>参数含义：该参数用于设置HTR配置局向是否生效。确定HTR流控的对象是使用命令<br>[**ADD HTROFC**](../配置局向/增加HTR局向(ADD HTROFC)_72345753.md)<br>配置的HTR局向还是系统检测到的局向。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”：HTR配置局向生效。<br>- “NO(否)”：HTR配置局向不生效。<br>系统初始设置值：<br>“NO(否)” |
| HTRFAILPERCENT | HTR流控启动阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置HTR流控启动阈值。当MAP-TCAP Interface层会话响应成功率低于该参数时，才可以进行流控。<br>数据来源：整网规划<br>取值范围：0~100<br>系统初始设置值：<br>“65”<br>配置原则：<br>- MAP-TCAP Interface层会话响应成功率低于该参数是启动流控的必需条件之一。 |
| HTRSUCCPERCENT | HTR流控恢复阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置HTR流控恢复阈值。当MAP-TCAP Interface层会话响应成功率高于该参数时，才可以解除流控。<br>数据来源：整网规划<br>取值范围：0~100，该参数的值必须大于<br>“HTRFAILPERCENT”<br>。<br>系统初始设置值：<br>“85”<br>配置原则：<br>- MAP-TCAP Interface层会话响应成功率高于该参数是解除流控的必需条件之一。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTR]] · HTR功能（HTR）

## 使用实例

设置记录，设置 “HTR功能开关” 为 “YES” ， “HTR功能手工开关” 为 “YES” ， “HTR流控启动阈值” 为 “40” ， “HTR流控恢复阈值” 为 “90” ：

SET HTR: HTRSWITCH=YES, HTRMANUALSWITCH=YES, HTRFAILPERCENT=40, HTRSUCCPERCENT=90;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-HTR.md`
