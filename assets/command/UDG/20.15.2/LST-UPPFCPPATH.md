---
id: UDG@20.15.2@MMLCommand@LST UPPFCPPATH
type: MMLCommand
name: LST UPPFCPPATH（查询路径相关属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPPFCPPATH
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- PFCP参数管理
- PFCP路径参数
status: active
---

# LST UPPFCPPATH（查询路径相关属性）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看PFCP路径相关属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPPFCPPATH]] · 路径相关属性（UPPFCPPATH）

## 使用实例

查询PFCP路径相关属性：

```
LST UPPFCPPATH:;
```

```

RETCODE = 0  操作成功。

PFCP路径配置
-----------
          
        发送PFCP心跳请求的间隔时间  =  60
        PFCP请求消息的重发时间间隔  =  3
    PFCP请求消息的最大尝试发送次数  =  5
      是否去活路径上已激活的上下文  =  使能
    路径断告警后发送心跳消息的次数  =  30                   
                          用户类型  =  MBS&普通用户              
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询路径相关属性（LST-UPPFCPPATH）_82837241.md`
