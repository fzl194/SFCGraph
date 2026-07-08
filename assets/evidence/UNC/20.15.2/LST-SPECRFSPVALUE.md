# 查询特征RFSP取值(LST SPECRFSPVALUE)

- [命令功能](#ZH-CN_MMLREF_0000001126305346__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305346__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305346__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305346__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305346__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305346__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305346__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305346)

**适用网元：SGSN、MME**

该命令用于查询特征RFSP(RAT/Frequency Selection Priority)的取值范围。

#### [注意事项](#ZH-CN_MMLREF_0000001126305346)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305346)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305346)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305346)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RFSPIDX | 特征RFSP索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定特征RFSP索引，该索引标识了一组或多组RFSP取值。<br>取值范围：0~49<br>默认值：无 |
| TYPE | 特征RFSP索引类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该特征RFSP索引的类型。<br>取值范围：<br>- “IMS_VOPS(IMS VoPS限制)”：表示该特征RFSP范围用于IMS VoPS限制。<br>- “ENODEB_IND(eNodeB指示)”：表示该特征RFSP范围用于将签约RFSP ID映射成SPID。<br>- “ACC_REJECT(区域接入控制)”：表示该特征RFSP范围用于区域接入控制。<br>默认值：无 |
| RFSP | RFSP | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个待查询的RFSP值。<br>取值范围：1~256<br>默认值：无<br>说明：如果指定该参数，则会将所有满足该RFSP值在起始RFSP和终止RFSP之间的所有结果输出，起始RFSP和终止RFSP为通过<br>[**ADD SPECRFSPVALUE**](增加特征RFSP取值(ADD SPECRFSPVALUE)_26145534.md)<br>命令添加的两个参数。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305346)

查询特征RFSP(RAT/Frequency Selection Priority)的取值范围：

LST SPECRFSPVALUE:;

```
%%LST SPECRFSPVALUE:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
    特征RFSP索引  =  0
特征RFSP索引类型  =  区域接入控制
        起始RFSP  =  1
        终止RFSP  =  10
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305346)

参见 [**ADD SPECRFSPVALUE**](增加特征RFSP取值(ADD SPECRFSPVALUE)_26145534.md) 的参数说明。
