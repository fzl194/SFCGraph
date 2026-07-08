---
id: UNC@20.15.2@MMLCommand@RMV S1ALGPRIORITY
type: MMLCommand
name: RMV S1ALGPRIORITY（删除S1模式加密和完整性算法优先级配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1ALGPRIORITY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- S1模式用户安全参数
status: active
---

# RMV S1ALGPRIORITY（删除S1模式加密和完整性算法优先级配置信息）

## 功能

![](删除S1模式加密和完整性算法优先级配置信息(RMV S1ALGPRIORITY)_72345249.assets/notice_3.0-zh-cn_2.png)

如果配置的加密性算法或者完整性算法优先级不合理，可能导致终端接入异常。

**适用网元：MME**

该命令用于删除S1模式加密和完整性算法优先级的信息。

## 注意事项

- 该命令执行后立即生效。
- 删除某算法优先级后，如果MME还配有其他算法优先级，则以其他算法中优先级最高的算法为准；如果所有算法均未设置优先级，系统会根据四种算法的默认优先级（从高到低分别为AES、SNOW 3G、ZUC、空加密/空完整性算法）和UE进行协商，最终确定采用的加密/完整性算法。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGTYPE | 算法类型 | 可选必选说明：必选参数<br>参数含义：该参数于指定对何种算法设置优先级。目前有加密算法和完整性算法两种类型。<br>数据来源：整网规划<br>取值范围：<br>- “CIPH(LTE加密算法)”<br>- “INTE(LTE完整性算法)”<br>默认值：无 |
| ALGCIPH | 加密算法 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定加密算法的类型。<br>数据来源：整网规划<br>前提条件：该参数在<br>“ALGTYPE（算法类型）”<br>设置为<br>“CIPH（LTE加密算法）”<br>时生效。<br>取值范围：<br>- “EEA0(采用空加密算法)”<br>- “EEA1(采用SNOW 3G加密算法)”<br>- “EEA2(采用AES加密算法)”<br>- “EEA3(采用ZUC加密算法)”<br>默认值：无 |
| ALGINTE | 完整性算法 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定完整性算法类型，完整性算法是用来保证信令源鉴权数据的完整性。<br>数据来源：整网规划<br>前提条件：该参数在<br>“ALGTYPE（算法类型）”<br>设置为<br>“INTE（LTE完整性算法）”<br>时生效。<br>取值范围：<br>- “EIA0(采用空完整性算法)”<br>- “EIA1(采用SNOW 3G完整性算法)”<br>- “EIA2(采用AES完整性算法)”<br>- “EIA3(采用ZUC完整性算法)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1ALGPRIORITY]] · S1模式加密和完整性算法优先级配置信息（S1ALGPRIORITY）

## 使用实例

删除算法类型为加密算法，算法为SNOW 3G加密算法的优先级配置信息：

RMV S1ALGPRIORITY: ALGTYPE=CIPH, ALGCIPH=EEA1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-S1ALGPRIORITY.md`
