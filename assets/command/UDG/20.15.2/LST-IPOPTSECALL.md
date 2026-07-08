---
id: UDG@20.15.2@MMLCommand@LST IPOPTSECALL
type: MMLCommand
name: LST IPOPTSECALL（查询IP全局选项安全配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPOPTSECALL
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- IP选项全局安全配置
status: active
---

# LST IPOPTSECALL（查询IP全局选项安全配置）

## 功能

该命令用于查询IP全局选项安全配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPOPTSECALL]] · IP全局选项安全配置（IPOPTSECALL）

## 使用实例

查询IP全局选项安全配置：

```
LST IPOPTSECALL:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
IP过滤规则 =  Permit
(返回结果 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPOPTSECALL.md`
