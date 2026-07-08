---
id: UNC@20.15.2@MMLCommand@LST REDCAPRATVALUE
type: MMLCommand
name: LST REDCAPRATVALUE（查询RedCap接入用户的RAT填写值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: REDCAPRATVALUE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- RedCap用户RAT值
status: active
---

# LST REDCAPRATVALUE（查询RedCap接入用户的RAT填写值）

## 功能

**适用NF：SMF**

该命令用于查询RedCap终端接入时UNC给周边网元UPF，PCF，CHF，N16SMF，N16aSMF，AAAACCT，AAAAUTH发送消息时RatType信元中填写的值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/REDCAPRATVALUE]] · RedCap接入用户的RAT填写值（REDCAPRATVALUE）

## 使用实例

显示RedCap终端接入与CHF交互时Rat值为NR_REDCAP，PCF交互时Rat值为NR_REDCAP，UPF交互时Rat值为NR_REDCAP，与AAAACCT交互时Rat值为NR_REDCAP，与AAAAUTH交互时Rat值为NR_REDCAP，与N16SMF交互时Rat值为NR_REDCAP，与N16aSMF交互时Rat值为NR_REDCAP：

```
LST REDCAPRATVALUE:;
RETCODE = 0  操作成功

结果如下
------------------------
                  和CHF交互使用的RAT值          =  NR_REDCAP
		  和PCF交互使用的RAT值          =  NR_REDCAP
	          和UPF交互使用的RAT值          =  NR_REDCAP
		  和AAAACCT交互使用的RAT值      =  NR_REDCAP
		  和AAAAUTH交互使用的RAT值      =  NR_REDCAP
		  和N16SMF交互使用的RAT值       =  NR_REDCAP
		  和N16ASMF交互使用的RAT值      =  NR_REDCAP
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RedCap接入用户的RAT填写值（LST-REDCAPRATVALUE）_68306125.md`
