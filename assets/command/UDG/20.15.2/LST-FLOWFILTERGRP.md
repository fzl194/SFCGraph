---
id: UDG@20.15.2@MMLCommand@LST FLOWFILTERGRP
type: MMLCommand
name: LST FLOWFILTERGRP（查询流过滤器组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FLOWFILTERGRP
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
- 流过滤器管理
- 流过滤器组
status: active
---

# LST FLOWFILTERGRP（查询流过滤器组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询所有的流过滤器组信息，或者查询指定名称的流过滤器组信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLWFLTRGRPNAME | 流过滤器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流过滤器组名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FLOWFILTERGRP]] · 流过滤器组（FLOWFILTERGRP）

## 使用实例

- 查询名为testflowfiltergrp的流过滤器组：
  ```
  LST FLOWFILTERGRP:FLWFLTRGRPNAME="testflowfiltergrp";
  ```
  ```

  RETCODE = 0  操作成功

    流过滤器组名称  =  testflowfiltergrp
      流过滤器名称  =  testflowfilter
  流过滤器逻辑分组  =  或
        配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的流过滤器组：
  ```
  LST FLOWFILTERGRP:;
  ```
  ```

  RETCODE = 0  操作成功

  流过滤器组名称     流过滤器名称     流过滤器逻辑分组        配置域名称

  testflowfiltergrp   testflowfilter   或                       NULL
  testflowfiltergrp2  testflowfilter2  或                       NULL
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询流过滤器组（LST-FLOWFILTERGRP）_86528844.md`
