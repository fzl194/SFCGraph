---
id: UNC@20.15.2@MMLCommand@SET PESELPLCY
type: MMLCommand
name: SET PESELPLCY（设置SGSN/MME选择策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PESELPLCY
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-SGSN_S10_S16_S3接口管理
- SGSN MME选择
status: active
---

# SET PESELPLCY（设置SGSN/MME选择策略）

## 功能

![](设置SGSN_MME选择策略（SET PESELPLCY）_72225643.assets/notice_3.0-zh-cn_2.png)

如果SGSN/MME选择策略参数设置不正确，可能导致大量234G间的切换业务失败。

**适用网元：SGSN、MME**

该命令用于设置SGSN/MME选择策略，选择策略用来识别对端网元是SGSN还是MME。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 该命令最大记录数为1。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEIDMODE | 对等网元识别模式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置指定的<br>“PEIDMODE（对等网元识别模式）”<br>，提供识别对端网元是SGSN还是MME的方法。缺省使用协议规定的方法：根据LAC/MME Group ID的最高bit位进行区分。<br>数据来源：整网规划<br>取值范围：<br>“MASK_MODE（掩码模式）”<br>，<br>“SECTION_MODE（区段模式）”<br>，<br>“DOMAIN_ROLLBACK_MODE（域名回退模式）”<br>系统初始设置值：MASK_MODE（掩码模式）<br>配置原则：<br>- “MASK_MODE（掩码模式）”：用掩码模式来识别对端网元是SGSN还是MME。<br>- “SECTION_MODE（区段模式）”：用区段模式来识别对端网元是SGSN还是MME。<br>- “DOMAIN_ROLLBACK_MODE（域名回退模式）”：用域名回退模式来识别对端网元是SGSN还是MME。<br>说明：如果配置为回退模式，则在识别UE的标识是否为本网元分配的时：<br>- 如果UE携带的标识位为GUTI，并且携带了Additional GUTI，则主用标识为GUTI映射的PTMSI/RAI，备选标识为GUTI。<br>- 如果UE携带的标识位为GUTI，但是没有携带Additional GUTI，则按照MMEGI/LAC最高bit位确定主用和备用标识。若最高bit位为1，主用标识为MMEGI，备用标识为LAC；若最高bit位为0，主用标识为LAC，备用标识为MMEGI。<br>- 如果UE携带的标识位为PTMSI/RAI，并且携带了Additional PTMSI/RAI，则主用标识为PTMSI/RAI映射的GUTI，备选标识为PTMSI/RAI。<br>- 如果UE携带的标识位为PTMSI/RAI，但是没有携带Additional PTMSI/RAI，则按照MMEGI/LAC最高bit位确定主用和备用标识。若最高bit位为1，主用标识为MMEGI，备用标识为LAC；若最高bit位为0，主用标识为LAC，备用标识为MMEGI。<br>然后根据主用标识和备用标识进行处理。<br>- 如果主用标识为GUTI，通过GUTI判断为非本网元分配后，需要使用PTMSI/RAI再进行一次判断。<br>- 如果主用标识为PTMSI/RAI，通过PTMSI/RAI判断为非本网元分配后，需要使用GUTI再进行一次判断。<br>- 如果UE携带的标识判断为非本网元分配，则使用主用标识进行DNS查询失败后，使用备用标识再进行一次DNS查询。即：使用MMEC域名查询失败后重试RAI域名，或使用RAI域名查询失败后重试MMEC域名。 |
| BITMASK | 比特掩码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置指定的比特掩码。<br>前提条件：当<br>“PEIDMODE（对等网元识别模式）”<br>为<br>“MASK_MODE（掩码模式）”<br>时显示。<br>数据来源：整网规划<br>取值范围：0～0xffff（十六进制数字）<br>系统初始设置值 ：0x8000<br>配置原则：<br>- LAC/MME Group ID与“BITMASK（比特掩码）”进行比特“与”操作之后，如果等于“BITMASK（比特掩码）”，则认为该标识是MME Group ID。<br>- 缺省取值是协议规定的LAC/MME Group ID区分方式。 |
| MMEGI | MME Group ID | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置指定的MMEGI（MME Group ID）。<br>前提条件：当<br>“PEIDMODE（对等网元识别模式）”<br>为<br>“SECTION_MODE（区段模式）”<br>时显示。<br>数据来源：整网规划<br>取值范围：0x0000～0xffff<br>系统初始设置值 ：0 |
| MMEGIRANGE | MME Group ID范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置指定的<br>“MME Group ID范围”<br>。<br>前提条件：当<br>“PEIDMODE（对等网元识别模式）”<br>为<br>“SECTION_MODE（区段模式）”<br>时显示。<br>数据来源：整网规划<br>取值范围：0x0000～0xffff（十六进制数值型）<br>系统初始设置值 ：0<br>配置原则：<br>- 要求大于或等于“ MMEGI（MME Group ID）”。<br>- 与“ MMEGI（MME Group ID）”参数构成一个MME Group ID区段，可以配置连续的位置区域。如果不输入，表示配置单个MME Group ID。 |
| RNCID | 使用RNC ID域名 | 可选必选说明：可选参数<br>参数含义：该参数用于设置指定的使用RNC ID域名。<br>数据来源：整网规划<br>取值范围：<br>- “NO(NO)”<br>- “YES(YES)”<br>系统初始设置值 ：<br>“YES(YES)”<br>配置原则：<br>- 在Handover/Relocation流程中是否使用“ RNCID（RNC ID域名）”进行查询，如果不使用“ RNCID（RNC ID域名）”，系统会组装RAI域名进行查询。 |
| IDTYPE | 使用ID TYPE | 可选必选说明：可选参数<br>参数含义：该参数用于控制<br>UNC<br>是否通过UE携带的GUTI Type/PTMSI Type信元来识别对端网元类型。<br>数据来源：整网规划<br>取值范围：<br>- “NO(NO)”：系统直接按照“PEIDMODE（对等网元识别模式）”的配置判断对端设备是MME还是SGSN。<br>- “YES(YES) ”：如果UE携带了GUTI Type/PTMSI Type，系统会根据携带信息确定移动性管理业务流程中的对端网元是MME还是SGSN；如果UE未携带GUTI Type/PTMSI Type，系统按照“PEIDMODE（对等网元识别模式）”的配置判断对端设备是MME还是SGSN。<br>系统初始设置值 ：<br>“YES(YES) ”<br>配置原则：<br>- UNC作为MME或融合的MME/SGSN，可以通过S10/S3/S16/Gn接口与其它MME或SGSN进行移动管理业务流程的交互，即需要区分对端设备是MME或SGSN，建议配置为YES。<br>- UNC作为GnGp SGSN，只能通过Gn接口与其它MME或SGSN进行移动管理业务流程的交互，即不区分对端设备是MME还是SGSN，建议配置为NO。 |

## 操作的配置对象

- [SGSN/MME选择策略（PESELPLCY）](configobject/UNC/20.15.2/PESELPLCY.md)

## 使用实例

使用PEIDMODE（对等网元识别模式）为DOMAIN_ROLLBACK_MODE（域名回退模式），RNCID（使用RNC ID域名）为NO（否），IDTYPE(使用ID TYPE )为YES（是）的SGSN/MME选择策略：

SET PESELPLCY: PEIDMODE=DOMAIN_ROLLBACK_MODE, RNCID=NO, IDTYPE=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SGSN_MME选择策略（SET-PESELPLCY）_72225643.md`
