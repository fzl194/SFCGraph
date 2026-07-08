---
id: UDG@20.15.2@MMLCommand@LST FEHEARTBEAT
type: MMLCommand
name: LST FEHEARTBEAT（查询FE心跳功能开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FEHEARTBEAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 转发引擎实例FEI
- 心跳开关
status: active
---

# LST FEHEARTBEAT（查询FE心跳功能开关）

## 功能

该命令用来查询FE心跳功能开关状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FEHEARTBEAT]] · FE心跳功能开关（FEHEARTBEAT）

## 使用实例

查询FE心跳功能开关状态：

```
LST FEHEARTBEAT:;
RETCODE = 0  操作成功

结果如下
--------
心跳开关  =  ON
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FEHEARTBEAT.md`
