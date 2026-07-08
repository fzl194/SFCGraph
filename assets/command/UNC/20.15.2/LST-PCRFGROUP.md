---
id: UNC@20.15.2@MMLCommand@LST PCRFGROUP
type: MMLCommand
name: LST PCRFGROUP（查询PCRF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCRFGROUP
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
- PCRF组
status: active
---

# LST PCRFGROUP（查询PCRF组）

## 功能

**适用NF：PGW-C、GGSN**

此命令用于查询PCRF组宕机备份功能、PCRF组的工作模式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF组的名字，要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCRFGROUP]] · PCRF组（PCRFGROUP）

## 使用实例

查询PCRFGROUP记录，输入PCRFGRPNAME为“huawei”：

```
LST PCRFGROUP:PCRFGRPNAME="huawei";
```

```

RETCODE = 0  操作成功。

PCRF组信息
----------
    PCRF组名称  =  huawei
  负荷分担模式  =  主备
  宕机备份开关  =  不使能
主用PCRF主机名  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PCRF组（LST-PCRFGROUP）_09897093.md`
