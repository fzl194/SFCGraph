---
id: UDG@20.15.2@MMLCommand@LST AFPOLICY
type: MMLCommand
name: LST AFPOLICY（查询防欺诈策略配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AFPOLICY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈策略
status: active
---

# LST AFPOLICY（查询防欺诈策略配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询判断出欺诈行为后的处理策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFPOLICYTYPE | 防欺诈策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定防欺诈策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DNS：指定DNS防欺诈。<br>- HTTP：指定HTTP防欺诈。<br>- HTTPS：指定HTTPS防欺诈。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFPOLICY]] · 防欺诈策略配置（AFPOLICY）

## 使用实例

- 假如运营商需要查询判断出DNS欺诈行为后的处理策略，则命令如下：
  ```
  LST AFPOLICY:AFPOLICYTYPE=DNS;
  ```
  ```

  RETCODE = 0  操作成功。

  防欺诈策略信息
  --------------
  防欺诈策略类型  =  DNS防欺诈
   PCC策略组名称  =  pccpolicygroup
  防欺诈应用标识  =  NULL
    分类属性名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询判断出欺诈行为后的处理策略，则命令如下：
  ```
  LST AFPOLICY:;
  ```
  ```

  RETCODE = 0  操作成功。

  防欺诈策略信息
  --------------
  防欺诈策略类型    PCC策略组名称     防欺诈应用标识    分类属性名称

  DNS防欺诈         pccpolicygroup    NULL              NULL        
  HTTP防欺诈        pccpolicygroup    NULL              NULL        
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询防欺诈策略配置（LST-AFPOLICY）_86527026.md`
