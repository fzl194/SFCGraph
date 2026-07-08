---
id: UDG@20.15.2@MMLCommand@LST FWSOFTPARA
type: MMLCommand
name: LST FWSOFTPARA（查询ServiceFabric软参）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FWSOFTPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软参配置管理
status: active
---

# LST FWSOFTPARA（查询ServiceFabric软参）

## 功能

该命令用于查询ServiceFabric的软件参数信息。

> **说明**
> 软参索引取值区间：1-2048。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAMETERSTYPE | 参数类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的类型。<br>数据来源：本端规划<br>取值范围：<br>- DWORD（双字）<br>- DWORD_EX（扩展双字）<br>默认值：无<br>配置原则：无 |
| DWORDINDEX | DWORD索引 | 可选必选说明：该参数在"PARAMETERSTYPE"配置为"DWORD"时为条件可选参数。<br>参数含义：该参数表示Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无<br>配置原则：无 |
| EXTENDDWORDINDEX | 扩展DWORD索引 | 可选必选说明：该参数在"PARAMETERSTYPE"配置为"DWORD_EX"时为条件可选参数。<br>参数含义：该参数表示Dword extend类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ServiceFabric软参（FWSOFTPARA）](configobject/UDG/20.15.2/FWSOFTPARA.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ServiceFabric软参（LST-FWSOFTPARA）_18818229.md`
