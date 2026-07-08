---
id: UNC@20.15.2@MMLCommand@LST DIAMCONNECTION
type: MMLCommand
name: LST DIAMCONNECTION（查询Diameter链路）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIAMCONNECTION
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diameter链路
status: active
---

# LST DIAMCONNECTION（查询Diameter链路）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询Diameter链路。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIAMCONNGRP | Diameter链路组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路的Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMCONNECTION]] · Diameter链路（DIAMCONNECTION）

## 使用实例

- 查询Diameter链路组conn1中的Diameter链路：
  ```
  LST DIAMCONNECTION: DIAMCONNGRP="conn1";
  ```
  ```

  RETCODE = 0  操作成功

  Diameter链路信息
  ----------------
                本端端口  =  16400
        Diameter链路组名  =  conn1
            对端地址类型  =  IPv4
              对端IP地址  =  10.10.10.11
        对端SCTP端点名称  =  NULL
              对端端口号  =  3868
              本端接口名  =  gxif1/0/0
  SCTP建链交换本端IP地址  =  不使能
  (结果个数 = 1)

  ---    END
  ```
- 查询所有Diameter链路：
  ```
  LST DIAMCONNECTION:;
  ```
  ```

  RETCODE = 0  操作成功。

  Diameter链路信息
  ----------------
  Diameter链路组名    本端接口名    对端地址类型    对端IP地址     对端端口号    对端SCTP端点名称    SCTP建链交换本端IP地址    本端端口

  conn1               gxif1/0/0     IPv4            10.10.10.11        3868          NULL                不使能                    16400       
  conn2               gxif1/0/0     IPv4            10.10.10.21        6838          NULL                不使能                    16463       
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter链路（LST-DIAMCONNECTION）_09897269.md`
