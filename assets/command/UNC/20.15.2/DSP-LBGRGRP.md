---
id: UNC@20.15.2@MMLCommand@DSP LBGRGRP
type: MMLCommand
name: DSP LBGRGRP（查询容灾组信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LBGRGRP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 服务管理
- 容灾组信息
status: active
---

# DSP LBGRGRP（查询容灾组信息）

## 功能

该命令用于查询容灾组信息。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRGROUPID | 容灾组ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示容灾组的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LBGRGRP]] · 容灾组信息（LBGRGRP）

## 使用实例

查询容灾组。

DSP LBGRGRP:;

```
%%DSP LBGRGRP:;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
  容灾组名称    =  gr_grp0
  容灾组ID     =  0
  容灾组优先级  =  100
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LBGRGRP.md`
