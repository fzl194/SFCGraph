---
id: UNC@20.15.2@MMLCommand@LST VLROFFLOADLAILST
type: MMLCommand
name: LST VLROFFLOADLAILST（查询位置区列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLROFFLOADLAILST
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- 基于LAI的IMSI分离配置信息
status: active
---

# LST VLROFFLOADLAILST（查询位置区列表）

## 功能

**适用网元：MME**

该命令用于查询并显示待处理的LAI列表。

## 注意事项

- 该命令执行后立即生效。
- 若未输入参数，表示查询LAI列表中所有记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | LAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区标识，标识一个位置区。<br>数据来源：整网规划<br>取值范围：9～10位的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLROFFLOADLAILST]] · 位置区列表（VLROFFLOADLAILST）

## 使用实例

1. 查看 “LAI” 为 “308015101” 的位置区信息：
  LST VLROFFLOADLAILST: LAI="308015101";
  ```
  %%LST VLROFFLOADLAILST: LAI="308015101";%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
     LAI  =  308015101
  (结果个数 = 1)
  ---    END
  ```
2. 查看系统中所有的位置区信息:
  LST VLROFFLOADLAILST:;
  ```
  %%LST VLROFFLOADLAILST:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   LAI      

   308015101
   308014103
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询位置区列表(LST-VLROFFLOADLAILST)_26145428.md`
