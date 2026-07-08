# 显示SMSF用户关键信息（DSP SMSFKEYDATA）

- [命令功能](#ZH-CN_MMLREF_0000001581200053__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001581200053__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001581200053__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001581200053__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001581200053__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001581200053)

**适用NF：SMSF**

该命令用于查询5G SMSF注册用户的关键信息，包括用户信息、用户短消息签约信息等。

## [注意事项](#ZH-CN_MMLREF_0000001581200053)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001581200053)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001581200053)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示SMSF用户查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “SUPI（SUPI）”：填写用户的IMSI<br>- “GPSI（GPSI）”：填写用户的MSISDN<br>默认值：无<br>配置原则：无 |
| SUPI | SUPI | 可选必选说明：该参数在"QUERYOPT"配置为"SUPI"时为条件必选参数。<br>参数含义：该参数用于表示SMSF用户SUPI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| GPSI | GPSI | 可选必选说明：该参数在"QUERYOPT"配置为"GPSI"时为条件必选参数。<br>参数含义：该参数用于表示SMSF用户GPSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001581200053)

当运营商希望查询SUPI为"123033500100001"的SMSF用户的关键信息时，执行如下命令：

```
DSP SMSFKEYDATA: QUERYOPT=SUPI, SUPI="123033500100001";
%%DSP SMSFKEYDATA: QUERYOPT=SUPI, SUPI="123033500100001";%%
RETCODE = 0  操作成功

结果如下：
------------------------
        SUPI  =  123033500100001
		GPSI  =  8613535000001
        AMF ID  =  AMF_Instance_0
      备份AMF信息 = {amf2.cluster1.net2.amf.5gc.mnc003.mcc460.3gppnetwork.org,46001822700}
        是否签约MT服务  =  TRUE
		是否禁止MT服务  =  FALSE
        是否禁止MT漫游服务  =  FALSE
		是否签约MO服务  =  TRUE
		是否禁止MO服务  =  FALSE
        是否禁止MO漫游服务  =  FALSE
		SMSF号 = 8613902111010
        跟踪区标识 =  12303350101
        NR小区全球标识 =  12303350110201
       GUAMIS = 12303822700
        AMF binding头域 =  NULL
是否由容灾恢复流程创建关键信息 = FALSE
          do索引 = 3
        用户关键信息更新时间  =  2023-07-22 11:30:44.288+00:00

(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0000001581200053)

| 输出项名称 | 输出项解释 |
| --- | --- |
| SUPI | 该参数用于表示SMSF用户SUPI信息。 |
| GPSI | 该参数用于表示SMSF用户GPSI信息。 |
| AMFID | 该参数用于表示SMSF所属的AMF的实例ID。 |
| 备份AMF信息 | 该参数用于表示SMSF用户的所属AMF的备份AMF信息。 |
| 是否签约MT服务 | 该参数用于表示SMSF是否签约MT服务。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| 是否禁止MT服务 | 该参数用于表示SMSF是否禁止MT服务。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| 是否禁止MT漫游服务 | 该参数用于表示SMSF是否禁止MT漫游服务。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| 是否签约MO服务 | 该参数用于表示SMSF是否签约MO服务。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| 是否禁止MO服务 | 该参数用于表示SMSF是否禁止MO服务。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| 是否禁止MO漫游服务 | 该参数用于表示SMSF是否禁止MO漫游服务。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| SMSF号 | 该参数用于表示用SMSF用户所属的SMSF号。 |
| 跟踪区标识 | 该参数用于表示SMSF用户的跟踪区标识。 |
| NR小区全球标识 | 该参数用于表示SMSF用户的NR小区全球标识。 |
| GUAMIS | 该参数用于表示SMSF用户的所属AMF的GUAMI。 |
| AMF binding头域 | 该参数用于表示SMSF用户的AMF binding头域。 |
| 是否由容灾恢复流程创建关键信息 | 该参数用于表示当前关键信息是否由容灾恢复流程创建。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| do索引 | 该参数用于表示关键信息表所存储的do索引。 |
| 用户关键信息更新时间 | 该参数用于表示SMSF用户关键信息更新时间。 |
