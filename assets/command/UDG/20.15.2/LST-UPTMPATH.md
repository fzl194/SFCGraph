---
id: UDG@20.15.2@MMLCommand@LST UPTMPATH
type: MMLCommand
name: LST UPTMPATH（查询TM路径相关属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPTMPATH
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- TM路径管理
- TM路径参数
status: active
---

# LST UPTMPATH（查询TM路径相关属性）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用来查看TM路径相关属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPTMPATH]] · TM路径相关属性（UPTMPATH）

## 使用实例

查询TM路径相关属性：

```
LST UPTMPATH:;
```

```

RETCODE = 0  操作成功

TM路径配置
----------
                      Echo开关  =  使能
      发送TM心跳请求的间隔时间  =  60
      TM请求消息的重发时间间隔  =  20
  TM请求消息的最大尝试发送次数  =  2
  是否去活路径上已激活的上下文  =  使能
路径断告警后发送echo消息的次数  =  5
        NE状态消息空闲检查开关  =  不使能
        NE状态消息空闲超时时长  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPTMPATH.md`
