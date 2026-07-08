---
id: UNC@20.15.2@MMLCommand@LST NGMNO
type: MMLCommand
name: LST NGMNO（查询5G模式移动网络运营商信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGMNO
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 5G 移动网络运营商管理
status: active
---

# LST NGMNO（查询5G模式移动网络运营商信息）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF**

该命令用于查询移动网络运营商的基本信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于在系统内唯一标识移动网络运营商。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGMNO]] · 5G模式移动网络运营商信息（NGMNO）

## 使用实例

- 查询“运营商标识”为“0”的移动网络运营商的基本信息，执行如下命令：
  ```
  %%LST NGMNO: NOID=0;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  运营商标识  =  0
  运营商全称  =  NULL
  运营商简称  =  NULL
    描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询移动网络运营商的基本信息，执行如下命令：
  ```
  %%LST NGMNO:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  运营商标识  =  0
  运营商全称  =  NULL
  运营商简称  =  NULL
    描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G模式移动网络运营商信息（LST-NGMNO）_09652431.md`
