# 查询按签约NSSAI分配Configed NSSAI的PLMN级别开关（LST NSSFCFGSUBSW）

- [命令功能](#ZH-CN_MMLREF_0000001098101324__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001098101324__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001098101324__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001098101324__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001098101324__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001098101324)

**适用NF：NSSF**

该命令用于查询按签约NSSAI生成configuredNssai信元的PLMN级别开关。

## [注意事项](#ZH-CN_MMLREF_0000001098101324)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001098101324)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001098101324)

无

## [使用实例](#ZH-CN_MMLREF_0000001098101324)

若运营商希望查询所有的数据，执行下列命令。

```
LST NSSFCFGSUBSW:;
%%LST NSSFCFGSUBSW:;%%
RETCODE = 0 执行成功

结果如下
------------------------
                       移动国家码  =  245
                         移动网号  =  38
按签约NSSAI分配configuredNssai开关  =  打开
(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0000001098101324)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 移动国家码 | 该参数用于描述移动国家码。 |
| 移动网号 | 该参数用于描述移动网号。 |
| 按签约NSSAI分配configuredNssai开关 | 该参数用于表示NSSF在处理切片选择请求时，响应消息中configuredNssai信元是否直接使用UE签约NSSAI生成。开关打开，configuredNssai信元为UE签约NSSAI；开关关闭，configuredNssai信元为PLMN支持NSSAI和UE签约NSSAI的交集。 |
