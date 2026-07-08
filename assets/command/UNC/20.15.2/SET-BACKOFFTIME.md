---
id: UNC@20.15.2@MMLCommand@SET BACKOFFTIME
type: MMLCommand
name: SET BACKOFFTIME（设置Back-off Time信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: BACKOFFTIME
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- Back-off Time信息
status: active
---

# SET BACKOFFTIME（设置Back-off Time信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于配置APN的Back-off time相关的参数。

## 注意事项

- 该命令执行后立即生效。

- APNNAME的值由ADD APN命令添加，OVERLOADSW、APNCONGESTIONSW的初始值是DISABLE，OVERLOADRATE的初始值是70，OVERLOADDETTIME的初始值是15，RESTORERATE的初始值是80，RESTOREDETTIME的初始值是15，INHERIT的初始值是NO，BACKOFFTIMER的初始值是600，IPEXHAUSTSW的初始值是DISABLE。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| OVERLOADSW | 系统过载场景下Back-off Time开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置系统过载场景下的Back-off Time开关。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIME查询当前参数配置值。<br>配置原则：无 |
| APNCONGESTIONSW | APN拥塞场景下Back-off Time开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置APN拥塞场景下Back-off Time开关。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIME查询当前参数配置值。<br>配置原则：<br>此参数目前无效。 |
| IPEXHAUSTSW | 地址资源耗尽场景下Back-off Time开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置地址资源耗尽场景下Back-off Time开关。当该参数置为“Enable”，则本地地址池资源耗尽时，使能Back-off Time。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIME查询当前参数配置值。<br>配置原则：无 |
| OVERLOADRATE | Back-off Time启动激活成功率阈值(%) | 可选必选说明：该参数在"APNCONGESTIONSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置APN拥塞的激活成功率。APN激活成功率低于此值时，开启Back-off Time。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIME查询当前参数配置值。<br>配置原则：<br>此参数目前无效。 |
| OVERLOADDETTIME | Back-off Time控制检测时长(秒) | 可选必选说明：该参数在"APNCONGESTIONSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用户设置APN拥塞阈值的检测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~120，单位是秒。生效值5的倍数，如果配置的值不是5的倍数，向上取整。例如配置的值为6，向上取整为10。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIME查询当前参数配置值。<br>配置原则：<br>此参数目前无效。 |
| RESTORERATE | Back-off Time恢复激活成功率(%) | 可选必选说明：该参数在"APNCONGESTIONSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置APN拥塞解除的成功率阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIME查询当前参数配置值。<br>配置原则：<br>此参数目前无效。 |
| RESTOREDETTIME | Back-off Time恢复检测时长(秒) | 可选必选说明：该参数在"APNCONGESTIONSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置APN拥塞恢复阈值的检测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~120，单位是秒。取值为5的倍数。如果配置的值不是5的倍数，向上取整。例如配置的值为6，向上取整为10。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIME查询当前参数配置值。<br>配置原则：<br>此参数目前无效。 |
| INHERIT | 是否继承全局Back-off时长 | 可选必选说明：可选参数<br>参数含义：该参数用于指示是否继承全局Back-off时长。<br>数据来源：本端规划<br>取值范围：<br>- “NO（否）”：以本配置的Back-off Time为准。<br>- “YES（是）”：以全局的Back-off Time为准。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIME查询当前参数配置值。<br>配置原则：<br>取值为YES时表示以全局的Back-off时长为准；取值为NO时表示以本配置的Back-off时长为准。 |
| BACKOFFTIMER | Back-off时长(秒) | 可选必选说明：该参数在"INHERIT"配置为"NO"时为条件可选参数。<br>参数含义：该参数用于设置Back-off时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~3600，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIME查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BACKOFFTIME]] · Back-off Time信息（BACKOFFTIME）

## 使用实例

当运营商需要设置某个APN为“huawei.com”下的Back-off time参数时，配置如下：

```
SET BACKOFFTIME: APNNAME = "huawei.com", OVERLOADSW = ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Back-off-Time信息（SET-BACKOFFTIME）_09652083.md`
