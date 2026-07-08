---
id: UNC@20.15.2@MMLCommand@RMV ALGPRIORITY
type: MMLCommand
name: RMV ALGPRIORITY（删除算法优先级配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ALGPRIORITY
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- Iu模式用户安全参数
status: active
---

# RMV ALGPRIORITY（删除算法优先级配置信息）

## 功能

**适用网元：SGSN**

该命令用于删除算法优先级的信息。

## 注意事项

- 该命令执行后立即生效。
- 删除某算法优先级后，如果SGSN还配有其他算法优先级，则以其他算法中优先级最高的算法为准；如果所有算法均未设置优先级，则随机排序。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGTYPE | 算法类型 | 可选必选说明：必选参数<br>参数含义：该参数于指定对何种算法设置优先级。目前有加密算法和完整性算法两种类型。<br>取值范围：<br>- “CIPH(UMTS加密算法)”<br>- “INTE(UMTS完整性算法)”<br>默认值：无 |
| ALGCIPH | 加密算法 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定加密算法的类型。加密算法是用来保密用户身份，用户数据及信令通道。<br>前提条件：该参数在<br>“ALGTYPE（算法类型）”<br>设置为<br>“CIPH（UMTS加密算法）”<br>时生效。<br>取值范围：<br>- “NOCIPH(不加密)”<br>- “UEA1(UEA1)”<br>- “UEA2(UEA2)”<br>默认值：无 |
| ALGINTE | 完整性算法 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定完整性算法类型，只在IU模式下使用。完整性算法是用来保证信令源鉴权数据的完整性。<br>前提条件：该参数在<br>“ALGTYPE（算法类型）”<br>设置为<br>“INTE（UMTS完整性算法）”<br>时生效。<br>取值范围：<br>- “UIA1(UIA1)”<br>- “UIA2(UIA2)”<br>默认值：无 |

## 操作的配置对象

- [算法优先级配置信息（ALGPRIORITY）](configobject/UNC/20.15.2/ALGPRIORITY.md)

## 使用实例

场景描述：如果SGSN与RNC协商采用UEA1加密算法，而SGSN侧配置的加密算法NOCIPH优先级别最高，可以删除该算法优先级。

删除算法类型为加密算法，算法为不加密的算法的优先级配置信息：

RMV ALGPRIORITY: ALGTYPE=CIPH, ALGCIPH=NOCIPH;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除算法优先级配置信息(RMV-ALGPRIORITY)_26305456.md`
