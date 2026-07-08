---
id: UDG@20.15.2@MMLCommand@LST REASTIMEOUT
type: MMLCommand
name: LST REASTIMEOUT（查询IPv4报文重组超时配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: REASTIMEOUT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- IPv4报文重组超时配置
status: active
---

# LST REASTIMEOUT（查询IPv4报文重组超时配置）

## 功能

该命令用于查询IPv4分片报文的重组超时时间。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/REASTIMEOUT]] · IPv4报文重组超时配置（REASTIMEOUT）

## 使用实例

查询IPv4报文重组超时配置：

```
LST REASTIMEOUT:;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
        IPv4报文重组超时时间（s）  =  100
        (结果个数 = 1)
        ---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-REASTIMEOUT.md`
