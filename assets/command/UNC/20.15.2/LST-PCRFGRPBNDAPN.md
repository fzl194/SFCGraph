---
id: UNC@20.15.2@MMLCommand@LST PCRFGRPBNDAPN
type: MMLCommand
name: LST PCRFGRPBNDAPN（查询APN和Pcrf组关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCRFGRPBNDAPN
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
- PCRF组绑定APN
status: active
---

# LST PCRFGRPBNDAPN（查询APN和Pcrf组关联关系）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来查询APN和Pcrf组关联关系。支持模糊查询，当给APN字段赋值，查询APN配置的所有记录；当给APN和IMSIMSISDNSEG字段赋值，查询APN基于IMSI/MSISDN号段PCRF组的所有记录。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN和Pcrf组关联关系（PCRFGRPBNDAPN）](configobject/UNC/20.15.2/PCRFGRPBNDAPN.md)

## 使用实例

查询APN和Pcrf组关联关系，APN为“aaa”：

```
LST PCRFGRPBNDAPN:APN="aaa";
```

```

RETCODE = 0  操作成功

APN与PCRF Group关联关系
-----------------------
            APN名称  =  aaa
           缺省标记  =  缺省
IMSI/MSISDN号段名称  =  NULL
         PCRF组名称  =  aaa
             优先级  =  0
               描述  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN和Pcrf组关联关系（LST-PCRFGRPBNDAPN）_09897109.md`
