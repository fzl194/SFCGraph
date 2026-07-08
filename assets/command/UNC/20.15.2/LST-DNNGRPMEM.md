---
id: UNC@20.15.2@MMLCommand@LST DNNGRPMEM
type: MMLCommand
name: LST DNNGRPMEM（查询DNN群组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNNGRPMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- DNN群组成员管理
status: active
---

# LST DNNGRPMEM（查询DNN群组成员）

## 功能

**适用NF：AMF**

该命令用于查询DNN群组中的DNN列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNGRPID | DNN群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNN群组标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。该参数依赖于DNNGRP对象，请确保相应DNNGRP已创建。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNGRPMEM]] · DNN群组成员（DNNGRPMEM）

## 使用实例

- 查询系统中“DNN群组标识”为“BIG_GROUP”的DNN群组以及群组内的DNN列表，执行如下命令：
  ```
  %%LST DNNGRPMEM: DNNGRPID="BIG_GROUP";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  DNN群组标识  =  BIG_GROUP
          DNN  =  DNNA
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的DNN群组以及群组内的DNN列表，执行如下命令：
  ```
  %%LST DNNGRPMEM:;%%
  RETCODE = 0 操作成功

  结果如下
  ------------------------
  DNN群组标识  =  BIG_GROUP
          DNN  =  DNNA
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DNNGRPMEM.md`
