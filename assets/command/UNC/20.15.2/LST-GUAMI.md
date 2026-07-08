---
id: UNC@20.15.2@MMLCommand@LST GUAMI
type: MMLCommand
name: LST GUAMI（查询AMF全局标识）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GUAMI
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- AMF全局标识符管理
status: active
---

# LST GUAMI（查询AMF全局标识）

## 功能

**适用NF：AMF**

该命令用于查询AMF全局标识符以及备用AMF信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | GUAMI索引 | 可选必选说明：可选参数<br>参数含义：该参数用以在UNC系统内唯一标识某个GUAMI，一个AMF可以最多定义256个GUAMI。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GUAMI]] · AMF全局标识（GUAMI）

## 使用实例

- 查询系统中AMF当前关联的“GUAMI索引”为“0”的GUAMI列表，执行如下命令：
  ```
  %%LST GUAMI: INDEX=0;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    GUAMI索引  =  0
     PLMN索引  =  0
  AMF区域标识  =  00
  AMF集合标识  =  001
    AMF指示符  =  01
  备用AMF名称  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中AMF当前关联的GUAMI列表，执行如下命令：
  ```
  %%LST GUAMI:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    GUAMI索引  =  0
     PLMN索引  =  0
  AMF区域标识  =  00
  AMF集合标识  =  001
    AMF指示符  =  01
  备用AMF名称  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF全局标识（LST-GUAMI）_09652365.md`
