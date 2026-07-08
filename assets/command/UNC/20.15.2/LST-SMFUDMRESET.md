---
id: UNC@20.15.2@MMLCommand@LST SMFUDMRESET
type: MMLCommand
name: LST SMFUDMRESET（查询SMF的UDM故障重选策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFUDMRESET
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- UDM故障处理策略管理
status: active
---

# LST SMFUDMRESET（查询SMF的UDM故障重选策略）

## 功能

**适用NF：SMF**

该命令用于查询SMF的UDM故障处理策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFUDMRESET]] · SMF的UDM故障重选策略（SMFUDMRESET）

## 使用实例

查询SMF的UDM故障处理策略。

```
%%LST SMFUDMRESET;%%
RETCODE = 0  操作成功

结果如下
--------
  recoveryTime变化时重选UDM开关  =  打开
链路故障或者去注册时重选UDM开关  =  关闭
	               扫描速率  =  5
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFUDMRESET.md`
