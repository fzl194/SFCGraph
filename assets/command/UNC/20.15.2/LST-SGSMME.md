---
id: UNC@20.15.2@MMLCommand@LST SGSMME
type: MMLCommand
name: LST SGSMME（查询SGS MME实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGSMME
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SGS MME实体
status: active
---

# LST SGSMME（查询SGS MME实体）

## 功能

**适用NF：SMSF**

该命令用于查询配置的SGS MME实体。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEX | MME索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个MME实体，在全局范围内唯一。<br>数据来源：本端规划<br>取值范围：0～1999。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGSMME]] · SGS MME实体（SGSMME）

## 使用实例

查询已经配置的所有的SGS MME实体记录。

```
%%LST SGSMME:;%%
RETCODE = 0  操作成功 
The result is as follows 
------------------------ 
MME索引     MME名          MME POOL标识     MME容量权重     
1           46000800101     126              23
2           46000800102     125              25
(结果个数 = 2)  
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGSMME.md`
