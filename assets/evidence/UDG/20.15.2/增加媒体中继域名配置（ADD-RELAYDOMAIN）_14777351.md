# 增加媒体中继域名配置（ADD RELAYDOMAIN）

- [命令功能](#ZH-CN_CONCEPT_0000207114777351__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000207114777351__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000207114777351__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000207114777351__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000207114777351__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000207114777351)

**适用NF：PGW-U、UPF**

该命令用于添加媒体中继域名配置。

#### [注意事项](#ZH-CN_CONCEPT_0000207114777351)

- 该命令执行后60s生效。
- 该命令最大记录数为100。

#### [操作用户权限](#ZH-CN_CONCEPT_0000207114777351)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000207114777351)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYTPLNAME | 媒体中继模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定媒体中继模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该取值必须和ADD RELAYTEMPLATE中配置的“RELAYTPLNAME”参数取值相同。 |
| RELAYDOMAINNAME | 媒体中继域名配置名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置媒体中继域名配置名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：RELAYDOMAINNAME参数不允许与RELAYTPLNAME相同。 |
| DOMAINVALUE | 域名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。仅支持数字、字母、'-'、'.'和'*'进行组合，'-'和'.'不能出现在开头或结尾。<br>默认值：无<br>配置原则：无 |
| TLSCFGNAME | TLS配置名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该Relay业务TLS配置描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该取值必须和ADD RELAYTLSCFG中配置的“TLSCONFIGNAME”参数取值相同。<br>- 输入单空格将删除该参数已有配置项。 |
| UESERVICEPROTO | UE业务请求协议 | 可选必选说明：可选参数<br>参数含义：该参数用于设置UE请求支持的协议。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- BOTH：同时支持HTTP和HTTPS方式的请求。<br>- HTTP：仅支持HTTP。<br>- HTTPS：仅支持HTTPS。<br>默认值：HTTPS<br>配置原则：<br>- HTTP：如果请求为HTTPS，会将终端的HTTPS请求强制重定向为HTTP方式。<br>- HTTPS：如果请求为HTTP，会将终端的HTTP请求强制重定向为HTTPS方式。 |
| ORIGINPULLPROTO | 业务回源协议 | 可选必选说明：可选参数<br>参数含义：该参数用于设置业务回源协议。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- FLWUE：Relay与CDN之间采用顺从UE请求模式发起连接。<br>- HTTPS：Relay与CDN之间采用HTTPS方式发起连接。<br>- HTTP：Relay与CDN之间采用HTTP方式发起连接。<br>默认值：HTTPS<br>配置原则：无 |
| SERVICETYPE | 业务服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置业务服务类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- VOD：点播类型。<br>- LIVE：直播类型。<br>- BOTH：点播和直播。<br>默认值：无<br>配置原则：无 |
| LIVEPROTOTYPE | 直播协议类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SERVICETYPE”配置为“LIVE” 或 “BOTH”时为必选参数。<br>参数含义：该参数用于设置直播协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FLV：FLV格式。<br>默认值：无<br>配置原则：无 |
| VODPROTOTYPE | 点播协议类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SERVICETYPE”配置为“VOD” 或 “BOTH”时为必选参数。<br>参数含义：该参数用于设置点播协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MP4：MP4格式。<br>默认值：无<br>配置原则：无 |
| DEFAULTVODSW | 缺省点播业务开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SERVICETYPE”配置为“VOD” 或 “BOTH”时为可选参数。<br>参数含义：该参数用于开启或关闭缺省点播业务开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：对于无法识别的资源请求，按异常资源处理，执行异常资源动作。<br>- ENABLE：对于无法识别的资源，按点播资源处理，尝试回源。<br>默认值：DISABLE<br>配置原则：无 |
| URLAUTHNAME | URL鉴权名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置URL鉴权名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该取值必须和ADD RELAYURLAUTH中配置的“RELAYURLAUTHNM”参数取值相同。<br>- 输入单空格将删除该参数已有配置项。 |
| RELAYPROTODEFNM | 媒体中继协议定义名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置媒体中继协议定义名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 如果使用缺省文件后缀无法完全识别直播和点播业务时，需要通过ADD RELAYPROTODEF命令配置媒体中继协议定义规则。<br>- 输入单空格将删除该参数已有配置项。 |
| REFERERCHKRULE | Referer检查规则 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Referer检查规则。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该取值必须和ADD RELAYRFCHKRULE中配置的“RELAYRFCHKNAME”参数取值相同。<br>- 输入单空格将删除该参数已有配置项。 |
| UNSPTMEDIAACT | 不支持的媒体访问动作 | 可选必选说明：可选参数<br>参数含义：该参数用于设置不支持的媒体访问动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- REDIRECT：重定向。<br>- FORBIDDEN：拒绝。<br>默认值：REDIRECT<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于设置优先级。优先级1-65535，越小优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型。<br>默认值：无<br>配置原则：不允许重复，以免同时匹配中多个。 |
| HTTPMSGCTRLNAME | 媒体中继Http消息控制名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置媒体中继Http消息控制名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该取值必须和ADD RELAYHTTPMCTL中配置的“HTTPMSGCTRLNAME”参数取值相同。<br>- 输入单空格将删除该参数已有配置项。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

#### [使用实例](#ZH-CN_CONCEPT_0000207114777351)

假如需要创建一组媒体中继域名配置，则命令如下：

```
ADD RELAYDOMAIN: RELAYTPLNAME="test", RELAYDOMAINNAME="test001", DOMAINVALUE="www.xxx.com", UESERVICEPROTO=HTTPS, ORIGINPULLPROTO=HTTPS, SERVICETYPE=VOD, VODPROTOTYPE=MP4-1, DEFAULTVODSW=DISABLE, UNSPTMEDIAACT=REDIRECT, PRIORITY=1;
```
