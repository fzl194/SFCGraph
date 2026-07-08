# 显示NF属性冲突核验记录（DSP NRFNFATTRVRY）

- [命令功能](#ZH-CN_MMLREF_0000001135519269__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135519269__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135519269__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135519269__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001135519269__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001135519269)

**适用NF：NRF**

该命令用于查询某个NF的属性冲突核验结果。

## [注意事项](#ZH-CN_MMLREF_0000001135519269)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001135519269)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135519269)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示进行属性冲突核验的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。<br>默认值：无<br>配置原则：<br>该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。 |

## [使用实例](#ZH-CN_MMLREF_0000001135519269)

查询某个NF的属性冲突核验结果：

```
DSP NRFNFATTRVRY: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
%%DSP NRFNFATTRVRY: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";%%
RETCODE = 0  操作成功

结果如下
--------
    NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
      核验结果  =  The check is passed.
    NF更新时间  =  2021-03-16 17:59:42
      执行时间  =  2021-03-16 20:17:35
  消耗时长(秒)  =  1
       Pod名称  =  uncpod-0
      核验进度  =  VerifiedNum:2;TotalNum:2;Percentage:100%;
  属性冲突类型  =  No Conflict
NF实例标识集合  =  NULL
下一跳NRFGroup  =  NULL
    NF冲突属性  =  NULL
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001135519269)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF实例标识 | 该参数表示进行属性冲突核验的NF实例标识。 |
| 核验结果 | 该参数表示本次核验的结果。<br>取值说明：<br>- PASS（核验通过）<br>- NOPASS（核验不通过）<br>- TIMEOUT（核验超时）<br>- ERROR（核验出错）<br>- VERIFYING（核验中） |
| NF更新时间 | 该参数表示核验时NF Profile的最新更新时间。 |
| 执行时间 | 该参数表示OPR NRFNFATTRVRY命令执行时间。 |
| 消耗时长(秒) | 该参数表示本次核验消耗时长。 |
| Pod名称 | 该参数表示执行所在的Pod名称。 |
| 核验进度 | 该参数表示当前核验已完成的进度，包括核验属性值的个数及百分比。 |
| 属性冲突类型 | 该参数表示核验结果的冲突类型。<br>取值说明：<br>- NFINTRACONFLICT（NF间属性冲突）<br>- NFREGIONCONFLICT（NF与跨大区路由数据冲突）<br>- NFINTRAANDREGIONCONFLICT（NF间属性冲突&NF与跨大区路由数据冲突）<br>- NFLARGERANGECONFLICT（NF IMSI/MSISDN/TAI/IPv6超大范围段属性冲突）<br>- NOCONFLICT（无冲突） |
| NF实例标识集合 | 该参数用于表示冲突的多个的NFInstanceID。 |
| 下一跳NRFGroup | 该参数用于表示冲突的下一跳的NRFGroup。 |
| NF冲突属性 | 该参数用于表示核验出的冲突属性。 |
