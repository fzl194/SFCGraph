# 增加eNodeB邻接关系(ADD ENBNSINDB)

- [命令功能](#ZH-CN_MMLREF_0000001172345859__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345859__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345859__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345859__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345859__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345859__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345859)

**适用网元：MME**

此命令用于手动添加eNodeB邻接关系。当激活“WSFD- 206001 LTE精准寻呼”特性时，整网所有eNodeB邻接关系的学习是一个漫长的过程，往往需要一周以上的时间，通过此命令可以避免等待系统自动学习邻接关系的大量时间消耗和切换流程的触发。

#### [注意事项](#ZH-CN_MMLREF_0000001172345859)

- 此命令执行后立即生效。
- 此命令最大记录数为10。
- 此命令仅用于测试、演示目的，在特性正式使用时，eNodeB邻接关系通过Handover等流程学习获取，而不能通过此命令添加。
- 通过此命令配置eNodeB邻接关系时，UNC通过SON消息和Handover流程学习的eNodeB邻接关系将被清除。
- 通过此命令配置的eNodeB邻接关系不会自动老化，若想删除eNodeB邻接关系，请执行[**RMV ENBNSINDB**](删除配置的eNodeB邻接关系(RMV ENBNSINDB)_26146260.md)命令。
- 当激活“WSFD-215202基于eNodeB覆盖等级的寻呼”特性后，若通过[**DSP MMCTX**](../../系统管理/用户数据库管理/显示MM上下文(DSP MMCTX)_26306164.md)命令查询的MM上下文中“推荐的eNodeB列表”非空，则此命令配置的邻接eNodeB列表失效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345859)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345859)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345859)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB和邻接eNodeB共用的类型。<br>数据来源：整网规划<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”：表示中心eNodeB类型为家庭基站，其标志长度为28位。<br>- “MACRO_ENODEB(Macro_eNodeB)”：表示中心eNodeB类型为宏基站，其标识长度为20位。<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB和邻接eNodeB共用的移动国家码。<br>数据来源：整网规划<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB和邻接eNodeB共用的移动网号。<br>数据来源：整网规划<br>取值范围：2～3位十进制数字<br>默认值：无 |
| ENBID | eNodeB标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB的ID。<br>数据来源：整网规划<br>取值范围：0～268435455<br>默认值：无<br>配置原则：<br>- 当“eNodeB类型”为“HOME_ENODEB(Home_eNodeB)”时，本参数的输入范围为0～268435455。<br>- 当“eNodeB类型”为“MACRO_ENODEB(Macro_eNodeB)”时，本参数的输入范围为0～1048575。 |
| NEIBLIST | 邻接eNodeB列表 | 可选必选说明：必选参数<br>参数含义：该参数用于指定邻接eNodeB列表，建立中心eNodeB及其邻接eNodeB关系。<br>数据来源：整网规划<br>取值范围：1～640位字符串<br>默认值：无<br>配置原则：<br>- 每个eNodeB的邻接eNodeB最大个数为64个。<br>- 每个eNodeB标识的取值范围为0～268435455。<br>- eNodeB标识之间有且只有一个“&”用以分隔。<br>- 每条记录内的邻接eNodeB标识不能与该记录的中心eNodeB标志相同。<br>- 每条记录内的邻接eNodeB标识不能重复。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345859)

手动添加一条eNodeB邻接关系，中心eNodeB的 “eNodeB类型” 为 “HOME_ENODEB(Home_eNodeB)” ， “移动国家码” 为 “123” ， “移动网号” 为 “01” ， “eNodeB标识” 为 “327697” ，其邻接的eNodeB标识分别为327696、327698、327699：

ADD ENBNSINDB: ENBTYPE=HOME_ENODEB, MCC="123", MNC="01", ENBID=327697, NEIBLIST="327696&327698&327699";
