# 查询ServiceFabric软参（LST FWSOFTPARA）

- [命令功能](#ZH-CN_MMLREF_0318818229__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0318818229__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0318818229__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0318818229__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0318818229__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0318818229)

该命令用于查询ServiceFabric的软件参数信息。

## [注意事项](#ZH-CN_MMLREF_0318818229)

软参索引取值区间：1-2048。

#### [操作用户权限](#ZH-CN_MMLREF_0318818229)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0318818229)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAMETERSTYPE | 参数类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的类型。<br>数据来源：本端规划<br>取值范围：<br>- DWORD（双字）<br>- DWORD_EX（扩展双字）<br>默认值：无<br>配置原则：无 |
| DWORDINDEX | DWORD索引 | 可选必选说明：该参数在"PARAMETERSTYPE"配置为"DWORD"时为条件可选参数。<br>参数含义：该参数表示Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无<br>配置原则：无 |
| EXTENDDWORDINDEX | 扩展DWORD索引 | 可选必选说明：该参数在"PARAMETERSTYPE"配置为"DWORD_EX"时为条件可选参数。<br>参数含义：该参数表示Dword extend类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0318818229)

查询软参值

```
%%LST FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1;%%
RETCODE = 0  操作成功

结果如下
--------
 参数类型  =  双字
DWORD索引  =  1
DWORD取值  =  0
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0318818229)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 参数类型 | 该参数表示软件参数的类型。 |
| 扩展DWORD索引 | 该参数表示Dword extend类型软件参数的索引。 |
| 扩展DWORD取值 | 该参数表示Dword extend类型软件参数的值。 |
| DWORD索引 | 该参数表示Dword类型软件参数的索引。 |
| DWORD取值 | 该参数表示Dword类型软件参数的值。 |
