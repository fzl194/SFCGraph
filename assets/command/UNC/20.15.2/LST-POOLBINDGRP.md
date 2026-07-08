---
id: UNC@20.15.2@MMLCommand@LST POOLBINDGRP
type: MMLCommand
name: LST POOLBINDGRP（查询地址池与地址池组的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: POOLBINDGRP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池组管理
status: active
---

# LST POOLBINDGRP（查询地址池与地址池组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询地址池与地址池组的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定已配置的地址池组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOLGRP命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POOLBINDGRP]] · 地址池与地址池组的绑定关系（POOLBINDGRP）

## 使用实例

查询地址池与地址池组的绑定关系：

```
LST POOLBINDGRP:;

结果如下
--------
地址池组名称  =  spoolgrp1
  地址池名称  =  spool1
地址池优先级  =  15
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-POOLBINDGRP.md`
