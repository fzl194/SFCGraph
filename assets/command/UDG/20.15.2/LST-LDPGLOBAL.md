---
id: UDG@20.15.2@MMLCommand@LST LDPGLOBAL
type: MMLCommand
name: LST LDPGLOBAL（查询LDP全局配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LDPGLOBAL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP全局配置
status: active
---

# LST LDPGLOBAL（查询LDP全局配置）

## 功能

该命令用于查询LDP全局配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/LDPGLOBAL]] · LDP全局配置（LDPGLOBAL）

## 使用实例

查询LDP全局配置：

```
LST LDPGLOBAL:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
           MTU私有信令能力  =  ENABLE
           MTU标准信令能力  =  DISABLE
                  触发策略  =  主机
            IP地址前缀名称  =  NULL
                    GR能力  =  DISABLE
       会话重链接时间（s）  =  300
          LSP恢复时间（s）  =  300
   对端存活定时器时间（s）  =  600
      BackOff初始时间（s）  =  15
      BackOff最大时间（s）  =  120
          动态通告能力使能  =  DISABLE
禁止建立代理Egress LDP LSP  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-LDPGLOBAL.md`
