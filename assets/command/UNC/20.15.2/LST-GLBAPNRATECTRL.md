---
id: UNC@20.15.2@MMLCommand@LST GLBAPNRATECTRL
type: MMLCommand
name: LST GLBAPNRATECTRL（查询全局APN速率控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBAPNRATECTRL
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 速率控制
- APN速率控制
- 全局APN速率控制配置
status: active
---

# LST GLBAPNRATECTRL（查询全局APN速率控制配置）

## 功能

**适用NF：PGW-C**

该命令用于查询全局APN速率控制配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBAPNRATECTRL]] · 全局APN速率控制配置（GLBAPNRATECTRL）

## 使用实例

查询全局APN速率控制配置信息：

```
%%LST GLBAPNRATECTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
APN速率控制开关  =  不使能
   上行时间单位  =  不限制
   最大上行速率  =  0
   下行时间单位  =  不限制
   最大下行速率  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GLBAPNRATECTRL.md`
