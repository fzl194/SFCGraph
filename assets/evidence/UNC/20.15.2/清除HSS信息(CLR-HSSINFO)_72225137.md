# 清除HSS信息(CLR HSSINFO)

- [命令功能](#ZH-CN_MMLREF_0000001172225137__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225137__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225137__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225137__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225137__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225137__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225137)

**适用网元：SGSN、MME**

该命令用于模拟HSS RESET流程，将注册在该HSS的用户“SGSN Location Information Confirmed in HLR/HSS”或“MME Location Information Confirmed in HLR/HSS”标识和自学习主机名等与HSS相关的信息置为无效。

#### [注意事项](#ZH-CN_MMLREF_0000001172225137)

HSS割接或者HSS修改本端主机名前使用此命令，以保证用户信息在SGSN/MME和HSS上一致。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225137)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225137)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225137)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSSHTNAME | HSS主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HSS主机名。<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：不能为非法字符，只允许输入字母，数字，“.”和“-”，大小写不敏感。例如：hss.epc.mnc123.mcc123.3gppnetwork.org |

#### [使用实例](#ZH-CN_MMLREF_0000001172225137)

清除主机名为hss.epc.mnc123.mcc123.3gppnetwork.org的HSS在SGSN/MME的相关信息：

CLR HSSINFO: HSSHTNAME="hss.epc.mnc123.mcc123.3gppnetwork.org";
