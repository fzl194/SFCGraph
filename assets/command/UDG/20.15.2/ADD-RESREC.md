---
id: UDG@20.15.2@MMLCommand@ADD RESREC
type: MMLCommand
name: ADD RESREC（增加DNS资源记录）
nf: UDG
version: 20.15.2
verb: ADD
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

# ADD RESREC（增加DNS资源记录）

## 功能

**适用NF：CloudEPSN**

本命令实现增加A、AAAA、NS、SRV、NAPTR记录的功能。

## 注意事项

- 该命令执行后立即生效。
- （CloudDNS无需执行）在依次执行SET DNSINFO、GEN DNSTASKID、EXC DNSCFGTASK初始化MML命令后，可以开始使用ADD RESREC命令。
- “域名”参数中分为绝对域名和部分域名，其中绝对域名即参数“域名”以“.”结尾；部分域名即参数“域名”不以“.”结尾，命令下发后，系统会自动将部分域名和区域名称拼接成绝对域名。例如：当参数“域名”不是以“.”结尾，是部分域名时：“区域名称”为“mnc000.mcc460.gprs”，“域名”为“cmnet”，绝对域名为“cmnet.mnc000.mcc460.gprs.”。
- “域名”参数输入为“@”时，设定为与当前区域名称同名的域名。（CloudDNS不支持此功能）。
- 在选择“记录类型”为“A”记录或“AAAA”记录时，出现“IP”参数进行输入，其中“IP”参数使用时，每次新增IP数量不能超过20个。
- 在选择“记录类型”为“AAAA”记录时，IPV6地址支持输入缩写。
- 在选择“记录类型”为“A”记录或“AAAA”记录时，若除“IP”参数不同外，其余参数一致，则进行追加操作；当“IP”参数与原记录没有重复时追加成功，否则追加失败。
- 在选择“记录类型”为“SRV”记录或“NAPTR”记录或“NS”记录时，改变任意参数，则为新增一条新记录。
- TTL输入为空时，则当前新增的域名TTL值，被赋予当前区域名称的TTL值。
- 当增加记录除TTL参数外参数一致时，无法增加该记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 任务ID | 可选必选说明：可选参数<br>参数含义：任务ID。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- CloudDNS无需配置此参数。<br>- 由GEN DNSTASKID生成，用于确定任务ID。 |
| TYPE | 记录类型 | 可选必选说明：必选参数<br>参数含义：增加的记录类型。<br>数据来源：本端规划<br>取值范围：<br>- A：A记录。<br>- AAAA：AAAA记录。<br>- NAPTR：NAPTR记录。<br>- SRV：SRV记录。<br>- NS：NS记录。<br>默认值：无<br>配置原则：<br>- A记录：由域名解析出IPV4地址的记录。<br>- AAAA记录：由域名解析出IPV6地址的记录。<br>- NS记录：配置区域所属的授权域名服务器的记录。<br>- SRV记录：根据某项服务的域名解析出主机名的记录。<br>- NAPTR记录：根据域名解析出替换域名的记录。 |
| VIEWNAME | 视图名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“SRV”、“A”、“AAAA”、“NAPTR” 或 “NS”时为可选参数。<br>参数含义：资源所属的域名解析视图名称。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 输入资源所属的域名解析视图名称。<br>- CloudDNS中视图默认值为"default"。<br>- CloudDNS当前支持视图最大规格为32字符。<br>- 视图最后一位不支持特殊字符。<br>- 执行命令时必须保证视图存在。 |
| ZONE | 区域名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”、“A”、“AAAA”、“NAPTR” 或 “NS”时为必选参数。<br>参数含义：资源记录的区域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持字符串最大长度为249，结尾必须以分隔符（.）结尾。 |
| DOMAIN | 域名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”、“A”、“AAAA”、“NAPTR” 或 “NS”时为必选参数。<br>参数含义：资源记录的域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 域名可以是完整域名，此时以（.）作为结束符；也可以是部分域名，此时不能以点（.）作为结束符，系统会自动将部分域名和区域名一起拼接成完整域名。<br>- 只输入“@”字符表示用同名与区域名称的域名。（CloudDNS当前不支持此功能）。<br>- 为了兼容DNS9816，在记录类型选择SRV、NAPTR、NS时候，支持输入下划线“_”。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS支持的最大长度为254字节，且不支持xn—开头。 |
| TTL | TTL | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“SRV”、“A”、“AAAA”、“NAPTR” 或 “NS”时为可选参数。<br>参数含义：非本域DNS保留授权域资源记录的时间，即资源记录的生存周期。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 增加资源记录时，如果未指定资源记录的生存周期，则默认取区域名称的TTL时间作为资源记录的生存周期。<br>- CloudDNS中TTL的默认值为3600。 |
| IP | IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“A” 或 “AAAA”时为必选参数。<br>参数含义：IP地址。<br>数据来源：全网规划<br>取值范围：最多支持输入20个IP地址。<br>默认值：无<br>配置原则：<br>- 当type选择A记录的时候，ip参数支持输入IPV4地址。 IPV4地址不能为0.0.0.0、255.255.255.255和环回地址等非法地址。<br>- 当type选择AAAA记录的时候，ip参数支持输入IPV6地址。 IPV6地址不能为全0、全F和环回地址等非法地址。 支持输入IPV6缩写地址和全量地址输入。 |
| PRIORITY | 优先级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”时为必选参数。<br>参数含义：SRV记录的优先级。当查询结果为多条记录时，客户端选择优先级高的记录。当优先级相同时，客户端根据“权重”值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数值越小，优先级越高。<br>- 此参数只用于SRV记录。 |
| WEIGHT | 权重 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”时为必选参数。<br>参数含义：SRV记录的权重。当几条记录的“优先级”值相同时，客户端根据此参数值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数值越大，选中概率越高。<br>- 此参数只用于SRV记录。 |
| PORT | 端口号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”时为必选参数。<br>参数含义：用于SRV记录，服务器上提供该种服务的端口号。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于SRV记录。<br>- CloudDNS不支持将端口设置为0。 |
| TARGET | 目标域名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“SRV”时为必选参数。<br>参数含义：用于SRV记录，提供该种服务的服务器域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于SRV记录。<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），连字符（-）以及分隔符（.）构成的以字母和数字开头的字符串。<br>- 必须为全地址域名格式，以分隔符结束。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持目标域名最大长度为254，结尾必须以分隔符（.）结尾，且不能以xn--开头。 |
| ORDER | 顺序 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：NAPTR记录的权重。当几条记录的“顺序”值相同时，客户端根据此参数值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于NAPTR记录。<br>- 此参数值越小，选中的概率越高。 |
| PREFERENCE | 偏好 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：NAPTR记录的优先级。当查询结果为多条记录时，客户端选择优先级高的记录。当优先级相同时，客户端根据“偏爱”值选择一条记录。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于NAPTR记录。<br>- 此参数值越小，优先级越高。 |
| FLAGS | 标志 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：用于NAPTR记录，表示下一次查询的类型。<br>数据来源：全网规划<br>取值范围：<br>- S：S。<br>- A：A。<br>- U：U。<br>- AAAA：AAAA。<br>- NULL：NULL。<br>默认值：无<br>配置原则：<br>- S：表示新域名为SRV记录域名，下一次需要进行SRV查询。<br>- A：表示新域名为A记录域名，下一次需要进行A记录查询。<br>- U：表示本次结果是满足RFC2396标准的absoluteURI，下次不需要进行DNS查询。<br>- AAAA：表示新域名为AAAA记录域名，下一次需要进行AAAA查询。<br>- NULL：表示下次还需要进行NAPTR查询。<br>- CloudDNS中不支持配置AAAA，若参数选为AAAA会自动转换为A。 |
| SERVICE | service | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：用于NAPTR记录，新目标上的服务，以及该服务交互使用的协议。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 通常使用字符“+”连接各个部分。<br>- 根据原域名生成新域名或URI的规则。<br>- 此参数大小写不敏感。<br>- 字段的格式为“x-3gpp-网元类型:x-接口类型-接口协议:x-接口类型-接口协议:……”。<br>- 支持输入大小写字母、数字、“+”、“-”、“：”几类字符。 |
| REGEXP | 正则表达式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为可选参数。<br>参数含义：NAPTR记录的正则表达式。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：此参数只用于NAPTR记录。 |
| REPLACEMENT | 替换域名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NAPTR”时为必选参数。<br>参数含义：NAPTR记录的替换域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于NAPTR记录。<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），连字符（-）以及分隔符（.）构成的以字母和数字开头的字符串，为了兼容DNS9816，支持下划线“_”。<br>- 必须为全地址域名格式，以分隔符结束。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持替换目标域名最大长度为254，结尾必须以分隔符（.）结尾，且不能以xn--开头。 |
| NAMESERVER | 域名服务器 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“NS”时为必选参数。<br>参数含义：NS记录的域名服务器参数。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 此参数只用于NS记录。<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），连字符（-）以及分隔符（.）构成的以字母和数字开头的字符串。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持域名服务器最大长度为254，结尾必须以分隔符（.）结尾，且不能以xn--开头。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RESREC]] · DNS资源记录（RESREC）

## 使用实例

- 添加一条A记录，“任务id”填写为“1”（CloudDNS无需配置），“记录类型”选择为“A”记录，“视图名称”填写为“default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“test.cmnet.mnc000.mcc460.gprs.”，“TTL”填写为“800”，“IP”填写为“192.168.1.1”：
  ```
  ADD RESREC: TYPE=A, VIEWNAME="default", ZONE="cmnet.mnc000.mcc460.gprs", DOMAIN="test.cmnet.mnc000.mcc460.gprs.",TTL=800,IP="192.168.1.1";
  ```
- 添加一条AAAA记录，“任务id”填写为“1” （CloudDNS无需配置），“记录类型”选择为“AAAA”记录，“视图名称”填写为“default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“test.cmnet.mnc000.mcc460.gprs”，“TTL”填写为“800”，“IP”填写为“2001:db8:85a3:8da:131b:8b2e:2590:6354”：
  ```
  ADD RESREC: TYPE=AAAA,VIEWNAME="default",ZONE="cmnet.mnc000.mcc460.gprs",DOMAIN="test.cmnet.mnc000.mcc460.gprs.",TTL=800,IP="2001:db8:85a3:8da:131b:8b2e:2590:6354";
  ```
- 添加一条NAPTR记录，“任务id”填写为“1” （CloudDNS无需配置），“记录类型”选择为“NAPTRA”记录，“视图名称”填写为“default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“test”，“TTL”填写为“800”，“顺序”填写为“10”，“偏好”填写为“10”，“标志”选择为“S”记录，“服务”填写为“x-3gpp-sgw:x-s5-gtp:x-s8-gtp:x-gn”，不采用正则表达式，“替换域名”填写为“test1.cmnet.mnc000.mcc460.gprs.”：
  ```
  ADD RESREC: TYPE=NAPTR, VIEWNAME="default", ZONE="cmnet.mnc000.mcc460.gprs", DOMAIN="test", TTL=800, ORDER=10, PREFERENCE=10, FLAGS=S, SERVICE="x-3gpp-sgw:x-s5-gtp:x-s8-gtp:x-gn", REPLACEMENT="test1.cmnet.mnc000.mcc460.gprs.";
  ```
- 添加一条SRV记录，“任务id”填写为“1” （CloudDNS无需配置），“记录类型”选择为“SRV”记录，“视图名称”填写为“default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“testmdy”，“TTL” 填写为“800”，“优先级”填写为“10”，“权重”填写为“7”，“端口”填写为“8080”，“目标”填写为“test1.cmnet.mnc000.mcc460.gprs.”：
  ```
  ADD RESREC: TYPE=SRV, VIEWNAME="default", ZONE="cmnet.mnc000.mcc460.gprs", DOMAIN="testmdy", TTL=800, PRIORITY=10, WEIGHT=7, PORT=8080, TARGET="test1.cmnet.mnc000.mcc460.gprs.";
  ```
- 添加一条NS记录，“任务id”填写为“1” （CloudDNS无需配置），“记录类型”选择为“NS”记录，“视图名称”填写为“default”，“区域名称”填写为“cmnet.mnc000.mcc460.gprs”，“域名”填写为“test.cmnet.mnc000.mcc460.gprs.”，“TTL”填写为“800”，“域名服务器”填写为“dns.shenyang.cmnet.mnc000.mcc460.gprs.”：
  ```
  ADD RESREC: TYPE=NS, VIEWNAME="default", ZONE="cmnet.mnc000.mcc460.gprs", DOMAIN="test.cmnet.mnc000.mcc460.gprs.", TTL=800, NAMESERVER="dns.shenyang.cmnet.mnc000.mcc460.gprs.";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-RESREC.md`
