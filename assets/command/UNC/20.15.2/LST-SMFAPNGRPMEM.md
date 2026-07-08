---
id: UNC@20.15.2@MMLCommand@LST SMFAPNGRPMEM
type: MMLCommand
name: LST SMFAPNGRPMEM（查询APN和DNS关联的APN组的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFAPNGRPMEM
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
- APN管理
- APN组管理
status: active
---

# LST SMFAPNGRPMEM（查询APN和DNS关联的APN组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询APN和DNS关联的APN组的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | APN组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFAPNGRPMEM]] · APN和DNS关联的APN组的绑定关系（SMFAPNGRPMEM）

## 使用实例

查询APN和DNS关联的APN组的绑定关系：

```
LST SMFAPNGRPMEM:GRPNAME="grp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN和DNS关联的APN组的绑定关系（LST-SMFAPNGRPMEM）_88697034.md`
