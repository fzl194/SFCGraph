---
id: UNC@20.15.2@MMLCommand@LST GLBCTXREQRATE
type: MMLCommand
name: LST GLBCTXREQRATE（查询全局初始请求计费绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBCTXREQRATE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 全局初始请求计费信息
status: active
---

# LST GLBCTXREQRATE（查询全局初始请求计费绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询全局的所有初始请求URR组的计费属性。

## 注意事项

当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBCTXREQRATE]] · 全局初始请求计费绑定关系（GLBCTXREQRATE）

## 使用实例

查询全局的所有初始请求URR组的计费属性：

```
LST GLBCTXREQRATE:;
```

```

RETCODE = 0  操作成功。

全局初始请求计费绑定关系信息
----------------------------
初始请求URR组名称  =  urrgrp1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局初始请求计费绑定关系（LST-GLBCTXREQRATE）_09897185.md`
