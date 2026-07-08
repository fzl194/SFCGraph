---
id: UDG@20.15.2@MMLCommand@LST GLBRLYSPARACTL
type: MMLCommand
name: LST GLBRLYSPARACTL（查询媒体中继全局业务参数控制）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBRLYSPARACTL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继全局业务参数控制
status: active
---

# LST GLBRLYSPARACTL（查询媒体中继全局业务参数控制）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询媒体中继全局业务参数控制。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBRLYSPARACTL]] · 媒体中继全局业务参数控制（GLBRLYSPARACTL）

## 使用实例

假如需要查询媒体中继全局业务参数控制，则命令如下：

```
LST GLBRLYSPARACTL:;
```

```

RETCODE = 0  操作成功
结果如下
------------------------
             UE业务等待时间（秒）  =  10
       回源业务数据等待时间（秒）  =  5
     点播推流最大数据块（千字节）  =  20
     获取CDN IP最大等待时长（秒）  =  10
             回源重试次数（次数）  =  2
       回源重定向最大次数（次数）  =  2
  回源DNS服务器故障重试间隔（秒）  =  5
回源DNS响应异常最小重试间隔（秒）  =  30
  回源DNS记录最大空闲时长（分钟）  =  30
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBRLYSPARACTL.md`
