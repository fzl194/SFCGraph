---
id: UNC@20.15.2@MMLCommand@DSP DRINFO
type: MMLCommand
name: DSP DRINFO（查询容灾信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DRINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# DSP DRINFO（查询容灾信息）

## 功能

该命令用于查询容灾信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| PEERDRINSTID | 对端容灾实例ID | 可选必选说明：可选参数。<br>参数含义：对端容灾实例标识，可以通过<br>**[LST DRINST](查询容灾实例(LST DRINST)_51012924.md)**<br>命令查询本端容灾实例ID，再通过<br>**[LST DRCOMM](查询容灾实例地址(LST DRCOMM)_51012928.md)**<br>命令查询到本端和对端容灾实例ID，从而得知对端容灾实例ID。<br>数据来源：全网规划。<br>取值范围：整型，0~63。<br>默认值：无。 |

## 操作的配置对象

- [容灾信息（DRINFO）](configobject/UNC/20.15.2/DRINFO.md)

## 使用实例

查询 “对端容灾实例ID” 为 “1” 的容灾信息：

```
DSP DRINFO: PEERDRINSTID=1;
%%DSP DRINFO: PEERDRINSTID=1;%%
RETCODE = 0  操作成功
操作结果如下：
--------------
本端容灾实例ID  =  0
对端容灾实例ID  =  1
  数据备份状态  =  数据实时备份状态
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询容灾信息(DSP-DRINFO)_51012929.md`
