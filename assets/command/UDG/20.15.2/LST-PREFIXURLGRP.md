---
id: UDG@20.15.2@MMLCommand@LST PREFIXURLGRP
type: MMLCommand
name: LST PREFIXURLGRP（查询前缀URL组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PREFIXURLGRP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 前缀URL组
status: active
---

# LST PREFIXURLGRP（查询前缀URL组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询所有的前缀URL组，或者查询指定名称的前缀URL组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PREURLGRPNAME | 前缀URL组名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定前缀URL组名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PREFIXURLGRP]] · 前缀URL组（PREFIXURLGRP）

## 使用实例

- 查询名为testurlgroup的前缀URL组：
  ```
  LST PREFIXURLGRP: PREURLGRPNAME="testurlgroup ";
  ```
  ```

  RETCODE = 0  操作成功。

  Prefixed URL组信息
  ------------------
  前缀URL组名称    前缀URL        配置域名称

  testurlgroup     www.huawei.com  NULL
  testurlgroup     www.example.com NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询所有的前缀URL组：
  ```
  LST PREFIXURLGRP:;
  ```
  ```

  RETCODE = 0  操作成功。

  Prefixed URL组信息
  ------------------
  前缀URL组名称    前缀URL          配置域名称

  testurlgroup     www.huawei.com    NULL
  testurlgroup     www.example.com   NULL
  testurlgroup2    www.example1.com  NULL
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PREFIXURLGRP.md`
