---
id: UNC@20.15.2@MMLCommand@LST COMMONSOFTPARA
type: MMLCommand
name: LST COMMONSOFTPARA（查询公共软参）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: COMMONSOFTPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软件参数管理
status: active
---

# LST COMMONSOFTPARA（查询公共软参）

## 功能

该命令用于查询公共软件参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- “DwCom（公共双字）”：公共双字<br>默认值：无<br>配置原则：无 |
| DWORDCOMNUM | Common Dword索引 | 可选必选说明：该参数在"DATATYPE"配置为"DwCom"时为条件可选参数。<br>参数含义：该参数表示Common Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1500。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@COMMONSOFTPARA]] · 公共软参（COMMONSOFTPARA）

## 使用实例

查询公共软件参数，数据类型是“DwCom”，Common Dword索引是“1”

```
LST COMMONSOFTPARA: DATATYPE=DwCom, DWORDCOMNUM=1;
RETCODE = 0  执行成功

操作结果如下:
-------------------------
     数据类型  =  公共双字
 软参记录索引  =  1
   软参记录值  =  3
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-COMMONSOFTPARA.md`
