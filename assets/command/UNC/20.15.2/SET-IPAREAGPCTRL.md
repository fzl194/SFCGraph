---
id: UNC@20.15.2@MMLCommand@SET IPAREAGPCTRL
type: MMLCommand
name: SET IPAREAGPCTRL（设置基于位置分配IP地址策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IPAREAGPCTRL
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
- 移动性管理
- 基于位置分配IP地址管理
- 基于位置分配IP地址策略管理
status: active
---

# SET IPAREAGPCTRL（设置基于位置分配IP地址策略）

## 功能

**适用网元：SGSN、MME**

该命令用于设置“基于位置的IP地址重分配”的策略。

IP区域群是“基于位置的IP地址重分配”功能的一个基本概念，是指一组TAC或者LAC，在同一个IP区域群中的用户具有相同的IP地址分配策略。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。
- 请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEAUSRSW | 用户下线开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户下线开关。若用户下线开关打开，则会将已经附着在该区域群中的用户下线。对2G和3G用户，则发起网络侧去激活PDP或者网络侧分离，具体类型由参数“ROAMTYPE（GU漫游用户限制方式）”或者“NONLOCALTYPE（GU本网异地用户限制方式）”设置；对4G用户，则发起网络侧分离。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>系统初始设置值：<br>“OFF(关闭)” |
| DEAUSRSPD | 用户下线速度（个/秒） | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置用户下线的速度。<br>前提条件: 该参数在“DEAUSRSW(用户下线开关)”设置为ON(开启)时生效。<br>数据来源：整网规划<br>取值范围：8~5000<br>系统初始设置值：200<br>说明：- 建议根据实际用户数和期望所有用户下线完成时长来配置此参数，即“用户下线速度(个/秒)”为：实际注册用户数/所有用户下线完成时长，例如系统当前实际注册用户数为80万，需要在1800秒内下线，故“用户下线速度(个/秒)”为：800000个 / 1800秒 = 445(个/秒)。<br>- 如果通过上面公式计算的值高于周边网元（如HSS，AAA服务器等）的实际处理能力，则以周边网元的处理能力为准。 |
| LOCALUSRSW | 是否区分本网本地和本网异地用户 | 可选必选说明：可选参数<br>参数含义：该参数用于标识是否区分本网本地和本网异地用户。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不区分)”<br>- “YES(区分)”<br>系统初始设置值：NO(不区分)<br>配置原则：<br>- 当运营商对本网异地用户采用Local Breakout策略时，本网异地用户和本网本地用户一样，都是通过本网的GGSN/PGW分配IP地址，这种情况下，运营商将本开关置为“NO(不区分)”。<br>- 如果运营商对本网异地用户采用Home Routed策略时，本网异地用户的IP地址通过归属地的GGSN/PGW来分配，此时，如果运营商期望限制本网异地用户的数据业务，可将本开关置为“YES(区分)”。<br>- 若开关置为“YES(区分)”，2G和3G用户需在[**ADD LOCALHLR**](../../../网络管理/LOCALHLR管理/增加本地HLR(ADD LOCALHLR)_72225755.md)配置本地HLR号码，4G用户需在[**ADD LOCALHSS**](../../../网络管理/LOCALHSS管理/增加本地HSS(ADD LOCALHSS)_26305888.md)配置本地HSS主机名，否则会将本网本地用户识别为本网异地用户。<br>说明：2G和3G本网本地用户，则发起网络侧去激活PDP上下文来触发IP重分配；4G本网本地用户，则发起网络侧分离来触发IP重分配；此参数设置为<br>“YES”<br>，且<br>[**ADD IPAREAGP**](../IP区域群管理/增加IP区域群(ADD IPAREAGP)_26305412.md)<br>命令的参数<br>“NONLOCALUSRSW”<br>设置为<br>“ON”<br>时，4G本网异地用户发起网络侧分离来触发IP重分配。 |
| ROAMTYPE | GU漫游用户限制方式 | 可选必选说明：可选参数<br>参数含义：该参数表示在启用“基于位置的IP地址重分配”功能后，选择将GPRS/UMTS漫游用户从网络中分离掉，还是去激活PDP上下文。<br>数据来源：本端规划<br>取值范围：<br>- “DEACTIVATION(去激活)”<br>- “DETACH(分离)”<br>系统初始设置值：DEACTIVATION(去激活)<br>说明：对于LTE漫游用户，都是通过分离的方式限制其数据业务的。 |
| NONLOCALTYPE | GU本网异地用户限制方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在<br>“LOCALUSRSW(是否区分本网本地和本网异地用户)”<br>设置为<br>“YES(区分)”<br>有效。<br>参数含义：该参数表示在启用“基于位置分配用户IP地址”功能后，选择将GPRS/UMTS本网异地用户从网络中分离掉，还是去激活PDP上下文。<br>数据来源：本端规划<br>取值范围：<br>- “DEACTIVATION(去激活)”<br>- “DETACH(分离)”<br>系统初始设置值：DEACTIVATION(去激活)<br>说明：对于LTE漫游用户，都是通过分离的方式限制其数据业务的。 |
| GUMMCAUSE | GU用户接入限制原因值 | 可选必选说明：可选参数<br>参数含义：该参数表示在启用“基于位置分配用户IP地址”功能后，<br>UNC<br>分离已附着的GPRS/UMTS本网异地用户或漫游用户，或者拒绝GPRS/UMTS本网异地用户或漫游用户附着请求的原因值。<br>数据来源：本端规划<br>取值范围：1~254<br>系统初始设置值：15<br>配置原则：<br>- GU用户接入限制的常见原因值有：#7（GPRS services not allowed）或者#15（No suitable cells in location area）。<br>- 其它原因值请参考3GPP TS 24.008。 |
| LTEMMCAUSE | LTE用户接入限制原因值 | 可选必选说明：可选参数<br>参数含义：该参数表示在启用“基于位置分配用户IP地址”功能后，<br>UNC<br>分离已附着的LTE本网异地用户或漫游用户，或者拒绝LTE本网异地用户或漫游用户附着请求的原因值。<br>数据来源：本端规划<br>取值范围：1~254<br>系统初始设置值：15<br>配置原则：<br>- LTE用户接入限制的常见原因值有：#7（EPS services not allowed）或者#15（No suitable cells in tracking area）。<br>- 其它原因值请参考3GPP TS 24.008。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPAREAGPCTRL]] · 基于位置分配IP地址策略（IPAREAGPCTRL）

## 使用实例

对一个激活的IP区域群用户下线，下线速度（个/秒）为2000，对2G和3G本网异地用户网络侧去激活PDP，对2G和3G漫游用户网络侧分离并设置原因值为#7（GPRS services not allowed），对LTE用户接入限制原因值设置为#7（EPS services not allowed）：

SET IPAREAGPCTRL: DEAUSRSW=ON, DEAUSRSPD=2000, LOCALUSRSW=YES, ROAMTYPE=DEACTIVATION, NONLOCALTYPE=DETACH, GUMMCAUSE=7, LTEMMCAUSE=7;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置基于位置分配IP地址策略(SET-IPAREAGPCTRL)_72345195.md`
