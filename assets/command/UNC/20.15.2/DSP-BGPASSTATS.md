---
id: UNC@20.15.2@MMLCommand@DSP BGPASSTATS
type: MMLCommand
name: DSP BGPASSTATS（查询BGP AS查询统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BGPASSTATS
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP AS号消息统计
status: active
---

# DSP BGPASSTATS（查询BGP AS查询统计）

## 功能

该命令用来用于显示收到的以前缀为key查询AS-Query消息和查询响应消息的统计计数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [BGP AS查询统计（BGPASSTATS）](configobject/UNC/20.15.2/BGPASSTATS.md)

## 使用实例

查询BGP AS查询统计：

```
DSP BGPASSTATS:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
收取消息计数   =  5678
发送消息计数   =  5678
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BGP-AS查询统计（DSP-BGPASSTATS）_50121338.md`
