---
id: UDG@20.15.2@MMLCommand@MOD RESREC
type: MMLCommand
name: MOD RESREC（修改DNS资源记录）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: RESREC
command_category: 配置类
applicable_nf:
- CloudEPSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用管理
- 资源记录管理
status: active
---

# MOD RESREC（修改DNS资源记录）

## 功能

**适用NF：CloudEPSN**

本命令实现修改A、AAAA、NS、SRV、NAPTR记录的功能。

## 注意事项

- 该命令执行后立即生效。
- 在选择“记录类型”为“A”、“AAAA”或“NS”记录时，只支持修改TTL。修改“A”或“AAAA”的TTL时，会将该域名下的其他IP的TTL值同步修改。
- 在选择“记录类型”为“NAPTR”记录时，支持修改TTL、顺序值、偏好值、service，修改字段均为可选参数，默认不修改。“修改NAPTR记录的字段类”用于控制顺序值、偏好值的修改，当“修改NAPTR记录的字段类”为“修改NAPTR记录的顺序值”时，该命令仅支持修改NAPTR的顺序值；当“修改NAPTR记录的字段类”为“修改NAPTR记录的偏好值”时，该命令仅支持修改NAPTR的偏好值；当“修改NAPTR记录的字段类”为“修改NAPTR记录的顺序值和偏好值”时，该命令同时修改NAPTR的偏好值和偏好值。
- 在选择“记录类型”为“SRV”记录时，支持修改TTL、偏好、权重，修改字段均为可选参数，默认不修改。“修改SRV记录的字段类”用于控制优先级、权重的修改，当“修改SRV记录的字段类”为“修改SRV记录的优先级”时，该命令仅支持修改SRV的优先级值；当“修改SRV记录的字段类”为“修改SRV记录的权重”时，该命令仅支持修改SRV的权重值；当“修改SRV记录的字段类”为“同时修改SRV记录的优先级和权重”时，该命令同时修改SRV的优先级和权重。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 任务ID | 可选必选说明：可选参数<br>参数含义：任务ID。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- CloudDNS无需配置此参数。<br>- 由GEN DNSTASKID生成，用于确定任务ID。 |
| TYPE | 记录类型 | 可选必选说明：必选参数<br>参数含义：增加的记录类型。<br>数据来源：本端规划<br>取值范围：<br>- A：A记录。<br>- AAAA：AAAA记录。<br>- NAPTR：NAPTR记录。<br>- SRV：SRV记录。<br>- NS：NS记录。<br>默认值：无<br>配置原则：<br>- A记录：由域名解析出IPV4地址的记录。<br>- AAAA记录：由域名解析出IPV6地址的记录。<br>- NS记录：配置区域所属的授权域名服务器的记录。<br>- SRV记录：根据某项服务的域名解析出主机名的记录。<br>- NAPTR记录：根据域名解析出替换域名的记录。 |
| VIEWNAME | 视图名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NS”、“SRV” 或 “NAPTR”时为可选参数。<br>参数含义：资源所属的域名解析视图名称。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 输入资源所属的域名解析视图名称。<br>- CloudDNS中视图默认值为"default"。<br>- CloudDNS当前支持视图最大规格为32字符。<br>- 视图最后一位不支持特殊字符。<br>- 执行命令时需要保证视图存在。 |
| ZONE | 区域名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NS”、“SRV” 或 “NAPTR”时为必选参数。<br>参数含义：资源记录的区域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS支持的域名最大长度为249，且不支持xn--开头。 |
| DOMAIN | 域名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NS”、“SRV” 或 “NAPTR”时为必选参数。<br>参数含义：资源记录的域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 域名可以是完整域名，此时以（.）作为结束符；也可以是部分域名，此时不能以点（.）作为结束符，系统会自动将部分域名和区域名一起拼接成完整域名。<br>- 只输入“@”字符表示用同名与区域名称的域名。<br>- 为了兼容DNS9816，在记录类型选择SRV、NAPTR、NS时候，支持输入下划线“_”。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持域名最大长度为254，结尾必须以分隔符（.）结尾，且不能以xn—开头。 |
| IP | IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“A” 或 “AAAA”时为必选参数。<br>参数含义：IP地址。<br>数据来源：全网规划<br>取值范围：最多支持输入20个IP地址。<br>默认值：无<br>配置原则：<br>- 当type选择A记录的时候，ip参数支持输入IPV4地址。 IPV4地址不能为0.0.0.0、255.255.255.255和环回地址等非法地址。<br>- 当type选择AAAA记录的时候，ip参数支持输入IPV6地址。 IPV6地址不能为全0、全F和环回地址等非法地址。 支持输入IPV6缩写地址和全量地址输入。 |
| PRIORITY | SRV记录的优先级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”时为必选参数。<br>参数含义：SRV记录的优先级。当查询结果为多条记录时，客户端选择优先级高的记录。当优先级相同时，客户端根据“权重”值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数值越小，优先级越高。<br>- 此参数只用于SRV记录。 |
| WEIGHT | SRV记录的权重 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”时为必选参数。<br>参数含义：SRV记录的权重。当几条记录的“优先级”值相同时，客户端根据此参数值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数值越大，选中概率越高。<br>- 此参数只用于SRV记录。 |
| PORT | SRV记录的端口号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”时为必选参数。<br>参数含义：用于SRV记录，服务器上提供该种服务的端口号。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于SRV记录。<br>- CloudDNS不支持将端口设置为0。 |
| TARGET | SRV记录的目标域名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”时为必选参数。<br>参数含义：用于SRV记录，提供该种服务的服务器域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于SRV记录。<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），连字符（-）以及分隔符（.）构成的以字母和数字开头的字符串。<br>- 必须为全地址域名格式，以分隔符结束。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持目标域名最大长度为254，结尾必须以分隔符（.）结尾，且不能以xn--开头。 |
| ORDER | NAPTR记录的顺序值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：NAPTR记录的权重。当几条记录的“顺序”值相同时，客户端根据此参数值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于NAPTR记录。<br>- 此参数值越小，选中的概率越高。 |
| PREFERENCE | NAPTR记录的偏好值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：NAPTR记录的优先级。当查询结果为多条记录时，客户端选择优先级高的记录。当优先级相同时，客户端根据“偏爱”值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于NAPTR记录。<br>- 此参数值越小，优先级越高。 |
| FLAGS | NAPTR记录的标志 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：用于NAPTR记录，表示下一次查询的类型。<br>数据来源：全网规划<br>取值范围：<br>- S：S。<br>- A：A。<br>- U：U。<br>- AAAA：AAAA。<br>- NULL：NULL。<br>默认值：无<br>配置原则：<br>- S：表示新域名为SRV记录域名，下一次需要进行SRV查询。<br>- A：表示新域名为A记录域名，下一次需要进行A记录查询。<br>- U：表示本次结果是满足RFC2396标准的absoluteURI，下次不需要进行DNS查询。<br>- AAAA：表示新域名为AAAA记录域名，下一次需要进行AAAA查询。<br>- NULL：表示下次还需要进行NAPTR查询。<br>- CloudDNS中不支持配置AAAA，若参数选为AAAA会自动转换为A。 |
| SERVICE | NAPTR记录的service | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：用于NAPTR记录，新目标上的服务，以及该服务交互使用的协议。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 通常使用字符“+”连接各个部分。<br>- 根据原域名生成新域名或URI的规则。<br>- 此参数大小写不敏感。<br>- 字段的格式为“x-3gpp-网元类型:x-接口类型-接口协议:x-接口类型-接口协议:……”。<br>- 支持输入大小写字母、数字、“+”、“-”、“：”几类字符。 |
| REGEXP | NAPTR记录的正则表达式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为可选参数。<br>参数含义：NAPTR记录的正则表达式。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 此参数只用于NAPTR记录。 |
| REPLACEMENT | NAPTR记录的替换域名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：NAPTR记录的替换域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于NAPTR记录。<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），连字符（-）以及分隔符（.）构成的以字母和数字开头的字符串，为了兼容DNS9816，支持下划线“_”。<br>- 必须为全地址域名格式，以分隔符结束。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持替换目标域名最大长度为254，结尾必须以分隔符（.）结尾，且不能以x--开头。 |
| NAMESERVER | NS记录的域名服务器 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NS”时为必选参数。<br>参数含义：NS记录的域名服务器参数。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于NS记录。<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），连字符（-）以及分隔符（.）构成的以字母和数字开头的字符串。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持域名服务器最大长度为254，结尾必须以分隔符（.）结尾，且不能以x--开头。 |
| NEW_TTL | 修改后的TTL时间 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“A”、“AAAA” 或 “NS”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“SRV” 或 “NAPTR”时为可选参数。<br>参数含义：非本域DNS保留授权域资源记录的时间，即资源记录的生存周期。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：增加资源记录时，如果未指定资源记录的生存周期，则默认取区域名称的TTL时间作为资源记录的生存周期。 |
| MOD_NAPTR_TYPE | 修改NAPTR记录的字段类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为可选参数。<br>参数含义：修改NAPTR记录的字段类型。<br>数据来源：本端规划<br>取值范围：<br>- NAPTR_ORDER：修改NAPTR记录的顺序值。<br>- NAPTR_PREFERENCE：修改NAPTR记录的偏好值。<br>- NAPTR_ORDER_PREFERENCE：修改NAPTR记录的顺序值和偏好值。<br>默认值：无<br>配置原则：<br>- 修改NAPTR记录的顺序值。<br>- 修改NAPTR记录的偏好值。<br>- 修改NAPTR记录的顺序值和偏好值。 |
| MOD_SRV_TYPE | 修改SRV记录的字段类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“SRV”时为可选参数。<br>参数含义：修改SRV记录的字段类型。<br>数据来源：本端规划<br>取值范围：<br>- SRV_PRIORITY：修改SRV记录的优先级。<br>- SRV_WEIGHT：修改SRV记录的权重。<br>- SRV_PRIORITY_AND_WEIGHT：同时修改SRV记录的优先级和权重。<br>默认值：无<br>配置原则：<br>- 修改SRV记录的顺序值。<br>- 修改SRV记录的偏好值。<br>- 修改SRV记录的顺序值和偏好值。 |
| NEW_PRIORITY | 修改后的SRV记录的优先级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MOD_SRV_TYPE”配置为“SRV_PRIORITY” 或 “SRV_PRIORITY_AND_WEIGHT”时为必选参数。<br>参数含义：修改后的SRV记录的优先级。当查询结果为多条记录时，客户端选择优先级高的记录。当优先级相同时，客户端根据“权重”值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 默认不修改。<br>- 此参数值越小，优先级越高。<br>- 此参数只用于SRV记录。 |
| NEW_WEIGHT | 修改后的SRV记录的权重 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MOD_SRV_TYPE”配置为“SRV_WEIGHT” 或 “SRV_PRIORITY_AND_WEIGHT”时为必选参数。<br>参数含义：修改后的SRV记录的权重。当几条记录的“优先级”值相同时，客户端根据此参数值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 默认不修改。<br>- 此参数值越大，选中概率越高。<br>- 此参数只用于SRV记录。 |
| NEW_ORDER | 修改后的NAPTR记录的顺序值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MOD_NAPTR_TYPE”配置为“NAPTR_ORDER” 或 “NAPTR_ORDER_PREFERENCE”时为必选参数。<br>参数含义：修改后的NAPTR记录的权重。当几条记录的“顺序”值相同时，客户端根据此参数值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 默认不修改。<br>- 此参数值越小，选中的概率越高。<br>- 此参数只用于NAPTR记录。 |
| NEW_PREFERENCE | 修改后的NAPTR记录的偏好值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MOD_NAPTR_TYPE”配置为“NAPTR_PREFERENCE” 或 “NAPTR_ORDER_PREFERENCE”时为必选参数。<br>参数含义：修改后的NAPTR记录的优先级。当查询结果为多条记录时，客户端选择优先级高的记录。当优先级相同时，客户端根据“偏爱”值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 默认不修改。<br>- 此参数值越小，优先级越高。<br>- 此参数只用于NAPTR记录。 |
| NEW_SERVICE | 修改后的NAPTR记录的service | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为可选参数。<br>参数含义：用于NAPTR记录，新目标上的服务，以及该服务交互使用的协议。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 默认不修改。<br>- 通常使用字符“+”连接各个部分。<br>- 根据原域名生成新域名或URI的规则。<br>- 此参数大小写不敏感。<br>- 字段的格式为“x-3gpp-网元类型:x-接口类型-接口协议:x-接口类型-接口协议:……”。<br>- 支持输入大小写字母、数字、“+”、“-”、“：”几类字符。 |

## 操作的配置对象

- [DNS资源记录（RESREC）](configobject/UDG/20.15.2/RESREC.md)

## 使用实例

- 修改一条A记录，“记录类型”选择为“A”记录，“视图名称”填写为“default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“test.cmnet.mnc000.mcc460.gprs.”，“IP”填写为“192.168.1.1”，“修改后的TTL”填写为“600”：
  ```
  MOD RESREC: TYPE=A, VIEWNAME="default", ZONE="cmnet.mnc000.mcc460.gprs", DOMAIN="test.cmnet.mnc000.mcc460.gprs.", IP="192.168.1.1", NEW_TTL=600;
  ```
- 修改一条AAAA记录，“记录类型”选择为“AAAA”记录，“视图名称”填写为“default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“test.cmnet.mnc000.mcc460.gprs.”，“IP”填写为“2001:db8:85a3:8da:131b:8b2e:2590:6354”，“修改后的TTL”填写为“600”：
  ```
  MOD RESREC: TYPE=AAAA, VIEWNAME="default", ZONE="cmnet.mnc000.mcc460.gprs", DOMAIN="test.cmnet.mnc000.mcc460.gprs.", IP="2001:db8:85a3:8da:131b:8b2e:2590:6354", NEW_TTL=600;
  ```
- 修改一条NS记录时，“记录类型”选择为“NS”记录, “视图名称”填写为 “default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“test”，“域名服务器”填写为“dns.shenyang.cmnet.mnc000.mcc460.gprs.”，“修改后的TTL”填写为600：
  ```
  MOD RESREC: TYPE=NS, VIEWNAME="default", ZONE="cmnet.mnc000.mcc460.gprs", DOMAIN="test ", NAMESERVER="dns.shenyang.cmnet.mnc000.mcc460.gprs.", NEW_TTL=600;
  ```
- 修改一条NAPTR纪录时，“纪录类型”选择为“NAPTR”纪录，“视图名称”填写为“default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“test”，“顺序值”填写为10，“偏好值”填写为7，“标志”填写为NULL，“service”填写为“x-3gpp-swg:x-s5-gpt:x-s8-gtp:x-gn”，“正则表达式”为空，“替换域名”填写为“test1.apn.epc.mncxxx.mccyyy.3gppnetwork.orgs.”，“修改后的TTL”填写为800，“修改NAPTR字段类型”选择“修改NAPTR的顺序值与偏好值”，“修改后的顺序值”为12，“修改后的偏好值”填写为9，“修改后的service”填写为“x-3gpp-swg:x-s5-gpt:x-s8-gtp”：
  ```
  MOD RESREC: TYPE=NAPTR, VIEWNAME=" default", ZONE=" cmnet.mnc000.mcc460.gprs, DOMAIN=" test ", ORDER=10, PREFERENCE=7, FLAGS=NULL, SERVICE="x-3gpp-swg:x-s5-gpt:x-s8-gtp:x-gn", REPLACEMENT="test1.apn.epc.mncxxx.mccyyy.3gppnetwork.orgs.", NEW_TTL=800, MOD_NAPTR_TYPE=NAPTR_ORDER_PREFERENCE, NEW_ORDER=12, NEW_PREFERENCE=9, NEW_SERVICE="x-3gpp-swg:x-s5-gpt:x-s8-gtp";
  ```
- 修改一条SRV纪录时，“纪录类型”选择为“SRV”纪录，“视图名称”填写为“default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“test”，“优先级”填写为20，“权重”填写为30，“端口号”填写为22， “目标”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.orgs.”，“修改后的TTL”填写为1200，“修改SRV字段类型”选择“修改SRV的优先级与权重”，“修改后的优先级”为10，“修改后的权重”填写为15：
  ```
  MOD RESREC: TYPE=SRV, ZONE="cmnet.mnc000.mcc460.gprs.", DOMAIN="testmdy", PRIORITY=20, WEIGHT=30, PORT=22, TARGET="apn.epc.mncxxx.mccyyy.3gppnetwork.orgs.", NEW_TTL=1200, MOD_SRV_TYPE=SRV_PRIORITY_AND_WEIGHT, NEW_PRIORITY=10, NEW_WEIGHT=15;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改DNS资源记录（MOD-RESREC）_31214254.md`
