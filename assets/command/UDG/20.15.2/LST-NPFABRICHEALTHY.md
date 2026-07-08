---
id: UDG@20.15.2@MMLCommand@LST NPFABRICHEALTHY
type: MMLCommand
name: LST NPFABRICHEALTHY（查询全局亚健康相关配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NPFABRICHEALTHY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# LST NPFABRICHEALTHY（查询全局亚健康相关配置）

## 功能

该命令用于查询全局亚健康相关配置：包括亚健康阈值和亚健康检测周期。

> **说明**
> - 该命令执行后立即生效。
> - 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NPFABRICHEALTHY]] · 全局亚健康相关配置（NPFABRICHEALTHY）

## 使用实例

查询全局亚健康相关配置：

```
LST NPFABRICHEALTHY:;
RETCODE = 0  操作成功

结果如下
--------
    亚健康阙值  =  50
亚健康探测周期  =  100
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NPFABRICHEALTHY.md`
