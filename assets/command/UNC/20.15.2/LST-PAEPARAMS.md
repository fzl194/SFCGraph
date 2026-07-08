---
id: UNC@20.15.2@MMLCommand@LST PAEPARAMS
type: MMLCommand
name: LST PAEPARAMS（查询PAE参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PAEPARAMS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- PAE软参
status: active
---

# LST PAEPARAMS（查询PAE参数）

## 功能

该命令用于查询PAE服务的相关参数。PAE主要功能是为微服务通信提供报文高速转发及适配。

## 注意事项

参数"PARAVALUE2"仅作为保留域，暂未启用。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAID | 参数ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定PAE参数ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PAEPARAMS]] · PAE参数（PAEPARAMS）

## 使用实例

查询PAE参数：

```
+++    UNC/*MEID:0 MENAME:unc*/        2025-03-25 17:22:47
O&M    #51
%%LST PAEPARAMS:;%%
RETCODE = 0  操作成功

结果如下
--------
参数ID  第一个参数值  第二个参数值  

0       1             NULL          
1       1             NULL          
2       1             NULL          
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PAEPARAMS.md`
