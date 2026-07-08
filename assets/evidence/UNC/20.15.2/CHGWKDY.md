# 设置星期配置(SET CHGWKDY)

- [命令功能](#ZH-CN_MMLREF_0000001126305210__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305210__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305210__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305210__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305210__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305210__1.3.6.1)
- [参考信息](#ZH-CN_MMLREF_0000001126305210__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305210)

**适用网元：SGSN**

该命令用于设置普通计费属性用户、预付费计费属性用户、包月制计费属性用户或实时计费属性用户的周一到周日的费率属性是正常工作日还是休息日。该命令与费率时段配置（ [**ADD CHGTARI**](../计费费率时段配置/增加费率时段配置(ADD CHGTARI)_26305208.md) ）相结合，进行灵活的费率时段控制。该命令的配置是为了实现对S-CDR话单进行不同费率时段的计费。

#### [注意事项](#ZH-CN_MMLREF_0000001126305210)

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 在星期配置表中，“星期序号”和“计费属性”唯一确定一条记录。
- 同一计费属性的周记录数固定为7，本表记录总数固定为28。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305210)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305210)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305210)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WKDAY | 星期序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个星期中的某一天。<br>数据来源：整网规划<br>取值范围：<br>- “MON(星期一)”<br>- “TUES(星期二)”<br>- “WED(星期三)”<br>- “THURS(星期四)”<br>- “FRI(星期五)”<br>- “SAT(星期六)”<br>- “SUN(星期日)”<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305210__tab1)<br>。 |
| CC | 计费属性 | 可选必选说明：必选参数<br>参数含义：该参数用来指定该天对普通计费属性用户、预付费计费属性用户、包月制计费属性用户还是对实时计费属性用户有效。<br>数据来源：整网规划<br>取值范围：<br>- “NORMAL(普通计费)”：表示普通计费属性，按照此种方式计费的用户按照常规的方式支付费用。<br>- “PREPAID(预付费)”：表示预付费计费属性，按照此种方式计费的用户在获取某种服务之前需要预支付一定的费用。<br>- “FLATRATE(包月制)”：表示包月制计费属性，按照此种方式计费的用户在一个月内的收费是固定的。<br>- “HOTBILLING(实时计费)”：表示实时计费属性，按照此种方式计费的用户将在短时间或流量达到某个值时及时生成话单，保证运营商对此类用户及时收费。<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305210__tab1)<br>。 |
| TT | 费率类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示是该天的费率类型。<br>数据来源：整网规划<br>取值范围：<br>- “WORK(工作日)”<br>- “WEEKEND(周休日)”<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305210__tab1)<br>。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305210)

设置一条包月制计费属性的星期表配置：将包月制计费属性的星期六的费率类型改为工作日，配置格式为：

SET CHGWKDY: WKDAY=SAT, CC=FLATRATE, TT=WORK;

#### [参考信息](#ZH-CN_MMLREF_0000001126305210)

*表1 系统初始设置值*

| 星期序号 | 计费属性 | 费率类型 |
| --- | --- | --- |
| SUN | HOTBILLING | WEEKEND |
| SAT | HOTBILLING | WEEKEND |
| FRI | HOTBILLING | WORK |
| THURS | HOTBILLING | WORK |
| WED | HOTBILLING | WORK |
| TUES | HOTBILLING | WORK |
| MON | HOTBILLING | WORK |
| SUN | FLATRATE | WEEKEND |
| SAT | FLATRATE | WEEKEND |
| FRI | FLATRATE | WORK |
| THURS | FLATRATE | WORK |
| WED | FLATRATE | WORK |
| TUES | FLATRATE | WORK |
| MON | FLATRATE | WORK |
| SUN | PREPAID | WEEKEND |
| SAT | PREPAID | WEEKEND |
| FRI | PREPAID | WORK |
| THURS | PREPAID | WORK |
| WED | PREPAID | WORK |
| TUES | PREPAID | WORK |
| MON | PREPAID | WORK |
| SUN | NORMAL | WEEKEND |
| SAT | NORMAL | WEEKEND |
| FRI | NORMAL | WORK |
| THURS | NORMAL | WORK |
| WED | NORMAL | WORK |
| TUES | NORMAL | WORK |
| MON | NORMAL | WORK |
