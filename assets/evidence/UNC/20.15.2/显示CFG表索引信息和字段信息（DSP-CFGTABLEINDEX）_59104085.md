# 显示CFG表索引信息和字段信息（DSP CFGTABLEINDEX）

- [命令功能](#ZH-CN_CONCEPT_0259104085__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0259104085__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0259104085__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0259104085__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0259104085__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0259104085__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0259104085)

该命令用于显示CFG表索引信息和字段信息。

#### [注意事项](#ZH-CN_CONCEPT_0259104085)

该命令仅用于研发问题定位。

#### [操作用户权限](#ZH-CN_CONCEPT_0259104085)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0259104085)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OMUTYPE | OMU类型 | 可选必选说明：必选参数<br>参数含义：主备OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- master：主主控。<br>- slave：备主控。<br>默认值：无 |
| DBTYPE | 数据库类型 | 可选必选说明：必选参数<br>参数含义：数据库类型，包括master，candidate，running等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- candidate：预提交的数据。<br>- running：运行的数据。<br>- paf：PAF数据。<br>- dynamic：动态数据。<br>默认值：无 |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：查询类型，可以查询Table内容，或者查询Table清单等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- table-data：表的数据。<br>- table-list：数据表列表。<br>- table-field：表的字段。<br>- table-index：表的索引。<br>- mem-info：数据表内存信息。<br>默认值：无 |
| TABLENAME | 表名称 | 可选必选说明：条件必选参数，该参数在“QUERYTYPE”配置为“table-data”、“table-field” 或 “table-index”时为必选参数。<br>参数含义：数据库表名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0259104085)

显示CFG表索引信息和字段信息：

```
DSP CFGTABLEINDEX:OMUTYPE=master,DBTYPE=paf,QUERYTYPE=table-list
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0 操作成功

结果如下:
----------
查询结果   =
Field(0)        Field(1)        Field(2)        Field(3)        Field(4)        Field(5)        Field(6)        
Table_Name      Table_Id        MaxRecNum       ActRecNum       RecLength       FieldNum        IndexNum        
defaultrec      0x8             0xfffff         0x9be           0x36            0x7             0x1  

(结果个数 = 1)

--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0259104085)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 查询结果 | 结果信息。 |
