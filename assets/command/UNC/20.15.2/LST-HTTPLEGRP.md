---
id: UNC@20.15.2@MMLCommand@LST HTTPLEGRP
type: MMLCommand
name: LST HTTPLEGRP（查询HTTP本端实体组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPLEGRP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP本端实体组管理
status: active
---

# LST HTTPLEGRP（查询HTTP本端实体组）

## 功能

该命令用于查询HTTP本端实体组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP本端实体组的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPLEGRP]] · HTTP本端实体组（HTTPLEGRP）

## 使用实例

- 若想查询一组索引为1的HTTP本端实体组的相关信息：
  ```
  %%LST HTTPLEGRP: INDEX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  索引  =  1
  描述  =  AMF
  (结果个数 = 1)

  ---    END
  ```
- 若想查询所有的配置的HTTP本端实体组的相关信息：
  ```
  %%LST HTTPLEGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  索引  描述  

  1      AMF          
  3      NRF          
  4      NSSF         
  5      BSF          
  (结果个数 = 4)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HTTPLEGRP.md`
