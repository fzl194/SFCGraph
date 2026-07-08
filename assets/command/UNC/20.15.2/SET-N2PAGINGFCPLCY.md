---
id: UNC@20.15.2@MMLCommand@SET N2PAGINGFCPLCY
type: MMLCommand
name: SET N2PAGINGFCPLCY（设置N2模式寻呼消息反压流控策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: N2PAGINGFCPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2模式反压流控管理
status: active
---

# SET N2PAGINGFCPLCY（设置N2模式寻呼消息反压流控策略）

## 功能

**适用NF：AMF**

该命令用于设置N2模式寻呼反压流控功能的相关参数。

## 注意事项

- 该命令执行后立即生效。

- 当“N2模式寻呼反压流控功能开关”打开时，“精准寻呼控制开关”与“寻呼重发控制开关”不能都关闭，否则无流控效果。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH | PRECISEPAGINGSW | PAGINGRESENDSW |
| --- | --- | --- |
| ON | OFF | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | N2模式寻呼反压流控功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否开启N2模式寻呼反压流控功能。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。<br>配置原则：无 |
| PRECISEPAGINGSW | 精准寻呼控制开关 | 可选必选说明：该参数在"SWITCH"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于控制N2模式寻呼反压流控功能开启时，是否按照Last gNodeB+TA List策略对N2模式数据和语音寻呼请求进行精准寻呼。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N2PAGINGFCPLCY查询当前参数配置值。<br>配置原则：<br>本参数设置为“ON(开启)”时，系统进入N2模式反压流控状态后，数据和语音触发的下行寻呼消息统一按照Last gNodeB+TA List策略进行精准寻呼；本参数设置为“OFF(关闭)”时，系统进入N2模式反压流控状态后，精准寻呼策略与正常状态一致。 |
| PAGINGRESENDSW | 寻呼重发控制开关 | 可选必选说明：该参数在"PRECISEPAGINGSW"配置为"OFF"时为条件可选参数。<br>参数含义：该参数用于控制寻呼反压流控功能开启时，是否不重复发送N2寻呼请求。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N2PAGINGFCPLCY查询当前参数配置值。<br>配置原则：<br>本参数设置为“ON(开启)”时，系统进入N2模式反压流控状态后，不重发N2模式寻呼消息；本参数设置为“OFF(关闭)”时，系统进入N2模式反压流控状态后，N2模式寻呼重发策略与正常状态相同。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N2PAGINGFCPLCY]] · N2模式寻呼消息反压流控策略（N2PAGINGFCPLCY）

## 使用实例

需要开启N2寻呼流控功能，且流控状态下不重复发送N2寻呼请求，按照Last gNodeB+TA List策略对N2模式数据和语音寻呼请求进行精准寻呼时，执行如下命令：

```
SET N2PAGINGFCPLCY: SWITCH=ON, PRECISEPAGINGSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-N2PAGINGFCPLCY.md`
