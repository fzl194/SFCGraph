---
id: UDG@20.15.2@MMLCommand@LST PROTREDEFINE
type: MMLCommand
name: LST PROTREDEFINE（查询重定义协议）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PROTREDEFINE
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
- 七层规则管理
- 协议重定义
status: active
---

# LST PROTREDEFINE（查询重定义协议）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示重定义协议类型。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCPROTNAME | 源协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置源协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该协议只能为默认协议，不支持自定义协议。 |
| FILTERNAME | 过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD FILTER命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PROTREDEFINE]] · 重定义协议（PROTREDEFINE）

## 使用实例

查询名为protRedefine的重定义协议详细信息：

```
LST PROTREDEFINE:SRCPROTNAME="ssl";
```

```

RETCODE = 0  操作成功。

重定义协议信息
--------------
      源协议名称  =  ssl
    目的协议名称  =  http
          优先级  =  1
      过滤器名称  =  filter1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PROTREDEFINE.md`
