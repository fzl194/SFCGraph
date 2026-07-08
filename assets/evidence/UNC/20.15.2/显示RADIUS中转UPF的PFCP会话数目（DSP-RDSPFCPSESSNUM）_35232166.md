# 显示RADIUS中转UPF的PFCP会话数目（DSP RDSPFCPSESSNUM）

- [命令功能](#ZH-CN_MMLREF_0000001135232166__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135232166__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135232166__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135232166__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001135232166__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001135232166)

**适用NF：PGW-C、SMF、GGSN**

该命令用于显示RADIUS中转UPF，UPC创建的会话数目。

## [注意事项](#ZH-CN_MMLREF_0000001135232166)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001135232166)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135232166)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（全部）<br>- UPFID（UP实例标识）<br>默认值：无<br>配置原则：无 |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"UPFID"时为条件必选参数。<br>参数含义：该参数用于指示UPF实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001135232166)

查询所有RADIUS中转UPF的会话数量。 DSP RDSPFCPSESSNUM: QUERYTYPE=ALL;

```
%%DSP RDSPFCPSESSNUM: QUERYTYPE=ALL;%%
RETCODE = 0  操作成功。

结果如下
------------------------
RADIUS中转UPF的PFCP会话数目  =  4
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001135232166)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RADIUS中转UPF的PFCP会话数目 | 表示Radius中转UPF会话的数量。 |
