# 删除特征RFSP取值(RMV SPECRFSPVALUE)

- [命令功能](#ZH-CN_MMLREF_0000001172225215__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225215__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225215__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225215__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225215__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225215__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225215)

**适用网元：SGSN、MME**

该命令用于把一组RFSP从特征RFSP(RAT/Frequency Selection Priority)中删除。

#### [注意事项](#ZH-CN_MMLREF_0000001172225215)

此命令执行后立即生效。

此命令执行后起始RFSP对应的整条记录都将被删除。

如果待删除的 “RFSPIDX(特征RFSP索引)” “RFSPIDX(特征RFSP索引)” 被其他命令引用，则该 “RFSPIDX(特征RFSP索引)” 下至少保留一条记录。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225215)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225215)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225215)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RFSPIDX | 特征RFSP索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要被删除的特征RFSP索引，该索引标识了一组RFSP取值。<br>数据来源：本端规划<br>取值范围：0~49<br>默认值：无 |
| BEGRFSP | 起始RFSP | 可选必选说明：必选参数<br>参数含义：该参数用于指定一段连续特征RFSP的起始值。<br>取值范围：1~256<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225215)

把一组RFSP从特征RFSP(RAT/Frequency Selection Priority)中删除：

RMV SPECRFSPVALUE: RFSPIDX=0, BEGRFSP=1;
