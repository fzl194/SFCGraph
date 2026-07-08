# 显示规则匹配报文信息构造状态（DSP RULEMATCHPARA）

- [命令功能](#ZH-CN_CONCEPT_0000202989650065__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202989650065__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202989650065__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202989650065__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202989650065__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000202989650065__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202989650065)

**适用NF：PGW-U、UPF**

该命令用于显示规则匹配报文信息构造状态。

#### [注意事项](#ZH-CN_CONCEPT_0000202989650065)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202989650065)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202989650065)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PACKETSOURCE | 报文信息来源 | 可选必选说明：可选参数<br>参数含义：规则匹配时选择的报文信息来源。<br>数据来源：本端规划<br>取值范围：<br>- USER_DEFINED：表示选择规则匹配时使用的报文信息为自定义。<br>默认值：无<br>配置原则：指定报文信息来源。 |

#### [使用实例](#ZH-CN_CONCEPT_0000202989650065)

显示规则匹配报文信息构造状态：

```
DSP RULEMATCHPARA: PACKETSOURCE=USER_DEFINED;
```

```

RETCODE = 0  Operation succeeded

The Status Of Packet Information Construction Required For Rule Matching
------------------------------------------------------------------------
                       Source of The Packet Information  =  user defined
Status Of Rule Matching Packet Information Construction  =  done
(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000202989650065)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 报文信息来源 | 规则匹配时选择的报文信息来源。 |
| 规则匹配报文信息构造状态 | 表示规则匹配报文信息构造状态。 |
