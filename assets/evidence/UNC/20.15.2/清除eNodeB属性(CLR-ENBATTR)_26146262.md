# 清除eNodeB属性(CLR ENBATTR)

- [命令功能](#ZH-CN_MMLREF_0000001126146262__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146262__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146262__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146262__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146262__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146262__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146262)

**适用网元：MME**

该命令用于手工清除指定eNodeB的某种属性信息，以满足业务的可维护需求。MME会通过S1-MME接口的信令消息学习eNodeB的某些属性信息，比如对MTC终端的增强寻呼等信息。

#### [注意事项](#ZH-CN_MMLREF_0000001126146262)

- 此命令执行后立即生效。
- 该命令每次只能清除指定eNodeB的某种属性信息，不支持同时清除两个或两个以上eNodeB的属性信息；
- 指定eNodeB的属性信息被手工清除后，MME仍可能学习到该属性并记录在eNodeB上下文中。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146262)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146262)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146262)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的类型。<br>取值范围：<br>- “HOME_ENODEB(Home eNodeB)”：表示eNodeB类型为家庭基站，其标志长度为28位。<br>- “MACRO_ENODEB(Macro eNodeB)”：表示eNodeB类型为宏基站，其标识长度为20位。<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的移动国家码。<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的移动网号。<br>取值范围：2～3位十进制数字<br>默认值：无 |
| ENBID | eNodeB标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的标识。<br>取值范围：0～268435455<br>默认值：无<br>说明：- 若参数“eNodeB类型”取值为“HOME_ENODEB(Home eNodeB)”，则该参数最大取值268435455。<br>- 若参数“eNodeB类型”取值为“MACRO_ENODEB(Macro eNodeB)”，则该参数最大取值1048575。 |
| ATTRTYPE | 属性类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待清除的属性信息。<br>数据来源：本端规划<br>取值范围：<br>- “RADIOPAGINGCAP(UE无线寻呼能力指示)”<br>- “ENBCEPAGINGCAP(eNodeB覆盖增强寻呼能力指示)”<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126146262)

手动清除一个eNodeB的UE无线寻呼能力指示信息，eNodeB的 “eNodeB类型” 为 “HOME_ENODEB(Home eNodeB)” ， “移动国家码” 为 “123” ， “移动网号” 为 “01” ， “eNodeB标识” 为 “327697” ：

CLR ENBATTR: ENBTYPE=HOME_ENODEB, MCC="123", MNC="01", ENBID=327697, ATTRTYPE=RADIOPAGINGCAP;
