---
id: UDG@20.15.2@MMLCommand@LST DIGIW
type: MMLCommand
name: LST DIGIW（查询电子保单信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DIGIW
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 版本信息
status: active
---

# LST DIGIW（查询电子保单信息）

## 功能

本命令用于查询指定网元的电子保单信息，包含首次上电时间、服务起始时间以及服务年限。

> **说明**
> 无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要按照哪个网元ID来查询电子保单信息。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：可以使用<br>[**LST ME**](查询网元配置信息（LST ME）_47084797.md)<br>命令查询获得。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DIGIW]] · 电子保单信息（DIGIW）

## 使用实例

查询电子保单信息：

```
%%LST DIGIW: MEID=55;%%
RETCODE = 0  操作成功
 
操作结果如下
------------
  首次上电时间  =  2012-01-17
  服务起始时间  =  2021-06-10
服务年限（月）  =  120
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询电子保单信息（LST-DIGIW）_75544595.md`
