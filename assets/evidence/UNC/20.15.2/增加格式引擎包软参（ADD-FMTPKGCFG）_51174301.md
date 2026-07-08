# 增加格式引擎包软参（ADD FMTPKGCFG）

- [命令功能](#ZH-CN_CONCEPT_0251174301__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0251174301__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0251174301__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0251174301__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0251174301__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0251174301__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0251174301)

![](增加格式引擎包软参（ADD FMTPKGCFG）_51174301.assets/notice_3.0-zh-cn_2.png)

此命令不能动态生效，需要执行“RST VNFC”重启服务。

**适用NF：NCG**

该命令用于增加格式引擎包的软参配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0251174301)

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 该命令最大记录数为4096。

#### [本地用户权限](#ZH-CN_CONCEPT_0251174301)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0251174301)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0251174301)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRFNAME | 格式引擎包名 | 可选必选说明：必选参数<br>参数含义：用于返回查询到的格式引擎配置包名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：“格式引擎包名称”可以通过<br>[**LST CDRPROC**](../话单处理/查询话单处理（LST CDRPROC）_51174275.md)<br>命令查询获取。 |
| CFGNAME | 格式引擎包软参名称 | 可选必选说明：必选参数<br>参数含义：用于返回格式引擎配置的软参名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：“格式引擎包软参名称”可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令获取，其他名称无法生效。 |
| CFGTYPE | 格式引擎软参类型 | 可选必选说明：必选参数<br>参数含义：格式引擎软参类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FEM_PARA_ENUM：FEM_PARA_ENUM。<br>- FEM_PARA_UINT：FEM_PARA_UINT。<br>- FEM_PARA_IPADDR：FEM_PARA_IPADDR。<br>- FEM_PARA_STRING：FEM_PARA_STRING。<br>默认值：无<br>配置原则：需与“格式引擎包软参名称”对应的“格式引擎包软参类型”匹配，“格式引擎包软参类型”可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令查询获取。 |
| CFG_BOOL_VALUE | 格式引擎软参值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CFGTYPE”配置为“FEM_PARA_ENUM”时为条件必选参数。<br>参数含义：与“格式引擎包软参名称”对应的取值范围为0～1的整数类型软参值，该值的具体含义可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1。<br>默认值：0<br>配置原则：“格式引擎软参值”在“格式引擎包软参名称”对应的“格式引擎包软参取值范围”内，“格式引擎包软参取值范围”可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令查询获取。 |
| CFG_UINT_VALUE | 格式引擎软参值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CFGTYPE”配置为“FEM_PARA_UINT”时为条件必选参数。<br>参数含义：与“格式引擎包软参名称”对应的整数类型的软参值，该值的具体含义可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令查询获取。例如格式引擎包“PS_R15_VF80_CBN.tar.gz”中，整数类型的软参名为“MergeSwitch”的含义为“是否开启话单合并功能”。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：0<br>配置原则：“格式引擎软参值”在“格式引擎包软参名称”对应的“格式引擎包软参取值范围”内，“格式引擎包软参取值范围”可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令查询获取。 |
| CFG_IP_VALUE | 格式引擎软参值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CFGTYPE”配置为“FEM_PARA_IPADDR”时为条件必选参数。<br>参数含义：与“格式引擎包软参名称”对应的IPv4地址类型的软参值，该值的具体含义可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：“格式引擎软参值”在“格式引擎包软参名称”对应的“格式引擎包软参取值范围”内，“格式引擎包软参取值范围”可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令查询获取。 |
| CFG_STR_VALUE | 格式引擎软参值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CFGTYPE”配置为“FEM_PARA_STRING”时为条件必选参数。<br>参数含义：与“格式引擎包软参名称”对应的字符串类型的软参值，该值的具体含义可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令查询获取。例如格式引擎包“PS_R15_VF80_CBN.tar.gz”中，字符串类型的软参名为“InnerRuBackup”的含义为“第二份最终话单在RU间备份的分发任务名称”。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～512。<br>默认值：无<br>配置原则：“格式引擎软参值”在“格式引擎包软参名称”对应的“格式引擎包软参取值范围”内，“格式引擎包软参取值范围”可以通过<br>[**DSP FMTSOFTPARA**](查询格式引擎包所有可配置软参（DSP FMTSOFTPARA）_51174305.md)<br>命令查询获取。 |

#### [使用实例](#ZH-CN_CONCEPT_0251174301)

用于增加格式引擎包软参：

整数类型：

```
ADD FMTPKGCFG: PRFNAME="PS_R9_V940_M_RT.tar.gz", CFGNAME="MaxDuration", CFGTYPE=FEM_PARA_UINT, CFG_UINT_VALUE=500;
```

字符类型：

```
ADD FMTPKGCFG: PRFNAME="PS_R15_VF80_NorthChina_CMCC.tar.gz", CFGNAME="BeijingIDList", CFGTYPE=FEM_PARA_STRING, CFG_STR_VALUE="FE80:172:0:150";
```
