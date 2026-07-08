---
id: UNC@20.15.2@MMLCommand@DSP DMRT
type: MMLCommand
name: DSP DMRT（显示Diameter域路由状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DMRT
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
- Diameter路由
status: active
---

# DSP DMRT（显示Diameter域路由状态）

## 功能

**适用网元：SGSN、MME**

该命令用户查询Diameter域路由状态。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的Diameter域路由索引。<br>取值范围：0~2047<br>默认值：无<br>说明：如果不输入，表示查询系统内所有Diameter域路由的状态。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMRT]] · Diameter域路由配置（DMRT）

## 使用实例

1. 不输入查询参数，查询所有Diameter域路由信息：
  DSP DMRT:;
  ```
  %%DSP DMRT:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   路由索引  路由名称  路由状态

   0         TO-HSS0   正常    
   1         TO-HSS1   故障    
  (结果个数 = 2)
  ---    END
  ```
2. 输入Diameter域路由索引，查询指定的Diameter域路由状态信息：
  DSP DMRT: ROUTEIDX=0;
  ```
  %%DSP DMRT: ROUTEIDX=0;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
  路由索引  =  0
  路由名称  =  TO-HSS0
  路由状态  =  正常
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示Diameter域路由状态(DSP-DMRT)_26306102.md`
