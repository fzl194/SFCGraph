---
id: UDG@20.15.2@MMLCommand@LST GLBCFFUNC
type: MMLCommand
name: LST GLBCFFUNC（查询内容过滤全局开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBCFFUNC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤全局开关
status: active
---

# LST GLBCFFUNC（查询内容过滤全局开关）

## 功能

**适用NF：PGW-U、UPF**

查询内容过滤全局开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [内容过滤全局开关（GLBCFFUNC）](configobject/UDG/20.15.2/GLBCFFUNC.md)

## 使用实例

查询内容过滤全局开关：

```
LST GLBCFFUNC:;
```

```

RETCODE = 0  操作成功

内容过滤全局开关
----------------
                         内容过滤全局开关  =  使能（开启）
单POD向同一个服务器发送Reqmod消息的链路数  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询内容过滤全局开关（LST-GLBCFFUNC）_50710734.md`
