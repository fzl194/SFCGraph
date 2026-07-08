---
id: UNC@20.15.2@MMLCommand@LST NGIPAREAGRP
type: MMLCommand
name: LST NGIPAREAGRP（查询5G IP区域群）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGIPAREAGRP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- IP细分管理
- 5G IP细分区域组管理
status: active
---

# LST NGIPAREAGRP（查询5G IP区域群）

## 功能

**适用NF：AMF**

该命令用于查询5G IP区域群记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域群标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGIPAREAGRP]] · 5G IP区域群（NGIPAREAGRP）

## 使用实例

- 不输入查询条件，查询表中全部IP区域群记录，执行如下命令：
  ```
  %%LST NGIPAREAGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  区域群标识  IP区域开关  漫游用户开关  

  Shanghai    关闭        关闭                
  SomeCity    关闭        关闭               
  (结果个数 = 2)

  ---    END
  ```
- 查询“区域群标识”为“SomeCity”的IP区域群记录，执行如下命令：
  ```
  %%LST NGIPAREAGRP: AREAID="SomeCity";%%
  RETCODE = 0  操作成功

  结果如下
  --------
        区域群标识  =  SomeCity
        IP区域开关  =  关闭
      漫游用户开关  =  关闭
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGIPAREAGRP.md`
