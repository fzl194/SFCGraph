---
id: UNC@20.15.2@MMLCommand@ADD USERPROFILE
type: MMLCommand
name: ADD USERPROFILE（增加用户模板）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: USERPROFILE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 5000
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板
status: active
---

# ADD USERPROFILE（增加用户模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加用户模板。用户模板可用于设置免费业务是否进行在线、离线计费和融合计费功能。

## 注意事项

- 该命令执行后立即生效。
- 当UPSPECTYPE参数不指定或者指定为DEFAULT时，该命令最大记录数为5000；当UPSPECTYPE参数指定为SPECIFICATION_LIMITED时，该命令最大记录数为100000。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- UNC应该尽量避免配置的Rule与UserProfile同名。
- PCRF下发Charging-Rule-Name时，在安装本地预定义的Rule的同时还会安装同名的UserProfile下绑定的静态Rule。
- PCRF下发Charging-Rule-Name时，由于Charging-Rule-Name对应的Rule与同名的UserProfile下绑定的所有Rule的安装和删除策略会保持一致，因此配置同名UserProfile时，要求同名的UserProfile下绑定的所有Rule名称不能与PCRF上配置的Charging-Rule-Name重复。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPTYPE | 用户模板类型 | 可选必选说明：必选参数<br>参数含义：参数用于设置用户模板类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- PCC：指定PCC类型用户模板。<br>- ULCL：指定ULCL类型用户模板。<br>- UPSELECT：指定UPSELECT类型用户模板。<br>默认值：PCC<br>配置原则：如果UPTYPE为空，不影响执行，系统默认填充PCC类型。 |
| FREESERONLCHG | 免费业务在线计费标识 | 可选必选说明：可选参数<br>参数含义：指定免费业务在线计费标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：ENABLE<br>配置原则：<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务不与OCS/CHF交互进行在线计费，则配置该参数为DISABLE。<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务与OCS/CHF交互进行在线计费，则配置该参数为ENABLE。 |
| FREESEROFFCHG | 免费业务离线计费标识 | 可选必选说明：可选参数<br>参数含义：指定免费业务离线计费标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：ENABLE<br>配置原则：<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务不记录话单，不进行离线计费，则配置该参数为DISABLE。<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务记录话单，进行离线计费，则配置该参数为ENABLE。 |
| FREESERCVGCHG | 免费业务融合计费标识 | 可选必选说明：可选参数<br>参数含义：指定免费业务融合计费标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：ENABLE<br>配置原则：<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务不记录话单，不进行融合计费，则配置该参数为DISABLE。<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务进行融合计费，则配置该参数为ENABLE。 |
| PROFILERANGE | 模板生效范围 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPTYPE”配置为“PCC”时为可选参数。<br>参数含义：该参数用于设置用户模板生效范围。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- ALL：表示对中心和边缘UPF（主锚点UPF和辅锚点UPF）均生效。<br>- CENTRAL：表示对中心UPF（主锚点）生效。<br>- LOCAL：表示对边缘UPF（辅锚点）生效。<br>默认值：ALL<br>配置原则：无 |
| UPSPECTYPE | 用户模板规格类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板规格类型，当取值为SPECIFICATION_LIMITED时，表示规格受限用户模板，表示用户安装的该类型用户模板数和该类型用户模板绑定的规则数量均比默认规格小，需要配合相应特性使用。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DEFAULT：默认配置。<br>- SPECIFICATION_LIMITED：规格受限配置。<br>默认值：DEFAULT<br>配置原则：该参数配置后不允许修改。 |
| QOSANASW | 质差分析开关 | 可选必选说明：可选参数<br>参数含义：该参数用于标识是否是质差分析业务相关的预定义规则。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：DISABLE<br>配置原则：默认不支持质差分析，当需要配置预定义规则支持质差分析时，开关需要打开。 |
| FREEONLFLAGSW | 免费在线业务携带在线相关标识开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“FREESERCVGCHG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置融合计费免费在线业务是否携带在线相关标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承软参DWORD530 BIT5和软参DWORD530 BIT6。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：INHERIT<br>配置原则：<br>- 该参数优先级高于软参DWORD530 BIT5和软参DWORD530 BIT6。<br>- 该参数设置为DISABLE时，在线免费RG的配额来源为配置SET STGTRIGGER中的参数PDUTIMELIMIT和PDUVOLUMELIMIT。 |
| RELAYSW | 媒体中继开关 | 可选必选说明：可选参数<br>参数含义：该参数用于标识是否是媒体中继业务相关的预定义规则。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：<br>- 默认不支持媒体中继，当需要配置预定义规则支持媒体中继时，开关需要打开。<br>- 用户取消签约媒体中继业务前，该参数的取值变更会导致去签约UPF选择规则场景下SMF不通知UPF去签约媒体中继业务。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USERPROFILE]] · 用户模板（USERPROFILE）

## 使用实例

假如运营商需要增加用户模板，用户模板名称为“testuserprofilename”：

```
ADD USERPROFILE: USERPROFILENAME="testuserprofilename", UPTYPE=PCC;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-USERPROFILE.md`
