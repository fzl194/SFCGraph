# 设置PLMN的计费属性参数(SET CHGPLMNCHAR)

- [命令功能](#ZH-CN_MMLREF_0000001126305204__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305204__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305204__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305204__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305204__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305204__1.3.6.1)
- [参考信息](#ZH-CN_MMLREF_0000001126305204__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305204)

**适用网元：SGSN**

该命令用于设置某个PLMN类型的用户计费属性的参数配置。

#### [注意事项](#ZH-CN_MMLREF_0000001126305204)

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 如果该命令配置了禁止生成某种话单，不管[**ADD CHGPLMNCFG**](../PLMN计费配置/增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md)、[**ADD CHGIMSICFG**](../IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)、[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)配置何种类型的值，都不生成话单；如果本命令配置了允许生成某种话单，用户是否生成话单将由[**ADD CHGPLMNCFG**](../PLMN计费配置/增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md)、[**ADD CHGIMSICFG**](../IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)、[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)中的配置决定。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305204)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305204)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305204)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMN | PLMN 类型 | 可选必选说明：必选参数<br>参数含义：该参数用于运营商对不同PLMN用户的话单生成采取不同的策略。<br>数据来源：整网规划<br>取值范围：<br>- “HPLMN（本地 PLMN）”：表示本网用户。<br>- “VPLMN（拜访 PLMN）”：表示拜访用户，非本网用户即拜访用户 。<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305204__tab1)<br>。 |
| MP | 生成M-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性用户是否生成M-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO（不生成）”<br>- “YES（生成）”<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305204__tab1)<br>。 |
| SP | 生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性用户是否生成S-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO（不生成）”<br>- “YES（生成）”<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305204__tab1)<br>。 |
| SMOP | 生成S-SMO-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性用户是否生成S-SMO-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO（不生成）”<br>- “YES（生成）”<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305204__tab1)<br>。 |
| SMTP | 生成S-SMT-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性用户是否生成S-SMT-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO（不生成）”<br>- “YES（生成）”<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305204__tab1)<br>。 |
| LCSMOP | 生成LCS-MO-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性用户是否生成LCS-MO-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO（不生成）”<br>- “YES（生成）”<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305204__tab1)<br>。 |
| LCSMTP | 生成LCS-MT-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性用户是否生成LCS-MT-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO（不生成）”<br>- “YES（生成）”<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305204__tab1)<br>。 |
| LCSNIP | 生成LCS-NI-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性用户是否生成LCS-NI-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO（不生成）”<br>- “YES（生成）”<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126305204__tab1)<br>。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305204)

设置本网用户的话单控制属性“生成S-SMO-CDR”为不生成，配置格式如下：

SET CHGPLMNCHAR: PLMN=HPLMN, SMOP=NO;

#### [参考信息](#ZH-CN_MMLREF_0000001126305204)

*表1 系统初始设置值*

| PLMN 类型 | 生成M-CDR | 生成S-CDR | 生成S-SMO-CDR | 生成S-SMT-CDR | 生成LCS-MO-CDR | 生成LCS-MT-CDR | 生成LCS-NI-CDR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HPLMN | YES | YES | YES | YES | YES | YES | YES |
| VPLMN | YES | YES | YES | YES | YES | YES | YES |
