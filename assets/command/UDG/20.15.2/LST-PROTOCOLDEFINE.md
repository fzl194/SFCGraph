---
id: UDG@20.15.2@MMLCommand@LST PROTOCOLDEFINE
type: MMLCommand
name: LST PROTOCOLDEFINE（查询自定义协议）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PROTOCOLDEFINE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 自定义协议
status: active
---

# LST PROTOCOLDEFINE（查询自定义协议）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询自定义协议的全部配置信息，或根据自定义协议名称查询指定名称的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTDEFINENAME | 自定义协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置自定义协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。必须和默认的协议大类/协议/协议子类名称不同。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROTOCOLDEFINE]] · 自定义协议（PROTOCOLDEFINE）

## 使用实例

查询名为protdefien的自定义协议详细信息：

```
LST PROTOCOLDEFINE:PROTDEFINENAME="protdefine";
```

```

RETCODE = 0  操作成功。

自定义协议信息
--------------
自定义协议名称  =  protdefine
    协议组名称  =  p2p
    过滤器名称  =  filter
        优先级  =  10
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PROTOCOLDEFINE.md`
