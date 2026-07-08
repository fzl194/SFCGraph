# 查询DCN映射关系(LST DCNMAP)

- [命令功能](#ZH-CN_MMLREF_0000001126145830__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145830__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145830__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145830__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145830__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145830__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145830__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145830)

**适用网元：MME**

该命令用于查询DCN与UE USAGE TYPE的映射关系。

#### [注意事项](#ZH-CN_MMLREF_0000001126145830)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145830)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145830)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145830)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCNID | DCN ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定DCN ID。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |
| BGNUEUSAGETYPE | 起始UE USAGE TYPE | 可选必选说明：可选参数<br>参数含义：该参数用于指定起始UE USAGE TYPE。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145830)

查询 “DCN ID” 为 “1” 的DCN与UE USAGE TYPE的映射关系：

LST DCNMAP: DCNID=1;

```
%%LST DCNMAP: DCNID=1;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
           DCN ID  =  1
起始UE USAGE TYPE  =  150
终止UE USAGE TYPE  =  180
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145830)

参见 [**ADD DCNMAP**](增加DCN映射关系(ADD DCNMAP)_26305638.md) 的参数说明。
