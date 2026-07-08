---
id: UNC@20.15.2@MMLCommand@LST DMLKS
type: MMLCommand
name: LST DMLKS（查询Diameter链路集配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMLKS
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter链路集
status: active
---

# LST DMLKS（查询Diameter链路集配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查看Diameter链路集配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKSIDX | Diameter链路集索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定准备显示的Diameter链路集的索引。<br>取值范围：0～639<br>默认值：无<br>说明：如果不输入，表示查询系统内所有Diameter链路集配置数据。 |

## 操作的配置对象

- [Diameter链路集配置（DMLKS）](configobject/UNC/20.15.2/DMLKS.md)

## 使用实例

1. 不输入Diameter链路集索引，查询已经配置的所有Diameter链路集数据：
  LST DMLKS:;
  ```
  LST DMLKS:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   Diameter链路集索引  本地实体索引  对端实体索引  选路模式  链路集名称

   0                   0             0             轮选      To-HSS0    
   1                   0             1             轮选      To-HSS1    
  (结果个数 = 2)
  ---    END
  ```
2. 输入Diameter链路集索引，查询指定的Diameter链路集数据：
  LST DMLKS: LINKSIDX=0;
  ```
  %%LST DMLKS: LINKSIDX=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
  Diameter链路集索引  =  0
        本地实体索引  =  0
        对端实体索引  =  0
            选路模式  =  轮选
          链路集名称  =  To-HSS0
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter链路集配置(LST-DMLKS)_26146280.md`
