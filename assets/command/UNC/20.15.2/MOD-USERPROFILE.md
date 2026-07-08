---
id: UNC@20.15.2@MMLCommand@MOD USERPROFILE
type: MMLCommand
name: MOD USERPROFILE（修改用户模板）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: USERPROFILE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板
status: active
---

# MOD USERPROFILE（修改用户模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改用户模板。用户模板可用于设置免费业务是否进行在线、离线计费功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| FREESERONLCHG | 免费业务在线计费标识 | 可选必选说明：可选参数<br>参数含义：指定免费业务在线计费标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务不与OCS/CHF交互进行在线计费，则配置该参数为DISABLE。<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务与OCS/CHF交互进行在线计费，则配置该参数为ENABLE。 |
| FREESEROFFCHG | 免费业务离线计费标识 | 可选必选说明：可选参数<br>参数含义：指定免费业务离线计费标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务不记录话单，不进行离线计费，则配置该参数为DISABLE。<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务记录话单，进行离线计费，则配置该参数为ENABLE。 |
| FREESERCVGCHG | 免费业务融合计费标识 | 可选必选说明：可选参数<br>参数含义：指定免费业务融合计费标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务不记录话单，不进行融合计费，则配置该参数为DISABLE。<br>- 如果运营商在计费规则绑定的计费属性为免费的业务，希望免费业务进行融合计费，则配置该参数为ENABLE。 |
| PROFILERANGE | 模板生效范围 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户模板生效范围。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- ALL：表示对中心和边缘UPF（主锚点UPF和辅锚点UPF）均生效。<br>- CENTRAL：表示对中心UPF（主锚点）生效。<br>- LOCAL：表示对边缘UPF（辅锚点）生效。<br>默认值：无<br>配置原则：对于已添加的模板，修改生效范围时，需检查UserProfile生效范围与其绑定的Rule生效范围是否冲突；只对新用户业务生效。 |
| QOSANASW | 质差分析开关 | 可选必选说明：可选参数<br>参数含义：该参数用于标识是否是质差分析业务相关的预定义规则。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：默认不支持质差分析，当需要配置预定义规则支持质差分析时，开关需要打开。 |
| FREEONLFLAGSW | 免费在线业务携带在线相关标识开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“FREESERCVGCHG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置融合计费免费在线业务是否携带在线相关标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承软参DWORD530 BIT5和软参DWORD530 BIT6。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：该参数优先级高于软参DWORD530 BIT5和软参DWORD530 BIT6。 |
| RELAYSW | 媒体中继开关 | 可选必选说明：可选参数<br>参数含义：该参数用于标识是否是媒体中继业务相关的预定义规则。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：默认不支持媒体中继，当需要配置预定义规则支持媒体中继时，开关需要打开。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USERPROFILE]] · 用户模板（USERPROFILE）

## 使用实例

假如运营商需要修改用户模板，用户模板名称为“testuserprofilename”，免费业务是否进行在线计费为“ENABLE”：

```
MOD USERPROFILE:USERPROFILENAME="testuserprofilename",FREESERONLCHG=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户模板（MOD-USERPROFILE）_09897207.md`
