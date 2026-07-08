---
id: UNC@20.15.2@MMLCommand@LST GWPROXYFUNC
type: MMLCommand
name: LST GWPROXYFUNC（查询网关Proxy功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GWPROXYFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- 网关Proxy功能
status: active
---

# LST GWPROXYFUNC（查询网关Proxy功能配置）

## 功能

**适用NF：PGW-C、GGSN**

此命令用于查询全局网关Proxy功能配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GWPROXYFUNC]] · 网关Proxy功能配置（GWPROXYFUNC）

## 使用实例

查询当前网关proxy功能的配置：

```
%%LST GWPROXYFUNC:;%%
RETCODE = 0  操作成功

结果如下
------------------------
Proxy功能开关  =  使能
   重启计数器  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GWPROXYFUNC.md`
