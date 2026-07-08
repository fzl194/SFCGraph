---
id: UNC@20.15.2@MMLCommand@LST PCRFBINDGRP
type: MMLCommand
name: LST PCRFBINDGRP（查询PCRF与PCRF Group的关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCRFBINDGRP
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF绑定
status: active
---

# LST PCRFBINDGRP（查询PCRF与PCRF Group的关联关系）

## 功能

**适用NF：PGW-C、GGSN**

此命令用于查询PCRF与PCRF分组的绑定信息。

## 注意事项

- 负荷分担模式下，未指定权重，则平均分配；指定权重的，按照指定值进行分配。
- 如果PCRF Group的工作模式为主备模式，则PCRF权重值为255，表示该参数为无效值。
- 使用EXP MML命令导出的配置文件中，WEIGHT参数为实际配置的值，与LST PCRFBINDGRP命令查询的PCRF权重值可能不一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF分组的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCRFBINDGRP]] · PCRF与PCRF Group的关联关系（PCRFBINDGRP）

## 使用实例

查询Pcrf与PCRF Group的关联关系，被查询的PCRF组名为“abc”：

```
LST PCRFBINDGRP:PCRFGRPNAME="abc";
```

```

RETCODE = 0  操作成功

PCRF组内PCRF信息
----------------
  PCRF组名称  =  abc
PCRF主机名称  =  aaa
    PCRF权重  =  100
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PCRF与PCRF-Group的关联关系（LST-PCRFBINDGRP）_09897099.md`
