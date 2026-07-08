# 修改本地HLR(MOD LOCALHLR)

- [命令功能](#ZH-CN_MMLREF_0000001172345677__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345677__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345677__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345677__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345677__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345677__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345677)

**适用网元：SGSN**

该命令用于修改本地HLR。

#### [注意事项](#ZH-CN_MMLREF_0000001172345677)

- 该命令执行后立即生效。
- 此配置涉及漫游用户QoS限制特性（特性编号：WSFD-105002，License部件编码：LKV2RSQR01），执行命令请使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345677)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345677)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345677)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HLRIDX | 本地HLR索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HLR索引。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无 |
| HLRNUM | 本地HLR号码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户归属的HLR的HLR号码。<br>UNC<br>将Update Location Ack消息中携带的HLR号码和本参数的配置进行匹配。如果匹配成功，则认为此UE是本地用户，否则为异地用户。<br>数据来源：整网规划<br>取值范围：1~16位十进制数字<br>默认值：无<br>配置原则：<br>HLR号码采用E.164（International PSTN/ISDN numbers）编码方式，编码格式为：CC+NDC+LSP。<br>- CC：国家码（Country Code），标识MS注册的国家。<br>- NDC：国内目的码（National Destination Code），标识MS对应的PLMN。<br>- LSP: 本地有效部分（Locally Significant Part），由运营商和其网络所在国家的编号机构达成一致。 |
| HLRNAME | 本地HLR名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户归属HLR的名称。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串。<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345677)

将索引为1的本地HLR信息，修改成号码为8612345678，名称为LOCALHLR1:

MOD LOCALHLR: HLRIDX=1, HLRNUM="8612345678", HLRNAME="LOCALHLR1";
