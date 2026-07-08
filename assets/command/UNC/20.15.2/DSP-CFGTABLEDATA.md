---
id: UNC@20.15.2@MMLCommand@DSP CFGTABLEDATA
type: MMLCommand
name: DSP CFGTABLEDATA（显示满足条件的CFG表数据）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CFGTABLEDATA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 配置维护
- 配置数据
status: active
---

# DSP CFGTABLEDATA（显示满足条件的CFG表数据）

## 功能

该命令用于显示满足条件的CFG表数据。

## 注意事项

该命令仅用于研发问题定位。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OMUTYPE | OMU类型 | 可选必选说明：必选参数<br>参数含义：主备OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- master：主主控。<br>- slave：备主控。<br>默认值：无 |
| DBTYPE | 数据库类型 | 可选必选说明：必选参数<br>参数含义：数据库类型，包括master，candidate，running等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- master：master数据。<br>- candidate：预提交的数据。<br>- running：运行的数据。<br>- cfg：CFG数据。<br>- paf：PAF数据。<br>- base：base数据。<br>- dynamic：动态数据。<br>默认值：无 |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：查询类型，可以查询Table内容，或者查询Table清单等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- table-data：表的数据。<br>- table-list：数据表列表。<br>- table-field：表的字段。<br>- table-index：表的索引。<br>- mem-info：数据表内存信息。<br>默认值：table-data |
| TABLENAME | 表名称 | 可选必选说明：条件必选参数，该参数在“QUERYTYPE”配置为“table-data”、“table-field” 或 “table-index”时为必选参数。<br>参数含义：数据库表名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无 |
| INDEX | 起始索引 | 可选必选说明：条件可选参数，该参数在“QUERYTYPE”配置为“table-data”时为可选参数。<br>参数含义：起始索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| NUM | 查询记录数 | 可选必选说明：条件可选参数，该参数在“QUERYTYPE”配置为“table-data”时为可选参数。<br>参数含义：查询得到的记录数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [满足条件的CFG表数据（CFGTABLEDATA）](configobject/UNC/20.15.2/CFGTABLEDATA.md)

## 使用实例

显示满足条件的CFG表数据：

```
DSP CFGTABLEDATA:OMUTYPE=master,DBTYPE=cfg,QUERYTYPE=table-list
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
---------
查询结果    
Field(0)        Field(1)        Field(2)        Field(3)        Field(4)        Field(5)        Field(6)        
Table_Name      Table_Id        MaxRecNum       ActRecNum       RecLength       FieldNum        IndexNum
        
StpTBL          0x0             0x1000          0x2             0x94            0x6             0x1             

(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示满足条件的CFG表数据（DSP-CFGTABLEDATA）_59103913.md`
