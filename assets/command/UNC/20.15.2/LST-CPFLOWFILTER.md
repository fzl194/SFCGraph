---
id: UNC@20.15.2@MMLCommand@LST CPFLOWFILTER
type: MMLCommand
name: LST CPFLOWFILTER（查询CP流过滤器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPFLOWFILTER
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N4 GTP-U管理
- 流过滤器
status: active
---

# LST CPFLOWFILTER（查询CP流过滤器）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询SMF和UPF之间的消息流过滤器。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CPFLOWFILTER]] · CP流过滤器（CPFLOWFILTER）

## 使用实例

查询所有SMF和UPF之间的消息流过滤器：

```
%%LST CPFLOWFILTER:;%%
RETCODE = 0  操作成功

结果如下
------------------------
流过滤器名称  =  RS
流过滤器类别  =  IPv6路由器通告
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CP流过滤器（LST-CPFLOWFILTER）_96805383.md`
