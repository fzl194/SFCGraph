---
id: UDG@20.15.2@MMLCommand@LST INSAFULLIFSW
type: MMLCommand
name: LST INSAFULLIFSW（查询全量智能SA识别开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: INSAFULLIFSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 智能SA管理
- 全部流量智能识别功能开关
status: active
---

# LST INSAFULLIFSW（查询全量智能SA识别开关）

## 功能

**适用NF：PGW-U、UPF**

查询全量智能SA识别开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@INSAFULLIFSW]] · 全量智能SA识别开关（INSAFULLIFSW）

## 使用实例

查询当前全量智能SA识别开关状态：

```
LST INSAFULLIFSW:;
```

```

RETCODE = 0 操作成功。

全量智能SA识别开关信息
------
 
        全量推理开关 = Enable

(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-INSAFULLIFSW.md`
