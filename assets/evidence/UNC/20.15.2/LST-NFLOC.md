# 查询目标NF发现和选择的位置匹配信息（LST NFLOC）

- [命令功能](#ZH-CN_MMLREF_0209653245__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653245__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653245__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653245__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653245__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653245)

**适用NF：AMF、SMF**

该命令用于查询为目标NF的发现和选择配置的位置匹配相关的信息。

## [注意事项](#ZH-CN_MMLREF_0209653245)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653245)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653245)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务发现的目标NF的请求者的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “NfAMF（NfAMF）”：AMF<br>- “NfSMF（NfSMF）”：SMF<br>默认值：无<br>配置原则：无 |
| TGTNFTYPE | 目标NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目标NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “NF_ALL（所有NF）”：所有NF<br>- “UDM（UDM）”：UDM<br>- “AMF（AMF）”：AMF<br>- “SMF（SMF）”：SMF<br>- “AUSF（AUSF）”：AUSF<br>- “PCF（PCF）”：PCF<br>- “SMSF（SMSF）”：SMSF<br>- “NSSF（NSSF）”：NSSF<br>- “LMF（LMF）”：LMF<br>- “GMLC（GMLC）”：GMLC<br>- “FIFTHG_EIR（5G_EIR）”：5G_EIR<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653245)

查询AMF在发现SMF时使用的优选区域信息，执行如下命令：

```
%%LST NFLOC: NFTYPE=NfAMF;%%
RETCODE = 0  操作成功

结果如下
--------
    NF类型  =  NfAMF
目标NF类型  =  所有NF
  位置类型  =  优选位置
  优选位置  =  DC2
  描述信息  =  prefer the NFs of DC2
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209653245)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于表示服务发现的目标NF的请求者的NF类型。 |
| 目标NF类型 | 该参数用于表示目标NF的类型。 |
| 位置类型 | 该参数用于表示目标NF发现和选择流程中用作匹配条件的位置类型。 |
| 优选位置 | 该参数用于表示目标NF的优选位置，即在该指定位置中的目标NF将被优先选择。 |
| 描述信息 | 该参数是对本NF配置优选区域的描述信息，在运维中起助记的作用。 |
