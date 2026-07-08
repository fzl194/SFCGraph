---
id: UNC@20.15.2@MMLCommand@LST DMHOSTRT
type: MMLCommand
name: LST DMHOSTRT（查询Diameter主机路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMHOSTRT
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
- Diameter主机路由
status: active
---

# LST DMHOSTRT（查询Diameter主机路由）

## 功能

**适用网元：SGSN、MME**

该命令用来查看Diameter主机路由的配置数据。主机路由是指通过主机名来选择对端。在 UNC 和Diameter对端直连时使用此命令。相同选路模式的主机路由可以通过命令 [**ADD DMRTGRP**](../Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) 配到同一个Diameter路由组中，业务通过引用路由组配置进行选路。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定准备显示的Diameter主机路由的索引。<br>取值范围：0~1023<br>默认值：无<br>说明：如果不输入，表示查询系统内所有Diameter主机路由配置数据。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMHOSTRT]] · Diameter主机路由（DMHOSTRT）

## 使用实例

1. 不输入Diameter主机路由索引，查询已经配置的所有Diameter主机路由数据：
  LST DMHOSTRT:;
  ```
  %%LST DMHOSTRT:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   路由索引  应用名称  选路模式    目的实体选择方式  对端实体索引  对端主机名  路由名称  优先级  权重  

   0         S6a/S6d   优先级权重  对端索引          0             NULL        noname    1       3     
   1         S6a/S6d   优先级权重  对端索引          1             NULL        noname    1       2   
   2         S6a/S6d   优先级权重  对端索引          2             NULL        noname    1       4  
  (结果个数 = 3)

  ---    END
  ```
2. 输入Diameter路由索引，查询指定的Diameter主机路由数据：
  LST DMHOSTRT: ROUTEIDX=0;
  ```
  %%LST DMHOSTRT: ROUTEIDX=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
          路由索引  =  0
          应用名称  =  S6a/S6d
          选路模式  =  优先级权重
  目的实体选择方式  =  对端索引
      对端实体索引  =  0
        对端主机名  =  NULL
          路由名称  =  noname
            优先级  =  1
              权重  =  3
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter主机路由(LST-DMHOSTRT)_72345873.md`
