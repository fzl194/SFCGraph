# 增加区域（ADD ZONE）

- [命令功能](#ZH-CN_CONCEPT_0000207114777353__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000207114777353__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000207114777353__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000207114777353__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000207114777353__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000207114777353)

**适用NF：CloudEPSN**

本命令实现增加区域名称的功能。

#### [注意事项](#ZH-CN_CONCEPT_0000207114777353)

- 该命令执行后立即生效。
- 除了CloudDNS外其他场景，需要依次执行SET DNSINFO、GEN DNSTASKID、EXC DNSCFGTASK初始化MML命令后，可以开始使用ADD ZONE命令。
- 在新增“区域名称”时，不能一次增加多层区域名称，只能增加一层，即当前区域名称为“cmnet.mnc000.mcc460.gprs”，只能增加为“test.cmnet.mnc000.mcc460.gprs”，不能增加为 “test1.test.cmnet.mnc000.mcc460.gprs”。

#### [操作用户权限](#ZH-CN_CONCEPT_0000207114777353)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000207114777353)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 任务ID | 可选必选说明：可选参数<br>参数含义：任务ID。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- CloudDNS无需配置此参数。<br>- 由GEN DNSTASKID生成，用于确定任务ID。 |
| VIEWNAME | 视图名称 | 可选必选说明：可选参数<br>参数含义：资源所属的域名解析视图名称。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 输入资源所属的域名解析视图名称。<br>- CloudDNS中视图默认值为"default"。<br>- CloudDNS当前支持视图最大规格为32字符。<br>- 视图最后一位不支持特殊字符。<br>- 执行命令时需要保证视图存在。 |
| ZONE | 区域名称 | 可选必选说明：必选参数<br>参数含义：资源记录的区域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持字符串最大长度为249，结尾必须以分隔符（.）结尾。 |
| DEPLOYABLE | 是否可部署 | 可选必选说明：可选参数<br>参数含义：部署。<br>数据来源：本端规划<br>取值范围：<br>- FALSE：否。<br>- TRUE：是。<br>默认值：无<br>配置原则：<br>- CloudDNS不设置此参数。<br>- 如果选择TRUE，则设置为部署；如果选择选择FALSE，则设置为不可部署；默认不选为不可部署。 |

#### [使用实例](#ZH-CN_CONCEPT_0000207114777353)

- CloudDNS场景：添加一条区域名称，“视图名称”填写为“default”，“区域名称”填写为“test.cmnet.mnc000.mcc460.gprs”：
  ```
  ADD ZONE: VIEWNAME="default", ZONE="test.cmnet.mnc000.mcc460.gprs";
  ```
- 其他场景：添加一条区域名称，“任务id”填写为“1”，“视图名称”填写为“default”，“区域名称”填写为“test.cmnet.mnc000.mcc460.gprs”，“部署”填写为“不可部署”：
  ```
  ADD ZONE: TASKID=1, VIEWNAME="default", ZONE="test.cmnet.mnc000.mcc460.gprs", DEPLOYABLE=FALSE;
  ```
