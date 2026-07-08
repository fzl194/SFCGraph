---
id: UDG@20.15.2@MMLCommand@LST FUIEXTFILTER
type: MMLCommand
name: LST FUIEXTFILTER（查询FUI扩展过滤器绑定配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FUIEXTFILTER
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- FUI重定向控制
- FUI扩展过滤器绑定
status: active
---

# LST FUIEXTFILTER（查询FUI扩展过滤器绑定配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询FUI扩展过滤器绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FUIEXTFILTER]] · FUI扩展过滤器绑定配置（FUIEXTFILTER）

## 使用实例

运营商想要查询全局扩展过滤器绑定关系，使用此命令：

```
LST FUIEXTFILTER:;
```

```

RETCODE = 0  操作成功。

FUI扩展过滤器绑定信息
---------------------
扩展过滤器名字1  =  ExtFilter1
扩展过滤器类型1  =  与
扩展过滤器名字2  =  ExtFilter2
扩展过滤器类型2  =  非
扩展过滤器名字3  =  NULL
扩展过滤器类型3  =  NULL
扩展过滤器名字4  =  NULL
扩展过滤器类型4  =  NULL
扩展过滤器名字5  =  NULL
扩展过滤器类型5  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FUIEXTFILTER.md`
