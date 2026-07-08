---
id: UNC@20.15.2@MMLCommand@LST QCICONV
type: MMLCommand
name: LST QCICONV（查询扩展QCI转换关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QCICONV
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- 扩展QCI转换关系
status: active
---

# LST QCICONV（查询扩展QCI转换关系）

## 功能

**适用网元：MME**

该命令用于查询系统中扩展QCI向标准QCI的转换关系配置表。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCIEXT | 扩展QCI基准值 | 可选必选说明：可选参数<br>参数含义：待查询的扩展QCI值。<br>取值范围：10~25<br>默认值：无<br>说明：如果不输入，则表示查询系统中整个扩展QCI向标准QCI的转换关系配置表。 |
| QCISTEP | 扩展QCI范围 | 可选必选说明：可选参数<br>参数含义：待查询的扩展QCI值的范围。<br>取值范围：0~244<br>默认值：无<br>说明：- 该参数必须结合扩展QCI基准值才能生效。<br>- 如果不输入，则表示查询系统中扩展QCI值为扩展QCI基准值向QCI标准值的转换关系。 |

## 操作的配置对象

- [扩展QCI转换关系（QCICONV）](configobject/UNC/20.15.2/QCICONV.md)

## 使用实例

1. 不输入扩展QCI基准值，查询系统中整个扩展QCI向标准QCI的转换关系配置表：
  LST QCICONV:;
  ```
  %%LST QCICONV:;%%
  RETCODE = 0  操作成功。

  QCI转换关系
  -------------
   扩展QCI基准值  标准QCI值

   10             1        
   11             1        
   12             1        
   13             1        
   14             1        
   15             1        
   16             1        
   17             1        
   18             1        
   19             1        
   20             1        
   21             1        
   22             1        
   23             1        
   24             1        
   25             1        
   26             1        
   27             1        
   28             1        
   29             1        
   30             1        
  (结果个数 = 21)

  ---    END
  ```
2. 输入扩展QCI基准值20，不输入扩展QCI的范围值，则查询系统中QCI值为20时向标准QCI的转换关系：
  LST QCICONV: QCIEXT=20;
  ```
  %%LST QCICONV: QCIEXT=20;%%
  RETCODE = 0  操作成功。

  QCI转换关系
  -------------
  扩展QCI基准值  =  20
      标准QCI值  =  1
  (结果个数 = 1)

  ---    END
  ```
3. 输入扩展QCI基准值20，输入扩展QCI的范围值10，则查询系统中QCI值从20到30内向标准QCI的转换关系：
  LST QCICONV: QCIEXT=20, QCISTEP=10;
  ```
  %%LST QCICONV: QCIEXT=20, QCISTEP=10;%%
  RETCODE = 0  操作成功。

  QCI转换关系
  -------------
   扩展QCI基准值  标准QCI值

   20             1        
   21             1        
   22             1        
   23             1        
   24             1        
   25             1        
   26             1        
   27             1        
   28             1        
   29             1        
   30             1        
  (结果个数 = 11)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询扩展QCI转换关系(LST-QCICONV)_72225893.md`
