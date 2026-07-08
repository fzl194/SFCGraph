---
id: UNC@20.15.2@MMLCommand@LST SCTPLEGRP
type: MMLCommand
name: LST SCTPLEGRP（查询SCTP本地实体组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPLEGRP
command_category: 查询类
applicable_nf:
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- SCTP本地实体组
status: active
---

# LST SCTPLEGRP（查询SCTP本地实体组）

## 功能

**适用网元：MME、AMF**

该命令用于查询配置的SCTP本端实体组信息。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPGROUPID | SCTP本地实体组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本地实体组的标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~255。<br>默认值：无<br>说明：如果不输入参数，则查询所有的SCTP本地实体组。 |

## 操作的配置对象

- [SCTP本地实体组（SCTPLEGRP）](configobject/UNC/20.15.2/SCTPLEGRP.md)

## 使用实例

查询已经配置的所有SCTP本地实体组数据。

```
%%LST SCTPLEGRP:;%% 
RETCODE = 0  操作成功 
The result is as follows 
------------------------ 
SCTP 本端实体组标识  =  1 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCTP本地实体组(LST-SCTPLEGRP)_19187146.md`
