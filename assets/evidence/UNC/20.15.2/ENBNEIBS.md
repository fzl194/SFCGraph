# 清除eNodeB邻接关系(CLR ENBNEIBS)

- [命令功能](#ZH-CN_MMLREF_0000001172225937__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225937__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225937__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225937__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225937__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225937__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225937)

**适用网元：MME**

本命令用于清除系统自学习的eNodeB邻接关系。如果要禁用策略寻呼，一般不需要清除系统内的eNodeB邻接关系，而是通过策略寻呼的控制命令 [**SET S1PAGINGCTRL**](../S1寻呼策略管理/设置S1寻呼策略控制表(SET S1PAGINGCTRL)_72345845.md) L完成。

#### [注意事项](#ZH-CN_MMLREF_0000001172225937)

- 此命令执行后立即生效。
- 删除邻接eNodeB会导致无法对邻接eNodeB进行寻呼。
- eNodeB邻接关系学习时间较长，清除系统内已学习到的所有eNodeB邻接关系，将会花一周以上时间才能恢复。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225937)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225937)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225937)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定清除所有还是特定eNodeB的eNodeB邻接列表。<br>取值范围：<br>- “All(All)”<br>- “SINGLE_ENODEB(Single eNodeB)”<br>默认值：无 |
| ENBTYPE | eNodeB类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定中心eNodeB的类型。<br>前提条件：该参数在<br>“操作类型”<br>参数配置为<br>“SINGLE_ENODEB(Single eNodeB)”<br>后生效。<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”<br>- “MACRO_ENODEB(Macro_eNodeB)”<br>默认值：无 |
| MCC | 移动国家代码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定中心eNodeB的移动国家码。<br>前提条件：该参数在<br>“操作类型”<br>参数配置为<br>“SINGLE_ENODEB(Single eNodeB)”<br>后生效。<br>取值范围：3位数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定中心eNodeB的移动网号。<br>前提条件：该参数在<br>“操作类型”<br>参数配置为<br>“SINGLE_ENODEB(Single eNodeB)”<br>后生效。<br>取值范围：2～3位数字<br>默认值：无 |
| ENBID | eNodeB 标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定中心eNodeB的标识。<br>前提条件：该参数在<br>“操作类型”<br>参数配置为<br>“SINGLE_ENODEB(Single eNodeB)”<br>后生效。<br>取值范围：0～268435455(数值型)<br>默认值：无 |
| LUT | 最后更新时间 | 可选必选说明：必选参数<br>参数含义：该参数用于指定清除邻接eNodeB时间阈值：在本参数时间内未更新的邻接eNodeB才被清除。<br>取值范围：0小时～720小时<br>默认值：无<br>说明：当取值是0时，不检查邻接eNodeB的更新时间，清除所有邻接eNodeB。推荐值为0。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225937)

删除所有1小时内未更新的邻接eNodeB关系：

CLR ENBNEIBS: OPTYPE=All, LUT=1;
