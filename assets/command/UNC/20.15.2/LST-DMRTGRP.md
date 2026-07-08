---
id: UNC@20.15.2@MMLCommand@LST DMRTGRP
type: MMLCommand
name: LST DMRTGRP（查询Diameter路由组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMRTGRP
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
- Diameter路由组
status: active
---

# LST DMRTGRP（查询Diameter路由组）

## 功能

**适用网元：SGSN、MME**

该命令用来查看Diameter路由组的配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPIDX | 路由组索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定准备显示的Diameter路由的索引。<br>取值范围：0~1023<br>默认值：无<br>说明：如果不输入，表示查询系统内所有Diameter路由组配置数据。 |
| RTMODE | 路由模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该条路由的路由索引对应的路由模式。<br>数据来源：整网规划<br>取值范围：<br>- “REALM_ROUTE（域路由）”：表示该条路由组的路由模式为域路由模式；<br>- “HOST_ROUTE（主机路由）”：表示该条路由组的路由模式为主机路由模式<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMRTGRP]] · Diameter路由组（DMRTGRP）

## 使用实例

1. 不输入Diameter路由组索引，查询已经配置的所有Diameter路由组数据：
  LST DMRTGRP:;
  ```
  %%LST DMRTGRP:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   路由组索引  路由模式  路由优选模式  路由索引  对端实体索引  路由组名称

   6           域路由    优选主机路由  NULL      NULL          noname    
   7           主机路由  优选主机路由  1         NULL          noname    
  (结果个数 = 2)

  ---    END
  ```
2. 输入Diameter路由组索引，查询指定的Diameter路由组数据：
  LST DMRTGRP: GRPIDX=7;
  ```
  %%LST DMRTGRP: GRPIDX=7;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
    路由组索引  =  7
      路由模式  =  主机路由
  路由优选模式  =  优选主机路由
      路由索引  =  1
  对端实体索引  =  NULL
    路由组名称  =  noname
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DMRTGRP.md`
