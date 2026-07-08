---
id: UDG@20.15.2@MMLCommand@LST CFPFSPECACTION
type: MMLCommand
name: LST CFPFSPECACTION（查询内容过滤策略特殊场景下的业务动作）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CFPFSPECACTION
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤策略特殊场景下的业务动作
status: active
---

# LST CFPFSPECACTION（查询内容过滤策略特殊场景下的业务动作）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询所有内容过滤策略特殊场景下的业务动作。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFPROFILENAME | 套餐名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFPFSPECACTION]] · 指定内容过滤策略特殊场景下的业务动作（CFPFSPECACTION）

## 使用实例

查询指定内容过滤策略特殊场景下的业务动作：

```
LST CFPFSPECACTION:;
```

```

RETCODE = 0  操作成功。
 
指定内容过滤策略特殊场景下的业务动作信息
----------------
套餐名称        默认策略动作    重定向名称    错误策略动作    重定向名称    未知策略动作    重定向名称
 
profile1_test    转发            NULL          转发          NULL          转发           NULL      
profile2_test    丢弃            NULL          转发          NULL          转发           NULL      
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CFPFSPECACTION.md`
