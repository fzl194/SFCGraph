---
id: UNC@20.15.2@MMLCommand@LST NGTAGP
type: MMLCommand
name: LST NGTAGP（查询5G TA群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGTAGP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN跟踪区管理
- NGRAN跟踪区群组管理
status: active
---

# LST NGTAGP（查询5G TA群组）

## 功能

**适用NF：AMF**

该命令用于查询TA群组记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAGPID | 跟踪区群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~256。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGTAGP]] · 5G TA群组（NGTAGP）

## 使用实例

- 查询所有TA群组记录。
  ```
  %%LST NGTAGP:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  跟踪区群组标识  跟踪区群组描述  

  1            shanghai
  2            nanjing       
  (结果个数 = 2)

  ---    END
  ```
- 查询跟踪区群组标识为1的记录。
  ```
  %%LST NGTAGP: NGTAGPID=1;%%
  RETCODE = 0   操作成功

  结果如下
  ------------------------
    跟踪区群组标识  =  1
    跟踪区群组描述  =  shanghai
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGTAGP.md`
