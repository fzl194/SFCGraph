---
id: UNC@20.15.2@MMLCommand@LST CPPOINT
type: MMLCommand
name: LST CPPOINT（查询CP端点信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPPOINT
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- CP管理
- CP端点管理
status: active
---

# LST CPPOINT（查询CP端点信息）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询CP端点信息，根据CP端点的索引等信息来查询。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPPOINTINDEX | CP端点索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定这个CP端点的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CPPOINT]] · CP端点信息（CPPOINT）

## 使用实例

- 查询有的CP端点： LST CPPOINT:;
  ```
  %%LST CPPOINT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  CP端点索引  =  0
  CP节点索引  =  0
      IP类型  =  IPv4
    IPv4地址  =  192.168.0.20
    IPv6地址  =  NULL
     VPN名称  =  _public_
  (结果个数 = 1)

  ---    END
  ```
- 查询CP端点索引为0的CP端点： LST CPPOINT: CPPOINTINDEX=0;
  ```
  %%LST CPPOINT: CPPOINTINDEX=0;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  CP端点索引  =  0
  CP节点索引  =  0
      IP类型  =  IPv4
    IPv4地址  =  192.168.0.20
    IPv6地址  =  NULL
     VPN名称  =  _public_
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CP端点信息（LST-CPPOINT）_09654424.md`
