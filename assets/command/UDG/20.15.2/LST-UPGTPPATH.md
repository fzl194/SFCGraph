---
id: UDG@20.15.2@MMLCommand@LST UPGTPPATH
type: MMLCommand
name: LST UPGTPPATH（查询路径相关属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPGTPPATH
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
- GTP路径管理
- GTP协议参数管理
- GTP路径全局参数
status: active
---

# LST UPGTPPATH（查询路径相关属性）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看GTP路径相关属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPGTPPATH]] · 路径相关属性（UPGTPPATH）

## 使用实例

查询GTP路径相关属性：

```
LST UPGTPPATH:;
```

```

RETCODE = 0  操作成功

GTP路径配置
-----------
                   V0 Echo开关  =  不使能
            V1数据路径Echo开关  =  使能
     发送GTP心跳请求的间隔时间  =  60
     GTP请求消息的重发时间间隔  =  3
 GTP请求消息的最大尝试发送次数  =  5
  是否去活路径上已激活的上下文  =  使能
路径断告警后发送echo消息的次数  =  30
                 EchoList 开关  =  不使能
                 EchoList 类型  =  黑名单
                  逻辑接口类型  =  N3&N9c&Pa&S11-U&S1-U&S5/S8-S&Sa&Sc
UAC GTP请求消息的最大尝试发送次数  =  5
   UAC GTP请求消息的重发时间间隔  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPGTPPATH.md`
