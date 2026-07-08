---
id: UNC@20.15.2@MMLCommand@LST DBDRAGING
type: MMLCommand
name: LST DBDRAGING（查询CSDB容灾数据老化开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DBDRAGING
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# LST DBDRAGING（查询CSDB容灾数据老化开关）

## 功能

该命令用于查询CSDB容灾数据老化开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LDRINSTID | 本端容灾实例ID | 可选必选说明：可选参数。<br>参数含义：本端容灾实例ID，可使用<br>**[LST DRINST](查询容灾实例(LST DRINST)_51012924.md)**<br>命令查询获取。如果不输入本参数，则表示查询所有本端容灾实例ID的容灾老化开关。<br>数据来源：全网规划<br>取值范围：0～63。<br>默认值：无。 |
| PDRINSTID | 对端容灾实例ID | 可选必选说明：可选参数。<br>参数含义：对端容灾实例ID，可使用<br>**[LST DRCOMM](查询容灾实例地址(LST DRCOMM)_51012928.md)**<br>命令查询获取。如果不输入本参数，则表示查询所有对端容灾实例ID的容灾老化开关。<br>数据来源：全网规划<br>取值范围：0~63。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DBDRAGING]] · CSDB容灾数据老化开关（DBDRAGING）

## 使用实例

查询所有容灾数据老化开关：

```
LST DBDRAGING:;
%%LST DBDRAGING:;%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
本端容灾实例ID  =  0
对端容灾实例ID  =  1
容灾老化开关    =  关闭容灾老化功能
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSDB容灾数据老化开关(LST-DBDRAGING)_92511652.md`
