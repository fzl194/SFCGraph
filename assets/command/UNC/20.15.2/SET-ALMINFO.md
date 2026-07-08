---
id: UNC@20.15.2@MMLCommand@SET ALMINFO
type: MMLCommand
name: SET ALMINFO（设置告警配置信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ALMINFO
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 告警管理
status: active
---

# SET ALMINFO（设置告警配置信息）

## 功能

本命令用于设置系统内告警的配置信息。

## 注意事项

重复执行相同的命令，会返回命令执行成功的提示信息。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要设置哪个网元的告警配置信息。<br>取值范围：0~65535<br>默认值：无。<br>配置原则：网元ID可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询。 |
| ALARMID | 告警ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要设置哪个告警ID的配置信息。<br>取值范围：0~999999999<br>默认值：无。<br>配置原则：无。 |
| CT | 配置类型 | 可选必选说明：可选参数。<br>参数含义：用于指示系统需要设置告警的哪种配置类型。<br>取值范围：<br>“MASK(屏蔽)”<br>，表示设置告警的屏蔽配置。<br>默认值：<br>“MASK(屏蔽)”<br>。<br>配置原则：若不输入，则表示设置告警的屏蔽配置。 |
| MASKED | 是否屏蔽 | 可选必选说明：必选参数。<br>参数含义：用于指定告警屏蔽标志。<br>取值范围：<br>- “YES(是)”：表示对指定告警进行屏蔽，系统将不上报该告警。<br>- “NO(否)”：表示对指定的告警不进行屏蔽，系统将上报该告警。<br>默认值：无。<br>配置原则：无。 |
| MASK_TYPE | 屏蔽类型 | 可选必选说明：可选参数。<br>参数含义：用于指示系统按照哪个屏蔽类型设置告警配置信息。<br>取值范围：<br>- “BYID(按告警ID)”：表示按告警ID设置告警配置信息。<br>- “BYPARAMS(按告警参数)”：表示按告警参数设置告警配置信息。<br>默认值：<br>“BYID(按告警ID)”<br>。<br>配置原则：<br>- 若不输入，则表示按告警ID设置告警配置信息。<br>- “BYPARAMS(按告警参数)”设置的告警屏蔽单网元最大支持配置1000条，单告警最大支持配置100条。<br>- “BYPARAMS(按告警参数)”设置的告警屏蔽仅限OM Portal界面和网管界面上的屏蔽，可能会出现OM Portal界面和网管告警界面没有活动告警，但使用**DSP ACTALM**还可以查询到部分告警。 |
| PARAMS | 屏蔽规则 | 可选必选说明：该参数在<br>“屏蔽类型”<br>配置为<br>“BYPARAMS(按告警参数)”<br>时为必选参数。<br>参数含义：用于指定告警的屏蔽规则。<br>取值范围：1~512个字符。<br>默认值：无。<br>配置原则：<br>- 屏蔽规则中填写告警定位信息中的参数对，例如：网元ID=12，其中“网元ID”为参数名称，“12”为该参数值，参数值中不能包含“,”。<br>- 屏蔽规则中若要配置多个参数对，每个参数对中间使用“,”连接，例如：网元ID=12,故障模块号=1111。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALMINFO]] · 告警配置信息（ALMINFO）

## 使用实例

设置告警配置信息：

```
%%SET ALMINFO: MEID=0, ALARMID=5521, MASKED=NO;%%
RETCODE = 0  操作成功

---    END

%%SET ALMINFO:ALARMID=36161, CT=MASK, MASKED=YES, MASK_TYPE=BYPARAMS, MEID=12, PARAMS="进程号=0,进程名=Test";%% 
RETCODE = 0  操作成功 

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-ALMINFO.md`
