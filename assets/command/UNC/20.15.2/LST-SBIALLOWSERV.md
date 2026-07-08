---
id: UNC@20.15.2@MMLCommand@LST SBIALLOWSERV
type: MMLCommand
name: LST SBIALLOWSERV（查询基于服务的白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBIALLOWSERV
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- 白名单管理
- 基于服务的白名单管理
status: active
---

# LST SBIALLOWSERV（查询基于服务的白名单）

## 功能

该命令用于查询已配置的服务白名单。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置的白名单索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于服务的白名单（SBIALLOWSERV）](configobject/UNC/20.15.2/SBIALLOWSERV.md)

## 使用实例

- 若运营商想查询配置的所有服务白名单，则执行如下命令。
  ```
  LST SBIALLOWSERV: ; 

  %%LST SBIALLOWSERV:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  索引  服务名称   网元类型   网元实例ID  

  1     nnrf-nfm   NFTypeNRF  NULL        
  2     namf-comm  NFTypeAMF  NULL        
  (结果个数 = 2)

  ---    END
  ```
- 若运营商想查询索引值为1的服务白名单，则执行如下命令。
  ```
  LST SBIALLOWSERV: INDEX=1; 

  %%LST SBIALLOWSERV:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
           索引  =  1
       服务名称  =  nnrf-nfm
       网元类型  =  NFTypeNRF
     网元实例ID  =  NULL
   (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于服务的白名单（LST-SBIALLOWSERV）_84132102.md`
