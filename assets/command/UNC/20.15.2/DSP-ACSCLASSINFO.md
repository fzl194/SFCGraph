---
id: UNC@20.15.2@MMLCommand@DSP ACSCLASSINFO
type: MMLCommand
name: DSP ACSCLASSINFO（查询配置表信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ACSCLASSINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 维护管理
status: active
---

# DSP ACSCLASSINFO（查询配置表信息）

## 功能

该命令用于查询ACS配置表的记录个数。

## 注意事项

该命令只支持查询配置类表的记录个数，不支持其他类。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| CLASSNAME | 表名称 | 可选必选说明：可选参数。<br>参数含义：配置类表的表名称。<br>取值范围：字符串类型，长度不超过15个字符。<br>默认值：无。<br>配置原则：当不输入<br>“表名称”<br>时表示查询所有配置类表的记录个数。输入<br>“表名称”<br>时注意区分大小写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACSCLASSINFO]] · 配置表信息（ACSCLASSINFO）

## 使用实例

查询所有配置类表的记录个数时，执行以下命令：

```
%%DSP ACSCLASSINFO:;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
  记录个数  =  2024553 
失败表个数  =  2 
(结果个数 = 1)  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询配置表信息(DSP-ACSCLASSINFO)_24524970.md`
