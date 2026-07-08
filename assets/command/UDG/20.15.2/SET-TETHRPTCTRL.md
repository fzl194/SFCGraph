---
id: UDG@20.15.2@MMLCommand@SET TETHRPTCTRL
type: MMLCommand
name: SET TETHRPTCTRL（设置tethering事件上报的相关参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TETHRPTCTRL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- Tethering事件上报控制
status: active
---

# SET TETHRPTCTRL（设置tethering事件上报的相关参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置tethering事件上报的相关参数。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 当SET TETHERDETGLBPARA的STATISTICMETHOD参数设为CONFIG时，每个用户下Tethering节点的最大个数，按照UserProfile下TetheringMaxNum参数配置值加1申请。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TETHSTOPRPTSW | TETHHYSTIMER | TETHRPTEVTMODE |
| --- | --- | --- | --- |
| 初始值 | DISABLE | 0 | TETHER_BEHAVIOR |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TETHSTOPRPTSW | Tethering Stop消息上报开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Tethering Stop消息上报开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- 当运营商需要上报Tethering Stop消息时，设置此参数值为ENABLE。<br>- 当运营商不需要上报Tethering Stop消息时，设置此参数值为DISABLE。 |
| TETHHYSTIMER | Tethering Stop消息上报迟滞时间（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“TETHSTOPRPTSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置Tethering Stop消息上报迟滞时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～3600，单位是秒。<br>默认值：无<br>配置原则：<br>- 当单用户Tethering的Start和Stop消息上报过于频繁时，建议调大此参数。<br>- 当希望Tethering的Start和Stop消息上报尽量精确时，建议调小此参数。<br>- 该参数配置为0时，认为Tethering Stop延迟上报功能关闭。 |
| TETHRPTEVTMODE | tethering上报事件模式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Tethering上报事件是基于Tethering行为还是基于Tethering接入的后台终端数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TETHER_BEHAVIOR：代表基于Tethering用户行为触发事件上报。<br>- TETHER_TERMINAL_NUM：代表基于Tethering用户接入的后台终端数触发事件上报。<br>默认值：无<br>配置原则：当运营商需要上报基于用户是否发生Tethering访问行为时，设置此参数值为TETHER_BEHAVIOR。 当运营商需要上报基于Tethering用户接入的后台终端数时，设置此参数值为TETHER_TERMINAL_NUM。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TETHRPTCTRL]] · tethering事件上报的相关参数（TETHRPTCTRL）

## 使用实例

- 需要上报Tethering Stop消息时，通过TethStopRptSw参数设置：
  ```
  SET TETHRPTCTRL: TETHSTOPRPTSW=ENABLE;
  ```
- 需要设置Tethering的Start和Stop消息上报频率时，通过TethHystimer参数设置：
  ```
  SET TETHRPTCTRL: TETHSTOPRPTSW=ENABLE, TETHHYSTIMER=10;
  ```
- 需要设置Tethering上报模式时，通过TethRptEvtMode参数设置：
  ```
  SET TETHRPTCTRL: TETHSTOPRPTSW=ENABLE, TETHRPTEVTMODE=TETHER_TERMINAL_NUM;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TETHRPTCTRL.md`
