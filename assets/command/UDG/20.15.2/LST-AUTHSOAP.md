---
id: UDG@20.15.2@MMLCommand@LST AUTHSOAP
type: MMLCommand
name: LST AUTHSOAP（查询网管登录认证策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTHSOAP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 登录认证管理
status: active
---

# LST AUTHSOAP（查询网管登录认证策略）

## 功能

该命令用于查询网管登录 UDG 认证策略。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [网管登录认证策略（AUTHSOAP）](configobject/UDG/20.15.2/AUTHSOAP.md)

## 使用实例

查询网管登录认证策略：

```
%%LST AUTHSOAP:;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------
认证策略  =  普通认证和增强认证 
(结果个数 = 1)  

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询网管登录认证策略（LST-AUTHSOAP）_97635699.md`
