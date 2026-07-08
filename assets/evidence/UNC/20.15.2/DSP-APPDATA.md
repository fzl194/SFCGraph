# 显示APPDB表数据（DSP APPDATA）

- [命令功能](#ZH-CN_CONCEPT_0259103691__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0259103691__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0259103691__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0259103691__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0259103691__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0259103691__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0259103691)

该命令用于显示APPDB表数据和表信息。

#### [注意事项](#ZH-CN_CONCEPT_0259103691)

该命令仅用于研发问题定位。

#### [操作用户权限](#ZH-CN_CONCEPT_0259103691)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0259103691)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCINDEX1 | 进程ID | 可选必选说明：必选参数<br>参数含义：进程ID（当在VNFP服务实例上执行该命令时，该参数通过<br>[**DSP RESPROCESSINFO**](../../../../../单体服务平台功能管理/操作维护/系统调测/进程和组件信息/显示进程信息（DSP RESPROCESSINFO）_04641826.md)<br>命令获取，其他服务实例上执行该命令时，该参数通过<br>[**DSP PROCESSINFO**](../../进程和组件信息/显示进程信息（DSP PROCESSINFO）_59103523.md)<br>命令获取）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：查询类型，可以查询Table内容，或者查询Table清单等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- table-data：表的数据。<br>- table-list：数据表列表。<br>- table-field：表的字段。<br>- table-index：表的索引。<br>默认值：无 |
| TABLENAME | 表名称 | 可选必选说明：条件必选参数，该参数在“QUERYTYPE”配置为“table-data”、“table-field” 或 “table-index”时为必选参数。<br>参数含义：数据库表名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无 |
| INDEX | 起始索引 | 可选必选说明：条件可选参数，该参数在“QUERYTYPE”配置为“table-data”时为可选参数。<br>参数含义：起始索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| DBTYPE | 数据库类型 | 可选必选说明：必选参数<br>参数含义：数据库类型，包括master，candidate，running等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- app：业务。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0259103691)

显示APPDB表数据和表信息：

```
DSP APPDATA:LOCINDEX1=3,QUERYTYPE=table-list,DBTYPE=app
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
----------
查询结果  
Field(0)        Field(1)        Field(2)        Field(3)        Field(4)        Field(5)        Field(6)        
Table_Name      Table_Id        MaxRecNum       ActRecNum       RecLength       FieldNum        IndexNum       
 
vAlmMonitor     0x19            0x1fffe         0x2             0x91            0x6             0x1             
vAlarmCutOut    0x1a            0x1fffe         0x0             0x4             0x1             0x1             
vAlmReportHost  0x1b            0x1fffe         0x0             0x6d            0x5             0x1             
vFomByFim       0x1c            0x1fffe         0x5c            0x9             0x3             0x1             
vFomAlarmDic    0x1d            0x13ff          0x22            0x71            0xd             0x1             
vFimAlarmDic    0x1e            0x13ff          0x22            0xcf            0x7             0x1             
CFGOsNodeInfo   0x24            0x20000         0x2             0x40            0x9             0x1             
CFGLocGrp       0x2a            0x20000         0xa             0x3c            0x8             0x1             
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0259103691)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 查询结果 | 结果信息。 |
