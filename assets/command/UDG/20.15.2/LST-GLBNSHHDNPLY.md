---
id: UDG@20.15.2@MMLCommand@LST GLBNSHHDNPLY
type: MMLCommand
name: LST GLBNSHHDNPLY（查询NSH头增强全局策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBNSHHDNPLY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- NSH头增强
- NSH全局策略
status: active
---

# LST GLBNSHHDNPLY（查询NSH头增强全局策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询NSH头增强全局策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBNSHHDNPLY]] · NSH头增强全局策略（GLBNSHHDNPLY）

## 使用实例

查询NSH头增强全局策略信息：

```
LST GLBNSHHDNPLY:;
```

```

RETCODE = 0  操作成功

全局NSH头增强策略信息
---------------------
    NSH头增强名称  =  nsh
 重定向IP协议版本  =  IPV4
   重定向IPV6地址  =  ::
   重定向IPV4地址  =  10.0.0.0
NSH对端设备端口号  =  6633
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBNSHHDNPLY.md`
