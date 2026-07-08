---
id: UDG@20.15.2@MMLCommand@LST CFPROFILE
type: MMLCommand
name: LST CFPROFILE（查询内容过滤策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CFPROFILE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤策略配置
status: active
---

# LST CFPROFILE（查询内容过滤策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询内容过滤策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFPROFILENAME | 内容过滤策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFPROFILE]] · 内容过滤策略（CFPROFILE）

## 使用实例

显示CFPROFILE相关内容：

```
LST CFPROFILE:;
```

```

RETCODE = 0  操作成功

内容过滤策略
------------
内容过滤策略名称  =  cfp1
          优先级  =  1
      配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询内容过滤策略（LST-CFPROFILE）_39717700.md`
