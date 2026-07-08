---
id: UNC@20.15.2@MMLCommand@ADD ALGPRIORITY
type: MMLCommand
name: ADD ALGPRIORITY（增加算法优先级配置信息）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD ALGPRIORITY（增加算法优先级配置信息）

## 功能

**适用网元：SGSN**

该命令用于配置算法优先级。SGSN在给RAN发送算法时会根据算法优先级排序。当 [**MOD IUAUTHCIPH**](修改Iu模式用户安全参数(MOD IUAUTHCIPH)_72345245.md) 命令中加密开关打开后，选择不同的加密算法或完整性算法，系统根据该命令配置的算法优先级对算法进行重排序。如果所有算法均未设置优先级，则为随机顺序。

## 注意事项

- 该命令执行后立即生效。
- 该表最多可以增加5条记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGTYPE | 算法类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对何种算法设置优先级。目前有加密算法和完整性算法两种类型。<br>数据来源：整网规划<br>取值范围：<br>- “CIPH（UMTS加密算法）”<br>- “INTE（UMTS完整性算法）”<br>默认值：无 |
| ALGCIPH | 加密算法 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定加密算法类型。加密算法是用于保密用户身份，用户数据及信令通道。<br>前提条件：该参数在<br>“ALGTYPE（算法类型）”<br>设置为<br>“CIPH（UMTS加密算法）”<br>时生效。<br>数据来源：整网规划<br>取值范围：<br>- “NOCIPH（不加密）”：表示对RNC建立的连接不加密，也可以通过不启动加密算法实现。<br>- “UEA1（UEA1）”<br>- “UEA2（UEA2）”<br>默认值：无 |
| ALGINTE | 完整性算法 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定完整性算法类型，只在IU模式下使用。完整性算法是用来保证信令源鉴权数据的完整性。<br>前提条件：该参数在<br>“ALGTYPE（算法类型）”<br>设置为<br>“INTE（UMTS完整性算法）”<br>时生效。<br>数据来源：整网规划<br>取值范围：<br>- “UIA1（UIA1）”<br>- “UIA2（UIA2）”<br>默认值：无<br>配置原则：根据<br>[**MOD IUAUTHCIPH**](修改Iu模式用户安全参数(MOD IUAUTHCIPH)_72345245.md)<br>中完整性算法的配置原则，对各完整性算法进行优先级配置。 |
| ALGPRI | 算法优先级 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置所选择算法的优先级。<br>前提条件：该参数在<br>“ALGTYPE（算法类型）”<br>设置为<br>“CIPH（UMTS加密算法）”<br>或者<br>“INTE（UMTS完整性算法）”<br>时生效。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>配置原则：<br>- 数值越小，优先级越高。<br>- 同一种算法类型下（加密或者完整性），算法的优先级值不能相同且算法唯一。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ALGPRIORITY]] · 算法优先级配置信息（ALGPRIORITY）

## 使用实例

1. 在完整性算法中指定算法UIA1的优先级为0：
  ADD ALGPRIORITY: ALGTYPE=INTE, ALGINTE=UIA1, ALGPRI=0;
2. 在加密算法中指定算法UEA1的优先级为2：
  ADD ALGPRIORITY: ALGTYPE=CIPH, ALGCIPH=UEA1, ALGPRI=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ALGPRIORITY.md`
