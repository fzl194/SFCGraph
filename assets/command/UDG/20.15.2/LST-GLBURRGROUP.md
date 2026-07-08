---
id: UDG@20.15.2@MMLCommand@LST GLBURRGROUP
type: MMLCommand
name: LST GLBURRGROUP（查询全局计费属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBURRGROUP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 全局使用量上报规则组
status: active
---

# LST GLBURRGROUP（查询全局计费属性）

## 功能

**适用NF：PGW-U、UPF**

本条命令用于查询全局计费属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBURRGROUP]] · 全局计费属性（GLBURRGROUP）

## 使用实例

查询显示全局计费属性：

```
LST GLBURRGROUP:;
```

```

RETCODE = 0  操作成功

全局使用量上报规则组信息
------------------------
上行发起URR名称1  =  uponurr
上行发起URR名称2  =  NULL
上行发起URR名称3  =  NULL
下行发起URR名称1  =  dnonurr
下行发起URR名称2  =  NULL
下行发起URR名称3  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBURRGROUP.md`
