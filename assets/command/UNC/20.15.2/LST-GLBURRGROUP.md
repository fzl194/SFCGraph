---
id: UNC@20.15.2@MMLCommand@LST GLBURRGROUP
type: MMLCommand
name: LST GLBURRGROUP（查询全局使用量上报规则组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBURRGROUP
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
- 全局使用量上报规则组
status: active
---

# LST GLBURRGROUP（查询全局使用量上报规则组）

## 功能

**适用NF：PGW-C、SMF**

本条命令用于PDP用户查询全局使用量上报规则组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBURRGROUP]] · 全局使用量上报规则组（GLBURRGROUP）

## 使用实例

查询显示全局使用量上报规则组：

```
LST GLBURRGROUP:;
```

```

RETCODE = 0  操作成功

全局计费属性信息
----------------
上行发起离线URR名称  =  offupurr
下行发起离线URR名称  =  offdnurr
上行发起在线URR名称  =  onupurr
下行发起在线URR名称  =  ondnurr
         不计费标记  =  无
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GLBURRGROUP.md`
