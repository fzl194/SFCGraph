---
id: UNC@20.15.2@MMLCommand@LST APNCTRLPARA
type: MMLCommand
name: LST APNCTRLPARA（查询基于APN的信令控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNCTRLPARA
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- 基于APN的信令控制参数
status: active
---

# LST APNCTRLPARA（查询基于APN的信令控制参数）

## 功能

**适用网元：SGSN**

该命令用于查询基于APN的信令控制参数。

## 注意事项

不指定APN组时，输出所有APN组的信令控制参数。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNGRPID | APNNI组号 | 可选必选说明：可选参数<br>参数含义：本参数用于指定开启APN信令控制功能的APNNI组号。<br>数据来源：全网规划<br>取值范围：0～15<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNCTRLPARA]] · 基于APN的信令控制参数（APNCTRLPARA）

## 使用实例

1. 查询所有记录：
  LST APNCTRLPARA:;
  ```
  %%LST APNCTRLPARA:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   APNNI组号  附着请求控制门限（次/秒）  PDP上下文请求控制门限（次/秒）

   0          1000                       1000                          
   1          5000                       5000                          
  (结果个数 = 2)

  ---    END
  ```
2. 查询指定的记录：
  LST APNCTRLPARA: APNGRPID=1;
  ```
  %%LST APNCTRLPARA: APNGRPID=1;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
                       APNNI组号  =  1
       附着请求控制门限（次/秒）  =  5000
  PDP上下文请求控制门限（次/秒）  =  5000
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于APN的信令控制参数(LST-APNCTRLPARA)_26305594.md`
