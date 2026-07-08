---
id: UDG@20.15.2@MMLCommand@LST NPECMPLOCALPRE
type: MMLCommand
name: LST NPECMPLOCALPRE（查询优选本单板TRUNK出接口开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NPECMPLOCALPRE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 转发引擎实例FEI
- 优选本单板TRUNK出接口
status: active
---

# LST NPECMPLOCALPRE（查询优选本单板TRUNK出接口开关）

## 功能

该命令用来查询NP优选本单板TRUNK出接口开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [优选本单板TRUNK出接口开关（NPECMPLOCALPRE）](configobject/UDG/20.15.2/NPECMPLOCALPRE.md)

## 使用实例

查询NP优选本单板TRUNK出接口开关的参数：

```
%%LST NPECMPLOCALPRE:;%%
RETCODE = 0  操作成功

结果如下
--------
关闭优选本单板TRUNK出接口开关  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询优选本单板TRUNK出接口开关（LST-NPECMPLOCALPRE）_84858620.md`
