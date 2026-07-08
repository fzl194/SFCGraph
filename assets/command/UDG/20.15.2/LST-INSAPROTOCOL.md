---
id: UDG@20.15.2@MMLCommand@LST INSAPROTOCOL
type: MMLCommand
name: LST INSAPROTOCOL（查询黑白名单协议配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: INSAPROTOCOL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 智能SA管理
- 协议类型配置
status: active
---

# LST INSAPROTOCOL（查询黑白名单协议配置）

## 功能

**适用NF：PGW-U、UPF**

查询黑白名单协议配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTTYPE | 协议类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示配置协议类型。<br>数据来源：本端规划<br>取值范围：<br>- BLACK：黑名单协议。<br>- ENHANCE：待增强协议。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/INSAPROTOCOL]] · 黑白名单协议配置（INSAPROTOCOL）

## 使用实例

查询所有黑名单协议配置：

```
LST INSAPROTOCOL:PROTTYPE=BLACK;
```

```

RETCODE = 0  操作成功。
 
黑白名单协议配置信息
------
           协议类型                      协议名称 
        Black Protocol                   http 
        Black Protocol                   https
 
(结果个数 = 2)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询黑白名单协议配置（LST-INSAPROTOCOL）_56165570.md`
