# 查询RedCap接入用户的RAT填写值（LST REDCAPRATVALUE）

- [命令功能](#ZH-CN_MMLREF_0000001568306125__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001568306125__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001568306125__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001568306125__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001568306125__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001568306125)

**适用NF：SMF**

该命令用于查询RedCap终端接入时UNC给周边网元UPF，PCF，CHF，N16SMF，N16aSMF，AAAACCT，AAAAUTH发送消息时RatType信元中填写的值。

## [注意事项](#ZH-CN_MMLREF_0000001568306125)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001568306125)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001568306125)

无

## [使用实例](#ZH-CN_MMLREF_0000001568306125)

显示RedCap终端接入与CHF交互时Rat值为NR_REDCAP，PCF交互时Rat值为NR_REDCAP，UPF交互时Rat值为NR_REDCAP，与AAAACCT交互时Rat值为NR_REDCAP，与AAAAUTH交互时Rat值为NR_REDCAP，与N16SMF交互时Rat值为NR_REDCAP，与N16aSMF交互时Rat值为NR_REDCAP：

```
LST REDCAPRATVALUE:;
RETCODE = 0  操作成功

结果如下
------------------------
                  和CHF交互使用的RAT值          =  NR_REDCAP
		  和PCF交互使用的RAT值          =  NR_REDCAP
	          和UPF交互使用的RAT值          =  NR_REDCAP
		  和AAAACCT交互使用的RAT值      =  NR_REDCAP
		  和AAAAUTH交互使用的RAT值      =  NR_REDCAP
		  和N16SMF交互使用的RAT值       =  NR_REDCAP
		  和N16ASMF交互使用的RAT值      =  NR_REDCAP
(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0000001568306125)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 和CHF交互使用的RAT值 | 该参数用于设置和CHF交互使用的RAT值。 |
| 和PCF交互使用的RAT值 | 该参数用于设置和PCF交互使用的RAT值。 |
| 和UPF交互使用的RAT值 | 该参数用于设置和UPF交互使用的RAT值。 |
| 和AAA计费交互使用的RAT值 | 该参数用于设置和ACCT交互使用的RAT值。 |
| 和AAA鉴权交互使用的RAT值 | 该参数用于设置和AUTH交互使用的RAT值。 |
| 和N16SMF交互使用的RAT值 | 该参数用于设置和N16SMF交互使用的RAT值。 |
| 和N16aSMF交互使用的RAT值 | 该参数用于设置和N16aSMF交互使用的RAT值。 |
